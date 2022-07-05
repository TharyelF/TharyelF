import pyqrcode
from tkinter import *
from tkinter import messagebox
def generateQR() :
    inputString  = enterTextField.get()
    Scale = enterScaleField.get()
    if len(Scale) :
        try : 
            Scale = int(Scale)
        except :
            messagebox.showerror("Error",
            "Scale shoud be integer value ex: 1, 2, 3 ..")
            return
    else :
        scale = 5
    if len(inputString) :
        qrCode = pyqrcode.create(inputString)
        savePath = "/home/tharyel/Área de Trabalho/Projetos/" + inputString + "_" + str(scale)
        qrCode.svg(savePath + ".svg", scale = scale)
        qrCode.svg(savePath + ".png", scale = scale)
        messagebox.showinfo("Concluido", "Seu qrCode foi salvo na pasta:" + savePath + ".png/.svg")
    else : 
        messagebox.showerror("Erro", "Campo de texto vazio")
def clearAll() :
    enterTextField.delete(0,END)
    enterTextField.focus_set()
if __name__ == "__main__":
    window = Tk()
    window.configure(background= 'Black')
    window.title("Gerador de QR Code")
    enterTextLabel = Label(window, text = " Insira o Texto", fg= 'black', bg= 'grey')
    enterTextLabel.grid(row = 2, column = 1, sticky = "E", padx = "10", pady = "10")
    enterScaleLabel = Label(window, text = "Enter Scale", fg = 'black', bg = 'grey')
    enterScaleLabel.grid(row = 2, column=4, sticky = "E", padx= "10", pady = "10")
    enterTextField = Entry(window)
    enterTextField.grid(row = 2, column = 2, sticky = "E", ipadx = "60", pady = "10")
    enterScaleField = Entry(window)
    enterScaleField.grid(row = 2, column = 5, sticky = "E", pady= "10")
    generateButton = Button(window, text = "Generate", bg= "red", fg = "black", command = generateQR)
    clearButton = Button(window, text = "Clear", bg= "red", fg = "black", command = clearAll)
    generateButton.grid(row = 3, column = 3)
    clearButton.grid(row = 4, column = 3, pady = "5")
    window.mainloop()