##this is for dividing the R and L image

import os
import shutil
from tqdm import tqdm


dataset_folder = r'E:\CMMD_mul'
output_img_folder= r'E:\cmmd_side\image_side'
output_mask_folder = r'E:\cmmd_side\mask_side'


patient_image_folders = [f.path for f in os.scandir(os.path.join(dataset_folder, 'image')) if f.is_dir()]
patient_mask_folders = [f.path for f in os.scandir(os.path.join(dataset_folder, 'label')) if f.is_dir()]


for patient_folder in tqdm(patient_image_folders,desc='Processing images'):
    patient_name = os.path.basename(patient_folder)


    left_img_folder = os.path.join(output_img_folder,patient_name, 'left')
    right_img_folder = os.path.join(output_img_folder, patient_name, 'right')
    #left_mask_folder = os.path.join(output_mask_folder, 'left', patient_name)
    #right_mask_folder = os.path.join(output_mask_folder, 'right', patient_name)
    os.makedirs(left_img_folder, exist_ok=True)
    os.makedirs(right_img_folder, exist_ok=True)
    #os.makedirs(left_mask_folder, exist_ok=True)
    #os.makedirs(right_mask_folder, exist_ok=True)


    for file_name in os.listdir(patient_folder):
        if file_name.endswith('.png'):
            file_path = os.path.join(patient_folder, file_name)

            if '_L' in file_name:
                output_path = os.path.join(left_img_folder, file_name)
            elif '_R' in file_name:
                output_path = os.path.join(right_img_folder, file_name)
            else:
                continue


            shutil.copy(file_path, output_path)
for patient_label_folder in tqdm(patient_mask_folders,desc='Processing masks'):
    patient_mask_name = os.path.basename(patient_label_folder)


    #left_img_folder = os.path.join(output_img_folder, 'left', patient_name)
    #right_img_folder = os.path.join(output_img_folder, 'right', patient_name)
    left_mask_folder = os.path.join(output_mask_folder, patient_mask_name,'left')
    right_mask_folder = os.path.join(output_mask_folder, patient_mask_name,'right')
    #os.makedirs(left_img_folder, exist_ok=True)
    #os.makedirs(right_img_folder, exist_ok=True)
    os.makedirs(left_mask_folder, exist_ok=True)
    os.makedirs(right_mask_folder, exist_ok=True)


    for file_mask_name in os.listdir(patient_label_folder):
        if file_mask_name.endswith('.png'):
            file_mask_path = os.path.join(patient_label_folder, file_mask_name)

            if '_L' in file_mask_name:
                output_mask_path = os.path.join(left_mask_folder, file_mask_name)
            elif '_R' in file_mask_name:
                output_mask_path = os.path.join(right_mask_folder, file_mask_name)
            else:
                continue

            shutil.copy(file_mask_path, output_mask_path)
