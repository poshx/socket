import csv

f = open('motorista.csv')
csv_f = csv.reader(f)
data = []

for row in csv_f:
    data.append(row)
f.close()

print(data[1:])

def convert_row(row):
    return """<Employee>
    <accountNumber>%s</accountNumber>
    <name>%s</name>
    <areaCode>%s</areaCode>
    <country>%s</country>
</Employee>""" % (row[0], row[1], row[2], row[3])

with open('output.xml', 'w') as f:
    f.write('\n'.join([convert_row(row) for row in data]))