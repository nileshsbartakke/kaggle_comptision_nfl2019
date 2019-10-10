import pandas as pd
import numpy as np

data_fire=pd.read_csv("C:\\Users\\admin\\Downloads\\train.csv")
np.random.seed(0)

print(data_fire.head(5))

missing_value_count=data_fire.isnull().sum()
#print(missing_value_count)
total_cell=np.product(data_fire.shape[1])
total_missing=missing_value_count.sum()
#print((total_cell/total_missing)*100)

colum_with_dropna=data_fire.dropna(axis=1)
#print(colum_with_dropna.head(15))

print("Original data ",data_fire.shape[1])
print("After dropna",colum_with_dropna.shape[1])

