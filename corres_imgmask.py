import os
import shutil
from tqdm import tqdm


image_folder = r'E:\cmmd_side_pro\image_side'
mask_folder = r'E:\cmmd_side_pro\masks_side'
new_image_folder = r'E:\processed_cmmd\imgs'
new_mask_folder = r'E:\processed_cmmd\masks'


os.makedirs(new_image_folder, exist_ok=True)
os.makedirs(new_mask_folder, exist_ok=True)

for patient_folder in tqdm(os.listdir(mask_folder)):
    patient_folder_path = os.path.join(mask_folder, patient_folder)

    if os.path.isdir(patient_folder_path):
        for side_folder in ['left', 'right']:
            current_folder = os.path.join(patient_folder_path, side_folder)

            if os.path.exists(current_folder):
                masks = [f for f in os.listdir(current_folder) if f.endswith('.png')]

                for mask_file in masks:
                    if '_Exclus' in mask_file:
                        continue

                    #corresponding_image_file = mask_file.replace('_mask', '')
                    label_name_sp = mask_file.split("_", 4)
                    corresponding_image_file = label_name_sp[0] + "_" + label_name_sp[1] + "_" + label_name_sp[2]+ "_" + label_name_sp[3] + ".png"



                    image_file_path = os.path.join(image_folder, patient_folder, side_folder, corresponding_image_file)


                    if os.path.exists(image_file_path):

                        new_image_folder_path = os.path.join(new_image_folder)
                        new_mask_folder_path = os.path.join(new_mask_folder)

                        if not os.path.exists(new_image_folder_path):
                            os.makedirs(new_image_folder_path)
                        if not os.path.exists(new_mask_folder_path):
                            os.makedirs(new_mask_folder_path)

                        new_image_file_path = os.path.join(new_image_folder_path, mask_file)
                        new_mask_file_path = os.path.join(new_mask_folder_path, mask_file)
                        shutil.copy2(image_file_path, new_image_file_path)
                        shutil.copy2(os.path.join(current_folder, mask_file), new_mask_file_path)
