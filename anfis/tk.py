import tkinter as tk
import numpy as np
import pandas as pd
import anfis
import membership.mfDerivs
import membership.membershipfunction
#from matplotlib.figure import Figure
#from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)

#from tkinter import *
root=tk.Tk()
root.config(bg='blue')
root.title('hi')
root.geometry('3100x3100')
heading='Depression'
para1='''Depression is classified as a mood disorder. It may be described as feelings of sadness, loss, or anger that interfere with a person’s everyday activities.It’s also fairly common. 
The Centers for Disease Control and Prevention (CDC)Trusted Source estimates that 8.1 percent of American adults ages 20 and over had depression in any given 2-week period from 2013 to 2016.
People experience depression in different ways. It may interfere with your daily work, resulting in lost time and lower productivity. It can also influence relationships and some chronic health conditions.
'''
para2='''It’s important to realize that feeling down at times is a normal part of life. Sad and upsetting events happen to everyone. But, if you’re feeling down or
hopeless on a regular basis, you could be dealing with depression.
Depression is considered a serious medical condition that can get worse without proper treatment. Those who seek treatment often see improvements in symptoms in just a few weeks.'''
heading2='Depression symptoms'
para3='''Depression can be more than a constant state of sadness or feeling “blue.”
Major depression can cause a variety of symptoms. Some affect your mood, and others affect your body. Symptoms may also be ongoing, or come and go.
The symptoms of depression can be experienced differently among men, women, and children differently.'''
heading3='Depression causes'
para4='''There are several possible causes of depression. They can range from biological to circumstantial.
Common causes include:

Family history: You’re at a higher risk for developing depression if you have a family history of depression or another mood disorder.
Early childhood trauma: Some events affect the way your body reacts to fear and stressful situations.
Brain structure; There’s a greater risk for depression if the frontal lobe of your brain is less active. However, scientists don’t know if this happens before or after the onset of depressive symptoms.
Medical conditions; Certain conditions may put you at higher risk, such as chronic illness, insomnia, chronic pain, or attention-deficit hyperactivity disorder (ADHD).
Drug use: A history of drug or alcohol misuse can affect your risk.'''
r=tk.Label(root,text=heading,font=("Arial", 22),bg='blue')
r.pack()
r1=tk.Label(root,text=para1,font=("Arial", 12),fg='blue')
r1.pack()
r2=tk.Label(root,text=para2,font=("Arial", 12),fg='blue')
r2.pack()
r3=tk.Label(root,text=heading2,font=("Arial", 22),bg='blue')
r3.pack()
r4=tk.Label(root,text=para3,font=("Arial", 12),fg='blue')
r4.pack()
r5=tk.Label(root,text=heading3,font=("Arial", 22),bg='blue')
r5.pack()
r6=tk.Label(root,text=para4,font=("Arial", 12),fg='blue')
r6.pack()


    
        
    
def gt():
    r.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    r5.destroy()
    r6.destroy()
    b.destroy()
    def sr():
        r7.destroy()
        b1.destroy()
        b2.destroy()
        
        ts = pd.read_csv("a2.csv")
            
        t2="Enter patient id"
        r8=tk.Label(root,text=t2,font=("Arial", 12))
        r8.pack()
        hg=tk.Entry(root)
        hg.pack()
        r8.place(relx=0.4,rely=0.3)
        hg.place(relx=0.5,rely=0.3)
        t5="Patient Id\n 1 - 1001\n2 - 1002\n3 - 1003\n4 - 1004\n5 - 1005\n6 - 1006\n7 - 1007\n8 - 1008\n9 - 1009\n10 - 1010\n11 - 1011\n12 - 1012\n13 - 1013\n14 - 1014\n15 - 1015\n16 - 1016\n17 - 1017\n18 - 1018\n19 - 1019\n20 - 1020\n"
        r10=tk.Label(root,text=t5,font=("Arial", 12))
        r10.pack()
        r10.place(relx=0,rely=0.1)
        t6="Diagnosis\n\n 0 - mild\n 1 - moderate\n 2 - severe"
        r11=tk.Label(root,text=t6,font=("Arial", 12))
        r11.pack()
        r11.place(relx=0.92,rely=0.3)
        t7="Gender\n\n 0 - Male\n 1 - Female"
        r14=tk.Label(root,text=t7,font=("Arial", 12))
        r14.pack()
        r14.place(relx=0,rely=0.8)
        def sr1():
            #hg1=hg.get()
            #hg1=int(hg1)
            hg1=hg.get()
            hg1=int(hg1)
            print(hg1)
            r=0
            for i in ts['patientid']:
            
                if i==hg1:
                   
                     #print(ts.iloc[r,:])
                     t3=ts.iloc[r,:]
                     
                     r9=tk.Label(root,text=t3,font=("Arial", 12))
                     r9.pack()
                     r9.place(relx=0.45,rely=0.6)
                     if t3['diagnosis']==0:
                         r18=tk.Label(root,text="You depression type : Mild",font=("Arial", 12))
                         r18.pack()
                         r18.place(relx=0.58,rely=0.6)
                         print('mild')
                     elif t3['diagnosis']==1:
                         print('moderate')
                         r18=tk.Label(root,text="You depression type : Moderate",font=("Arial", 12))
                         r18.pack()
                         r18.place(relx=0.58,rely=0.6)
                     else:
                         print('severe')
                         r18=tk.Label(root,text="You depression type : Severe",font=("Arial", 12))
                         r18.pack()
                         r18.place(relx=0.58,rely=0.6)
                else:
                     r=r+1
                     
        b3=tk.Button(root,text="search",command=sr1)
        b3.pack()
        b3.place(relx=0.48,rely=0.5)
    def mr1():
        r7.destroy()
        b1.destroy()
        b2.destroy()
        def mr2():
            ts = pd.read_csv("a2.csv")
    
    
            X = ts.iloc[:,3:5]
            Y = ts.iloc[:,8]
            
            mf = [[['gaussmf',{'mean':0.,'sigma':1.}],['gaussmf',{'mean':-1.,'sigma':2.}],['gaussmf',{'mean':-4.,'sigma':10.}],['gaussmf',{'mean':-7.,'sigma':7.}]],
                        [['gaussmf',{'mean':1.,'sigma':2.}],['gaussmf',{'mean':2.,'sigma':3.}],['gaussmf',{'mean':-2.,'sigma':10.}],['gaussmf',{'mean':-10.5,'sigma':5.}]]]
            
            
            mfc = membership.membershipfunction.MemFuncs(mf)
            anf = anfis.ANFIS(X, Y, mfc)
            k=anf.trainHybridJangOffLine(epochs=10)
            r13=tk.Label(root,text="current error")
            r13.pack()
            r13.place(relx=0.47,rely=0.17)
            r12=tk.Label(root,text=k)
            r12.pack()
            r12.place(relx=0.47,rely=0.2)
            #fig=Figure(figsize=(4,4),dpi=100)
            #plot=fig.add_subplot(1,1,1)
            r16=tk.Label(root,text="see main IDE window for graph")
            r16.pack()
            r16.place(relx=0.47,rely=0.7)
            
            print("Plotting errors")
            anf.plotErrors()
           
            print("Plotting results")
            anf.plotResults()
            #canvas=FigureCanvasTkAgg(fig,master=root)
            #canvas.draw()
            #canvas.get_tk_widget().pack()
            #toolbar=NavigationToolbar2Tk(canvas,root)
            #toolbar.update()
            #canvas.get_tk_widget().pack()
        b4=tk.Button(root,text="start activity",command=mr2)
        b4.pack()
        
    t1='''\n Two options are present single record and other is for multiple records.
    if we click on single record you can search each persons record by inputing values to knw about condition of patient.
    if we click on multiple records we can see optimization of all records by using adaptive neuro fuzzy.'''
    r7=tk.Label(root,text=t1,font=("Arial", 12),fg='blue')
    r7.pack()
    b1=tk.Button(root,text="single record",command=sr)
    b1.pack()
    b2=tk.Button(root,text="multiple record",command=mr1)
    b2.pack()
    b1.place(relx=0.4,rely=0.3)
    b2.place(relx=0.5,rely=0.3)

    



b=tk.Button(root,text="click to start",command=gt)

b.pack()
b.place(relx=0.5,rely=0.8)

root.mainloop()