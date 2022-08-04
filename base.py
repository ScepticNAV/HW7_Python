import csv

def view_base():
    view_csv = open("guide.csv", 'r')
    n = csv.reader(view_csv)
    for row in n:
        print(*row)
    view_csv.close()

def check_base(value):
    view_csv = open("guide.csv", 'r')
    n = csv.reader(view_csv)
    for row in n:
        if [' '.join(value)] == row:
            check_status = False
            break
    else:
        check_status = True
    view_csv.close()
    return check_status

def write_base(value):
    if check_base(value):
        value = ' '.join(value)
        data_csv = open("guide.csv", 'a')
        data_csv.write(f'{value}\n')
        data_csv.close()


