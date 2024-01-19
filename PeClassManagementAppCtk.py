from PeClassDb import PeClassDb
from PeClassManagementGUI import PeClassManagementGuiCtk

def main():
    db = PeClassDb(init=False, dbName='PeClassDb.csv')
    app = PeClassManagementGuiCtk(dataBase=db)
    app.mainloop()

if __name__ == "__main__":
    main()