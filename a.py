from tkinter import *
from tkinter import ttk
from tkcalendar import *
import sqlite3

root = Tk()

# Create Database
cdb = sqlite3.connect('Database_file.db')

# Cursor
c = cdb.cursor()

# CreateTable
def create_t():
    cdb = sqlite3.connect('Database_file.db')
    c = cdb.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS addresses (
room_number INTEGER, 
client_name TEXT, 
date_started INTEGER, 
elec_consump INTEGER)'''
)
    cdb.commit()

create_t()

# Frame
rec_frame = LabelFrame(root, text='Records')
rec_frame.pack(fill='both', pady=5, padx=5)
info_frame = LabelFrame(root, text='Information')
info_frame.pack(padx=5, pady=5)

# Create TextBox
rm_num = Entry(info_frame, width=20)
name = Entry(info_frame, width=20)
name.grid(row=1, column=1, pady=5)
ds = DateEntry(info_frame, width=17)
ds.grid(row=2, column=1, pady=5)
ec = Entry(info_frame, width=20)
ec.grid(row=3, column=1, pady=5)

# LabelBox
rm_num_label = Label(info_frame, text='Room No.')
rm_num_label.grid(row=0, column=0)
name_label = Label(info_frame, text='Client Name')
name_label.grid(row=1, column=0)
ds_label = Label(info_frame, text='Date Started')
ds_label.grid(row=2, column=0)
ec_label = Label(info_frame, text='Electricity Consump.')
ec_label.grid(row=3, column=0)

# Treeview
trv = ttk.Treeview(rec_frame, columns=(1, 2, 3, 4), show='headings', height=5)
trv.pack(fill='both', padx=5, pady=5)

trv.heading(1, text='Room No.')
trv.heading(2, text='Client Name')
trv.heading(3, text='Date Started')
trv.heading(4, text='Electricity Consump.')

trv.column(1, width=70)
trv.column(2, width=300)
trv.column(3, width=300)
trv.column(4, width=300)

# ComboBox
rm = ['1', '2', '3', '4', '5', '6']
cmb = ttk.Combobox(info_frame, value=rm, width=17)
cmb.grid(row=0, column=1, pady=5)
cmb.current()


# Submit Function
def submit():
  cdb = sqlite3.connect('Database_file.db')
  c = cdb.cursor()
  c.execute('INSERT INTO addresses VALUES (:room_number, :client_name, :date_started, :elec_consump)',
            {
                'room_number': cmb.get(),
                'client_name': name.get(),
                'date_started': ds.get(),
                'elec_consump': ec.get()
            }
            )

  cdb.commit()
  cmb.delete(0, END)
  name.delete(0, END)
  ec.delete(0, END)


# Submit Button
submit_btn = Button(info_frame, text='Add', command=submit)
submit_btn.grid(row=5, columnspan=2, ipadx=80, pady=5)

# Delete Button
delete_btn = Button(info_frame, text='Delete')
delete_btn.grid(row=6, columnspan=2, ipadx=75, pady=5)

# Commit changes
cdb.commit()

# Close connection
cdb.close()

root.mainloop()
