#Step 1: takes raw message csv and removes tags and puts messages into one line saves new csv in cleanData folder

import re
import csv

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

with open('./relevantInfo/core_message_posts.csv') as csvfile, open("./cleanData/clean_core_message_posts.csv", 'w') as f_out:
  writer = csv.writer(f_out, delimiter='|')
  csv_reader = csv.reader(csvfile, delimiter=',')
  header = next(csv_reader)
  writer.writerow(["message","ip","author"])
  for row in csv_reader:
    writer.writerow([cleanhtml(row[3]).replace("\n", " "),row[6],row[5]])