import run_perceptron
import os
import CsvFormater

sms_features_file_name = "features.csv"
sms_tags_file_name = "tags.csv"

email_features_file_name = "featuresEmail.csv"
email_tags_file_name = "tagsEmail.csv"

num_of_runs = 10

if (os.path.exists(sms_features_file_name)):
    os.remove(sms_features_file_name)
CsvFormater.create_files()
avarge = 0
for i in range (num_of_runs):
    avarge += run_perceptron.run(email_features_file_name, email_tags_file_name)
print(avarge/num_of_runs)
#run_perceptron.run(email_features_file_name, email_tags_file_name)
#run_perceptron.run(sms_features_file_name, sms_tags_file_name)

