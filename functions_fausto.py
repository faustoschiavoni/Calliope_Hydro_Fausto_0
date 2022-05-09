import datetime
import smtplib


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

