# Multimodel_task_for_cmmd

## Overview

### Data
The original dataset is from [Kaggle The Chinese Mammography Database (CMMD) 2022](https://www.kaggle.com/datasets/tommyngx/cmmd2022), which includes the classification label. 
We revised this dataset, it now has subtype labels and corresponding lesion masks for various subtypes. By Tohoku university Clinical Imageing

### Preprocess

Before the training step, it is required that process the file name like below.
```
D1-0001_R_MLO_Benign_calc_1-1_0_0_1.png
```
You can use the following file to compelete this step.
```python
class_label_process.py
```


