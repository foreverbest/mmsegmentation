import os.path as osp

from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
class L430svDataset(CustomDataset):
    """L430sv dataset.

     The``img_suffix`` is fixed to '.jpg' and ``seg_map_suffix`` is fixed to
    '.png'.
    """

    CLASSES = ('_background_','Vegetation','Sky','Road','Person','Sign',
                'Stuff','Bike','Car','Building','Sidewalk')


    PALETTE = [[0,0,0],[107,142,35],[70,130,180],[128,64,128],[220,20,60],
                [153,153,153],[190,153,153],[119,11,32],[0,0,142],
                [70,70,70],[244,35,232]]

    def __init__(self, **kwargs):
        super(L430svDataset, self).__init__(
            img_suffix='.jpg',
            seg_map_suffix='_mask.png',
            **kwargs)
        assert osp.exists(self.img_dir)