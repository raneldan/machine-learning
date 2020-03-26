import csv

filename = "SMSSpamCollection"

with open(filename,'r',encoding="utf8") as csvin,\
        open('tags.csv', 'w', newline='', encoding='utf-8') as csvoutForTags,\
            open('data.csv', 'w', newline='', encoding='utf-8') as csvoutForData:
    csvin = csv.reader(csvin, delimiter='\t')
    csvoutForTags = csv.writer(csvoutForTags)
    csvoutForData = csv.writer(csvoutForData)
    for row in csvin:
        csvoutForTags.writerow([row[0]])
        csvoutForData.writerow(row[1:])
