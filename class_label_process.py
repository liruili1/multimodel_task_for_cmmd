##Before the training of the multi-task and model, it is necessary to add the class label into the file name
##This py file is for completing this step
##update 5.24  
#1 add the subtype label of cmmd dataset into file name
#2 distinguish the left side and right side of the cmmd dataset

from tqdm import tqdm
import os
import shutil


img_path = r"E:\cmmd_prepo_test\imgs"
mask_path = r"E:\cmmd_prepo_test\masks"


cls_img_path = r"E:\cls_cmmd\imgs"
cls_mask_path = r"E:\cls_cmmd\masks"


os.makedirs(cls_img_path, exist_ok=True)
os.makedirs(cls_mask_path, exist_ok=True)

disease_labels = {
    "calc": 0,
    "dist": 1,
    "FAD-": 2,
    "mass": 3,
    "FA--": 4,
    "TC--": 5
}

bm_labels = {
    "Benign":0,
    "Malign":1
}

Left_Right_labels = {
    "L":0,
    "R":1
}

img_files = [filename for filename in os.listdir(img_path) if filename.endswith((".jpg", ".png"))]
for i, filename in tqdm(enumerate(img_files), total=len(img_files), desc="Processing"):
    imgs_path = os.path.join(img_path, filename)
    masks_path = os.path.join(mask_path, filename)

    img_name, img_ext = os.path.splitext(filename)

    if "Benign" in img_name:
        img_label = "_0"


    elif "Malign" in img_name:
        img_label = "_1"

    for disease, label in disease_labels.items():
        if disease in img_name:
            img_label += "_" + str(label)
    if '_L' in img_name:
        img_label += "_0"
    elif '_R' in img_name:
        img_label += "_1"

    #for side,mark in Left_Right_labels.items():
        #if side in img_name:
            #img_label += "_"+ str(mark)



    new_img_name = img_name + img_label + img_ext
    new_mask_name = img_name + img_label + img_ext


    new_img_path = os.path.join(cls_img_path, new_img_name)
    new_mask_path = os.path.join(cls_mask_path, new_mask_name)

    shutil.copyfile(imgs_path, new_img_path)
    shutil.copyfile(masks_path, new_mask_path)

