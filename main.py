from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database

host = "localhost"
user = "root"
password = "Rahul"
database = "EmployeeDB"

db = Database(host, user, password, database)

root = Tk()
root.title("DataVision Innovations")
root.geometry("1920x1080+0+0")
root.config(bg="#7E84F7")
root.state("zoomed")

name = StringVar()
age = StringVar()
doj = StringVar()
gender = StringVar()
email = StringVar()
contact = StringVar()

font_name = "Segoe UI"
font_size = 12

# Entry Frame
entries_frame = Frame(root, bg="#7F82BB")
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="DataVision Innovations", font=(font_name, 16, "bold"), bg="#7F82BB", fg="White")
title.grid(row=0, columnspan=2, padx=10, pady=10, sticky="w")

# Name
lbl_name = Label(entries_frame, text="Name", font=(font_name, font_size), bg="#7F82BB", fg="White")
lbl_name.grid(row=1, column=0, padx=10, pady=10, sticky="w")
txtname = Entry(entries_frame, textvariable=name, font=(font_name, font_size), width=30)
txtname.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Age
lbl_age = Label(entries_frame, text="Age", font=(font_name, font_size), bg="#7F82BB", fg="White")
lbl_age.grid(row=1, column=2, padx=10, pady=10, sticky="w")
txtage = Entry(entries_frame, textvariable=age, font=(font_name, font_size), width=30)
txtage.grid(row=1, column=3, padx=10, pady=10, sticky="w")

# DOJ
lbl_doj = Label(entries_frame, text="D.O.J", font=(font_name, font_size), bg="#7F82BB", fg="White")
lbl_doj.grid(row=2, column=0, padx=10, pady=10, sticky="w")
txtdoj = Entry(entries_frame, textvariable=doj, font=(font_name, font_size), width=30)
txtdoj.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# Gender
lbl_gender = Label(entries_frame, text="Gender", font=(font_name, font_size), bg="#7F82BB", fg="White")
lbl_gender.grid(row=2, column=2, padx=10, pady=10, sticky="w")
combobox_gender = ttk.Combobox(entries_frame, font=(font_name, font_size), width=28, textvariable=gender, state="readonly")
combobox_gender["values"] = ("Male", "Female")
combobox_gender.grid(row=2, column=3, padx=10, pady=10, sticky="w")

# Email
lbl_email = Label(entries_frame, text="Email", font=(font_name, font_size), bg="#7F82BB", fg="White")
lbl_email.grid(row=3, column=0, padx=10, pady=10, sticky="w")
txtemail = Entry(entries_frame, textvariable=email, font=(font_name, font_size), width=30)
txtemail.grid(row=3, column=1, padx=10, pady=10, sticky="w")

# Contact
lbl_contact = Label(entries_frame, text="Contact", font=(font_name, font_size), bg="#7F82BB", fg="White")
lbl_contact.grid(row=3, column=2, padx=10, pady=10, sticky="w")
txtcontact = Entry(entries_frame, textvariable=contact, font=(font_name, font_size), width=30)
txtcontact.grid(row=3, column=3, padx=10, pady=10, sticky="w")

# Address
lbl_address = Label(entries_frame, text="Address", font=(font_name, font_size), bg="#7F82BB", fg="White")
lbl_address.grid(row=4, column=0, padx=10, pady=10, sticky="w")
txtaddress = Text(entries_frame, width=85, height=5, font=(font_name, font_size))
txtaddress.grid(row=5, column=0, columnspan=4, padx=10, sticky="w")

# CRUD Functions
def getData(event):
    selected_row = tv.focus()
    if not selected_row:
        return
    data = tv.item(selected_row)
    global row
    row = data["values"]
    if not row:
        return
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    gender.set(row[4])
    email.set(row[5])
    contact.set(row[6])
    txtaddress.delete(1.0, END)
    txtaddress.insert(END, row[7])

def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)

