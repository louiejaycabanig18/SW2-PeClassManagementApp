import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from PeClassDbSqlite import PeClassDbSqlite
from PIL import Image, ImageTk
import os


class PeClassManagementGuiCtk(customtkinter.CTk):
    def __init__(self, dataBase=PeClassDbSqlite('AppDb.db')):
        super().__init__()
        self.db = dataBase
        
        self.title('PE Class Management System')
        self.geometry('1070x620')
        self.config(bg='#FFF8DC') #######
        self.resizable(False, False)

        self.font1 = ('Roboto Serif', 20, 'bold')
        self.font2 = ('Roboto Serif', 12, 'bold')


        # Data Entry Form
        # 'Class No' Label and Entry Widgets
        self.id_label = self.newCtkLabel('Class No:')
        self.id_label.place(x=330, y=400)
        self.id_entry = self.newCtkEntry()
        self.id_entry.place(x=440, y=400)

        # 'Name' Label and Entry Widgets
        self.name_label = self.newCtkLabel('Name:')
        self.name_label.place(x=330, y=480)
        self.name_entry = self.newCtkEntry()
        self.name_entry.place(x=440, y=480)

        # 'Course' Label and Combo Box Widgets
        self.course_label = self.newCtkLabel('Course:')
        self.course_label.place(x=330, y=560)
        self.course_entry = self.newCtkEntry()
        self.course_entry.place(x=440, y=560)

        # 'BMI' Label and Combo Box Widgets
        self.bmi_label = self.newCtkLabel('BMI:')
        self.bmi_label.place(x=760, y=400)
        self.bmi_entry = self.newCtkEntry()
        self.bmi_entry.place(x=830, y=400)

        # 'Sport' Label and Combo Box Widgets
        self.sport_label = self.newCtkLabel('Sport:')
        self.sport_label.place(x=760, y=480)
        self.sport_cboxVar = StringVar()
        self.sport_cboxOptions = ['Basketball', 'Football', 'Bowling', 'Chess', 'Running', 'Badminton', 'Weightlifting']
        self.sport_cbox = self.newCtkComboBox(options=self.sport_cboxOptions, 
                                    entryVariable=self.sport_cboxVar)
        self.sport_cbox.place(x=830, y=480)

        self.dirname = os.path.dirname(__file__)

        self.add_img = ImageTk.PhotoImage(Image.open(os.path.join(self.dirname, "add.png")).resize((20,20)))
        self.remove_img = ImageTk.PhotoImage(Image.open(os.path.join(self.dirname, "trash.png")).resize((20,20)))
        self.clear_img = ImageTk.PhotoImage(Image.open(os.path.join(self.dirname, "broom.png")).resize((20,20)))
        self.export_img = ImageTk.PhotoImage(Image.open(os.path.join(self.dirname, "export.png")).resize((20,20)))
        self.import_img = ImageTk.PhotoImage(Image.open(os.path.join(self.dirname, "import_icon.png")).resize((20,20)))
        self.update_img = ImageTk.PhotoImage(Image.open(os.path.join(self.dirname, "system-update.png")).resize((20,20)))
        self.logo_img = ImageTk.PhotoImage(Image.open(os.path.join(self.dirname, "logo.png")).resize((250,250)))
        


        self.logo_label = self.newCtkLabel("", image=self.logo_img)
        self.logo_label.place(x=35, y=20)

        self.add_button = self.newCtkButton(text='Add Student',
                                onClickHandler=self.add_entry,
                                fgColor='#05A312',
                                hoverColor='#00850B',
                                borderColor='#05A312',
                                image=self.add_img
                                )
        self.add_button.place(x=50,y=310)

        self.new_button = self.newCtkButton(text='Clear',
                                borderColor='#FF8000',
                                onClickHandler=lambda:self.clear_form(True),
                                image=self.clear_img)
        self.new_button.place(x=830,y=560)

        self.update_button = self.newCtkButton(text='Update Details',
                                    onClickHandler=self.update_entry,
                                    image=self.update_img)
        self.update_button.place(x=50,y=410)

        self.delete_button = self.newCtkButton(text='Remove Student',
                                    onClickHandler=self.delete_entry,
                                    fgColor='#E40404',
                                    hoverColor='#AE0000',
                                    borderColor='#E40404',
                                    image=self.remove_img)
        self.delete_button.place(x=50,y=360)

        self.export_button = self.newCtkButton(text='Export to CSV',
                                    onClickHandler=self.export_to_csv,
                                    image=self.export_img)
        self.export_button.place(x=50,y=510)
        
        self.import_button = self.newCtkButton(text='Import CSV',
                                    onClickHandler=self.import_csv,
                                    image=self.import_img)
        self.import_button.place(x=50, y=460)

        self.exportjson_button = self.newCtkButton(text='Export to JSON',
                                    onClickHandler=self.export_to_json,
                                    image=self.export_img)
        self.exportjson_button.place(x=50, y=560)


        # Tree View for Database Entries
        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.style.configure('Treeview', 
                        font=self.font2, 
                        foreground='#fff',
                        background='#000',
                        fieldlbackground='#313837')

        self.style.map('Treeview', background=[('selected', 'lightyellow')])

        self.tree = ttk.Treeview(self, height=10)
        self.tree['columns'] = ('Class No', 'Name', 'Course', 'BMI', 'Sport')
        self.tree.column('#0', width=0, stretch=tk.NO)
        self.tree.column('Class No', anchor=tk.CENTER, width=10)
        self.tree.column('Name', anchor=tk.CENTER, width=120)
        self.tree.column('Course', anchor=tk.CENTER, width=130)
        self.tree.column('BMI', anchor=tk.CENTER, width=10)
        self.tree.column('Sport', anchor=tk.CENTER, width=100)


        self.tree.heading('Class No', text='Class No')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Course', text='Course')
        self.tree.heading('BMI', text='BMI')
        self.tree.heading('Sport', text='Sport')

        self.tree.tag_configure("")

        self.tree.place(x=330, y=20, width=700, height=350)
        self.tree.bind('<ButtonRelease>', self.read_display_data)
        
        self.tree.tag_configure('Healty', background='black')
        self.tree.tag_configure('Overweight', background='red')
        self.tree.tag_configure('Underweight', background='orange')

        self.add_to_treeview()

    # new Label Widget
    def newCtkLabel(self, text = 'CTK Label', image=None):
        widget_Font=self.font1
        widget_TextColor='#000'
        widget_BgColor='#FFF8DC'
        widget_Image = image
