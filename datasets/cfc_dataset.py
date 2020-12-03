# custom dataloader class for WVU-CFC fingerprint dataset
# built december 3rd, 2020 by Aidan Draper

# copy this structure '/media/dwaypa-ssd/monodepth2/kitti_data/2011_09_26/2011_09_26_drive_0095_sync/image_03/data/0000000185.jpg

from __future__ import absolute_import, division, print_function
import os 
import numpy as np
import PIL.Image as pil

from .mono_dataset import MonoDataset

class CFCDataset(MonoDataset):

    def __init__(self, *args, **kwargs):
        super(CFCDataset, self).__init__(*args, **kwargs)

    def get_image_path(self, folder, frame_index, side):
        f_str = "insert stuff here"

    def get_color(self, folder, frame_index, side, do_flip):
        color = self.loader(self.get_image_path(folder, frame_index, side))

        if do_flip:
            color = color.transpose(pil.FLIP_LEFT_RIGHT)

        return color

