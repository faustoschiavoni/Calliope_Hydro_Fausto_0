# import calliope
# # from plotting_fausto import plotting
import calliope
import matplotlib.pyplot as plt
import os
# import configparser
# import datetime
# import time
# import shutil
# import pickle
import glob
# import sys


percorso_modello_1 = 'Results/results_20220428-200432_nospillage/results_2/model.nc'
percorso_modello_2 = 'Results/results_20220420-135034/results_2/model.nc'
# 'Results/results_20220428-200432_nospillage/results_2/model.nc'
# 'Results/results_20220429-000921/results_1/model.nc'


model1 = calliope.read_netcdf(percorso_modello_1)
model2 = calliope.read_netcdf(percorso_modello_2)
def compare_storage_of_two_calliope_models(x, y):
    # locs_techs = len(model_data.data_vars['storage'].coords['loc_techs_store'])
    # if x._model_data.data_vars['storage'].equals(y._model_data.data_vars['storage']):
    #     print('sono uguali')

    locs_techs_ordered = ['Zambia::storageA', 'Zambia::storageB', 'Zambia::storageC', 'Moz-North-Center::storageD']
    for locstech in locs_techs_ordered:
        gino1 = x._model_data.data_vars['storage'].loc[locstech]
        gino2 = y._model_data.data_vars['storage'].loc[locstech]

        if gino1.equals(gino2):
            coo = ''
        else:
            coo = 'NON'
        mex = f"`{gino1.coords['loc_techs_store'].values}` " \
              f"del modello " \
              f"`{percorso_modello_1}`" \
              f"{coo} è uguale al " \
              f"`{gino2.coords['loc_techs_store'].values}` " \
              f"del modello " \
              f"`{percorso_modello_2}`."
        print(mex)

# print(type(model1._model_data.data_vars['storage']))  # dataArray
# print(model1._model_data.data_vars['storage'][0])  # Zambia::storageA
# print(model1._model_data.data_vars['storage'].loc['Zambia::storageA'])  # Zambia::storageA
# print(model1._model_data.data_vars['storage'][0].coords['loc_techs_store'].values)
# print(type(model1._model_data.data_vars['storage'][0]))  # DataArray


compare_storage_of_two_calliope_models(model1, model2)

# gino3 = model1._model_data.data_vars['storage'].loc['Zambia::storageA'] - model2._model_data.data_vars['storage'].loc['Zambia::storageA']
# gino4 = gino3.where(gino3 != 0)
# print(gino4)
# print(*gino4.dropna('timesteps'))
