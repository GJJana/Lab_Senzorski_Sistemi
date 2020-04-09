import csv
import math
import matplotlib.pyplot as plt

list = []
with open('sensor.csv', 'r') as file:
    reader = csv.reader(file)
    next(file)
    for row in reader:
        list.append(row[4])
    list_freq3 = []
    list_freq5 = []
    for i in range(0, len(list), 3):
        list_freq3.append(list[i])
    for i in range(0, len(list), 5):
        list_freq5.append(list[i])

    # threshoold 3 stepeni
    threshold = [0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3]

    # LA

    list_sent = []
    list_MSE = []
    for t in threshold:
        # graf algoritam
        sent = 1
        list_values = []
        list_values.append(list[0])
        # graf MSE
        MSE = 0
        for m in range(1, len(list)):
            if math.fabs(float(list[m]) - float(list_values[m - 1])) >= t:
                sent += 1
                list_values.append(list[m])
            else:
                list_values.append(list_values[m - 1])
            MSE =float(MSE)+ pow(float(list[m]) - float(list_values[m]), 2)

        list_MSE.append(float(MSE) / len(list))
        list_sent.append(sent * 100 / len(list))

    # freq3
    listfreq3_sent = []

    for t in threshold:
        # graf algoritam
        sent = 1
        list_values = []
        list_values.append(list_freq3[0])

        for m in range(1, len(list_freq3)):
            if math.fabs(float(list_freq3[m]) - float(list_values[m - 1])) >= t:
                sent += 1
                list_values.append(list_freq3[m])
            else:
                list_values.append(list_values[m - 1])

        listfreq3_sent.append(sent * 100 / len(list_freq3))


    # freq5
    listfreq5_sent = []
    for t in threshold:
        # graf algoritam
        sent = 1
        list_values = []
        list_values.append(list_freq5[0])

        for m in range(1, len(list_freq5)):
            if math.fabs(float(list_freq5[m]) - float(list_values[m - 1])) >= t:
                sent += 1
                list_values.append(list_freq5[m])
            else:
                list_values.append(list_values[m - 1])

        listfreq5_sent.append(sent * 100 / len(list_freq5))


    # MA

    list_sent1 = []
    list_MSE1 = []

    for t in threshold:
        # algoritam
        list_values1 = []
        list_values1.append(list[0])
        list_values1.append(list[1])
        sent1 = 2
        # MSE graf
        MSE1 = 0
        for k in range(2, len(list)):
            avg = round(float((float(list_values1[k - 2]) + float(list_values1[k - 1])) / 2), 1)
            if math.fabs(avg - float(list[k])) >= t:
                sent1 += 1
                list_values1.append(list[k])
            else:
                list_values1.append(avg)
            MSE1=float(MSE1)+ pow(float(list[k]) - float(list_values1[k]), 2)
        list_MSE1.append(float(MSE1) / len(list))

        list_sent1.append(sent1 * 100 / len(list))

    # freq3
    listfreq3_sent1 = []
    for t in threshold:
        # algoritam
        list_values1 = []
        list_values1.append(list_freq3[0])
        list_values1.append(list_freq3[1])
        sent1 = 2
        for k in range(2, len(list_freq3)):
            avg = round(float((float(list_values1[k - 2]) + float(list_values1[k - 1])) / 2), 1)
            if math.fabs(avg - float(list_freq3[k])) >= t:

                sent1 += 1
                list_values1.append(list_freq3[k])
            else:
                list_values1.append(avg)

        listfreq3_sent1.append(sent1 * 100 / len(list_freq3))

    # freq5

    listfreq5_sent1 = []
    for t in threshold:
        # algoritam
        list_values1 = []
        list_values1.append(list_freq5[0])
        list_values1.append(list_freq5[1])
        sent1 = 2
        for k in range(2, len(list_freq5)):
            avg = round(float((float(list_values1[k - 2]) + float(list_values1[k - 1])) / 2), 1)
            if math.fabs(avg - float(list_freq5[k])) >= t:

                sent1 += 1
                list_values1.append(list_freq5[k])
            else:
                list_values1.append(avg)

        listfreq5_sent1.append(sent1 * 100 / len(list_freq5))





    # graf algritmi
    # x oska ->threshold
    # y oska ->list_sent i list_sent1

    plt.figure(num='LA vs MA(2)')
    plt.plot(threshold, list_sent, label='LA', color='#ded007')
    plt.plot(threshold, list_sent1, label='MA(2)', color='#4c29ab')
    plt.legend()
    plt.xlabel('THRESHOLD')
    plt.ylabel('DATA_SENT(%)')
    plt.title('LP/MA(2)')
    plt.show()

    # graf frekfencii
    # x oska ->threshold
    # y oska ->listfreq3_sent i listfreq5_sent i list_sent
    plt.figure(num='Frequency')
    plt.plot(threshold, list_sent,label='Frequency 1',color='#61b50c')
    plt.plot(threshold, listfreq3_sent,label='Frequency 3', color='#3669e0')
    plt.plot(threshold, listfreq5_sent,label='Frequency 5', color='#d9370e')
    plt.legend()
    plt.xlabel('THRESHOLD')
    plt.ylabel('DATA_SENT(%)')
    plt.title('LP - Frequency')
    plt.show()

    plt.figure(num='Frequency')
    plt.plot(threshold, list_sent1,label='Frequency 1',color='#61b50c')
    plt.plot(threshold, listfreq3_sent1,label='Frequency 3', color='#3669e0')
    plt.plot(threshold, listfreq5_sent1,label='Frequency 5', color='#d9370e')
    plt.legend()
    plt.xlabel('THRESHOLD')
    plt.ylabel('DATA_SENT(%)')
    plt.title('MA(2)- Frequency')
    plt.show()


    # graf MSE
    #x oska-> threshold
    # y oska->list_MSE i list_MSE1
    plt.figure(num='MSE')
    plt.plot(threshold, list_MSE, label='LA MSE', color='#ff4400')
    plt.plot(threshold, list_MSE1, label='MA(2) MSE', color='#1ea84c')
    plt.legend()
    plt.xlabel('THRESHOLD')
    plt.ylabel('MSE')
    plt.title('LP/MA(2) MSE')
    plt.show()

