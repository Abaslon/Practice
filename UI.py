import tkinter as tk
from tkinter.ttk import *
from tkinter import*
'''
button=input('Select Login Option')

if button=='Doctor Login':                     #Doctor Login Portion starts here
    lt2=[1,2,3]                                         #sample list for doctor login IDs
    lt3=[4,5,6]                                           #sample list for doctor passwords
    o1=input('Enter ')                                   
    if (o1 in lt2):
        p1=input('Enter Password')
        if (p1 in lt3):
            print('Access Granted')
        else:
            print('Access Denied')

    patient1=('Divy','Headache','crocin','none')
    patient2=('Piyush','Hairline Fracture','pain-killers','none')
    patient3=('Avanish','Stomach Ache','Pudhinara','none')
    patient3=('Aditya','Concussion','Blood Thinners','Bed rest')
    patient3=('Rohit','Sore throat','lozenges','warm water')


    k=input('Enter Patient Name')                          #search for patient entries

    if (k in patient1):
        print(patient1)
    if (k in patient2):
        print(patient2)
    if (k in patient3):
        print(patient3)


    
if button=="Patient Login":                          #Patient Login Feature Starts here
    lt=[8,9,10]                                           #sample list for patient login IDs
    lt1=[5,6,7]                                         #sample list for patient passwords
    o=input('Enter Patient ID')
    if o in lt:
        p=input('Enter Password')
        if p in lt1:
            print('Access Granted')

    else:
        print('Access Denied')
    
    patient1=('Divy','Headache','crocin','none')
    patient2=('Piyush','Hairline Fracture','pain-killers','none')
    patient3=('Avanish','Stomach Ache','Pudhinara','none')
    patient3=('Aditya','Concussion','Blood Thinners','Bed rest')
    patient3=('Rohit','Sore throat','lozenges','warm water')

    lst=[]
    n=5
    for i in range(1,6):                          #for a new patient entry
        i1=input('')
        lst.append(i1)

    print(lst)
'''    
HEIGHT = 660
WIDTH = 600
Ui = Tk()
def clickd():
	dsrn=Toplevel(Ui)
	canvas = Canvas(dsrn, bg='#51b3f5',height=HEIGHT, width=WIDTH)
	canvas.pack()

	buttonss =Button(dsrn, text="Sypmtom Search", bg='gray', highlightbackground='#3E4149')
	buttonss.place(relx=0.02, rely=0.05, relwidth=0.25, relheight=0.06)

	buttonds =Button(dsrn, text="Disease Search", bg='gray')
	buttonds.place(relx=0.02, rely=0.15, relwidth=0.25, relheight=0.06)

	buttonps =Button(dsrn, text="Patient Search", bg='gray')
	buttonps.place(relx=0.02, rely=0.25, relwidth=0.25, relheight=0.06)

	entry = Entry(dsrn, bg='#808a91')
	entry.place(relx=0.3, rely=0.12, relwidth=0.6357, relheight=0.13 )
	'''
		display = Entry(dsrn, bg='White', insert("Divy,Headache,crocin,none\n Divy,Headache,crocin,none'" ))
	display.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.5)
	'''
	dsrn.mainloop()

def clickp():
	psrn=Toplevel(Ui)
	canvas = Canvas(psrn, bg='#51b3f5',height=HEIGHT, width=WIDTH)
	canvas.pack()
	#canvas.place(height=HEIGHT, width=WIDTH)

	labels = Label(psrn, text="Sypmtoms", bg='#ff0026')
	labels.place(relx=0.02, rely=0.15, relwidth=0.25, relheight=0.075)

	entrys = Entry(psrn, bg='#808a91')
	entrys.place(relx=0.3, rely=0.15, relwidth=0.644, relheight=0.075)
	
	labelm = Label(psrn, text="Medication", bg='#ff0026')
	labelm.place(relx=0.02, rely=0.25, relwidth=0.25, relheight=0.075)
	
	entrym = Entry(psrn, bg='#808a91')
	entrym.place(relx=0.3, rely=0.25, relwidth=0.644, relheight=0.075)
	
	labelt = Label(psrn, text="Other Treatment", bg='#ff0026')
	labelt.place(relx=0.02, rely=0.35, relwidth=0.25, relheight=0.075)
	
	entryt = Entry(psrn, bg='#808a91')
	entryt.place(relx=0.3, rely=0.35, relwidth=0.644, relheight=0.075 )
	'''
	buttonsd = Button(psrn, text="Save Deatils")
	buttonsd.place(relx=0.3,rely=0.45,relwidth=0.4, relheight=0.25)
	'''
	psrn.mainloop()

canvas = Canvas(Ui, bg='#1f1e1e', height=HEIGHT, width=WIDTH)
canvas.pack()

buttond = Button(Ui, text="Doctor login", bg='gray', fg='#290707', command=lambda:clickd())
buttond.place(relx=0.4, rely=0.5, relwidth=0.2, relheight=0.06)

buttonp = Button(Ui, text="Patient Login", bg='gray', fg='#290707', command=lambda:clickp())
buttonp.place(relx=0.4, rely=0.65, relwidth=0.2, relheight=0.06)

'''   


entry = Entry(Ui, bg='green')
entry.place(relx=0.8, rely=0, relwidth=0.25, relheight=0.25)
'''
Ui.mainloop()
