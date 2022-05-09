# from plotting_fausto import plotting
# import matplotlib.pyplot as plt
# import os
# import configparser
# import datetime
# import time
# import shutil
# import pickle
# import glob
# import sys
import calliope
from functions_fausto import compare_storage_of_two_calliope_models

percorso_modello_1 = 'Results/results_20220428-165545_nospillage/results_1/model.nc'
percorso_modello_2 = 'Results/results_20220502-130204/results_1/model.nc'

model1 = calliope.read_netcdf(percorso_modello_1)
model2 = calliope.read_netcdf(percorso_modello_2)


compare_storage_of_two_calliope_models(model1, model2, percorso_modello_1, percorso_modello_2)
