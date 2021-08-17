from sqlpack import sql
from qrcodegen import qrscan

choice = int(input("What do you want to do?\n 1]Add new Patient Record\n 2]Add new Medical Authority\n 3]Add new Insurance Authority\n"))

if choice == 1:
    aadharNumber = input("Please enter the patient's aadhar card number")
    runner = True
    while runner:
        sql.inserteverything(aadharNumber)
        qrscan.qrmaker(aadharNumber)
        askAgain = input("Do you want to insert again?(y/n)\n")
        if askAgain == 'n':
            print("Exiting Process....")
            runner = False

elif choice == 2:
    runner = True
    while runner:
        sql.insert_newMOrganisation()
        askAgain = input("Do you want to insert again?(y/n)\n")
        if askAgain == 'n':
            print("Exiting Process....")
            runner = False


elif choice == 3:
    runner = True
    while runner:
        sql.insert_newIOrganisation()
        askAgain = input("Do you want to insert again?(y/n)\n")
        if askAgain == 'n':
            print("Exiting Process....")
            runner = False



