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



