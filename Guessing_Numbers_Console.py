import random as rd

Default = rd.randint(1,12)

print(Default)
while True:
    User_value = int(input("1부터 12까지 입력해주세요.\t"))

    if Default + User_value == 13:
        print(f"정답입니다. \n랜덤 값 : {Default}")

        break

    print("틀렸습니다. ")
