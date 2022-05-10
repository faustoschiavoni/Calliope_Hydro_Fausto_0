import calliope
import matplotlib.pyplot as plt

'''
percorso_modello_1 = 'Results/results_20220502-130204/results_2/model.nc'
model1 = calliope.read_netcdf(percorso_modello_1)


# gino_prod = model1.results.carrier_prod.loc['Moz-North-Center::spillageD::waterE']
# 'Zambia::spillageA::waterB','Zambia::spillageC::waterD','Zambia::spillageB::waterD','Moz-North-Center::spillageD::waterE'

gino_con = model1.results.carrier_con.loc['Moz-North-Center::spillageD::waterD']

gino_con.plot(color='blue')

axes = plt.gca()
y_min, y_max = axes.get_ylim()  # questo trova il valore più grande e più piccolo rappresentabile nel grafico (estremi della y), non quelli reali delle curve


rerer = (gino_con.max().values + gino_con.min().values) / 2
# gino_eff = model1.inputs.energy_eff.loc['Moz-North-Center::spillageD'] * rerer # qui c'è lo spillageA perché spillageD è sempre 0
gino_eff = model1.inputs.energy_eff.loc['Zambia::spillageA'] * rerer  # qui c'è lo spillageA perché spillageD è sempre 0

gino_eff.plot(linestyle='', marker='o', markersize=2)

# gino_eff = model1.inputs.energy_eff.loc['Zambia::spillageA']  # qui c'è lo spillageA perché spillageD è sempre 0
# rescaled_unitary_eff = (y_max + y_min) / 2
#
# # import numpy
# # print(gino_con.min.values, gino_con.max.values, y_min, y_max)
# print(type(gino_con.max().values), '\n\n', gino_con.min().values)
# print('\n\n\n\n\n', y_min, y_max)
#
# gino_eff_pandas = gino_eff.to_dataframe().replace(1, rescaled_unitary_eff)
# plt.scatter(gino_eff_pandas.index, gino_eff_pandas['energy_eff'], color='red', s=5)
#
# # gino_prod.plot(color='green')

plt.show()
'''

from plotting_fausto import plotting
import configparser


path_model = 'Results/results_20220429-171645_nospillage/results_2/model.nc'
# path_model = 'Results/results_20220502-130204/results_2/model.nc'
model = calliope.read_netcdf(path_model)
plots_folder = 'ginoprova/'

config = configparser.ConfigParser(allow_no_value=False, inline_comment_prefixes='#')
config.read_file(open("Calliope_Hydro_config.conf"))
spillage_percentage = config.getfloat('Settings', 'spillage_percentage')


plotting.FaPlotting(model).plot_storage_and_carriers(show=True, save=True,
                                                     path=plots_folder, spillage_coeff=spillage_percentage)

# creare questo grafico per ogni "results" in Results (magari prima copio anche quelli da 4 iterazioni)

