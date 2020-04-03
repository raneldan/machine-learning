import run_perceptron
import os
import CsvFormater
import matplotlib.pyplot as plt

sms_features_file_name = "features.csv"
sms_tags_file_name = "tags.csv"

email_features_file_name = "featuresEmail.csv"
email_tags_file_name = "tagsEmail.csv"

num_of_runs = 6

if (os.path.exists(sms_features_file_name)):
    os.remove(sms_features_file_name)
CsvFormater.create_files()
average = []
for i in range (num_of_runs):
    average.append(run_perceptron.run(email_features_file_name, email_tags_file_name))

print(sum(average) / len(average))
plt.axis([0, num_of_runs, min(average) - 5, max(average) + 5])
plt.plot(average, marker='o', color='g', linewidth=2.0)
plt.ylabel('perceptron  on emails')
plt.xlabel('test number')
plt.ylabel('sucsses rate')
plt.show()
#run_perceptron.run(email_features_file_name, email_tags_file_name)
#run_perceptron.run(sms_features_file_name, sms_tags_file_name)

