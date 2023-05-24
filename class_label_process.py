##Before the training of the multi-task and model, it is necessary to add the class label into the file name
##This py file is for completing this step

from tqdm import tqdm
import os
import shutil

img_path = r"E:\cmmd_prepo_test\imgs"
mask_path = r"E:\cmmd_prepo_test\masks"
cls_img_path = r"E:\cls_cmmd\imgs"
cls_mask_path = r"E:\cls_cmmd\masks"


os.makedirs(cls_img_path, exist_ok=True)
os.makedirs(cls_mask_path, exist_ok=True)


img_files = [filename for filename in os.listdir(img_path) if filename.endswith((".jpg", ".png"))]
for i, filename in tqdm(enumerate(img_files), total=len(img_files), desc="Processing"):
    imgs_path = os.path.join(img_path, filename)
    masks_path = os.path.join(mask_path, filename)

    img_name, img_ext = os.path.splitext(filename)

    if "Benign" in img_name:
        new_img_name = img_name + "_0" + img_ext
        new_mask_name = img_name + "_0" + img_ext

 
    elif "Malign" in img_name:
        new_img_name = img_name + "_1" + img_ext
        new_mask_name = img_name + "_1" + img_ext

    new_img_path = os.path.join(cls_img_path, new_img_name)
    new_mask_path = os.path.join(cls_mask_path, new_mask_name)

    shutil.copyfile(imgs_path, new_img_path)
    shutil.copyfile(masks_path, new_mask_path)
