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


