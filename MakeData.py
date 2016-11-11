import csv
import re
import split
import time
import OpenFile

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
                    del UserList[X.UserID]
                    break

                if X.UserID not in UserList :
                    i = i+1

                    UserList['%s' %X.UserID] = 1
                    UserList[word] = HowManyListen

                    #print('%s %s %s' % (X.UserID, word, UserList[word] ))

                    HowManyListen = 0
                    TrainingCount = 0
                    wordcount = wordcount +1
                    word = X.UserID

                else :
                    if TrainingCount < self.TrainingData:
                        # 주어진 training 개수만큼 array 배열에 사용자가 최근에 들은 순서대로 musicid  저장
                        if re.search(X.UserID, line) :
                            if X.MusicID not in MusicList:
                                #사용자 X가 들은 음악이 musiclist에 없으면 추가하기
                                MusicList['%s' % X.MusicID] = 1
                                TrainingCount = TrainingCount + 1
                                #print('%s %s' %(X.MusicID, MusicList[X.MusicID]))

start_time = time.time()
MusicList= {} #테스트를 위한 음악 list
UserList = {} #테스트에 사용된 사용자 목록
MakeFile = reprocess(101, 1001, 5, 10)
MakeFile.LoadData()
print(len(MusicList))
print(UserList)
#df = DataFrame(dictionary_list).T.fillna(0)
#print(dictionary_list)
#pprint(df)
#print(np.multiply())
print("---------------%s seconds-----------"% (time.time() - start_time))