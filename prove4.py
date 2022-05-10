import calliope
from plotting_fausto import plotting
import configparser


path_model = 'Results/results_20220429-171645_nospillage/results_2/model.nc'
# path_model = 'Results/results_20220502-130204/results_2/model.nc'
model = calliope.read_netcdf(path_model)
plots_folder = 'ginoprova/'

config = configparser.ConfigParser(allow_no_value=False, inline_comment_prefixes='#')
config.read_file(open("Calliope_Hydro_config.conf"))
spillage_percentage = config.getfloat('Settings', 'spillage_percentage')


plotting.FaPlotting(model).plot_storage_and_carriers(show=True, save=False,
                                                     path=plots_folder, spillage_coeff=spillage_percentage)

