import csv
from rowToVector import RowToVector

filenameSms = "SMSSpamCollection"
filenameEmail = "spam_ham_dataset.csv"

def create_files():
    create_email_files()
    create_sms_files()

def create_email_files():
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
            csvoutForData.writerow([row[2]])
            csvoutForFeatures.writerow(RowToVector([row[2]]).vector)

def create_sms_files():
    with open(filenameSms, 'r', encoding="utf8") as csvin,\
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
