import run_perceptron
import os
import CsvFormater
import matplotlib.pyplot as plt
from typing import List
from datetime import datetime

number_of_features = 12
max_features_to_ignore = 4

sms_features_file_name = "features.csv"
sms_tags_file_name = "tags.csv"

email_features_file_name = "featuresEmail.csv"
email_tags_file_name = "tagsEmail.csv"


def get_cur_time() -> str:
    now = datetime.now()
    return str(now.strftime("%d_%m_%Y_%H_%M_%S"))


def run_once(num_of_runs: int, ignore_features_lst: List[int] = [], result_file_name: str = "res"):
    if os.path.exists(sms_features_file_name):
        os.remove(sms_features_file_name)
    if os.path.exists(email_features_file_name):
        os.remove(email_features_file_name)

    CsvFormater.create_files(ignore_features=ignore_features_lst)
    average = []
    for i in range(num_of_runs):
        average.append(run_perceptron.run(email_features_file_name, email_tags_file_name))
    ignore_features_str = '_'.join(str(x) for x in ignore_features_lst)
    print("sum is:"+str(sum(average) / len(average))+" for ignoring" + ignore_features_str)
    plt.axis([0, num_of_runs, min(average) - 5, max(average) + 5])
    plt.plot(average, marker='o', color='g', linewidth=2.0)
    plt.ylabel('perceptron  on emails')
    plt.xlabel('test number')
    plt.ylabel('sucsses rate')
    plt.savefig(
        "results/" + result_file_name + ignore_features_str + '_' + get_cur_time() + ".pdf")


def main():
    num_of_runs_per_feature_set = 6
    run_once(num_of_runs_per_feature_set)
    for x in range(number_of_features):
        for y in range(x + 1, number_of_features + 1):
            features_to_ignore = [x, y]
            run_once(num_of_runs_per_feature_set, ignore_features_lst=features_to_ignore)
    # run_perceptron.run(email_features_file_name, email_tags_file_name)
    # run_perceptron.run(sms_features_file_name, sms_tags_file_name)


if __name__ == "__main__":
    main()
