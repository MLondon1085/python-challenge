import os
import csv

PyPoll_csv_path = os.path.join('..', 'PyPoll', 'election_data.csv')


with open(PyPoll_csv_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

