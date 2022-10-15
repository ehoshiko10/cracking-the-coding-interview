#問い：文字列内に存在する空白文字をすべて”%20”で置き換えるメソッド

#最終回答方針：
# ・空のListを作っておく
# ・そこに全角スペースなら％20、全角スペース以外なら元の文字を入れる
# ・最後に"".join()で、stringに変換

#回答作成時間：2時間半。。。


def replaceTwoByteChar(testWord):
    testWordList = list(testWord)   #後の結合のためList化しておく
    print("list化したもの:", testWordList)
    replacedTestWordList = []       #放り込んでいくための空の容器を用意する

    for count in range(len(testWord)):     #置き換え前の文字数分、ループを回す。何回目のループかはcountで管理
        print(count) #Debug用
        if testWordList[count] == "　":
            replacedTestWordList.append("%") 
            replacedTestWordList.append("2") 
            replacedTestWordList.append("0") 
            print(replacedTestWordList) #Debug用
        else:
            replacedTestWordList.append(testWordList[count])
            print(replacedTestWordList) #Debug用
    
    replacedTestWord =  "".join(replacedTestWordList)
    print(testWord) #Debug用
    print(replacedTestWord)
    

word = input("Enter the test word:")
replaceTwoByteChar(word)


#回答解説：
#・まず、空白文字の数を数える。
#・空白文字は3文字に置き換えるので、空白文字数の3倍の数が、置き換え後の全文字数
#・置き換え後の全文字数が分かった後は、後ろから入れていく。元の文字はもとのまま、空白文字は0,2,%の順で入れていく
# def replaceTwoByteChar(testWord, n):
#     spaceCount = 0
#     for letter in testWord:
#         if letter == "　":
#             spaceCount += 1
    
#     testWord += list("　" * (spaceCount*2))
#     index = n + spaceCount*2 - 1

#     for i in reversed(range(n)):
#         if testWord[i] == "　":
#             testWord[index-2 : index+1] = list("%20")
#             index -= 2
#         else:
#             testWord[index] = testWord[i]
#             index -= 1
#     return testWord
    

# testWord = input("Enter the test word:")
# print(replaceTwoByteChar(testWord, len(testWord)))

#tips!
#strlist = list('Python')  # 'P'、'y'、't'、'h'、'o'、'n'を要素とするリストを作成

#以下、全角文字が何個あったかを数える関数、前段階として作成してみた
# def replaceTwoByteChar(testWord):
#     spaceCount = 0
#     for letter in testWord:
#         if letter == "　":
#             spaceCount += 1
#     print(spaceCount)

# replaceTwoByteChar("test　test test")