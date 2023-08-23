import os
import argparse
import json


argparser = argparse.ArgumentParser()
argparser.add_argument("-f", "--file", help="txt file path", required=True, type=str)
argparser.add_argument("-l", help="level", required=True, type=str)
argparser.add_argument("-t", help="theme", required=True, type=str)

args = argparser.parse_args()
file_path = args.file
level = args.l
theme = args.t

if not os.path.exists(file_path):
    print("File not found")
    exit()

with open(file_path) as file:
    words = file.read().split("\n")

with open("most_common_words.json", "r") as file:
    most_common_words = json.load(file)

with open("most_common_words.json", "w") as file:
    if most_common_words.get(level) is None:
        most_common_words[level] = {}
    most_common_words[level][theme] = words
    json.dump(most_common_words, file, indent=4)
