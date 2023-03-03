import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('300x600')
        self.main_window.title("Responsive Regestration Form")

        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)
        self.frame4 = tkinter.Frame(self.main_window)
        self.frame5 = tkinter.Frame(self.main_window)
        self.frame6 = tkinter.Frame(self.main_window)
        self.frame7 = tkinter.Frame(self.main_window)
        self.frame8 = tkinter.Frame(self.main_window)
        self.frame9 = tkinter.Frame(self.main_window)
        self.frame10 = tkinter.Frame(self.main_window)
        self.frame11 = tkinter.Frame(self.main_window)
        self.frame12 = tkinter.Frame(self.main_window)
        self.frame13 = tkinter.Frame(self.main_window)

        self.emailLabel = tkinter.Label(self.frame1,text="Email: ")
        self.emailEntry = tkinter.Entry(self.frame1,width=40)

        self.emailLabel.pack(side='left')
        self.emailEntry.pack(side='right', anchor='ne')

        self.passwordLabel = tkinter.Label(self.frame2,text="Password: ")
        self.passwordEntry = tkinter.Entry(self.frame2, width=36)
        
        self.passwordLabel.pack(side='left')
        self.passwordEntry.pack(side='right', anchor='ne')

        self.reEnterLabel = tkinter.Label(self.frame3,text="Re-Enter Password")
        self.reEnterEntry = tkinter.Entry(self.frame3,width=29)

        self.reEnterLabel.pack(side='left')
        self.reEnterEntry.pack(side='right')

        self.FirstNameLabel = tkinter.Label(self.frame4,text="First Name: ")
        self.FirstnameEntry = tkinter.Entry(self.frame4, width=10)
        
        self.FirstnameEntry.pack(side='right')
        self.FirstNameLabel.pack(side='left')

        self.LastNameLabel = tkinter.Label(self.frame4,text='Last Name: ')
        self.LastNameEntry = tkinter.Entry(self.frame4,width=10)

        self.LastNameEntry.pack(side='left')
        self.LastNameLabel.pack(side='right')

        self.dummyLabel = tkinter.Label(self.frame5,text="")
        self.dummyLabel.pack(side='left')
              
        
        self.dateRB1 = tkinter.Radiobutton(self.frame6,text='Male',value='M')
        self.dateRB2 = tkinter.Radiobutton(self.frame6,text='Female',value='F')
        

        self.dateRB1.pack(side='left')
        self.dateRB2.pack(side='left')
        

        self.dummyLabel2 = tkinter.Label(self.frame7,text="")
        self.dummyLabel2.pack(side='left')

        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        

      
        self.terms = tkinter.Checkbutton(self.frame8,text='I agree with the terms and conditions',variable=self.cb_var1)
        self.news = tkinter.Checkbutton(self.frame9,text='I want to recive a Newsletter',variable=self.cb_var2)
       
        self.terms.pack(anchor='w')
        self.news.pack(anchor='w')
       
        self.dummyLabel3 = tkinter.Label(self.frame12,text="")
        self.dummyLabel3.pack(side='left')

        self.registerButton = tkinter.Button(self.frame13,text="Register",command=self.register,bg='yellow',width=20)
        
        

        self.registerButton.pack(side='bottom',anchor='c')
        
        

        self.frame1.pack(anchor='w')
        self.frame2.pack(anchor='w')
        self.frame3.pack(anchor='w')
        self.frame4.pack(anchor='w')
        self.frame5.pack(anchor='w')
        self.frame6.pack(anchor='w')
        self.frame7.pack(anchor='w')
        self.frame8.pack(anchor='w')
        self.frame9.pack(anchor='w')
        self.frame10.pack(anchor='w')
        self.frame11.pack(anchor='c')
        self.frame12.pack(anchor='w')
        self.frame13.pack(anchor='c')

        

        tkinter.mainloop()

    def register(self):
        register = True
       

        if register:
            tkinter.messagebox.showinfo('Success','You have registered')
       
        

myHomework = MyGUI()