######
        widget = customtkinter.CTkLabel(self, 
                                    text=text,
                                    font=widget_Font, 
                                    text_color=widget_TextColor,
                                    bg_color=widget_BgColor,
                                    image=widget_Image

        )
        return widget

    # new Entry Widget
    def newCtkEntry(self, text = 'CTK Label'):
        widget_Font=self.font1
        widget_TextColor='#000'
        widget_FgColor='#FFF'
        widget_BorderColor='#FF8000'
        widget_BorderWidth=2
        widget_Width=200

        widget = customtkinter.CTkEntry(self,
                                    font=widget_Font,
                                    text_color=widget_TextColor,
                                    fg_color=widget_FgColor,
                                    border_color=widget_BorderColor,
                                    border_width=widget_BorderWidth,
                                    width=widget_Width)
        return widget

    # new Combo Box Widget
    def newCtkComboBox(self, options=['DEFAULT', 'OTHER'], entryVariable=None):
        widget_Font=self.font1
        widget_TextColor='#000'
        widget_FgColor='#FFF'
        widget_DropdownHoverColor='#0C9295'
        widget_ButtonColor='#0C9295'
        widget_ButtonHoverColor='#0C9295'
        widget_BorderColor='#FF8000'
        widget_BorderWidth=2
        widget_Width=200
        widget_Options=options

        widget = customtkinter.CTkComboBox(self,
                                        font=widget_Font,
                                        text_color=widget_TextColor,
                                        fg_color=widget_FgColor,
                                        border_color=widget_BorderColor,
                                        width=widget_Width,
                                        variable=entryVariable,
                                        values=options,
                                        state='readonly')
        
        # set default value to 1st option
        widget.set(options[0])

        return widget

    # new Button Widget
    def newCtkButton(self, text = 'CTK Button', onClickHandler=None, fgColor='#EEEEE0', hoverColor='#FF5002', bgColor='#FFF8DC', borderColor='#FF8000', image=None):
        widget_Font=self.font1
        widget_TextColor='#000'
        widget_FgColor=fgColor
        widget_HoverColor=hoverColor
        widget_BackgroundColor=bgColor
        widget_BorderColor=borderColor
        widget_BorderWidth=2
        widget_Cursor='hand2'
        widget_CornerRadius=15
        widget_Width=200
        widget_Function=onClickHandler
        widget_Image = image

        widget = customtkinter.CTkButton(self,
                                        text=text,
                                        command=widget_Function,
                                        font=widget_Font,
                                        text_color=widget_TextColor,
                                        fg_color=widget_FgColor,
                                        hover_color=widget_HoverColor,
                                        bg_color=widget_BackgroundColor,
                                        border_color=widget_BorderColor,
                                        border_width=widget_BorderWidth,
                                        cursor=widget_Cursor,
                                        corner_radius=widget_CornerRadius,
                                        width=widget_Width,
                                        image=widget_Image)
       
        return widget

    # Handles
    def add_to_treeview(self):
        entries = self.db.fetch_student()
        self.tree.delete(*self.tree.get_children())
        my_tag='Normal'
        for entry in entries:
            if entry[3] >= 18.5 and entry[3]<= 24.9:
                my_tag='Healthy'
            elif entry[3]> 24.9:
                my_tag='Overweight'
            elif entry[3]< 18.5:
                my_tag='Underweight'
            print(entry)
            self.tree.insert('', END, values=entry, tags=(my_tag))

    def clear_form(self, *clicked):
        if clicked:
            self.tree.selection_remove(self.tree.focus())
            self.tree.focus('')
        self.id_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.course_entry.delete(0, END)
        self.bmi_entry.delete(0,END)
        self.sport_cboxVar.set('Basketball')

    def read_display_data(self, event):
        selected_item = self.tree.focus()
        if selected_item:
            row = self.tree.item(selected_item)['values']
            self.clear_form()
            self.id_entry.insert(0, row[0])
            self.name_entry.insert(0, row[1])
            self.course_entry.insert(0, row[2])
            self.bmi_entry.insert(0, row[3])
            self.sport_cboxVar.set(row[4])
        else:
            pass

    def add_entry(self):
        id=self.id_entry.get()
        name=self.name_entry.get()
        course=self.course_entry.get()
        bmi=float(self.bmi_entry.get())
        sport=self.sport_cboxVar.get()

        if not (id and name and course and bmi and sport):
            messagebox.showerror('Error', 'Enter all fields.')
        elif self.db.id_exists(id):
            messagebox.showerror('Error', 'ID already exists')
        else:
            self.db.insert_student(id, name, course, bmi, sport)
            self.add_to_treeview()
            self.clear_form()
            messagebox.showinfo('Success', 'Data has been inserted')

    def delete_entry(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showerror('Error', 'Choose an employee to delete')
        else:
            id = self.id_entry.get()
            self.db.delete_student(id)
            self.add_to_treeview()
            self.clear_form()
            messagebox.showinfo('Success', 'Data has been deleted')

    def update_entry(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showerror('Error', 'Choose an employee to update')
        else:
            id=self.id_entry.get()
            name=self.name_entry.get()
            course=self.course_entry.get()
            bmi=float(self.bmi_entry.get())
            sport=self.sport_cboxVar.get()
            self.db.update_student(name, course, bmi, sport, id)
            self.add_to_treeview()
            self.clear_form()
            messagebox.showinfo('Success', 'Data has been updated')

    def export_to_csv(self):
        self.db.export_csv()
        messagebox.showinfo('Success', f'Data exported to {self.db.dbName}')

    def import_csv(self):
        self.db.import_csv()
        self.add_to_treeview()
        messagebox.showinfo('Success', f'Data from {self.db.importdbName} has been imported')

    def export_to_json(self):
        self.db.export_json()
        messagebox.showinfo('Success', f'Data exported to {self.db.dbNameJSON}')
