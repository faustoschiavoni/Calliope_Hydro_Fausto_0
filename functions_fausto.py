import datetime
import smtplib
import shutil
import glob
import os


def notify_via_email(mex):

    gmail_user = 'tesiFaustonotify@gmail.com'
    gmail_pwd = 'tesifausto'
    FROM = 'tesiFaustonotify@gmail.com'
    TO = ['fausto.schiavoni@mail.polimi.it']  # , 'faustoschiavoni@gmail.com']
    SUBJECT = 'Last Execution Tesi update (Calliope Hyrdo)'
    datehour = datetime.datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
    TEXT = f'Date: {datehour} \n\n{mex}'

    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ', '.join(TO), SUBJECT, TEXT)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_pwd)
    server.sendmail(FROM, TO, message)
    server.close()


def compare_storage_of_two_calliope_models(calliope_model_1, calliope_model_2, path_model_1, path_model_2):

    '''
    Esempio di utilizzo della funzione:

    percorso_modello_1 = 'Results/results_20220428-165545_nospillage/results_1/model.nc'
    percorso_modello_2 = 'Results/results_20220502-130204/results_1/model.nc'

    model1 = calliope.read_netcdf(percorso_modello_1)
    model2 = calliope.read_netcdf(percorso_modello_2)


    compare_storage_of_two_calliope_models(model1, model2, percorso_modello_1, percorso_modello_2)
    '''

    locs_techs_ordered = ['Zambia::storageA', 'Zambia::storageB', 'Zambia::storageC', 'Moz-North-Center::storageD']
    bool_list = []
    mex = []
    for locstech in locs_techs_ordered:
        gino1 = calliope_model_1._model_data.data_vars['storage'].loc[locstech]
        gino2 = calliope_model_2._model_data.data_vars['storage'].loc[locstech]

        if gino1.equals(gino2):
            bool_list.append(True)
            coo = ''
        else:
            bool_list.append(False)
            coo = 'NOT'
        mex.append(f"`{gino1.coords['loc_techs_store'].values}` "
                   f"of model "
                   f"`{path_model_1}` "
                   f"is {coo} EQUAL to "
                   f"`{gino2.coords['loc_techs_store'].values}` "
                   f"of model "
                   f"`{path_model_2}`.")

    print(f'{"ALL EQUAL" if all(bool_list) else "NOT ALL EQUAL"}\n', *mex, sep='\n')


def create_right_files():

    for ii in ['CB', 'ITT', 'KA', 'KG']:
        with open(f"Timeseries_original_updated_with_positives/evapLoss_{ii}.txt", "r") as testo:

            linee = testo.readlines()

            blocca_alla_riga = 10e100  # 3

            numerii, timestamps = [], []
            for numero, gee in enumerate(linee):

                if numero == 0:
                    header = gee
                    continue  # salto le intestazioni

                # print(gee[20:])
                # numerii.append(float(gee[20:-2]))

                numerii.append(gee[20:-1])
                timestamps.append(gee[:20])

                if numero == blocca_alla_riga:
                    print(numerii, timestamps, type(numerii[1]))
                    break

        listone = list(map(float, numerii))
        listariella = list(map(lambda x: str(abs(x)*10e3), listone))
        # print(listone, type(listone[0]))

        with open(f"Timeseries_original_updated_with_positives/evapLoss_{ii}.txt", "w") as testo2:

            testo2.writelines(header)

            for gino in range(len(numerii)):

                testo2.writelines(timestamps[gino] + listariella[gino] + '\n')

    shutil.copytree("Timeseries/Initialize_Loop", "PROVADIR_2", dirs_exist_ok=True)


def writing_spillage_effs():
    with open("Timeseries/evapLoss_KA.txt", "r") as testo:

        linee = testo.readlines()

        blocca_alla_riga = 10e100  # 3  # to debug

        numerii, timestamps = [], []
        for numero, gee in enumerate(linee):

            if numero == 0:
                header = gee
                continue  # salvate le le intestazioni

            timestamps.append(gee[:20])

            if numero == blocca_alla_riga:
                print(numerii, timestamps, type(numerii[1]))
                break

    for ii in ['A', 'B', 'C', 'D']:  # ci sono 4 tecnologie di spillage (A, B, C, D) tra la Zambia e il Mozambico
        with open(f"Timeseries/spillage{ii}_eff.txt", "w") as testo2:

            if ii == 'D':
                testo2.writelines(header.replace('Zambia', 'Moz-North-Center'))
            else:
                testo2.writelines(header)

            for gino in range(len(timestamps)):
                testo2.writelines(timestamps[gino] + '0' + '\n')


def get_latest_file_or_folder_from_directory(directory: str, last=-1):
    '''
    Returns the "last"th-latest file/folder (modified/created) in a directory of folders (if last=-1 is the latest)
    '''

    list_of_folders = glob.glob(directory.strip(r"\ /") + '/*')  # * means all, if needed a specific format then *.csv

    # list_of_folders.remove('Results\\results_debug')
    # latest_folder = max(list_of_folders, key=os.path.getctime)

    latest_folder = sorted(list_of_folders, key=os.path.getctime)[last]

    return latest_folder


def apply_plot_function_to_all_results():
    import calliope
    from plotting_fausto import plotting

    all_results = []
    for folders in glob.glob('Results/*'):
        if folders != 'Results\\results_debug':  # excluding the results_debug folder
            for folder in glob.glob(f'{folders}/*'):
                (all_results.append(folder) if folder[-4:] != '.txt' else None)

    for result in all_results:
        model = calliope.read_netcdf(f'{result}\\model.nc')
        plots_folder = f'{result}\\plots\\'

        plotting.FaPlotting(model).plot_storage_and_carriers(path=plots_folder)
