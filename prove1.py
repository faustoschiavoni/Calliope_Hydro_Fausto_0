# for ii in ['CB', 'ITT', 'KA', 'KG']:
#     with open(f"Timeseries_original_updated_with_positives/evapLoss_{ii}.txt", "r") as testo:
#
#         linee = testo.readlines()
#
#         blocca_alla_riga = 10e100  # 3
#
#         numerii, timestamps = [], []
#         for numero, gee in enumerate(linee):
#
#             if numero == 0:
#                 header = gee
#                 continue  # salto le intestazioni
#
#             # print(gee[20:])
#             # numerii.append(float(gee[20:-2]))
#
#             numerii.append(gee[20:-1])
#             timestamps.append(gee[:20])
#
#             if numero == blocca_alla_riga:
#                 print(numerii, timestamps, type(numerii[1]))
#                 break
#
#     listone = list(map(float, numerii))
#     listariella = list(map(lambda x: str(abs(x)*10e3), listone))
#     # print(listone, type(listone[0]))
#
#     with open(f"Timeseries_original_updated_with_positives/evapLoss_{ii}.txt", "w") as testo2:
#
#         testo2.writelines(header)
#
#         for gino in range(len(numerii)):
#
#             testo2.writelines(timestamps[gino] + listariella[gino] + '\n')


# import shutil
# shutil.copytree("Timeseries/Initialize_Loop", "PROVADIR_2", dirs_exist_ok=True)

