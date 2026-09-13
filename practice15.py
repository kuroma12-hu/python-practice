try:
    age = int(input("年齢を入力してください:"))
    print("年齢は", age, "歳です")

except ValueError:
    print("数字を入力してください")