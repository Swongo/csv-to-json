import csv
import json
import sys

try:
    csvfile = open(sys.argv[1], 'r')
    jsonfile = open(sys.argv[2], 'w')
    delimiterType = (sys.argv[3])
    columnName = (sys.argv[4:])

    reader = csv.DictReader(csvfile, columnName, delimiter=delimiterType, quoting=csv.QUOTE_NONE)

    output = list(reader)

    for row in output:
        if row == output[-1]:
            json.dump(row, jsonfile)
            jsonfile.write(']')
        elif row == output[0]:
            jsonfile.write('[')
            json.dump(row, jsonfile)
            jsonfile.write(',\n')
        else:
            json.dump(row, jsonfile)
            jsonfile.write(',\n')

    print(sys.argv[2] + " created")

except Exception:
    print("Usage: specifiy input output delimiter columns -> ex. py CsvToJson.py \'Input.csv\' \'Output.json\' \',\' \'Id' 'Firstname' 'Lastname\' ")