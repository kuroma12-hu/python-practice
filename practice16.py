try:
    math = int(input("数学の点数を入力してください:"))
    english = int(input("英語の点数を入力してください:"))
    japanese = int(input("国語の点数を入力してください:"))

    print("数学: " ,math)
    print("英語: " ,english)
    print("国語: " ,japanese)


    ave = (math + english + japanese) / 3

    print("平均点は", ave, "点です")

    if ave >= 60:
        print("合格です")
    else:
        print("不合格です")

except ValueError:
    print("数字を入力してください")