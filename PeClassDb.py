from PeClassDbEntry import PeClassDbEntry
from tkinter import filedialog
import csv


class PeClassDb:

    def __init__(self, init=False, dbName='PeClassDb.csv', importdbName='DbImport.csv', dbNameJSON='PeClassDb.json'):
   

        # CSV filename 
        self.dbName = dbName
        self.importdbName = importdbName
        self.dbNameJSON = dbNameJSON
        # initialize container of database entries 
        self.dbEntries = []
        print('TODO: __init__')


    def fetch_student(self):


        tupleList = []
        print('TODO: fetch_orders')
        for entry in self.dbEntries:
            tupleList.append((entry.id, entry.name, entry.course, entry.bmi, entry.sport))
        return tupleList

    def insert_student(self, id, name, course, bmi, sport):


        newEntry = PeClassDbEntry(id=id, name=name, course=course, bmi=bmi, sport=sport)
        self.dbEntries.append(newEntry)
        print('TODO: insert_order')

    def delete_student(self, id):
        """
        - deletes the corresponding entry in the database as specified by 'id'
        - no return value
        """
        print('TODO: delete_order')
        for entry in self.dbEntries:
            if getattr(entry, "id") == id:
                self.dbEntries.remove(entry)


    def update_student(self, new_name, new_course, new_bmi, new_sport, id):
        """
        - updates the corresponding entry in the database as specified by 'id'
        - no return value
        """
        print('TODO: update_order')
        for entry in self.dbEntries:
            if getattr(entry, "id") == id:
                entry.name = new_name
                entry.course = new_course
                entry.bmi = new_bmi
                entry.sport = new_sport

    def export_csv(self):
        """
        - exports database entries as a CSV file
        - CSV : Comma Separated Values
        - no return value
        - example
        12,Eileen Dover,SW-Engineer,Male,On-Site
        13,Ann Chovey,HW-Engineer,Female,On-Site
        14,Chris P. Bacon,SW-Engineer,Male,On-Leave
        15,Russell Sprout,SW-Engineer,Male,Remote
        16,Oscar Lott,Project-Manager,Male,On-Site        
        """
        print('TODO: export_csv')
        with open(self.dbName, "w") as file:
            for entry in self.dbEntries:
                file.write(f"{entry.id},{entry.name},{entry.course},{entry.bmi},{entry.sport} \n")

    def import_csv(self):
        print('TODO: import_csv')
        self.dbEntries.clear()
        fld = filedialog.askopenfilename(title="Open CSV", filetypes = (('CSV File', '*.csv'), ("All Files", "*.*")))
        with open(fld) as file:
            csv_reader = csv.reader(file, delimiter=",")
            for row in csv_reader:
                newId = row[0]
                newName = row[1]
                newCourse = row[2]
                newBMI = float(row[3])
                newSport = row[4]
                self.insert_student(newId, newName, newCourse, newBMI, newSport)
                

    def export_json(self):
        print('TODO: export_json')
        with open(self.dbNameJSON, "w") as file:
            for entry in self.dbEntries:
                file.write(f"{entry.id},{entry.name},{entry.course},{entry.bmi},{entry.sport} \n")


    def id_exists(self, id):
        """
        - returns True if an entry exists for the specified 'id'
        - else returns False
        """
        for entry in self.dbEntries:
            if getattr(entry, "id") == id:
                return True
        else:
            return False
        
    
