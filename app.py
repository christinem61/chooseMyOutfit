import os
import tkinter as tk
import random
from PIL import Image, ImageTk
from playsound import playsound

TOPS = [str('tops/') + imgFile for imgFile in os.listdir('tops/')]
BOTTOMS = [str('bottoms/') + imgFile for imgFile in os.listdir('bottoms/')]

class OutfitApp:
    def __init__(self, root):
        self.root = root
        self.topImg = TOPS
        self.bottomImg = BOTTOMS
        self.topPath = self.topImg[0]
        self.bottomPath = self.bottomImg[0]
        self.topFrame = tk.Frame(self.root, bg = '#d0b4dc')
        self.bottomFrame = tk.Frame(self.root, bg = '#d0b4dc')
        self.topLabel = self.display_photo(self.topPath, self.topFrame)
        self.topLabel.pack(side=tk.TOP)
        self.bottomLabel = self.display_photo(self.bottomPath, self.bottomFrame)
        self.bottomLabel.pack(side=tk.TOP)
        self.create_display()

    def create_display(self):
        self.root.title("Pick My Outfit")
        lbl=tk.Label(self.root, text="Choose My Outfit", bg = '#a95aec', fg='black', font=("Comic Sans MS", 20), width=600, pady=10)
        lbl.pack(side=tk.TOP)
        text=tk.Label(self.root, text="Select the 'Create Outfit' button to randomly choose an outfit or ", bg = '#d0b4dc', fg='navy', font=("Comic Sans MS", 12))
        text2=tk.Label(self.root, text = "use the surrounding buttons for your own customization. ", bg = '#d0b4dc', fg='navy', font=("Comic Sans MS", 12))
        text.pack( anchor = tk.CENTER,  fill = tk.BOTH)
        text2.pack( anchor = tk.CENTER, fill = tk.BOTH)
        self.root.geometry('520x620')
        self.btns()
        self.topFrame.pack(fill = tk.BOTH, expand = tk.YES)
        self.bottomFrame.pack(fill = tk.BOTH, expand = tk.YES)

    def display_photo(self, imgPath, frame):
        img = Image.open(imgPath)
        newImg = img.resize((200,200), Image.ANTIALIAS)
        tkImg = ImageTk.PhotoImage(newImg)
        labelImg = tk.Label(frame, image = tkImg, anchor = tk.CENTER)
        labelImg.image = tkImg
        return labelImg

    def btns(self):
        topPrev = tk.Button(self.topFrame, text="Prev", command = self.prevTop, font=("Comic Sans MS",12), activebackground='purple', activeforeground='white')
        topPrev.pack(side = tk.LEFT)
        topNext = tk.Button(self.topFrame, text="Next", command = self.nextTop , font=("Comic Sans MS",12), activebackground='purple', activeforeground='white')
        topNext.pack(side = tk.RIGHT)

        bottomPrev = tk.Button(self.bottomFrame, text="Prev", command = self.prevBottom, font=("Comic Sans MS",12), activebackground='purple', activeforeground='white' )
        bottomPrev.pack(side = tk.LEFT)
        bottomNext = tk.Button(self.bottomFrame, text="Next", command = self.nextBottom, font=("Comic Sans MS",12), activebackground='purple', activeforeground='white' )
        bottomNext.pack(side = tk.RIGHT)

        makeOutfit = tk.Button(self.topFrame, text = "Create Outfit", command = self.createOutfit, font=("Comic Sans MS",14), activebackground='purple', activeforeground='white', borderwidth=4)
        makeOutfit.pack(anchor = tk.CENTER)

    def btnNext(self, current, group, incr = True):
        index = group.index(current)
        final = len(group) - 1
        nexti = 0
        if incr and index == final:
            nexti = 0
        elif not incr and index == 0:
            nexti = final
        else:
            increment = 1 if incr else -1
            nexti = index + increment
        nextImg = group[nexti]
        if current in self.topImg:
            imgLabel = self.topLabel
            self.topPath = nextImg
        else:
            imgLabel = self.bottomLabel
            self.bottomPath = nextImg
        self.update_photo(nextImg, imgLabel)

    def createOutfit(self):
        top = random.randint(0, len(self.topImg)-1)
        bottom = random.randint(0, len(self.bottomImg)-1)
        self.display_photo(self.topImg[top], self.topLabel)
        self.display_photo(self.bottomImg[bottom], self.bottomLabel)
    
    def nextTop(self):
        self.btnNext(self.topPath, self.topImg, incr = True)
    def prevTop(self):
        self.btnNext(self.topPath, self.topImg, incr = False)
    def prevBottom(self):
        self.btnNext(self.bottomPath, self.bottomImg, incr = False)
    def nextBottom(self):
        self.btnNext(self.bottomPath, self.bottomImg, incr = True)

    def update_photo(self, imgPath, imgLabel):
        img = Image.open(imgPath)
        newImg = img.resize((200,200), Image.ANTIALIAS)
        tkImg = ImageTk.PhotoImage(newImg)
        imgLabel.configure(image = tkImg)
        imgLabel.image = tkImg
    

if __name__ == '__main__':
    root = tk.Tk()
    app = OutfitApp(root)
    root.mainloop()