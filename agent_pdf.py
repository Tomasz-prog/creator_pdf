from fpdf import FPDF
from tkinter import messagebox
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image

def main():

    def pdf_create():

        file_with_paths = open("paths.txt", "r")
        pics = file_with_paths.readline()
        pics = pics[:-1]
        ready_docs = file_with_paths.readline()
        ready_docs = ready_docs[:-1]
        file_with_paths.close()

        print(pics)
        print(ready_docs)

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        nazwa_pliku = nazwa.get()
        ilosc_zdjec = int(zdjecia.get())

        numer_zdjecia = 1
        for i in range(ilosc_zdjec):
            pdf.add_page()
            ImageFile = pics + str(numer_zdjecia) + '.jpg'
            print(ImageFile)
            try:
                cover = Image.open(ImageFile)
            except:
                messagebox.showwarning("Ostrzeżenie", f"brak pliku o numerze {numer_zdjecia}. dokument PDF nie został stworzony.")
                main()
            width, height = cover.size
            pdf.image(ImageFile, 0, 0, 595, 842)
            if numer_zdjecia == ilosc_zdjec:
                file_output = ready_docs + '\\' + nazwa_pliku + '.pdf'
                print(f"file_output {file_output}")
                try:
                    pdf.output(file_output)
                    messagebox.showinfo("Informacja", f"Plik o nazwie {nazwa_pliku}.pdf został poprawnie stworzony.")
                except:
                    messagebox.showerror("brak lokalizacji", f"nie istnieje folder {ready_docs} dlatego nie można zapisać dokumentu PDF, stworz wymienone foldery lub zmienc lokalizacje w pliku paths.txt")
                    main()

            numer_zdjecia += 1
            main()

    info = tk.Label(root, text="Kreowanie dokumentu PDF").place(x=80, y=10)
    info = tk.Label(root, text="Podaj nazwę pliku:").place(x=10, y=50)
    info = tk.Label(root, text="Ilosc zdjec:").place(x=10, y=120)


    nazwa = tk.Entry(root, justify=CENTER)
    nazwa.focus()
    nazwa.place(x=10,y=80, width=150)

    zdjecia = tk.Entry(root, justify=CENTER)
    zdjecia.place(x=10,y=150, width=30)

    przycisk = tk.Button(root, text="Create PDF", command=pdf_create)
    przycisk.place(x=10, y=200)



root = Tk()
root.title('Tworzenie dokumnetu PDF')
root.geometry('300x300')

main()

root.mainloop()
