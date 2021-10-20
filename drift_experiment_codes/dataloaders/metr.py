import os
import h5py
import pandas as pd


data_path = os.path.join(os.path.split(__file__)[0], '../data/metr-la.h5')
data = pd.read_hdf(data_path)
