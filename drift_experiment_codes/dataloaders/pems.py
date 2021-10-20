import os
import h5py
import pandas as pd


data_path = os.path.join(os.path.split(__file__)[0], '../data/pems-bay.h5')
data = pd.read_hdf(data_path)