from tkinter import *

def start(root):
    root.title("Home")
    root.geometry('400x300')

    head =  Label(root, text = 'Welcome to Blood Bank Management Portal')
    head.pack()

    # Launch Patient Details from home
    patient = Button(root, text = 'Patient Details', command = lambda: ChangeToPatient(root))
    patient.pack()


    # Launch Donor Details from home
    donor = Button(root, text = 'Donor Details', command = lambda: ChangeToDonor(root))
    donor.pack()

    # Launch Blood Bank details from home
    bbank = Button(root, text = 'Blood Bank Details', command = lambda: ChangeToBank(root))
    bbank.pack()

    # Cancel
    Button(root, text="Cancel", command=root.destroy).pack()

def ChangeToPatient(root):
    import Patient as pt
    root.destroy()
    pt.patient()

def ChangeToDonor(root):
    import Donor as dn
    root.destroy()
    dn.donor()

def ChangeToBank(root):
    import BloodBank as bb
    root.destroy()
    bb.BloodBank()
 
def call():
    root = Tk()
    start(root)
    root.mainloop()

if __name__=="__main__":
    call()
    
