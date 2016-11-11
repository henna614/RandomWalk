import csv
import sys
import pandas
import re
import split

count = 0
count_word = 0
userid = "user_000001"

def OpenData(self):

    with open('testdata.tsv', newline='', encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='\t')

        for row in spamreader:
            word = ', '.join(row)[0:11] #user id 자르는거. 0:11 번째까지.
    #        print(', '.join(row)[0:10])
            line =  ', '.join(row)

            f = open("D:\\write.txt", 'a', encoding="utf-8")

            if userid != word:
                WriteLine = "%s, %d \n" %(userid, count)
                f.write(WriteLine)
                count_word += 1
                userid = word
                count = 0
            f.close()

            count += len(re.findall(r"%s" % word, line))
