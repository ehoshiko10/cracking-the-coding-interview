#二つの文字列を与えられたときに、片方が片方の並べ替えになっているかどうか判定


def anagramCheck(testWord1, testWord2):
    if len(testWord1) != len(testWord2):
        return False
    
    used_letter = {}
    for letter in testWord1:
        if letter in used_letter:
            used_letter[letter] += 1
        else:
            used_letter[letter] = 1
    print(used_letter)   #Debug用、例えばaabccと入力した場合、{'a': 2, 'b': 1, 'c': 2}と出力される！

    for letter in testWord2:
        if letter not in used_letter: #文字数が同じだけど、testWord1に含まれていない文字があるかをチェック
            return False
        else:
            if used_letter[letter] < 1:
                print("stop", used_letter) #Debug用、例えばaabbcと入力した場合、stop {'a': 0, 'b': 0, 'c': 2}と出力される！もうこれ以上bを減らせない=testWord1よりもbが多いことを示す
                return False
            else:
                used_letter[letter] -= 1
    print(used_letter)

    return True
    

testWord1 = input("Enter the first test word:")
testWord2 = input("Enter the second test word:")
# print(anagramCheck(testWord1, testWord2))
anagramCheck(testWord1, testWord2)


#tips!
#sorted関数を使えば一瞬で終わる
#return sorted(testWord1) == sorted(testWord2)

#"-=" は、値を引いて代入を意味します。 count = count - 1 と　count -= 1 は同じ意味