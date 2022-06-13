import tkinter as tk
from tkinter import messagebox
from Cathedral import Board


def CathedralGUI():
    global wdow
    wdow = tk.Tk()
    wdow.title("Cathedral")
    bgColor = "#856F64"
    wdow.configure(bg = bgColor)

    topButtons = tk.Frame(wdow, bg = bgColor)


    playerLabel = tk.Label(topButtons, text = "Current Player: White", height = 5, font = ("Georgia", 20), bg = "thistle3")
    whiteSquaresLeft = tk.Label(topButtons, text = "White Tiles Remaining: 47", height = 5, font = ("Georgia", 17), bg = "AntiqueWhite2")
    blackSquaresLeft = tk.Label(topButtons, text = "Black Tiles Remaining: 47", height = 5, font = ("Georgia", 17), bg = "AntiqueWhite3")


    #Exit Button
    exitButton=tk.Button(topButtons, width = 35, text="Quit",command=wdow.destroy,font=("COMIC SANS MS",10,"bold"))
    #exitButton.grid(column = 3, row = 0)

    topButtonSpacingX = 5
    topButtonSpacingY = 5
    playerLabel.pack(side=tk.LEFT, padx = topButtonSpacingX, pady= topButtonSpacingY)
    whiteSquaresLeft.pack(side=tk.LEFT, padx = topButtonSpacingX, pady= topButtonSpacingY)
    exitButton.pack(side=tk.RIGHT, padx = topButtonSpacingX, pady= topButtonSpacingY)
    blackSquaresLeft.pack(side=tk.RIGHT, padx = topButtonSpacingX, pady= topButtonSpacingY)
    topButtons.pack(side = tk.TOP)

    boardCanvas = tk.Canvas(wdow, bg = "#a7948b")
    
    
    tk.Label(boardCanvas, text = "xdxdxdddd").pack()

    boardCanvas.pack()

    wdow.update_idletasks()
    cvas_h = boardCanvas.winfo_reqheight()
    print(str(cvas_h))



    #piece1 = tk.Label(wdow, text = "  o\nooo\n o ", height = 5, font = ("Courier", 20), bg = "thistle3")
    #piece1.grid(column = 0, row = 3)
    wdow.mainloop()

CathedralGUI()