def add_employee():
    if txtname.get() == "" or txtage.get() == "" or txtdoj.get() == "" or combobox_gender.get() == "" or txtemail.get() == "" or txtcontact.get() == "" or txtaddress.get(1.0, END).strip() == "":
        messagebox.showerror("Error In Input", "Please Fill The Details")
        return
    db.insert(txtname.get(), txtage.get(), txtdoj.get(), combobox_gender.get(), txtemail.get(), txtcontact.get(), txtaddress.get(1.0, END).strip())
    displayAll()
    messagebox.showinfo("Success", "Record Inserted")
    clear_employee()

def Update_employee():
    if txtname.get() == "" or txtage.get() == "" or txtdoj.get() == "" or combobox_gender.get() == "" or txtemail.get() == "" or txtcontact.get() == "" or txtaddress.get(1.0, END).strip() == "":
        messagebox.showerror("Error In Input", "Please Fill The Details")
        return
    db.update(row[0], txtname.get(), txtage.get(), txtdoj.get(), combobox_gender.get(), txtemail.get(), txtcontact.get(), txtaddress.get(1.0, END).strip())
    displayAll()
    messagebox.showinfo("Success", "Record Updated")
    clear_employee()

def delete_employee():
    selected_items = tv.selection()
    if not selected_items:
        messagebox.showerror("Error", "Please select at least one record to delete.")
        return

    confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete the selected record(s)?")
    if confirm:
        for item in selected_items:
            data = tv.item(item)
            row_id = data["values"][0]
            db.delete(row_id)

        clear_employee()
        displayAll()
        messagebox.showinfo("Success", "Record(s) Deleted")

def delete_all_employees():
    confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete all records?")
    if confirm:
        db.delete_all()
        displayAll()
        messagebox.showinfo("Success", "All records deleted and ID reset")

def clear_employee():
    name.set("")
    age.set("")
    doj.set("")
    gender.set("")
    email.set("")
    contact.set("")
    txtaddress.delete(1.0, END)

# Button Frame
btn_frame = Frame(entries_frame, bg="#7F82BB")
btn_frame.grid(row=6, column=0, columnspan=5, padx=10, pady=10, sticky="w")

btn_add = Button(btn_frame, command=add_employee, text="Add", width=10, font=(font_name, 12, "bold"), bg="#46A9F7", fg="White", bd=0)
btn_add.grid(row=0, column=0, padx=10)

btn_update = Button(btn_frame, command=Update_employee, text="Update", width=10, font=(font_name, 12, "bold"), bg="#46A9F7", fg="White", bd=0)
btn_update.grid(row=0, column=1, padx=10)

btn_clear = Button(btn_frame, command=clear_employee, text="Clear", width=10, font=(font_name, 12, "bold"), bg="#46A9F7", fg="White", bd=0)
btn_clear.grid(row=0, column=2, padx=10)

btn_delete = Button(btn_frame, command=delete_employee, text="Delete", width=10, font=(font_name, 12, "bold"), bg="#46A9F7", fg="White", bd=0)
btn_delete.grid(row=0, column=3, padx=10)

btn_delete_all = Button(btn_frame, command=delete_all_employees, text="Delete All Records", width=20, font=(font_name, 12, "bold"), bg="#46A9F7", fg="White", bd=0)
btn_delete_all.grid(row=0, column=4, padx=10)


# Table Frame
tree_frame = Frame(root, bg="#ecf0f1")
tree_frame.place(x=0, y=400, width=1920, height=520)

# Treeview
tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=50)  # Adjusted width for ID column
tv.heading("2", text="Name")
tv.heading("3", text="Age")
tv.column("3", width=50)  # Adjusted width for Age column
tv.heading("4", text="D.O.J")
tv.column("4", width=100)  # Adjusted width for D.O.J column
tv.heading("5", text="Gender")
tv.column("5", width=80)  # Adjusted width for Gender column
tv.heading("6", text="Email")
tv.heading("7", text="Contact")
tv.column("7", width=100)  # Adjusted width for Contact column
tv.heading("8", text="Address")
tv.column("8", width=200)  # Adjusted width for Address column
tv["show"] = "headings"
tv.pack(fill=BOTH, expand=True)  # Adjusted pack options


# Bind the getData function to the Treeview selection
tv.bind("<ButtonRelease-1>", getData)

displayAll()

root.mainloop()
