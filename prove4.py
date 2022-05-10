import calliope
import matplotlib.pyplot as plt


percorso_modello_1 = 'Results/results_20220502-130204/results_2/model.nc'
model1 = calliope.read_netcdf(percorso_modello_1)

# print(model1.results.carrier_prod)
# print(list(model1.results.carrier_prod.coords[].values))
# print(list(model1.results.carrier_prod.coords[].values))

# for ii in model1.results.carrier_prod.coords:
#     print(model1.results.carrier_prod.coords[ii].values)  # [...'Zambia::spillageA::waterB' 'Zambia::spillageC::waterD' 'Zambia::spillageB::waterD' 'Moz-North-Center::spillageD::waterE']

# print(model1.results.carrier_prod.coords)

# print(model1.results.carrier_prod.loc['Moz-North-Center::spillageD::waterE'])  # <class 'xarray.core.dataarray.DataArray'>
# print(model1.results.carrier_con.loc['Moz-North-Center::spillageD::waterD'])  # <class 'xarray.core.dataarray.DataArray'>

gino_prod = model1.results.carrier_prod.loc['Moz-North-Center::spillageD::waterE']
gino_con = model1.results.carrier_con.loc['Moz-North-Center::spillageD::waterD']

# print(gino_prod.where(gino_prod != 0, drop=True))  # 0 valori
# print('\n\n', gino_con.where(gino_con != 0, drop=True))  # 470 valori

# gino_eff = model1.inputs.energy_eff.loc['Moz-North-Center::spillageD'] * 1e7
# gino_eff = model1.inputs.energy_eff.loc['Zambia::spillageA'] * - 1e7
# print(gino_eff.where(gino_eff != 0, drop=True))

# gino_eff_pandas = gino_eff.to_pandas()
# print(gino_eff_pandas.columns)
# gino_eff_pandas = gino_eff.to_pandas().unstack()
# gino_eff_pandas = gino_eff.to_dataframe()
# gino_eff_pandas = gino_eff.to_dataframe().reset_index()
# print(gino_eff_pandas, '\n\n', gino_eff_pandas.iloc[0][0])
# print(gino_eff_pandas.columns)  # loc_techs, energy_eff
# print(gino_eff_pandas)

gino_con.plot(label='SpillageD consumption')


axes = plt.gca()
y_min, y_max = axes.get_ylim()

gino_eff = model1.inputs.energy_eff.loc['Zambia::spillageA']
rescaled_unitary_eff = (y_max + y_min) / 2
gino_eff_pandas = gino_eff.to_dataframe().replace(1, rescaled_unitary_eff)


# gino_eff.plot(label='SpillageD efficiency')
# gino_eff_pandas.plot.scatter(label='SpillageD efficiency')
# plt.scatter(gino_eff_pandas)
#
# gino_eff.plot.scatter(x='timesteps')
# plt.scatter(gino_eff_pandas.loc_techs, )

# gino_eff_pandas.plot.scatter(y=1, use_index=True)
# plt.scatter(gino_eff_pandas.index, gino_eff_pandas['energy_eff'], color='red', markersize=2)
# gino_eff_pandas.plot(x=gino_eff_pandas.index, y=gino_eff_pandas['energy_eff'], color='red', s=5, kind='scatter')
plt.scatter(gino_eff_pandas.index, gino_eff_pandas['energy_eff'], color='red', s=5)
plt.show()

