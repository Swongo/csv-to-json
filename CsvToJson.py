import csv
import json
import sys

try:
    csvfile = open(sys.argv[1], 'r')
    jsonfile = open(sys.argv[2], 'w')
    delimiterType = (sys.argv[3])
    fieldnamesArgs = (sys.argv[4:])

    reader = csv.DictReader(csvfile, fieldnamesArgs, delimiter=delimiterType, quoting=csv.QUOTE_NONE)

    for row in reader:
        json.dump(row, jsonfile)
        jsonfile.write('\n')

    print(sys.argv[2] + " created")

except Exception:
    print("Usage: specifiy input output delimiter fieldnames -> ex. py CsvToJson.py \'Input.csv\' \'Output.json\' \',\' \'Id' 'Firstname' 'Lastname\' ")