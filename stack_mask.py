import os
import numpy as np
from PIL import Image
import cv2
from tqdm import tqdm



color_map = {
    '_calc': (255, 0, 0),     #  red
    '_mass': (0, 255, 0),     #  green
    '_FA': (0, 0, 255),     #  blue
    '_TC': (255, 255, 0),   #  yellow
    '_FAD': (255, 0, 255),   #  purple
    '_dist': (255, 255, 255)    #  white

}


data_folder = r'E:\cmmd_side_525_2\mask_side'
new_folder = r'E:\cmmd_side_pro'

for patient_folder in tqdm(os.listdir(data_folder)):
    patient_folder_path = os.path.join(data_folder, patient_folder)

    if os.path.isdir(patient_folder_path):
        for side_folder in ['left', 'right']:
            current_folder = os.path.join(patient_folder_path, side_folder)

            if os.path.exists(current_folder):
                masks = [f for f in os.listdir(current_folder) if f.endswith('.png')]


                if masks:
                    
                    pre_mask_name = masks[0]
                    label_name_sp = pre_mask_name.split("_", 4)
                    label_name_tag = label_name_sp[0] + "_" + label_name_sp[1] + "_" + label_name_sp[2] + "_" + \
                                 label_name_sp[3]
                    first_mask = cv2.imread(os.path.join(current_folder, masks[0]), cv2.IMREAD_GRAYSCALE)
                    combined_mask = np.zeros((first_mask.shape[0], first_mask.shape[1], 3), np.uint8)

                    
                    diseases = set()

                    for mask_file in masks:
                        mask = cv2.imread(os.path.join(current_folder, mask_file), cv2.IMREAD_GRAYSCALE)

                        
                        for disease, color in color_map.items():
                            if disease in mask_file:
                                colored_mask = np.repeat(mask[:, :, np.newaxis], 3, axis=2)
                                colored_mask[(colored_mask == [255, 255, 255]).all(axis=2)] = color
                                diseases.add(disease)
                                break

                       
                        combined_mask = np.minimum(combined_mask + colored_mask, 255)

                    
                    new_folder_path = os.path.join(new_folder, patient_folder, side_folder)

                    if not os.path.exists(new_folder_path):
                        os.makedirs(new_folder_path)

                    
                    file_name = label_name_tag + '_'.join(diseases) + '.png'

                    
                    cv2.imwrite(os.path.join(new_folder_path, file_name), combined_mask)
