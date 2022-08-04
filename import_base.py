import csv
import base

def import_csv_format(file_name):
    import_csv = open(file_name, 'r')
    value = csv.reader(import_csv)
    temp = []
    for row in value:
        if row != []:
            temp.append(''.join(row))
        else:
            base.write_base(temp)
            temp = []
    import_csv.close()