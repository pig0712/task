import random as rd # 랜덤
import tkinter as tt # GUI

def Activ2(a):
    lb1 = tt.Label(window, relief="groove",
                   text=f"정답입니다. \n랜덤한 값은 {Default} 입니다.\n5초뒤 종료됩니다.")
    lb1.place(x=500, y=450)
    window.after(5000, window.destroy)

def Activ(a):
    if Default + a == 13:
        Activ2(a)

    else:
        lb2 = tt.Label(window,relief = "groove" ,text = f"틀렸습니다.")
        lb2.place(x=500,y=450)




Default = rd.randint(1,12) # 랜덤 값 지정

window = tt.Tk() # 윈도우창 생성 (인스턴스 생성)

window.title("숫자 추론") # 윈도우 창 제목 설정
window.geometry("1200x500+0+0") # 윈도우 창 크기 1024 x 1024 윈도우 창 x,y 초기 좌표 설정
window.resizable(False, False) # x,y 윈도우 창 크기 조절 가능 여부 Tuer = 1, False = 0

label = tt.Label(window,relief = "groove" ,text = "랜덤한 값을 모르는 상태에서 1~12까지 선택하여 13값을 만드는 숫자 추론 게임입니다.\n 버튼을 클릭해주세요.")
label.place(x=350,y=0,)


# label1 = tt.Label(window, text=f"{Default}")
# label1.place(x=0,y=0,)

st = {}
# 여러 변수 한번에 생성 후 버튼 배열

im1 = tt.Button(window, text=f"13", width=5, height=2,
                overrelief="groove", borderwidth=3, bg="#6ba4ff")
im1.place(x = 550, y = 375)

im2 = tt.Button(window, text=f"{Default}", width=5, height=2, overrelief="groove", borderwidth=3, bg="#6ba4ff")
im2.place(x = 550, y = 60)

im3 = tt.Button(window, text=f"+", width=5, height=2, overrelief="groove", borderwidth=3, bg = "#6ba4ff")
im3.place(x = 550, y =125)

im4 = tt.Button(window, text=f"=", width=5, height=2, overrelief="groove", borderwidth=3, bg = "#6ba4ff")
im4.place(x = 550, y = 315)




for i in range(1,13):
    globals()[f"bu{i}"] = tt.Button(window, text=f"{i}", width=10, height=5, overrelief="groove", borderwidth=3, bg = "#6ba4ff", command=lambda i=i: Activ(i)) # 버튼 생성
    globals()[f"bu{i}"].place(x = 70+(i*75) ,y=200) # 버튼 배치

window.mainloop() # 윈도우가 종료될 때 까지 실행 (마우스 클릭 같은 이벤트 발생) - 코드 맨 마지막에 작성 -


