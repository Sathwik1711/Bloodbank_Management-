from tkinter import *
import csv

def donor_run(root):
    #Donor Label
    DonorL = Label(root, text = 'Donor ID:')
    DonorL.grid(row = 0, column = 0, padx = 20, pady = 5)
    # Donor Entry
    dId = IntVar()
    DonorId = Entry(root, textvariable = dId)
    DonorId.grid(row = 0, column = 1)

    def GetDonor():
        donor_ID = dId.get()
        fields = ['DonorID', 'FirstName', 'LastName', 'Gender', 'BloodRequired', 'PhoneNumber', 'Address']
        with open('CSVData/Donor.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file, fieldnames=fields)
            FirstName.delete(0, END)
            LastName.delete(0, END)
            Gender.delete(0, END)
            BloodRequired.delete(0, END)
            phoneNumber.delete(0, END)
            Address.delete(0, END)
            for row in reader:
                if row['DonorID']==str(donor_ID):
                    FirstName.insert(0, row['FirstName'])
                    LastName.insert(0, row['LastName'])
                    Gender.insert(0, row['Gender'])
                    BloodRequired.insert(0, row['BloodRequired'])
                    phoneNumber.insert(0, row['PhoneNumber'])
                    Address.insert(0, row['Address'])


    # Get Donor Button
    onClick = Button(root, command = GetDonor, text = 'Get Donor')
    onClick.grid(row = 0, column = 2, padx = 5)
    
    # FirstName Label
    FnameL = Label(root, text = 'First Name:')
    FnameL.grid(row = 1, column = 0, padx = 20, pady = 5)
    # FirstName Entry
    fname = StringVar()
    FirstName = Entry(root, textvariable = fname)
    FirstName.grid(row = 1, column = 1)

    # LastName Label
    LnameL = Label(root, text = 'Last Name:')
    LnameL.grid(row = 2, column = 0, padx = 20, pady = 5)
    # LastName Entry
    lname = StringVar()
    LastName = Entry(root, textvariable = lname)
    LastName.grid(row = 2, column = 1)
    
    # Gender Label
    GenderL = Label(root, text = 'Gender:')
    GenderL.grid(row = 3, column =0, padx = 20, pady = 5)
    # Gender Entry
    gender = StringVar()
    Gender = Entry(root, textvariable = gender)
    Gender.grid(row = 3, column = 1)

    # Blood required label
    bloodL = Label(root, text = 'Blood Required:')
    bloodL.grid(row = 4, column = 0, padx= 20, pady = 5)
    # Blood required Entry
    blood = StringVar()
    BloodRequired =  Entry(root, textvariable = blood)
    BloodRequired.grid(row = 4, column = 1)
    
    # Phone number label 
    phoneL = Label(root, text = 'Phone Number:')
    phoneL.grid(row = 5, column = 0, padx= 20, pady = 5)
    # Phone number Entry
    phone = StringVar()
    phoneNumber = Entry(root, textvariable = phone)
    phoneNumber.grid(row = 5, column = 1)

    # Address Label
    addressL = Label(root, text = 'Address:')
    addressL.grid(row=6, column =0, padx =20, pady = 5)
    # Address Entry
    address = StringVar()
    Address = Entry(root, textvariable = address)
    Address.grid(row = 6, column = 1)

    def SaveChanges():
        from tempfile import NamedTemporaryFile
        import shutil
        
        filename = 'CSVData/Donor.csv'
        tempfile = NamedTemporaryFile(mode='w', delete=False)

        fields = ['DonorID', 'FirstName', 'LastName', 'Gender', 'BloodRequired', 'PhoneNumber', 'Address']

        with open(filename, 'r') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=fields)
            writer = csv.DictWriter(tempfile, fieldnames=fields)
            for row in reader:
                if row['DonorID'] == str(dId.get()):
                    row['FirstName'], row['LastName'], row['Gender'], row['BloodRequired'], row['PhoneNumber'], row['Address'] \
                                  = fname.get(), lname.get(), gender.get(), blood.get(), phone.get(), address.get()
                row = {'DonorID': row['DonorID'], 'FirstName': row['FirstName'], 'LastName': row['LastName'], 'Gender': row['Gender'],
                   'BloodRequired': row['BloodRequired'], 'PhoneNumber': row['PhoneNumber'], 'Address':row['Address']}
                writer.writerow(row)

        shutil.move(tempfile.name, filename) 


     # Edit Details
    edit = Button(root, command = SaveChanges, text = 'Save Changes')
    edit.grid(row = 7, column =0, pady = 5)

    def ClearScreen():
        FirstName.delete(0, END)
        LastName.delete(0, END)
        Gender.delete(0, END)
        BloodRequired.delete(0, END)
        phoneNumber.delete(0, END)
        Address.delete(0, END)
        
    # Clear Details
    clr = Button(root, command=ClearScreen, text = 'Clear')
    clr.grid(row =7, column= 1, pady =5)
       
    # Cancel
    Button(root, text="Cancel", command=root.destroy).grid(row = 8, column = 0, pady = 5)

    def GoToHome(root):
        import main
        root.destroy()
        main.call()
        
    #Home
    Button(root, text = 'Home', command = lambda: GoToHome(root)).grid(row=8, column =1, pady = 5)


def donor():
    root = Tk()
    root.title("Donor Details")
    root.geometry('400x300')
    donor_run(root)
    root.mainloop()
