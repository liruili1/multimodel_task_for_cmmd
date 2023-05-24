##this file is for checking the numbers of disease for multi-task learning

import os

folder_path = r"E:\cmmd_prepo_test\imgs"

file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

disease_set = set()

for file_name in file_names:
    label_name_sp = file_name.split("_", 5)
    label_name = label_name_sp[0] + "_" + label_name_sp[1] + "_" + label_name_sp[2] + "_" + label_name_sp[3] + "_" + \
                 label_name_sp[4]+"_"+label_name_sp[5]
    diease = label_name_sp[4]
    disease_set.add(diease)
num_diseases = len(disease_set)
print(num_diseases)
print(disease_set)
