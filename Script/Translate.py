from tkinter import *
from googletrans import Translator

class Translate:
    
    def __init__(self, *args, **kwargs):
        super(Translate, self).__init__(*args, **kwargs)
        
        self.root = Tk()
        self.root.title('Translate by Ekozi')
        self.root.configure(bg='ivory3')
        self.root.geometry('700x530')
        self.root.resizable(0,0)

        self.front()
        self.root.mainloop()

    def translate(self,bahasa):
        translator     = Translator()
        katadapat      = self.inputKata.get("1.0", "end-1c")
        self.Hasil.delete('1.0',END)
        if (bahasa == "check"):
            hasil       = translator.detect(katadapat)
            hasilkata   = translator.translate(katadapat,dest='en')
            kata        = str(hasil.lang) + "\n" + str(hasilkata.text)
            self.Hasil.insert(END,"Bahasa = " + kata)
        else:
            hasil       = translator.translate(katadapat,dest=bahasa)
            self.Hasil.insert(END,hasil.text)

    def front(self):
        self.lbl        = Label(self.root,text="Masukan Kata Untuk Diubah",bg='ivory3',fg='black')
        self.inputKata  = Text(self.root,height=10,width=80)
        self.lblhasil   = Label(self.root,text="Hasil",bg='ivory3',fg='black')
        self.Hasil      = Text(self.root,height=10,width=80)
        self.footer     = Label(self.root,text="Thanks for use",bg='ivory3',fg='black')
        
        self.enToInd    = Button(self.root,text="En To Ind", command=lambda : self.translate('id'))
        self.Check      = Button(self.root,text="Check Lang\n&\ntranslate to En",font=("helvetica","10"), command=lambda : self.translate("check"))
        self.indToEn    = Button(self.root,text="Ind To En",command=lambda : self.translate('en'))

        self.pos()

    def pos(self):
        self.lbl.place(y=20,relx=0.5,anchor=CENTER)
        self.inputKata.place(y=120,relx=0.5,anchor=CENTER)

        self.indToEn.place(y=250,relx=0.8,anchor=CENTER)
        self.Check.place(y=250,relx=0.5,anchor=CENTER)
        self.enToInd.place(y=250,relx=0.2,anchor=CENTER)

        self.lblhasil.place(y=300,relx=0.5,anchor=CENTER)
        self.Hasil.place(y=400,relx=0.5,anchor=CENTER)

        self.footer.place(y=510,relx=0.9,anchor=CENTER)