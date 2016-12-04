# ******************************************************#
#   Random Walk 2 step**********************************#
#   Create Matrix And Selecte Top K                     #
#   Use split File  ************************************#
# ******************************************************#

import re
import split
import numpy as np
from collections import OrderedDict
import operator
import time


class MakeMatrix:
    def __init__(self, TopK):
        self.MusicList = {}
        self.Top_K = TopK
        print("This Is Matrix For Random Walk")

    def LoadFile(self):
        #File Open
        ReadMusicList = open("MusicList.txt", 'r', encoding="utf-8")
        MusicListLine = ReadMusicList.readlines()

        for line in MusicListLine:
            #print(line)
            X = split.LoadMusicList(line)
            #print("%s %s" %(X.MusicID, X.Count))
            self.MusicList["%s"%X.MusicID] = X.Count

        #self.Multiply()

    def Multiply(self):
        print("This Is Multiply")
        b = np.matrix(self.MusicList)
        #np.set_printoptions(threshold=np.nan)  # 매트릭스 전체 출력하기

        # print(b*(b.T*b))
        #b = b * (b.T * b)
        print(b)

    def Selection(self):
        print("This is Selection")
        TopKCount =0
        #임시로 MusicList로 테스트 해보자.
        # operator,itemgetter() 에서 0은 key를 기준으로 정렬, 1은 value를 기준으로 정렬
        # reverse 가 True 이면 작은 값부터 출력됨. #sorted_x = sorted(self.MusicList.items(), key=operator.itemgetter(1), reverse=True)
        sorted_x = sorted(self.MusicList.items(), key=operator.itemgetter(1))

        #print(sorted_x)

        for select in sorted_x:
            if float(select[1]) != 0.0 :
                TopKCount = TopKCount + 1

                print("%s %s" %(select[0], select[1]))

                if TopKCount >= self.Top_K:
                    break

    def Compare(self):
        print("This is Compare Top K and Test Data")

        ReadTestList = open("TestList.txt", 'r', encoding="utf-8")
        TestLine = ReadTestList.readlines()

        ReadTrainingList = open("MusicList.txt", 'r', encoding="utf-8")
        TrainingLine = ReadTrainingList.readlines()

        for Training in TrainingLine:
            B = split.LoadMusicList(Training)
            for Test in TestLine:
                #print(line)
                T = split.LoadMusicList(Test)
                print("%s %s" %(T.MusicID,T.Count))
                if T.MusicID == B.MusicID:
                    print("MID : %s TestCount : %s, Result: %s" %(T.MusicID, T.Count, B.Count))







################################
#   Run Run Run Run Run Run    #
################################
start_time = time.time()

Read = MakeMatrix(10)
#               Top K
Read.LoadFile()
Read.Selection()
#Read.Compare()
print("---------------%s seconds-----------"% (time.time() - start_time))

