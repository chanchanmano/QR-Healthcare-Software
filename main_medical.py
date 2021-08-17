from sqlpack import sql
from qrcodegen import qrscan

choice = int(input("What do you want to do?\n 1]Retrieval of data \n 2]Updation of an instane for Existing Patient\n 3]Insertion of an Instance for Existing Patient\n"))
seccode = int(input("Please Enter the Organisation's Access Code"))

if choice == 1:
    iorm = input("Please enter  Retrieval Password.\n")
    runner = True

    while runner:
        aadharNumber = qrscan.qrscanner()
        sql.retreivalm(aadharNumber)
        askAgain = input("Do you want to retrieve again?(y/n)\n")
        if askAgain == 'n':
            print("Exiting Process....")
            runner = False

elif choice == 2:
    iorm = input("Please enter  Updation Password.\n")
    runner = True
    whichtable=input("")
    while runner:
        aadharNumber = qrscan.qrscanner()
        sql.update_value(aadharNumber)
        askAgain = input("Do you want to update another value again?(y/n)\n")
        if askAgain == 'n':
            print("Exiting Process....")
            runner = False

elif choice == 3:
    iorm = input("Please enter Insertion Password.\n")
    runner = True

    while runner:
        aadharNumber = qrscan.qrscanner()
        sql.insertoneinstance(aadharNumber)
        askAgain = input("Do you want to insert another instance for the same patient?(y/n)\n")
        if askAgain == 'n':
            print("Exiting Process....")
            runner = False