from PIL import Image #用PIL处理图像
import os
import time
import shutil
import numpy as np
#import cv2 ——如果要用opencv时需导入

#####图像重复度检测+图像去重##########

#均值哈希算法
def aHash(image):
    image_new=image
    #计算均值
    avreage = np.mean(image_new) 
    hash = [] 
    for i in range(image.shape[0]): 
        for j in range(image.shape[1]): 
            if image[i,j] > avreage: 
                hash.append(1) 
            else: 
                hash.append(0) 
    return hash

#计算汉明距离
def Hamming_distance(hash1,hash2): 
    num = 0
    for index in range(len(hash1)): 
        if hash1[index] != hash2[index]: 
            num += 1
    return num

#比较两张照片计算相似度
def check_duplicate(image1,image2):
     #缩小尺寸并灰度化
    image1=np.array(image1.resize((8, 16), Image.ANTIALIAS).convert('L'), 'f')
    image2=np.array(image2.resize((8, 16), Image.ANTIALIAS).convert('L'), 'f')
    #opencv
    #img1 = cv2.imread('image1')
    #img2 = cv2.imread('image2') 
    #缩小尺寸并灰度化
    #image1=cv2.cvtColor(cv2.resize(img1,(8,8),interpolation=cv2.INTER_CUBIC),cv2.COLOR_BGR2GRAY)
    #image2=cv2.cvtColor(cv2.resize(img2,(8,8),interpolation=cv2.INTER_CUBIC),cv2.COLOR_BGR2GRAY)
    hash1 = aHash(image1)
    hash2 = aHash(image2)
    dist = Hamming_distance(hash1, hash2)
    #将距离转化为相似度
    similarity = 1 - dist * 1.0 / 128 
    #print('dist is '+'%d' % dist)
    #print('similarity is ' +'%.2f' % similarity)
    return similarity

def visualization(image1,image2):       #可视化比较功能
    img_compare = Image.new('RGB',(1024*2,512))
    img_compare.paste(image1,(0,0,1024,512))
    img_compare.paste(image2,(1024,0,1024*2,512))
    img_compare.show()

if __name__ == "__main__":
    #PIL
    start_time=time.time()
    path = 'testdata/origin/dianmendajie'   #原始数据文件夹
    out_path = 'testdata/dianmendajie_washed'   #存储数据文件夹
    
    isExists=os.path.exists(out_path)   #确定存储路径是否存在
    if not isExists:
        os.mkdir(out_path)

    imagefile = [name for name in os.listdir(path) if os.path.splitext(name)[1]=='.jpg']
    print("Start! Total %d images."%(len(imagefile)))
    n = 0
    
    for image in imagefile:
        image1 = Image.open(path + '/' + image)
        #shutil.copyfile(path +'/'+ image,out_path + '/' + image)
        for image_d in imagefile:
            if image_d != image:
                image2 = Image.open(path + '/' + image_d)
                if check_duplicate(image1,image2) == 1:
                    print(image + " is similar with " + image_d)
                    #visualization(image1,image2)
                    imagefile.remove(image_d)
                    n += 1                
        #imagefile.remove(image)

    for image in imagefile:
        shutil.copyfile(path +'/'+ image,out_path + '/' + image)
    end_time=time.time()
    print("Finished in %.2fs! Total %d duplicate images."%(end_time-start_time,n))

    print("Saving to %s"%out_path)
    



   
    
    
    