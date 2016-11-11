import csv
import re
from pandas import *
from mock.mock import self
from numpy.core.defchararray import splitlines
from operator import itemgetter
from collections import OrderedDict
from pprint import pprint
import numpy as np
import time

class divide:
    #line 받아와서 uid 만 따로 떼 내는 작업
    def __init__(self, *args):  # 생성자 / 객체 생성시 호출되며, GuestID 필요로 한다
        word = args[0]
        self.UserID = word.split('\t')[0]
        self.TimeStamp = word.split('\t')[1]
        self.ArtistID = word.split('\t')[2]
        self.ArtistName = word.split('\t')[3]
        self.MusicID = word.split('\t')[4]
        self.MusicName = word.split('\t')[5]

#    def __del__(self):  # 소멸자 / 객체 소멸시 호출
#        print("User Out")

    def __str__(self):
        return "UserX: %s, TimeStamp: %s, ArtistID: %s, ArtistName: %s, MusicID: %s, MusicName: %s" % (self.UserID, self.TimeStamp, self.ArtistID, self.ArtistName, self.MusicID, self.MusicName)

class UserY:
    def __init__(self, *args):
        word = args[0]
        self.UserID = word.split('\t')[0]
        self.DataID = word.split('\t')[1]
        self.CountNumber = word.split('\t')[2]

    def __str__(self):
        return "UserID : %s, DataID : %s, CountNumber: %s" %(self.UserID, self.DataID, self.CountNumber)

class MakeList:
    def __init__(self):
        # 이게 찾고자하는 USER에 대한 데이터 찾는 과정
        self.FindUserX()

    def FindCount(self, UserID, MusicID):

        with open('D:\\CountMusicAll.txt', newline='', encoding="utf8") as csvfile:
            origindata = csv.reader(csvfile, delimiter=' ', quotechar='\t')

            for row in origindata:
                line = ' '.join(row)
                Y = UserY(line)

                if re.search(UserID, line):
                    if re.search(MusicID, line):
                        return Y.CountNumber

    def FindUserX(self):
        with open('D:\\SmallDataT_10.txt', newline='', encoding="utf8") as csvfile:
            origindata = csv.reader(csvfile, delimiter=' ', quotechar='\t')

            count = 0
            self.UserX_Data = list()

            for row in origindata:
                line = ' '.join(row)
                word = ', '.join(row)[0:11]
                OriginData = UserY(line)
                print("UserID: %s" %OriginData.UserID)
                CountData = self.FindCount(OriginData.UserID, OriginData.DataID)
                dictionary_list['%s' %OriginData.DataID] ={'%s'%OriginData.UserID : CountData}

#            print(len(dictionary_list))
start_time = time.time()
dictionary_list = {}
MakeList()
#df = DataFrame(dictionary_list).T.fillna(0)
#print(dictionary_list)
#pprint(df)
#print(np.multiply())
print(dictionary_list.items())
print("---------------%s seconds-----------"% (time.time() - start_time))
