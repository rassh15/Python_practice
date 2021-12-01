# Pickling iris datasets
import requests
import csv
import pandas as pd
import pickle

# iris_data = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
# iris_data = iris_data.content
file_path = "C:\\Users\\Ars\\Downloads\\iris.data"
# iris_data = pd.read_csv(file_path, delimiter=",")

inf = open(file_path, "r")

lines = inf.readlines()



iris_list = []

for line in lines:
    iris_list.append([line])

iris_pickle_file = "iris_pickle_file.pkl"
iris_pkl_obj = open(iris_pickle_file, 'wb')
pickle.dump(iris_list, iris_pkl_obj)
iris_pkl_obj.close()

unpkl = "iris_pickle_file.pkl"
fobj = open(unpkl, 'rb')
mc = pickle.load(fobj)

print(mc[:5])