import csv
import re

from mock.mock import self
from numpy.core.defchararray import splitlines
from operator import itemgetter
from collections import OrderedDict
from pprint import pprint
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

class UserX:
    def __init__(self, x):
        # 이게 찾고자하는 USER에 대한 데이터 찾는 과정
        self.FindUserX(x)

    def FindUserX(self, x):
        #user 당 최신 데이터 10곡씩 뽑는 코드
        with open('D:\\CountMusicAll.txt', newline='', encoding="utf8") as csvfile:
            origindata = csv.reader(csvfile, delimiter=' ', quotechar='\t')

            count = 0
            self.UserX_Data = list()
            xcount =0
            for row in origindata:
                line = ' '.join(row)
                word = ', '.join(row)[0:11]
                f = open("D:\\SmallDataT_10.txt", 'a', encoding="utf-8")
                if re.search(x, line):

                    A = UserY(line)

                    if count < 10:
                        count = count + 1
                    elif count < 20:
                        print(A)
                        WriteLine = "%s\t%s\t%s\n" % (A.UserID, A.DataID, A.CountNumber)
                        f.write(WriteLine)
                        count += 1
                else :
                    print("word %s x %s" %(word, x))
                    if word != x :
                        x = word
                        xcount += 1
                        count = 0
                        if xcount == 11:
                            break

    def WriteFile(self, line):
        with open('D:\\SmallData.txt', newline='', encoding="utf8") as csvfile:
            SmallData = csv.reader(csvfile, delimiter=' ', quotechar='\t')

            A = UserY(line)
            WriteLine = "%s %s %s \n" % (A.UserID, A.DataID, A.CountNumber)
            SmallData.write(WriteLine)

    def compare(self):
        # UserX의 최근 데이터를 보고 UserYs를 찾는 과정
        array0 = list()
        array1 = list()
        array0 = self.FindUserYs(self.UserX_Data, 0)
        array1 = self.FindUserYs(self.UserX_Data, 1)
        #최종 UserYs 를 출력
        print(set(array0) & set(array1))

    def FindUserYs(self, ListenList , x):
        #print(self.UserX_Data[0])
        # list 에서 findall 로 해당 id 를 가진 user 찾아서 저장.
        self.userYlist = list()
        with open('D:\\CountMusicAll.txt', newline='', encoding="utf8") as csvfile:
            origindata = csv.reader(csvfile, delimiter=' ', quotechar='\t')

            for row in origindata:
                line = ' '.join(row)
                Y = UserY(line)
                print(line)
                if self.UserX_Data[x] in Y.DataID:
                    # userYlist 중복체크
                    if Y.UserID not in self.userYlist:
                        self.userYlist.append('%s'%Y.UserID)
                        print('user ID: %s' %Y.UserID)

            #print(self.userYlist)
        return self.userYlist
            #similar user 찾기

class MostListen():
        with open('D:\\CountMusicAll.txt', newline='', encoding="utf8") as csvfile:
            origindata = csv.reader(csvfile, delimiter=' ', quotechar='\t')

            for row in origindata:
                line = ' '.join(row)
                Y = UserY(line)

                d = {Y.DataID: Y.CountNumber}
                #print(Y.UserID)

                if(Y.UserID =='user_000002'):
                    d.update({Y.DataID:Y.CountNumber})
                if(Y.UserID =='user_000004'):
                    break
            OrderedDict(sorted(d.items(), key=lambda t:t[1]))
            pprint(d)


#찾고자하는 UserX를 괄호 안에 넣는다.
UserX('user_000001')
#FindUserYs('user_000002')
#MostListen()
#최근에 들은 10곡의 횟수

