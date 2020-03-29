import csv
import re
from rowToVector import RowToVector

filename = "SMSSpamCollection"
filenameEmail = "spam_ham_dataset.csv"

with open(filenameEmail, 'r', encoding="utf8") as csvin, \
        open('tagsEmail.csv', 'w', newline='', encoding='utf-8') as csvoutForTags, \
        open('dataEmail.csv', 'w', newline='', encoding='utf-8') as csvoutForData, \
        open('featuresEmail.csv', 'w', newline='', encoding='utf-8') as csvoutForFeatures:
    csvin = csv.reader(csvin, delimiter=',')
    csvoutForTags = csv.writer(csvoutForTags)
    csvoutForData = csv.writer(csvoutForData)
    csvoutForFeatures = csv.writer(csvoutForFeatures)
    for row in csvin:
        csvoutForTags.writerow([row[1]])
        x = row[2]
        csvoutForData.writerow([row[2]])
        csvoutForFeatures.writerow(RowToVector(row[2]).vector)
        # for word in row:
        #     if (re.search('\"Subject"', word)):
        #         print(row)
        #         buffer = ""
        #     else:
        #         buffer += word

def create_files():
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
            csvoutForData.writerow(row[1:])
            csvoutForFeatures.writerow(RowToVector(row[1:]).vector)
