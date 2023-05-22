##This is a rename_file for preprocessing the revised CMMD(The Chinese Mammography Database) 
##by Tohoku university tucim
import os
import shutil
from tqdm import  tqdm


dataset_path = r"E:\CMMD525"
new_img_folder = r"E:\cmmd_pre_1\imgs"
new_mask_path = r"E:\cmmd_pre_1\masks"


label_folder = os.path.join(dataset_path, "label")
for root, dirs, files in os.walk(label_folder):

    for sub_dir in tqdm(dirs,desc="subfolders"):
        dirs_name_sp = sub_dir.split("_")
        if  dirs_name_sp[1] == 1 or 2:


         sub_label_folder = os.path.join(root, sub_dir)
         sub_img_folder = os.path.join(dataset_path, "image", sub_dir)

        
         for label_file in os.listdir(sub_label_folder):
             label_name_sp = label_file.split("_",4)
             label_name = label_name_sp[0] + "_" + label_name_sp[1] + "_" + label_name_sp[2]+ "_" + label_name_sp[3] + "_" + label_name_sp[4]

             img_path_name = label_name_sp[0] + "_" + label_name_sp[1] + "_" + label_name_sp[2]+ "_" + label_name_sp[3] + ".png"


             if "Benign"  not in label_name_sp and "Malign" not in label_name_sp:
                 continue



            #label_name, label_ext = os.path.splitext(label_file)
             image_name = label_name  

             img_path = os.path.join(sub_img_folder,img_path_name)
             mask_path = os.path.join(sub_label_folder, label_name)

            
             if os.path.exists(mask_path):
                
                 new_img_name = label_name
                 #new_img_path = os.path.join(sub_img_folder, new_img_name)
                 #os.rename(img_path, new_img_path)
                 shutil.copy(img_path, new_img_folder)
                 copy_path = os.path.join(new_img_folder,img_path_name)
                 copy_folder = os.path.join(new_img_folder,new_img_name)
                 os.rename(copy_path,copy_folder)


                 shutil.copy(mask_path, new_mask_path)  
                 #shutil.copy(new_img_path, new_img_folder)



             else:

                 os.remove(img_path)
