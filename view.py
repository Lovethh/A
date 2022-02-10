import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkcalendar import *

class View(tk.Tk):

    CREDENTIALS = ['Room No.', 'Tenant Name', 'Date Started', 'Electricity Consump.']
    BUTTONS = ['Add', 'Delete']
    INFO_INNER_FRAMES = 2

    def __init__(self, controller):
        super().__init__()

        self.controller = controller

        self._render_components()

    def main(self):
        self.mainloop()

    def _render_components(self):
        self._window_settings()
        self._make_record_section()
        self._make_credential_inputs()
        self._make_buttons()

    def _window_settings(self):
        pass

    def _make_record_section(self):
        '''Treeview Widget'''
        record_frame = ttk.LabelFrame(self, text='Records')
        record_frame.pack(fill='both', pady=5, padx=5)
        self.record_tree = ttk.Treeview(record_frame, columns=(1, 2, 3, 4), show='headings', height=5)
        self.record_tree.pack(fill='both', padx=5, pady=5)
        self._record_tree_cols()

    def _record_tree_cols(self):
        '''Display Treeview CREDENTIALS'''
        column_title = 0
        for index in range(1, len(self.CREDENTIALS)+1):
            self.record_tree.column(f'#{index}')
            self.record_tree.heading(f'#{index}', text=f'{self.CREDENTIALS[column_title]}', anchor='center')
            column_title += 1

    def _make_credential_inputs(self):
        '''Display Tenant Information section'''
        self.main_info_frame = ttk.LabelFrame(self, text='Tenant Information')
        self.main_info_frame.pack(padx=5, pady=5)   

        self.outer_frame = ttk.Frame(self.main_info_frame)
        self.outer_frame.pack()

        fieldname_frame = ttk.Frame(self.outer_frame)
        fieldname_frame.pack(side='left')

        inputs_frame = ttk.Frame(self.outer_frame)
        inputs_frame.pack(side='left')

        for caption in self.CREDENTIALS:
            fieldname = ttk.Label(fieldname_frame, text=f'{caption}')
            fieldname.pack(anchor='w', padx=5, pady=5)
            
        entry_box_count = 0

        for count in range(len(self.CREDENTIALS)):
            entrybox = ttk.Entry(inputs_frame, width=20)
            entrybox.pack(anchor='w', padx=5, pady=5)

            if entry_box_count == 0:
                room = ['1', '2', '3', '4', '5', '6']
                room_number_label = ttk.Combobox(inputs_frame, value=room, width=18)
                room_number_label.pack(anchor='w', padx=5, pady=5)
                room_number_label.current()
                entrybox.destroy()

            if entry_box_count == 2:
                date_started = DateEntry(inputs_frame, width=18)
                date_started.pack(anchor='w', padx=5, pady=5)
                entrybox.destroy()

            entry_box_count += 1

    def _make_buttons(self):
        '''Display Buttons'''

        for i in range(2):
            submit_btn = ttk.Button(self.main_info_frame, text=f'{self.BUTTONS[i]}')
            submit_btn.pack(padx=5, pady=5, fill='both')
