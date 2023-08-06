from tkinter import *
import csv

def bloodBank_run(root):
    #BloodType Label
    btypeL = Label(root, text = 'Blood Type:')
    btypeL.grid(row = 0, column =0, padx=20, pady =5)
    # BloodType Entry
    btp = StringVar()
    btype = OptionMenu(root, btp, 'O+', 'O-', 'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-')
    btype.grid(row = 0, column =1)

    def GetQuantity():
        btype_ID = btp.get()
        fields = ['BloodType', 'Quantity']
        with open('CSVData/BloodBank.csv', 'r') as csv_file:
            reader =  csv.DictReader(csv_file, fieldnames=fields)
            Quantity.delete(0, END)
            for row in reader:
                if row['BloodType'] == str(btype_ID):
                    Quantity.insert(0, row['Quantity'])

    # Get Quantity by BloodType
    onClick = Button(root, command = GetQuantity, text = 'Get Quantity')
    onClick.grid(row =0, column =2, padx = 5)

    # Quantity Label
    qtyL = Label(root, text = 'Quantity:')
    qtyL.grid(row = 1, column = 0, padx =20, pady =5)
    # Quantity Entry
    qty =  IntVar()
    Quantity = Entry(root, textvariable = qty)
    Quantity.grid(row =1, column =1)

    def SaveChanges():
        from tempfile import NamedTemporaryFile
        import shutil
        filename = 'CSVData/Bloodbank.csv'
        tempfile = NamedTemporaryFile(mode ='w', delete = False)

        fields = ['BloodType', 'Quantity']
        with open(filename, 'r') as csvfile, tempfile:
            reader =  csv.DictReader(csvfile, fieldnames = fields)
            writer =  csv.DictWriter(tempfile, fieldnames = fields)
            for row in reader:
                if row['BloodType']==str(btp.get()):
                    row['Quantity']=qty.get()
                row = {'BloodType':row['BloodType'], 'Quantity': row['Quantity']}
                writer.writerow(row)
        shutil.move(tempfile.name, filename)

    # Edit Details
    edit = Button(root, command = SaveChanges, text = 'Save Changes')
    edit.grid(row = 2, column =0, pady = 5)

    def ClearScreen():
        Quantity.delete(0, END)
    
    # Clear Details
    clr = Button(root, command=ClearScreen, text = 'Clear')
    clr.grid(row =2, column= 1, pady =5)
    
    # Cancel
    Button(root, text="Cancel", command=root.destroy).grid(row = 3, column = 0, pady = 5)
    def GoToHome(root):
        import main
        root.destroy()
        main.call()
        
    #Home
    Button(root, text = 'Home', command = lambda: GoToHome(root)).grid(row=3, column =1, pady = 5)

def BloodBank():
    
    root = Tk()
    root.title("Blood Bank Details")
    root.geometry('400x300')
    bloodBank_run(root)
    root.mainloop()
