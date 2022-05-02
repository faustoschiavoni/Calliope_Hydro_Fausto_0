import calliope
import glob
import os
from plotting_fausto import plotting
import configparser
import matplotlib


latest = (True, -1)  # if True automatically open the latest folder created in the directory 'Results/', the number specify which 'latest' folder to open (-1=latest, -2=the one prior to the latest...)
save_in_the_latest = True  # if latest=True, overrides folder_where_to_save
which_results = 2  # if latest=True, '1' --> 'results_1' folder, '2' --> 'results_2' folder ...

# matplotlib.use('Agg')
# print(matplotlib.get_backend())
# print(matplotlib.rcsetup.non_interactive_bk)

specific_model = 'Results/results_20220428-200432_nospillage/results_2/model.nc'
# 'Results/results_20220422-114317/results_2/model.nc'
# 'C:/Users/utente/Documents/CODICI di Fausto/Tesi/calliope/NEW_MODEL_FAUSTO/modello_netcdf.nc' <-- non ha più senso
folder_where_to_save = 'Prove3_prova_debugger/'  # directory where plots are saved if latest=False or if latest=True and save_in_the_latest=False

# ----------------------------------------------


# Settings loading
config = configparser.ConfigParser(inline_comment_prefixes='#')
config.read_file(open("Calliope_Hydro_config.conf"))
sp = config.getfloat('Settings', 'spillage_percentage')  # TODO: get this value from Settings.txt not from .conf since it can change on .conf
if latest:
    list_of_folders = glob.glob('Results/*')  # * means all, if needed a specific format then *.csv
    list_of_folders.remove('Results\\results_debug')
    # latest_folder = max(list_of_folders, key=os.path.getctime)
    latest_folder = sorted(list_of_folders, key=os.path.getctime)
    latest_folder = latest_folder[latest[1]]

    specific_model = f'{latest_folder}/results_{which_results}/model.nc'
    if save_in_the_latest:
        folder_where_to_save = f'{latest_folder}/results_{which_results}/plots'

model = calliope.read_netcdf(specific_model)

if latest:
    print(
        f"Soglia_storageA: {sp * model._model_data.data_vars['storage_cap'].loc['Zambia::storageA'].values:.2e}\n"
        f"Soglia_storageB: {sp * model._model_data.data_vars['storage_cap'].loc['Zambia::storageB'].values:.2e}\n"
        f"Soglia_storageC: {sp * model._model_data.data_vars['storage_cap'].loc['Zambia::storageC'].values:.2e}\n"
        f"Soglia_storageD: {sp * model._model_data.data_vars['storage_cap'].loc['Moz-North-Center::storageD'].values:.2e}\n"
    )

# plotting.FaPlotting(model).plot_storage_timeseries(path=folder_where_to_save, save=False, show=False,
#                                                    show_subs=False, spillage_coeff=sp)  # lslice=0, rslice=120)

plotting.FaPlotting(model).write_excel(path=folder_where_to_save, exist_ok=True)
plotting.FaPlotting(model).plot_storage_timeseries(path=folder_where_to_save, spillage_coeff=sp)



# def plot_storage(model_data, lslice=None, rslice=None, show_storage_cap_max=True, frmt='svg', show=False, save=True,
#                  path='Results', exist_ok=True, show_spillage_line=True, spillage_coeff=0.95, create_subplots=True,
#                  show_subs=False):


# if float(StorageA_nuovo.iloc[a]) > sp * model._model_data.data_vars['storage_cap'].loc['Zambia::storageA']:
# if float(StorageB_nuovo.iloc[k]) > sp * model._model_data.data_vars['storage_cap'].loc['Zambia::storageB']:
# if float(StorageC_nuovo.iloc[j]) > sp * model._model_data.data_vars['storage_cap'].loc['Zambia::storageC']:
# if float(StorageD_nuovo.iloc[i]) > sp * model._model_data.data_vars['storage_cap'].loc['Moz-North-Center::storageD']

