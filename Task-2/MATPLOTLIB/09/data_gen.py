import csv
import random
import time

x_value = 0  # here x is the series number from which it starts the series
total_1 = 1000
total_2 = 1000

fieldnames = ["x_value", "total_1", "total_2"]


with open('data9.csv', 'w') as csv_file:  # w is used for the write option
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

    with open('data9.csv', 'a') as csv_file:  # here a means append data
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "x_value": x_value,
            "total_1": total_1,
            "total_2": total_2
        }

        csv_writer.writerow(info)
        print(x_value, total_1, total_2)

        x_value += 1
        total_1 = total_1 + random.randint(-2, 7)
        total_2 = total_2 + random.randint(-4, 9)

    time.sleep(1)  # this is the time gap which is taken before each operation
