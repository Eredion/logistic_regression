#!/usr/bin/env python3

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data_train = pd.read_csv('./dataset_train.csv').to_numpy()
data_test= pd.read_csv('./dataset_test.csv').to_numpy()
for i in range(data_train.shape[0]):
    print(f"{data_train[i][6]}")
#print(data_test)
lab = ["uno", "dos", "tres", "cuatro", "cinco"]
x = [1, 18, 15, 9, 10]
plt.bar(range(len(lab)), x, tick_label=lab)
plt.show()

if __name__ == "__main__":
    print("Hola")

