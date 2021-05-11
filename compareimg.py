import os
from PIL import Image

high_size = 512#高
width_size = 1024#宽
#图片路径集合
path_damdj = 'testdata/compare/origin/dianmendajie'
path_damdj_fcn = 'testdata/fcn_r50-d8_40k/dianmendajie'
path_damdj_psanet = 'testdata/psanet_r50-d8_40k/dianmendajie'
path_damdj_pspnet='testdata/pspnet_r50-d8_512x1024_40k_cityscapes_test/dianmendajie'
path_damdj_fastscnn='testdata/fast_scnn/dianmendajie'
path_damdj_deeplabv3plus='testdata/deeplabv3plus_r50-d8_512x1024_40k_cityscapes_test/dianmendajie'
path_meht = 'testdata/compare/origin/maoerhutong'   #测试图片
path_meht_fcn='testdata/fcn_r50-d8_40k/maoerhutong'
path_meht_psanet='testdata/psanet/maoerhutong'
path_meht_pspnet='testdata/pspnet_r50-d8_512x1024_40k_cityscapes_test/maoerhutong'
path_meht_fastscnn='testdata/psanet_r50-d8_40k/maoerhutong'
path_meht_deeplabv3plus='testdata/deeplabv3plus_r50-d8_512x1024_40k_cityscapes_test/maoerhutong'
path_meht_l430sv='testdata/deeplabv3plus_l430sv_10_20000/maoerhutong'
#输出路径
outpath = 'testdata/compare/maoerhutong_ori_l430sv_fcn_psa_psp_fscnn_dlbv3p.jpg'
#本程序测试路径
set1 = path_meht
set2 = path_meht_l430sv
set3 = path_meht_fcn
set4 = path_meht_psanet
set5 = path_meht_pspnet
set6 = path_meht_fastscnn
set7 = path_meht_deeplabv3plus
#获取当前文件路径下的图片个数
imagefile=[name for name in os.listdir(set1) (if os.path.splitext(name)[1]=='.jpg')]
target = Image.new('RGB',(width_size*7,high_size*len(imagefile)))#最终拼接的图像的大小
#x,y,w,h
y1 = 0
h1 = high_size

i = 0
for image in imagefile:
    target.paste(Image.open(set1 + '/' + image),(0,y1,width_size,h1))
    target.paste(Image.open(set2 + '/' + image),(width_size,y1,width_size*2,h1))
    target.paste(Image.open(set3 + '/' + image),(width_size*2,y1,width_size*3,h1))
    target.paste(Image.open(set4 + '/' + image),(width_size*3,y1,width_size*4,h1))
    target.paste(Image.open(set5 + '/' + image),(width_size*4,y1,width_size*5,h1))
    target.paste(Image.open(set6 + '/' + image),(width_size*5,y1,width_size*6,h1))
    target.paste(Image.open(set7 + '/' + image),(width_size*6,y1,width_size*7,h1))

    y1 += high_size#从上往下拼接，左上角的纵坐标递增
    h1 += high_size#右下角的纵坐标也递增
    if i%5 == 0:
        p=i/len(imagefile)*100
        print('processing %.2f%%...'%p)
    i += 1    
    target.save(outpath,quality=20)
print("finish!")