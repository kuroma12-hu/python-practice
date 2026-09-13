text = input("保存したい文字を入力してください:")

with open("memo.txt", "w", encoding="utf-8")as file:
    file.write(text)
    print("保存しました")