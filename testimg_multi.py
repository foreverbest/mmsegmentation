from mmseg.apis import inference_segmentor, init_segmentor
import mmcv
import os
import numpy as np

config_file = 'configs/ocrnet/ocrnet_hr18_512x1024_20k_l430sv.py'
checkpoint_file = 'work_dirs/ocrnet_hr18_512x1024_20k_l430sv_40/latest.pth'

# build the model from a config file and a checkpoint file
model = init_segmentor(config_file, checkpoint_file, device='cuda:0')

path='data/l430sv/images/val'
outpath='testdata/test/'
imglist = os.listdir(path)
# test images and show the results

def save_seg(result, out_file=None):
    seg = result[0].astype(np.uint8)
    mmcv.imwrite(seg,out_file)

if __name__ == '__main__':
    for i in imglist:
        if os.path.splitext(i)[1]=='.jpg':
            img = path+i  # or img = mmcv.imread(img), which will only load it once
            result = inference_segmentor(model, img)
            
            #save_seg(result,outpath+i)  #output only the segment result even without the pattle *optional
        
        #CLASSES = ('_background_','Vegetation','Sky','Road','Person','Sign',
        #        'Stuff','Bike','Car','Building','Sidewalk')
# visualize the results in a new window
        #model.show_result(img, result, show=True)
# or save the visualization results to image files
        
            model.show_result(img, result, out_file=outpath+i)      #output img + result *optional

            print('saving image %s ...'%i)
    print('finish!')

