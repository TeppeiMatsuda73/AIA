# -*- coding: utf-8 -*-

# モジュール・パッケージ
from random import choice
import calendar
# カレンダー表示
# print(calender.month(2020 , 1))


# 文字結合
print("あ" + "い" + "う")  #あいう
print("あいうえお" * 5)  #あいうえおあいうえおあいうえおあいうえおあいうえお

# 配列
list = ["apple", "banana", "cyder"]
for i in list:
    print(i)
# 辞書型
jisyo = {"aa" : "aaa", "bb" : "bbb"}
for i in jisyo:
    print(i)

# 辞書型のデータをループ
for i, v in jisyo.items():
    print("key: {} value: {}".format(i, v))

# range(x):0からx-1までの連番のリストを返す
# range(x,y):xからy-1までの連番のリストを返す
# リスト内包表記
result = [x**2 for x in range(1,11)]
print(result)

result = []
for i in range(1, 11):
    result.append(i**3)
print(result)

# 配列を逆に扱う方法
for i in reversed(["GO!", 1, 2, 3]):
    print(i)

result = []
for i in range(1, 101):
    if i%2 == 0:
        # 配列への追加
        result.append(i)
print(result)

# 文字サイズ
print(len("aiueo"))  # 5
# 要素数
list1 = [1,2,3,4,5,6,7,8,9,0]
print(len(list1))  #10

# while文
n = 0
while n < 10:
    print(n)
    n += 1
    # n++ は使えない

sum_d = 0
data = [20, 40, 60, 88]
for d in data:
    sum_d += d
# for文やwhile文では、elseを記述する事で最後に1度だけ処理を行う事ができる
else:
    print(sum_d)  # 208

# break,continue
for i in range(10):
    if i == 5:
        break
    elif i == 2:
        continue
    print(i)  # 0134

list2 = [10, 20, 30, 40, 50]
# randomモジュール
print(choice(list2))

# 関数定義
def hello():
    print("Hello")
# 関数呼び出し
hello()

# 関数を定義したが何もしない場合
def nanimosinai():
    pass

# 標準入力
# print("名前を入力")
# input_name = input()
# input()は文字列としてキャストされるため、整数などの場合には int(input())
# print("あなたの名前は" + input_name + "です")

# 関数・引数
def say_hello(name):
    print("こんにちは" + str(name) + "さん")

say_hello("松田")

# 引数にデフォルト値を設定
def multi_hikisu(a, b=5):
    print(a)
    print(b)
multi_hikisu(3,10)  #3と10が出力
multi_hikisu(3)  #3と5が出力

