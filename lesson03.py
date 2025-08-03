# カンタン計算機のプログラム

# input()で、それぞれの変数に値を入力してもらう
num1 = input("最初の数字を入力してください：")
num2 = input("次の数字を入力してください：")

Answer = float(num1) + float(num2) # float()で変数をfloat型に変換
print("足し算の答えは：",Answer,"です") # print()は","（カンマ）で値をつなぐことができる