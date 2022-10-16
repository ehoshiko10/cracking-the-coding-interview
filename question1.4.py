#問い：ある文字列が回文の順列であるかどうかを調べる

#回答：
# ・回文＝「存在する文字が偶数個あることが最低条件。奇数個の文字は一つか、奇数個の文字がないこと」
# ・各文字が何回出現するかを調べる

#回答方針：
# ・testWordをリスト化する
# ・リストの要素をカウントする   ←Collections　の　Counter()　を使えば一発だけど、別の方法でやる

# ・set()にリストを渡して、重複のないリストを作る
# ・set()は文字を抽出不可なので、これをlist()で再びリストにすればOK。
# ・重複のないリストから、一つずつ抜き出して、それが元のリストで何個あるかを調べる
# ・x % y    x / y の剰余 を使って、出てきた個数が偶数か期数かを判別
# ・奇数が何個あるかはカウントしておく、2個以上でてきた段階でbreak


def palindromeCheck(testWord):
    if len(testWord) > 128:
        return False
    
    testWord = testWord.lower()
    
    testWordList = list(testWord)
    noDuplicate = list(set(testWordList)) # ・set()は文字を抽出不可なので、これをlist()で再びリストにすればOK。
    print(noDuplicate)
    oddCount = 0

    for i in range(len(noDuplicate)):        
        letterCount = testWordList.count(noDuplicate[i])
        print(noDuplicate[i] + "の数:", letterCount) #Debug用
        if letterCount % 2 != 0:
            oddCount += 1
            if oddCount >= 2:
                return False
        print("奇数の数:", oddCount) #Debug用
    
    return True

word = input("Enter the test word:")
print(palindromeCheck(word))



#tips!
# set型は重複した要素をもたないデータ型で、set()にリストなどを渡すと、重複する値は無視されて一意な値のみが要素となるset型のオブジェクトを返す。
# for文の場合、処理内でreturnするとfor文を抜ける。
# forEachの場合、participantsの全ての要素に対して処理を実行する。処理の中でreturnしても、forEach文を抜けることは出来ない。