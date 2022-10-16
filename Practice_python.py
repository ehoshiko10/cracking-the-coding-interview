# home = "america"
# if home == "america":
#     print("yes")
# else:
#     print("no")


# def printtest(x):
#     if x == 2:
#         return "number2"
#     if x % 2 == 0:
#         return "even"

# y = printtest(2)

# print(y)

# 関数の基礎
# def f(x, y, z):
#     return x * y * z

# result = f(1, 2, 3)
# print(result)

# 組み込み関数
# x = len("Monty")
# print(x)

# input関数
# age = input("Enter your age : ")
# int_age = int(age)
# if int_age > 21:
#     print("you are over 21")
# elif int_age < 21:
#     print("you are under 21")
# else:
#     print("you are 21")

# 関数を再利用する
# def even_odd():
#     n = input("type a number : ")
#     int_n = int(n)
#     if int_n % 2 == 0:
#         print("even")
#     else:
#         print("odd")

# even_odd()
# even_odd()

# def f(x=2):
#     return x ** x

# print(f())


# 例外処理
# a = input("type a number: ")
# b = input("type a number:")
# a = int(a)
# b = int(b)

# try:
#     print(a/b)
# except ZeroDivisionError:
#     print("b cannot be zero.")


# 例外処理
# try:
#     a = input("type a number: ")
#     b = input("type a number:")
#     a = int(a)
#     b = int(b)

#     print(a/b)

# except (ZeroDivisionError, ValueError):
#     print("b cannot be zero.")

# リスト
# colors = ["blue", "red", "purple"]
# guess = input("何色でしょうか:")


# if guess in colors:
#     print("that's right!")
# else:
#     print("wrong")

# testWord = "abcde"
# print(testWord[i])

# 1.3
# space=2
# replacedSpace = 1 + space*3
# print(replacedSpace)

# print(len("　"))
# 全角文字も1文字扱い

# Word = "g"
# print(Word)
# words = "abc"
# NewWord = Word + words[1]
# print(NewWord)

# 1.4
# l = [1,2,3,4,5,1,1,1]
# print(l.count(l[0]))

# for i in range(len(l)):
#     print(l.count(l[i]))

#　同じ文字だったらスキップしたい
# set型は重複した要素をもたないデータ型で、set()にリストなどを渡すと、重複する値は無視されて一意な値のみが要素となるset型のオブジェクトを返す。
