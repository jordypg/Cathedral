from tkinter import *
from tkinter import messagebox
from myarrays import nXnArray

count = 0
board = nXnArray(3, '')

def Quit():
    global t
    msg = messagebox.askquestion("Exit Game", "Are you sure you want to quit?")
    if msg=='yes':
        t.destroy()

#Destructs the winner window and game window
def destruct():
 global t,winnerWindow
 t.destroy()
 winnerWindow.destroy()

#Displays the winning condition
def displayWinner(winner):
    global t,winnerWindow,ID    
    winnerWindow=Tk()
    winnerWindow.title("Winner Window")
    winnerWindow.configure(bg="Black")
    l2=Label(winnerWindow,text="THE WINNER IS: ",font=("COMIC SANS MS",15),bg="Black",fg="White")
    l2.pack()
    l3=Label(winnerWindow,text=winner,font=("COMIC SANS MS",15),bg="Black",fg="White")
    l3.pack()
    bproceed=Button(winnerWindow,text="Proceed",font=("COMIC SANS MS",10,"bold"),command=destruct)
    bproceed.pack()

#Checks for the winner        
def checkWinner():
    global count,board
    if (board.getCoord(0, 0)==board.getCoord(0, 1)==board.getCoord(0, 2)=="X"
    or board.getCoord(1, 0)==board.getCoord(1,1)==board.getCoord(1,2)=="X"
    or board.getCoord(2, 0)==board.getCoord(2, 1)==board.getCoord(2, 2)=="X"
    or board.getCoord(0, 0)==board.getCoord(1, 0)==board.getCoord(2, 0)=="X"
    or board.getCoord(0, 1)==board.getCoord(1, 1)==board.getCoord(2, 1)=="X"
    or board.getCoord(0, 2)==board.getCoord(1, 2)==board.getCoord(2, 2)=="X"
    or board.getCoord(0, 0)==board.getCoord(1, 1)==board.getCoord(2, 2)=="X"
    or board.getCoord(0, 2)==board.getCoord(1, 1)==board.getCoord(2, 0)=="X"):
        displayWinner("Player X")
    elif (board.getCoord(0, 0)==board.getCoord(0, 1)==board.getCoord(0, 2)=="O"
    or board.getCoord(1, 0)==board.getCoord(1,1)==board.getCoord(1,2)=="O"
    or board.getCoord(2, 0)==board.getCoord(2, 1)==board.getCoord(2, 2)=="O"
    or board.getCoord(0, 0)==board.getCoord(1, 0)==board.getCoord(2, 0)=="O"
    or board.getCoord(0, 1)==board.getCoord(1, 1)==board.getCoord(2, 1)=="O"
    or board.getCoord(0, 2)==board.getCoord(1, 2)==board.getCoord(2, 2)=="O"
    or board.getCoord(0, 0)==board.getCoord(1, 1)==board.getCoord(2, 2)=="O"
    or board.getCoord(0, 2)==board.getCoord(1, 1)==board.getCoord(2, 0)=="O"):
        displayWinner("Player O")
    elif count==9:
        displayWinner("NONE! IT IS A TIE!")

#Changes the value of the button
def changeVal(button,boardValRow,boardValCol):
    global count
    #Checking if button is available
    if button["text"]=="":
        if count%2==0:
            button["text"]="X"
            l1=Label(t,text="PLAYER: 2(O)",height=3,font=("COMIC SANS MS",10,"bold"),bg="white").grid(row=0,column=0)
            board.setCoord("X", boardValCol, boardValRow)
        else:
            button["text"]="O"
            l1=Label(t,text="PLAYER: 1(X)",height=3,font=("COMIC SANS MS",10,"bold"),bg="white").grid(row=0,column=0)
            board.setCoord("O", boardValCol, boardValRow)
        count=count+1
        if count>=5:
            checkWinner()
    else:
        messagebox.showerror("Error","This box already has a value!")


def TicTacToeGUI():
    global t
    t = Tk()
    t.title("TIC TAC TOE")
    t.configure(bg="white")
    #Making the background of the window as white
    #Displaying the player
    l1=Label(t,text="PLAYER: 1(X)",height=3,font=("COMIC SANS MS",10,"bold"),bg="white")
    l1.grid(row=0,column=0)
    #Quit button
    exitButton=Button(t,text="Quit",command=Quit,font=("COMIC SANS MS",10,"bold"))
    exitButton.grid(row=0,column=2)
    #Grid buttons
    b1=Button(t,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b1,0,0))
    b2=Button(t,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b2,0,1))
    b3=Button(t,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b3,0,2))
    b4=Button(t,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b4,1,0))
    b5=Button(t,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b5,1,1))
    b6=Button(t,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b6,1,2))
    b7=Button(t,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b7,2,0))
    b8=Button(t,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b8,2,1))
    b9=Button(t,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command=lambda: changeVal(b9,2,2))
    b1.grid(row=2,column=0)
    b2.grid(row=2,column=1)
    b3.grid(row=2,column=2)
    b4.grid(row=3,column=0)
    b5.grid(row=3,column=1)
    b6.grid(row=3,column=2)
    b7.grid(row=4,column=0)
    b8.grid(row=4,column=1)
    b9.grid(row=4,column=2)
    t.mainloop()

print('fuck')
TicTacToeGUI()