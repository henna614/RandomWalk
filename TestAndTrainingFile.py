# ******************************************************#
#   Random Walk 1 step**********************************#
#   Make Test And Training File                         #
#   Use Split File     *********************************#
# ******************************************************#

import numpy as np
import split
import csv
import time
import re

class AllMusicFile:

    def __init__(self, UserID, Tu, q, Iu):
        # UserID : test 하고 자 하는 User의 ID
        # Tu : Test Item 개수
        # q: 전체 Item 개수
        # Iu : 사용자가 본 item 개수

        self.UserID = UserID
        self.Tu = Tu
        self.q = q
        self.Iu =Iu
        self.MusicList = {}
        self.TestList = {}
        self.ListenCount = 0
        print("Make Music List Text File and Matrix")

    def LoadData(self):
        #file로 부터 데이터 line 읽어 들이기
        TotalMusicNumber =0
        UserCount = 0
        TestCount = 0
        with open('C:\\Users\\HelloHenna\\Desktop\\project_test\\Data\\testdata.tsv', newline='', encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='\t')

            for row in spamreader:
                line = ' '.join(row)
                X = split.divide(line)

                if re.search(self.UserID, line):
                    self.ListenCount = self.ListenCount + 1
                    if X.MusicID == '':
                        # print('null ')
                        continue
                    if UserCount > self.Iu :
                        #사용자가 본 item 개수 제한
                        continue
                    else:
                        # print("%s %s" %(self.Tu, TestCount))
                        if TestCount < self.Tu:
                            # Test List 따로 뽑아내는 작업
                            TestCount = TestCount + 1
                            self.TestList['%s' % X.MusicID] = 1
                            #print("%s %s" %(TestCount, X.MusicID))

                        UserCount = UserCount + 1
                        if X.MusicID in self.MusicList:
                            self.MusicList['%s' % X.MusicID] += 1
                        else:
                            self.MusicList['%s' % X.MusicID] = 1
                            TotalMusicNumber = TotalMusicNumber + 1

                else :
                    if X.MusicID not in self.MusicList:
                        self.MusicList['%s' % X.MusicID] = 0
                        TotalMusicNumber = TotalMusicNumber + 1
                    """
                    # 사용자 X 가 들은 곡 이외의 값들은 0의 값을 가지고 곡 목록만 추가 됨
                    if X.MusicID in self.MusicList:
                        self.MusicList['%s' % X.MusicID] += 1
                    else:
                        self.MusicList['%s' % X.MusicID] = 1
                        TotalMusicNumber = TotalMusicNumber + 1
                """
                if TotalMusicNumber >= self.q :
                    # 전체 item 개수를 넘으면 break
                    break

            #print("Listen Count %s" %self.ListenCount)
            #print("%s" %len(self.MusicList))

    def SaveData(self):
        WriteMusicList = open("MusicList.txt", 'w', encoding="utf-8")
        WriteTestLine = open("TestList.txt", 'w', encoding="utf-8")
        print("TestList %s \nListen Count - Tu \n%s - %s = %s" %(len(self.TestList),self.ListenCount, self.Tu, self.ListenCount-self.Tu))
        for MusicID in self.MusicList.keys():
            if MusicID == '':
                # print('null ')
                continue

            WriteLine = "%s\t%s\t\n" % (MusicID, self.MusicList[MusicID]/(self.ListenCount - self.Tu))

            for TestID in self.TestList.keys():
                #print(TestID)
                if MusicID == TestID:
                    TestLine = "%s\t%s\t\n" % (MusicID, self.MusicList[MusicID])
                    WriteTestLine.write(TestLine)
                    WriteLine = "%s\t%s\t\n" % (MusicID, 0)
                    #print(WriteLine)

            #File 에 쓰기.
            WriteMusicList.write(WriteLine)

    def __del__(self):
        self.MusicList.clear()
        self.TestList.clear()
        print("delete Music List Matrix")






################################
#   Run Run Run Run Run Run    #
################################

start_time = time.time()
MakeFile = AllMusicFile("user_000001", 10, 1000, 100)
#                          UserID,     Tu,     q,  Iu
MakeFile.LoadData( )
MakeFile.SaveData()
print("---------------%s seconds-----------"% (time.time() - start_time))














