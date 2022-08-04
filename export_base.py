import csv

def export_csv_format():
    view_csv = open("guide.csv", 'r')
    export_csv = open("export.csv", 'w')
    s = csv.reader(view_csv)
    for row in s:
        for i in ''.join(row).split():
            export_csv.write(i + '\n')
        export_csv.write('\n')
    export_csv.close()
    view_csv.close()