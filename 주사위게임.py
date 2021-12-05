from tkinter import *
import random




def Play():
    player = random.randint(1,6)
    computer = random.randint(1,6)

    if player == 1:
        left00.config(image = photo1)

    elif player == 2:
        left00.config(image = photo2)

    elif player == 3:
        left00.config(image = photo3)

    elif player == 4:
        left00.config(image = photo4)

    elif player == 5:
        left00.config(image = photo5)

    elif player == 6:
        left00.config(image = photo6)




    if computer == 1:
        right00.config(image = photo1)

    elif computer == 2:
        right00.config(image = photo2)

    elif computer == 3:
        right00.config(image = photo3)

    elif computer == 4:
        right00.config(image = photo4)

    elif computer == 5:
        right00.config(image = photo5)

    elif computer == 6:
        right00.config(image = photo6)
        

    if player < computer:
        midtxt.config(text = "컴퓨터의 승리.")

    elif player == computer:
        midtxt.config(text = "비겼습니다.")

    elif player > computer:
        midtxt.config(text = "사용자의 승리.")
        
        







top = Tk()
top.title("주사위게임")


photo1 = PhotoImage(file = '1.png')
photo2 = PhotoImage(file = '2.png')
photo3 = PhotoImage(file = '3.png')
photo4 = PhotoImage(file = '4.png')
photo5 = PhotoImage(file = '5.png')
photo6 = PhotoImage(file = '6.png')

left00 = Label(top,compound=TOP,text="사용자",image=photo6)
left00.grid(row = 0, column=0)
right00 = Label(top,compound=TOP,text="컴퓨터",image=photo6)
right00.grid(row = 0, column=2)

Result = "게임시작"
midtxt = Label(top,text = Result)
midtxt.grid(row = 0, column=1)

Playing = Button(top, text="주사위 굴리기",width=30, command = Play).grid(row=1,column=1)

top.mainloop()
