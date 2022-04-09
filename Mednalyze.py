'''
import webbrowser
import wikipedia
import os
import matplotlib
import math
import speech_recognition as sr
import voices
import wolframalpha
import PyAudio
import mysql.connector as msc
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

    patient1=('Divy','Headache','','','')
    patient2=('Piyush','Hairline Fracture','','','')
    patient3=('Avanish','','','','')
    patient3=('Aditya','','','','')
    patient3=('Rohit','','','','')


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
    
    patient1=('Sanidhya','','','','')
    patient2=('Piyush','','','','')
    patient3=('Avanish','','','','')

    lst=[]
    n=5
    for i in range(1,6):                          #for a new patient entry
        i1=input('')
        lst.append(i1)

    print(lst)