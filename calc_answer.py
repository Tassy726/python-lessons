num1 = float(input("1つ目の数字を入力してください: "))
ope = input("計算したい記号を入力してください（+、-、*、/）: ")
num2 = float(input("2つ目の数字を入力してください: "))

if ope == "+":
    print("答えは", num1 + num2, "です")
elif ope == "-":
    print("答えは", num1 - num2, "です")
elif ope == "*":
    print("答えは", num1 * num2, "です")
elif ope == "/":
    print("答えは", num1 / num2, "です")
else:
    print("対応していない記号です")
