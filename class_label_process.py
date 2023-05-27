from tqdm import tqdm
import os
import shutil


img_path = r"E:\processed_cmmd\imgs"
mask_path = r"E:\processed_cmmd\masks"


cls_img_path = r"E:\processed_cmmd\cls_imgs"
cls_mask_path = r"E:\processed_cmmd\cls_masks"


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
    "Malign":1,
    "Ambigu":2,
    "Typica":3

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

    elif "Ambigu" in img_name:
        img_label = "_2"

    elif "Typica" in img_name:
        img_label = "_3"







    #for disease, label in disease_labels.items():
        #if disease in img_name:
            #img_label += "-" + str(label)
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
