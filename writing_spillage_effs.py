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
