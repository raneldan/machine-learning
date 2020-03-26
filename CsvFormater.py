import csv
from rowToVector import RowToVector

filename = "SMSSpamCollection"

with open(filename,'r',encoding="utf8") as csvin,\
        open('tags.csv', 'w', newline='', encoding='utf-8') as csvoutForTags,\
            open('data.csv', 'w', newline='', encoding='utf-8') as csvoutForData,\
                 open('features.csv', 'w', newline='', encoding='utf-8') as csvoutForFeatures:
    csvin = csv.reader(csvin, delimiter='\t')
    csvoutForTags = csv.writer(csvoutForTags)
    csvoutForData = csv.writer(csvoutForData)
    csvoutForFeatures = csv.writer(csvoutForFeatures)
    for row in csvin:
        csvoutForTags.writerow([row[0]])
        csvoutForFeatures.writerow(RowToVector(row[1:]))
