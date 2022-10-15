#問い：ある文字列が、すべて固有である(重複がないか)チェックする


def uniqueCheck(testWord):
    if len(testWord) > 128:
        return False

    for i in range(len(testWord)-1):
        print("reached check1")
        for j in range(i+1, len(testWord)):
            if testWord[i] == testWord[j]:
                return False
    print("reached check")
    return True

testWord = input("Enter the test word:")
# uniqueCheck(testWord)
print(uniqueCheck(testWord))

#tips!
# len 関数は引数に指定したオブジェクトの長さや要素の数を取得します。
# for 文で、組み込み関数である range() 関数を使うと、指定回数分だけの処理が行われます。