import csv
import re
import split
import time
import numpy as np
import pandas as pd
from pandas import *
from collections import defaultdict

class reprocess:

    def __init__(self, NumberUser, TrainingData, PopularMusic, TestData):
        self.NumberUser = NumberUser
        self.TrainingData = TrainingData
        self.PopularMusic = PopularMusic
        self.TestData = TestData

    def LoadData(self):
        #file로 부터 데이터 line 읽어 들이기
        i =0
        wordcount = 0

        with open('C:\\Users\\HelloHenna\\Desktop\\project_test\\Data\\testdata.tsv', newline='', encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='\t')
            #word = ', '.join(row)[0:11]  # user id 자르는거. 0:11 번째까지.
            word = "user_000001"
            array = {}
            HowManyListen = 0
            for row in spamreader:
                line = ' '.join(row)
                X = split.divide(line)

                #X.UserID 이런식으로 사용하면 됨.
                HowManyListen = HowManyListen + 1

                if wordcount > self.NumberUser:
                    #초과된 user id 목록에서 삭제
                    print('word count %s' %wordcount)
                    del UserList[X.UserID]
                    #df = DataFrame(UserMusicMatrix).T.fillna(0)
                    #print(df)
                    break

                if X.UserID not in UserList :
                    i = i+1
                    UserMusicMatrix["%s" % X.UserID] = {}
                    UserList['%s' %X.UserID] = 1
                    UserList[word] = HowManyListen
                    #print(UserMusicMatrix)
                    print('UserList[%s] = %s' % (word, UserList[word] ))

                    HowManyListen = 0
                    TrainingCount = 0
                    wordcount = wordcount +1
                    word = X.UserID

                else :
                    #if TrainingCount < self.TrainingData:
                        # 주어진 training 개수만큼 array 배열에 사용자가 최근에 들은 순서대로 musicid  저장
                        if re.search(X.UserID, line) :
                            # 사용자 X가 들은 음악이 musiclist에 없으면 추가하기
                            if X.MusicID in MusicList:
                                MusicList['%s' % X.MusicID] += 1
                            else:
                                MusicList['%s' % X.MusicID] = 1
                                UserMusicMatrix["%s" % X.MusicID] = {}

                            if X.MusicID in UserMusicMatrix[X.UserID]:
                                if X.MusicID == '':
                                    #print('null ')
                                    continue
                                else:
                                    UserMusicMatrix["%s" %X.UserID]["%s" %X.MusicID] += 1
                            else:
                                UserMusicMatrix["%s" % X.UserID]["%s" % X.MusicID] = 1
                                #print('add Music list')
                                #print('UserId %s MusicId %s UserMusicMatrix %s' %(X.UserID, X.MusicID, UserMusicMatrix[X.UserID][X.MusicID]))


    def MusicMatrix(self):
        print('Music Matrix Make')
        matrix = [[0 for j in range(len(MusicList))] for i in range(self.NumberUser)]
        print('Music Matrix start')
        i = 0
        j = 0
        f = open("10_1000_MatrixMultiple.txt", 'a', encoding="utf-8")

        for row in UserList.keys():
            #print('MakeMatrix %s' % row)
            for col in MusicList.keys() :
#                matrix.append(UserMusicMatrix[row][col])
                #print(UserMusicMatrix[row])

                if col not in UserMusicMatrix[row]:
                    matrix[i][j] = 0
                else :
                    #print('%s' %UserList[row])
                    #print('%s\t%s\t%s' %(row, col, UserMusicMatrix[row][col]))
                    #print('%s'%UserMusicMatrix[row][col])
                    matrix[i][j] = (UserMusicMatrix[row][col] / UserList[row])

                j = j+1
            i = i+1
            j = 0

        b = np.matrix(matrix)
        #np.set_printoptions(threshold=np.nan) # 매트릭스 전체 출력하기

        #print(b*(b.T*b))
        b =b*(b.T*b)

        print(b)

    # file 에 Music Id 순서대로 쓰기
        #for col in MusicList.keys():
        #    WriteLine ="%s\t" %col
        #    f.write(WriteLine)

    def ranking(self, Tu, q, Iu ):
        #Tu는 사용자 u에 대한 test item 의 set
        #q 는 I의 개수(Item 개수) , 만들어진 item 개수 여기서는 MusicList의 len
        #Iu 는 사용자 u 와 관련된 모든 아이템 개수
        print("Ranking Start")

        print(q)





start_time = time.time()
MusicList= {} #테스트를 위한 음악 list
UserList = {} #테스트에 사용된 사용자 목록
UserMusicMatrix = {} # MusicList 와 UserList 로 만든 Matrix
MakeFile = reprocess(10, 100, 5, 10)
MakeFile.LoadData()
print("---------------%s seconds-----------"% (time.time() - start_time))
print(len(MusicList))
MakeFile.MusicMatrix()
#UserList.clear()
print("---------------%s seconds-----------"% (time.time() - start_time))
MakeFile.ranking(10, len(MusicList), 1000)
#np.load("test.npy")

