# Multimodel_task_for_cmmd

## Overview

### Data
The original dataset is from [Kaggle The Chinese Mammography Database (CMMD) 2022](https://www.kaggle.com/datasets/tommyngx/cmmd2022), which includes the classification label. 
We revised this dataset, and it now has subtype labels and corresponding lesion masks for various subtypes. By Tohoku university Clinical Imageing

### Preprocess

#### Step 1

Use the ```divide_rf.py``` to split the right/left mlo image and corresponding mask into right/left directory

#### Step2

Use ```stack_mask.py``` to process the multi-mask into one mask image with different colors.
Processed mask is like below:

![image](https://github.com/liruili1/multimodel_task_for_cmmd/blob/main/sample/mask_sample.png)

#### Step 3

Use ```corres_imgmask.py``` to correspond processed image and mask file into image and mask folder.
The processed CMMD dataset is like below:
  ```
    ├── CMMD
    │   ├── images
    │   │   ├── D1-0001_R_MLO_Benign_calc.png
    │   │   └── D1-0002_L_MLO_Benign_calc.png
    |   |   └── ...
    │   ├── labels
    │   │   ├── D1-0001_R_MLO_Benign_calc.png
    │   │   ├── D1-0002_L_MLO_Benign_calc.png
    |   |   └── ...


```

#### Step 4  
Use ```class_label_process.py``` to process the class tag. This is a sample of processed img with class tags ``` D1-0045_L_MLO_Malign_calc_1_0.png ``` 
### Training



