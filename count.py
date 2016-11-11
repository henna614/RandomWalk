import csv
import re
from operator import itemgetter
import operator

from mock.mock import self
from numpy.core.defchararray import splitlines

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

class UserX:
    def __init__(self, x):
        # 이게 찾고자하는 USER에 대한 데이터 찾는 과정
        self.FindUserX(x)


    def FindUserX(self, x):
        with open('D:\\testdata.tsv', newline='', encoding="utf8") as csvfile:
            origindata = csv.reader(csvfile, delimiter=' ', quotechar='\t')

            f = open("D:\\CountMusicSort.txt", 'a', encoding="utf-8")

            self.UserX_Data = list()

            #ArtistID_Count = {}
            #ArtistName_Count = {}
            # MusicName_Count = {}
            MusicID_Count = {}

            UX = x

            for row in origindata:

                line = ' '.join(row)
                #print("%s ********" % x)
                #print(line)

                if re.search(UX, line):
                   #UserX에 대한 Data를 UserX_Data 라는 list에 저장 해 놓은 형태
                   X_TD = divide(line)
                   if X_TD.MusicID not in MusicID_Count:
                       MusicID_Count[X_TD.MusicID] = 1
                   else:
                       print(X_TD.MusicID)
                       MusicID_Count[X_TD.MusicID] += 1

#                   print("%s %s" % (X_TD.MusicID, MusicID_Count[X_TD.MusicID])
                else:
                    Other = divide(line)
                    #print("********************************+++++++++++++++++++++++++++++++++++++++++++++++++++++")
                    UX = Other.UserID

                    #sorted(MusicID_Count.items(), key=operator.itemgetter(1))

                    #for k in sorted(MusicID_Count.keys()):
                        #print(sorted(MusicID_Count.iteritems(), key=itemgetter(1), reverse=True))
                        #WriteLine = "%s\t%s\t%d\n" % (X_TD.UserID, k, MusicID_Count[k])
                        #f.write(WriteLine)

                    MusicID_Count.clear()
                    continue
                print(UX)

    def __del__(self):
        print("delete User data")


#찾고자하는 UserX를 괄호 안에 넣는다.
UserX('user_000001') #UserX에 대한 데이터 뽑는 것 까지만 함
#UserX('user_000002')
#FindUserYs('user_000002')
