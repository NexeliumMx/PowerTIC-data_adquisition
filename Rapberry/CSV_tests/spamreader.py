import csv
with open('/home/luis08islas/VScode/PowerTIC/Rapberry/CSV_tests/measurement_address.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))
