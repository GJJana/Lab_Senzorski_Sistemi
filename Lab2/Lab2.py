import csv
import math
import matplotlib.pyplot as plt

list = []
listsec = []
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

    # vtor parmetar
    file.seek(0)
    next(file)
    for row in reader:
        listsec.append(row[7])
    listsec_freq3 = []
    listsec_freq5 = []
    for i in range(0, len(listsec), 3):
        listsec_freq3.append(listsec[i])
    for i in range(0, len(listsec), 5):
        listsec_freq5.append(listsec[i])

    # threshoold 3 stepeni
    threshold = [0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3]
    threshold1 = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5]
    print(len(list))
    print(len(listsec))
    # LA
    list_sent = []
    list_MSE = []
    for t in range(len(threshold)):
        # graf algoritam
        sent = 1
        list_values = []
        listsec_values = []
        list_values.append(list[0])
        listsec_values.append(listsec[0])
        # graf MSE
        MSE1 = 0
        MSE2=0
        for m in range(1, len(list)):
            if (math.fabs(float(list[m]) - float(list_values[m- 1])) >= threshold[t]) or (
                    math.fabs(float(listsec[m]) - float(listsec_values[m - 1])) >= threshold1[t]):
                sent += 1
                if math.fabs(float(list[m]) - float(list_values[len(list_values) - 1])) >= threshold[t]:
                    list_values.append(list[m])
                else:
                    list_values.append(list_values[m - 1])
                if math.fabs(float(listsec[m]) - float(listsec_values[m - 1])) >= threshold1[t]:
                    listsec_values.append(listsec[m])
                else:
                    listsec_values.append(listsec_values[m - 1])
            else:
                list_values.append(list_values[m - 1])
                listsec_values.append(listsec_values[m - 1])


            MSE1 = float(MSE1) + pow(float(list[m]) - float(list_values[m]), 2)
            MSE2=float(MSE2)+ pow(float(listsec[m]) - float(listsec_values[m]), 2)
        list_MSE.append(float(MSE1) / len(list)+float(MSE2)/len(listsec))
        list_sent.append(sent * 100 / len(list))

    # freq3
    listfreq3_sent = []

    for t in range(len(threshold)):
        # graf algoritam
        sent = 1
        list_values = []
        listsec_values = []
        list_values.append(list_freq3[0])
        listsec_values.append(listsec_freq3[0])
        for m in range(1, len(list_freq3)):
            if math.fabs(float(list_freq3[m]) - float(list_values[m - 1])) >= threshold[t] or math.fabs(
                    float(listsec_freq3[m]) - float(listsec_values[m - 1])) >= threshold1[t]:
                sent += 1
                if math.fabs(float(list_freq3[m]) - float(list_values[m - 1])) >= threshold[t]:
                    list_values.append(list_freq3[m])
                else:
                    list_values.append(list_values[m - 1])
                if math.fabs(float(listsec_freq3[m]) - float(listsec_values[m - 1])) >= threshold1[t]:
                    listsec_values.append(listsec_freq3[m])
                else:
                    listsec_values.append(listsec_values[m - 1])
            else:
                list_values.append(list_values[m - 1])
                listsec_values.append(listsec_values[m - 1])


        listfreq3_sent.append(sent * 100 / len(list_freq3))

    # freq5
    listfreq5_sent = []
    for t in range(len(threshold)):
        # graf algoritam
        sent = 1
        list_values = []
        list_values.append(list_freq5[0])
        listsec_values = []
        listsec_values.append(listsec_freq5[0])

        for m in range(1, len(list_freq5)):
            if math.fabs(float(list_freq5[m]) - float(list_values[m - 1])) >= threshold[t] or math.fabs(
                    float(listsec_freq5[m]) - float(listsec_values[m - 1])) >= threshold1[t]:
                sent += 1
                if math.fabs(float(list_freq5[m]) - float(list_values[m - 1])) >= threshold[t]:
                    list_values.append(list_freq5[m])
                else:
                    list_values.append(list_values[m - 1])
                if math.fabs(float(listsec_freq5[m]) - float(listsec_values[m - 1])) >= threshold1[t]:
                    listsec_values.append(listsec_freq5[m])
                else:
                    listsec_values.append(listsec_values[m - 1])
            else:
                list_values.append(list_values[m - 1])
                listsec_values.append(listsec_values[m - 1])

        listfreq5_sent.append(sent * 100 / len(list_freq5))

    # MA(2)
    list_sent1 = []
    list_MSE1 = []
    for t in range(len(threshold)):
        # algoritam
        list_values1 = [list[0], list[1]]
        listsec_values1 = [listsec[0], listsec[1]]
        sent1 = 2
        # MSE graf
        MSE1 = 0
        MSE2=0
        for k in range(2, len(list)):
            avg = round(float((float(list_values1[k - 2]) + float(list_values1[k - 1])) / 2), 1)
            avg1 = round(float((float(listsec_values1[k - 2]) + float(listsec_values1[k - 1])) / 2), 1)
            if math.fabs(avg - float(list[k])) >= threshold[t] or math.fabs(avg1 - float(listsec[k])) >= threshold1[t]:
                sent1 += 1
                if math.fabs(avg - float(list[k])) >= threshold[t]:
                    list_values1.append(list[k])
                else:
                    list_values1.append(avg)
                if math.fabs(avg1 - float(listsec[k])) >= threshold1[t]:
                    listsec_values1.append(listsec[k])
                else:
                    listsec_values1.append(avg1)
            else:
                list_values1.append(avg)
                listsec_values1.append(avg1)


            MSE1 = float(MSE1) + pow(float(list[k]) - float(list_values1[k]), 2)
            MSE2=float(MSE2)+ pow(float(listsec[k]) - float(listsec_values1[k]), 2)
        list_MSE1.append(float(MSE1) / len(list)+float(MSE2)/len(listsec))
        list_sent1.append(sent1 * 100 / len(list))
    # freq3
    listfreq3_sent1 = []
    for t in range(len(threshold)):
        # algoritam
        list_values1 = [list_freq3[0], list_freq3[1]]
        listsec_values1 = [listsec_freq3[0], listsec_freq3[1]]
        sent1 = 2
        for k in range(2, len(list_freq3)):
            avg = round(float((float(list_values1[k - 2]) + float(list_values1[k - 1])) / 2), 1)
            avg1 = round(float((float(listsec_values1[k - 2]) + float(listsec_values1[k - 1])) / 2), 1)
            if math.fabs(avg - float(list_freq3[k])) >= threshold[t] or math.fabs(avg1 - float(listsec_freq3[k])) >= \
                    threshold1[t]:
                sent1 += 1
                if math.fabs(avg - float(list_freq3[k])) >= threshold[t]:

                    list_values1.append(list_freq3[k])
                else:
                    list_values1.append(avg)
                if math.fabs(avg1 - float(listsec_freq3[k])) >= threshold1[t]:
                    listsec_values1.append(listsec_freq3[k])
                else:
                    listsec_values1.append(avg1)
            else:
                list_values1.append(avg)
                listsec_values1.append(avg1)


        listfreq3_sent1.append(sent1 * 100 / len(list_freq3))

    # freq5

    listfreq5_sent1 = []
    for t in range(len(threshold)):
        # algoritam
        list_values1 = []
        list_values1.append(list_freq5[0])
        list_values1.append(list_freq5[1])
        listsec_values1 = [listsec_freq5[0], listsec_freq5[1]]
        sent1 = 2
        for k in range(2, len(list_freq5)):
            avg = round(float((float(list_values1[k - 2]) + float(list_values1[k - 1])) / 2), 1)
            avg1 = round(float((float(listsec_values1[k - 2]) + float(listsec_values1[k - 1])) / 2), 1)
            if math.fabs(avg - float(list_freq5[k])) >= threshold[t] or math.fabs(avg1 - float(listsec_freq5[k])) >= \
                    threshold1[t]:
                sent1 += 1
                if math.fabs(avg - float(list_freq5[k])) >= threshold[t]:

                    list_values1.append(list_freq5[k])
                else:
                    list_values1.append(avg)
                if math.fabs(avg1 - float(listsec_freq5[k])) >= threshold1[t]:
                    listsec_values1.append(listsec_freq5[k])
                else:
                    listsec_values1.append(avg1)
            else:
                list_values1.append(avg)
                listsec_values1.append(avg1)

        listfreq5_sent1.append(sent1 * 100 / len(list_freq5))

    # MA(3)
    list_sent2 = []
    list_MSE2 = []
    for t in range(len(threshold)):
        # algoritam
        list_values1 = [list[0], list[1], list[2]]
        listsec_values1 = [listsec[0], listsec[1], listsec[2]]
        sent1 = 3
        # MSE graf
        MSE1=0
        MSE2 = 0
        for k in range(3, len(list)):
            avg = round(
                float((float(list_values1[k - 3]) + float(list_values1[k - 2]) + float(list_values1[k - 1])) / 3), 1)
            avg1 = round(
                float((float(listsec_values1[k - 3]) + float(listsec_values1[k - 2]) + float(
                    listsec_values1[k - 1])) / 3), 1)
            if math.fabs(avg - float(list[k])) >= threshold[t] or math.fabs(avg1 - float(listsec[k])) >= threshold1[t]:
                sent1 += 1
                if math.fabs(avg - float(list[k])) >= threshold[t]:

                    list_values1.append(list[k])
                else:
                    list_values1.append(avg)
                if math.fabs(avg1 - float(listsec[k])) >= threshold1[t]:

                    listsec_values1.append(listsec[k])
                else:
                    listsec_values1.append(avg1)
            else:
                list_values1.append(avg)
                listsec_values1.append(avg1)
            MSE1 = float(MSE1) + pow(float(list[k]) - float(list_values1[k]), 2)
            MSE2=float(MSE2)+ pow(float(listsec[k]) - float(listsec_values1[k]), 2)
        list_MSE2.append(float(MSE1) / len(list)+float(MSE2)/len(listsec))
        list_sent2.append(sent1 * 100 / len(list))

    # freq3
    listfreq3_sent2 = []
    for t in range(len(threshold)):
        # algoritam
        list_values1 = [list[0], list[1], list[2]]
        listsec_values1 = [listsec_freq3[0], listsec_freq3[1], listsec_freq3[2]]
        sent1 = 3
        for k in range(3, len(list_freq3)):
            avg = round(
                float((float(list_values1[k - 3]) + float(list_values1[k - 2]) + float(list_values1[k - 1])) / 3), 1)
            avg1 = round(
                float((float(listsec_values1[k - 3]) + float(listsec_values1[k - 2]) + float(
                    listsec_values1[k - 1])) / 3), 1)
            if math.fabs(avg - float(list_freq3[k])) >= threshold[t] or math.fabs(avg1 - float(listsec_freq3[k])) >= \
                    threshold1[t]:
                sent1 += 1
                if math.fabs(avg - float(list_freq3[k])) >= threshold[t]:
                    list_values1.append(list_freq3[k])
                else:
                    list_values1.append(avg)
                if math.fabs(avg1 - float(listsec_freq3[k])) >= threshold1[t]:

                    listsec_values1.append(listsec_freq3[k])
                else:
                    listsec_values1.append(avg1)
            else:
                list_values1.append(avg)
                listsec_values1.append(avg1)

        listfreq3_sent2.append(sent1 * 100 / len(list_freq3))

    # freq5

    listfreq5_sent2 = []
    for t in range(len(threshold)):
        # algoritam
        list_values1 = []
        list_values1.append(list[0])
        list_values1.append(list[1])
        list_values1.append(list[2])
        listsec_values1 = [listsec_freq5[0], listsec_freq5[1], listsec_freq5[2]]
        sent1 = 3
        for k in range(3, len(list_freq5)):
            avg = round(
                float((float(list_values1[k - 3]) + float(list_values1[k - 2]) + float(list_values1[k - 1])) / 3), 1)
            avg1 = round(
                float((float(listsec_values1[k - 3]) + float(listsec_values1[k - 2]) + float(
                    listsec_values1[k - 1])) / 3), 1)
            if math.fabs(avg - float(list_freq5[k])) >= threshold[t] or math.fabs(avg1 - float(listsec_freq5[k])) >= \
                    threshold1[t]:
                sent1 += 1
                if math.fabs(avg - float(list_freq5[k])) >= threshold[t]:
                    list_values1.append(list_freq5[k])
                else:
                    list_values1.append(avg)
                if math.fabs(avg1 - float(listsec_freq5[k])) >= threshold1[t]:

                    listsec_values1.append(listsec_freq5[k])
                else:
                    listsec_values1.append(avg1)
            else:
                list_values1.append(avg)
                listsec_values1.append(avg1)

        listfreq5_sent2.append(sent1 * 100 / len(list_freq5))

    threshold=["0/0", "0.2/0.5", "0.4/1", "0.6/1.5", "0.8/2", "1/2.5", "1.2/3", "1.4/3.5", "1.6/4", "1.8/4.5", "2/5", "2.2/5.5", "2.4/6", "2.6/6.5", "2.8/7", "3/7.5"]
    # graf algritmi
    # x oska ->threshold
    # y oska ->list_sent i list_sent1 i list_sent_2
    plt.figure(num='Frequency - 1 ')
    plt.plot(threshold, list_sent, label='LA', color='red')
    plt.plot(threshold, list_sent1, label='MA(2)', color='green')
    plt.plot(threshold, list_sent2, label='MA(3)', color='navy')
    plt.legend()
    plt.xlabel('THRESHOLD')
    plt.ylabel('DATA_SENT(%)')
    plt.title('LP/MA(2)/MA(3) Frequency 1')
    plt.show()

    # graf frekfencii
    # x oska ->threshold
    # y oska ->listfreq3_sent i listfreq5_sent
    plt.figure(num='Frequency - 3')
    plt.plot(threshold, listfreq3_sent, label='LA', color='red')
    plt.plot(threshold, listfreq3_sent1, label='MA(2)', color='green')
    plt.plot(threshold, listfreq3_sent2, label='MA(3)', color='navy')
    plt.legend()
    plt.xlabel('THRESHOLD')
    plt.ylabel('DATA_SENT(%)')
    plt.title('LP/MA(2)/MA(3) Frequency 3')
    plt.show()
    print(len(listfreq5_sent))
    print(len(listfreq5_sent1))
    print(len(listfreq5_sent2))
    plt.figure(num='Frequency - 5')
    plt.plot(threshold, listfreq5_sent, label='LA', color='red')
    plt.plot(threshold, listfreq5_sent1, label='MA(2)', color='green')
    plt.plot(threshold, listfreq5_sent2, label='MA(3)', color='navy')
    plt.legend()
    plt.xlabel('THRESHOLD')
    plt.ylabel('DATA_SENT(%)')
    plt.title('LA/MA(2)/MA(3) Frequency 5')
    plt.show()

    # graf MSE
    # x oska-> threshold
    # y oska->list_MSE i list_MSE1
    plt.figure(num='MSE')
    plt.plot(threshold, list_MSE, label='LA MSE', color='red')
    plt.plot(threshold, list_MSE1, label='MA(2) MSE', color='#1ea84c')
    plt.plot(threshold, list_MSE2, label='MA(3) MSE', color='navy')
    plt.legend()
    plt.xlabel('THRESHOLD')
    plt.ylabel('MSE')
    plt.title('LP/MA(2)/MA(3) MSE')
    plt.show()
