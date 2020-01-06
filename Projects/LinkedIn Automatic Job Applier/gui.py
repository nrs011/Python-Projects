import tkinter as TK
from tkinter import *
from tkinter import filedialog
import LinkedinEasyApply
import time
import sendMail
import ReportingModule
import datetime as dt
from tkinter.messagebox import showinfo

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("LinkedIn Easy Apply")

        Frame = TK.Frame(master)
        Frame.grid(row=0, column=0, rowspan=13, columnspan=3, sticky='nsew')

        self.var = StringVar(master)
        self.stringvar1 = TK.StringVar(master)
        self.stringvar2 = TK.StringVar(master)
        self.stringvar3 = TK.StringVar(master)
        self.stringvar4 = TK.StringVar(master)
        self.stringvar6 = TK.StringVar(master)
        self.stringvar7 = TK.StringVar(master)
        self.stringvar8 = TK.StringVar(master)
        self.stringvar9 = TK.StringVar(master)
        self.stringvar10 = TK.StringVar(master)

        self.var.trace("w", self.validate)
        self.stringvar1.trace("w", self.validate)
        self.stringvar2.trace("w", self.validate)
        self.stringvar3.trace("w", self.validate)
        self.stringvar4.trace("w", self.validate)
        self.stringvar6.trace("w", self.validate)
        self.stringvar7.trace("w", self.validate)
        self.stringvar8.trace("w", self.validate)
        self.stringvar9.trace("w", self.validate)
        self.stringvar10 = TK.StringVar(master)

        self.emailEntry = TK.Entry(Frame, textvariable=self.var)
        self.emailEntry.grid(row=0, column=1, padx=5, pady=5, sticky=TK.N + TK.S + TK.E + TK.W)
        self.emailEntryLabel = TK.Label(Frame, text="Email Address:")
        self.emailEntryLabel.grid(row=0, column=0, sticky=TK.W)

        self.emailPass = TK.Entry(Frame, textvariable=self.stringvar1)
        self.emailPass.grid(row=1, column=1, padx=5, pady=5, sticky=TK.N + TK.S + TK.E + TK.W)
        self.emailPassLabel = TK.Label(Frame, text="Email Password:")
        self.emailPassLabel.grid(row=1, column=0, sticky=TK.W)

        self.linkedInUserNameEntry = TK.Entry(Frame, textvariable=self.stringvar2)
        self.linkedInUserNameEntry.grid(row=2, column=1, padx=5, pady=5, sticky=TK.N + TK.S + TK.E + TK.W)
        self.linkedInUserNameLabel = TK.Label(Frame, text="LinkedIn Username:")
        self.linkedInUserNameLabel.grid(row=2, column=0, sticky=TK.W)

        self.linkedInPass = TK.Entry(Frame, textvariable=self.stringvar3)
        self.linkedInPass.grid(row=3, column=1, padx=5, pady=5, sticky=TK.N + TK.S + TK.E + TK.W)
        self.linkedInPassLabel = TK.Label(Frame, text="LinkedIn Password:")
        self.linkedInPassLabel.grid(row=3, column=0, sticky=TK.W)

        self.jobTitle = TK.Entry(Frame, textvariable=self.stringvar4)
        self.jobTitle.grid(row=4, column=1, padx=5, pady=5, sticky=TK.N + TK.S + TK.E + TK.W)
        self.jobTitleLabel = TK.Label(Frame, text="Desired Job Title:")
        self.jobTitleLabel.grid(row=4, column=0, sticky=TK.W)

        self.city = TK.Entry(Frame)
        self.city.grid(row=6, column=1, padx=5, pady=5, sticky=TK.N + TK.S + TK.E + TK.W)
        self.cityLabel = TK.Label(Frame, text="Location City:")
        self.cityLabel.grid(row=6, column=0, sticky=TK.W)

        self.state = TK.Entry(Frame, textvariable=self.stringvar6)
        self.state.grid(row=7, column=1, padx=5, pady=5, sticky=TK.N + TK.S + TK.E + TK.W)
        self.stateLabel = TK.Label(Frame, text="Location State:")
        self.stateLabel.grid(row=7, column=0, sticky=TK.W)

        self.phone = TK.Entry(Frame, textvariable=self.stringvar7)
        self.phone.grid(row=8, column=1, padx=5, pady=5, sticky=TK.N + TK.S + TK.E + TK.W)
        self.phoneLabel = TK.Label(Frame, text="Your Phone Number:")
        self.phoneLabel.grid(row=8, column=0, sticky=TK.W)

        self.num_loops_label = TK.Label(Frame, text="Page Limit:")
        self.num_loops_label.grid(row=9, column=0, sticky=TK.W)
        self.num_loops = TK.Entry(Frame, textvariable=self.stringvar10)
        self.num_loops.grid(row=9, column=1,  sticky=TK.N + TK.S + TK.E + TK.W, padx=5, pady=5)

        self.resume_path = TK.Entry(Frame, textvariable=self.stringvar8)
        self.resume_path.grid(row=10, column=1, padx=5, pady=5, sticky=TK.N + TK.S + TK.E + TK.W)
        self.resume_path_label = TK.Label(Frame, text="Resume Path:")
        self.resume_path_label.grid(row=10, column=0, sticky=TK.W)
        self.resume_path.configure(state="readonly")

        self.resumeBtn = HoverButton(Frame, text='Browse Resume', activebackground='lightgrey', command=self.askopenfileResume)
        self.resumeBtn.grid(row=10, column=2,  sticky=TK.N + TK.S + TK.E + TK.W, padx=5, pady=5)

        self.driver_path = TK.Entry(Frame, textvariable=self.stringvar9)
        self.driver_path.grid(row=11, column=1, padx=5, pady=5, sticky=TK.N + TK.S + TK.E + TK.W)
        self.driver_path_label = TK.Label(Frame, text="Driver Path:")
        self.driver_path_label.grid(row=11, column=0, sticky=TK.W)
        self.driver_path.configure(state="readonly")

        self.driver_btn = HoverButton(Frame, text='Browse Drivers', activebackground='lightgrey', command=self.askopenfileDriver)
        self.driver_btn.grid(row=11, column=2,  sticky=TK.N + TK.S + TK.E + TK.W, padx=5, pady=5)

        self.submit_button = HoverButton(Frame, text="Submit", activebackground='lightgrey', command=self.apply)
        self.submit_button.grid(row=12, column=0, columnspan=2,  sticky=TK.N + TK.S + TK.E + TK.W, padx=5, pady=5)

    def askopenfileResume(self):
        f = filedialog.askopenfile(mode='r')
        if f:
            filename = f.name

            self.resume_path.configure(state="normal")
            self.resume_path.delete(0, 'end')
            self.resume_path.insert(0, filename)
            self.resume_path.configure(state="readonly")

    def askopenfileDriver(self):
        f = filedialog.askopenfile(mode='r')
        if f:
            filename = f.name

            self.driver_path.configure(state="normal")
            self.driver_path.delete(0, 'end')
            self.driver_path.insert(0, filename)
            self.driver_path.configure(state="readonly")

    def validate(self, *args):
        a = self.var.get()
        b = self.stringvar1.get()
        c = self.stringvar2.get()
        d = self.stringvar3.get()
        e = self.stringvar4.get()
        g = self.stringvar6.get()
        h = self.stringvar7.get()
        i = self.stringvar8.get()
        j = self.stringvar9.get()

        if a and b and c and d and e and g and h and i and j:
            self.submit_button.config(state='normal')
        else:
            self.submit_button.config(state='disabled')

    def apply(self):
        c = LinkedinEasyApply.linkedinApply(phone=self.phone.get(), username=self.linkedInUserNameEntry.get(), password=self.linkedInPass.get(), driverPath=self.driver_path.get(), jobTitle=self.jobTitle.get(),
                                            city=self.city.get(), state=self.state.get(), resumeLocation=self.resume_path.get(), num_loops=self.num_loops.get())

        c.init_driver()
        time.sleep(3)
        print ("Logging into Linkedin account ...")
        c.login()
        time.sleep(1)
        dicts = c.searchJobs()
        subject = "LinkedIn Job Application Report: " + str(dt.date.today())

        df = ReportingModule.saveReportAsCSV(dicts)
        time.sleep(1)
        sendMail.send_email(user=self.emailEntry.get(), pwd=self.emailPass.get(), recipient=self.emailEntry.get(), subject=subject, df=df)

        TK.messagebox.showinfo("Success", "Sequence Complete!")


class HoverButton(TK.Button):
    """HoverButton class to change color of button when hovering.

    Attributes:
        defaultBackground: Background instance of window
        defaultForeground: Foreground instance of window
        bind: Event to trigger color change of button

    """
    def __init__(self, master, **kw):
        """Inits SampleClass with master widget."""
        TK.Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.defaultForeground = self["foreground"]

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        """Hover over button event"""
        self['background'] = self['activebackground']
        self['foreground'] = self['activeforeground']

    def on_leave(self, e):
        """Hover off button event"""
        self['background'] = self.defaultBackground
        self['foreground'] = self.defaultForeground
