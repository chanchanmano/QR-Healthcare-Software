import sqlite3

import guifunc
from hashalgo import hashfun
import re
from sqlite3 import Error

ltablcolm = [('ID','Name','DOB','Gender','PhoneNo', 'EmailId','EmergencyContact','Address','BloodGroup','Comorbid','MaritalStatus',
            'EmployementStatus','Insured','MedicalContact','Terminated'),('PID','Height','Weight','BP','HeartRate','Hemoglobin',
            'RespirationRate'),('PID','Allergen','Effect','Fatal'),('PID','Deficiency'),('PID','TechnicalName','DOI','Doses','State','City','Status'
            'SideEffect'),('PID','Speciality','ProcedureName','DateTime','HospitalPerformedAt','Surgeon'),('PID','Name','Intensity',
            'ConsultationDate','VascularSystemEffected'),('PID','Name','UndergoingTreatmentFor','MedicationAdministered','PrescribedOn',
            'Duration','PrescribedBy','Status'),('PID','Author','AuthorDesignation','Pertaining')]

def printcols(x):
    indx = 1
    for i in ltablcolm[x]:

        print(indx,"]",i,"\n")
        indx += 1

ltable = ['Patient','General_Medical_Information','Known_Allergies','Deficiencies','Vaccinations','Previous_Surgeries','Medical_Conditions','Treatments','Remarks']

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def update_value(aadharnum):

    database = r"Apollo_Systems.db"


    #if x == '1234':
    hkey = hashfun.hashalgorithm(aadharnum)
    con = create_connection(database)
    cur = con.cursor()
    sqlquery = ''''''
    whatWant = int(input(
        "What data is to be updated? \n 1]Patient Information \n 2]General Medical Information \n 3]Known Allergies \n 4]Deficiencies \n 5]Vaccinations \n 6]Previous Surgeries \n 7]Medical Conditions \n 8]Treatments \n 9]Remarks"))
    print("Fetching Table and it's columns")
    printcols((whatWant-1))
    colspecify = int(input("Enter the index of the attribute to be updated"))
    colselected = ltablcolm[whatWant-1][colspecify-1]
    tblselected = ltable[whatWant-1]
    valueUpdatedto = input("Enter the updated value: ")

    sqlquery = '''UPDATE ''' + tblselected + ''' SET ''' + colselected + '''= \''''+ valueUpdatedto+ '''\' WHERE ID=\'''' + hkey + '''\''''
    cur.execute(sqlquery)
    con.commit()


def create_patient(conn, patient):

    sql = """INSERT INTO patient(ID,Name,DoB,Gender,PhoneNo,EmailId,EmergencyContact,Address,
                                BloodGroup,Comorbid,MaritalStatus,EmployementStatus,Insured,
                                MedicalContact,Terminated)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql,patient)
    conn.commit()
    return cur.lastrowid

def insert_patient(aadharnum):

    hkey=hashfun.hashalgorithm(aadharnum)

    database = r"Apollo_Systems.db"
    IDip=hkey
    NameIP = input("Enter full name of patient(FirstName MiddleName LastName): ")
    DoBIP = input("Enter DoB (YYYY-MM-DD): ")
    GenderIP = input("Enter Gender (M,F,O): ")
    PhnNoIP = input("Enter Contact No.: ")
    EmailIdIP = input("Enter Email-id of patient: ")
    EmergencyContactIP = input("Enter emergency contact for the patient: ")
    AddressIP = input("Enter address of patient: ")
    BloodGroupIP = input("Enter blood group of patient: ")
    ComorbidIP = input("Is patient comormid?(0,1): ")
    MaritalStatusIP = input("Enter marital status of the patient: ")
    EmploymentStatusIP = input("Enter employment status: ")
    InsuredIP = input("Does the patient have an insurance? (0,1): ")
    MedicalContactIP = input("Enter Medical Contact number of the patient: ")
    TerminatedIP = input("Has patient terminated?(0,1): ")

    conn = create_connection(database)
    with conn:
        # create a new project
        patient = (IDip,NameIP,DoBIP,GenderIP,PhnNoIP,EmailIdIP,EmergencyContactIP,AddressIP,BloodGroupIP,ComorbidIP,
                     MaritalStatusIP,EmploymentStatusIP,InsuredIP,MedicalContactIP,TerminatedIP)
        create_patient(conn, patient)

def inserteverything(aadharnum):

    insert_patient(aadharnum)
    print("\nSuccessfully inserted data")
    insert_general_medical_information(aadharnum)
    print("\nSuccessfully inserted data")

    x = int(input("How many records are to be inserted Known Allergies?"))
    for i in range(x):
        insert_known_allergies(aadharnum)
    print("\nSuccessfully inserted data")

    x = int(input("How many records are to be inserted Deficiencies?"))
    for i in range(x):
        insert_deficiency(aadharnum)
    print("\nSuccessfully inserted data")

    x = int(input("How many records are to be inserted in Vaccinations ?"))
    for i in range(x):
        insert_vaccination(aadharnum)
    print("\nSuccessfully inserted data")

    x = int(input("How many records are to be inserted in Previous Surgeries?"))
    for i in range(x):
        insert_previous_surgeries(aadharnum)
    print("\nSuccessfully inserted data")

    x = int(input("How many records are to be inserted in Medical Conditions?"))
    for i in range(x):
        insert_medical_conditions(aadharnum)
    print("\nSuccessfully inserted data")

    x = int(input("How many records are to be inserted in Treatments?"))
    for i in range(x):
        insert_treatments(aadharnum)
    print("\nSuccessfully inserted data")

    x = int(input("How many records are to be inserted in Remarks?"))
    for i in range(x):
        insert_remarks(aadharnum)
    print("\nSuccessfully inserted data")



def retreivalm(aadharnum):

    database = r"Apollo_Systems.db"
    x = input("Validate Retrieval By entering Organisation Password")

    if x == '1234':
        hkey=hashfun.hashalgorithm(aadharnum)
        con = create_connection(database)

        cur=con.cursor()
        sqlquery=''''''
        whatWant=int(input("What data is to be retrieved? \n 1]Patient Information \n 2]General Medical Information \n 3]Known Allergies \n 4]Vaccinations \n 5]Previous Surgeries \n 6]Medical Conditions \n 7]Treatments \n 8]Remarks"))
        if whatWant == 1:
            sqlquery='''SELECT * FROM Patient WHERE ID=\''''+hkey+'''\''''
        elif whatWant == 2:
            sqlquery = '''SELECT * FROM General_Medical_Information WHERE PID=\'''' + hkey + '''\''''
        elif whatWant == 3:
            sqlquery = '''SELECT * FROM Known_Allergies WHERE PID=\'''' + hkey + '''\''''
        elif whatWant == 4:
            sqlquery = '''SELECT * FROM Vaccinations WHERE PID=\'''' + hkey + '''\''''
        elif whatWant == 5:
            sqlquery = '''SELECT * FROM Previous_Surgeries WHERE PID=\'''' + hkey + '''\''''
        elif whatWant == 6:
            sqlquery = '''SELECT * FROM Medical_Conditions WHERE PID=\'''' + hkey + '''\''''
        elif whatWant == 7:
            sqlquery = '''SELECT * FROM Treatments WHERE PID=\'''' + hkey + '''\''''
        elif whatWant == 8:
            sqlquery = '''SELECT * FROM Remarks WHERE PID=\'''' + hkey + '''\''''
        else:
            "Please Select A Valid Option! Process will Start Again."
        cur.execute(sqlquery)
        records = cur.fetchall()
        match = re.findall("FROM (\S+\S)", sqlquery)
        tablename = match[0]
        retinfo(records,tablename)
    else:
        print("Entered password is wrong")


def retreivalmgui(tableindx,key):
    database = r"Apollo_Systems.db"

    con = create_connection(database)
    cur = con.cursor()
    sqlquery=''''''
    whatWant = int(tableindx)
    if whatWant == 0:
        sqlquery = '''SELECT * FROM Patient WHERE ID=\'''' + key + '''\''''
    elif whatWant == 1:
        sqlquery = '''SELECT * FROM General_Medical_Information WHERE PID=\'''' + key + '''\''''
    elif whatWant == 2:
        sqlquery = '''SELECT * FROM Known_Allergies WHERE PID=\'''' + key + '''\''''
    elif whatWant == 3:
        sqlquery = '''SELECT * FROM Deficiencies WHERE PID=\'''' + key + '''\''''
    elif whatWant == 4:
        sqlquery = '''SELECT * FROM Vaccinations WHERE PID=\'''' + key + '''\''''
    elif whatWant == 5:
        sqlquery = '''SELECT * FROM Previous_Surgeries WHERE PID=\'''' + key + '''\''''
    elif whatWant == 6:
        sqlquery = '''SELECT * FROM Medical_Conditions WHERE PID=\'''' + key + '''\''''
    elif whatWant == 7:
        sqlquery = '''SELECT * FROM Treatments WHERE PID=\'''' + key + '''\''''
    elif whatWant == 8:
        sqlquery = '''SELECT * FROM Remarks WHERE PID=\'''' + key + '''\''''
    else:
        "Please Select A Valid Option! Process will Start Again."
    cur.execute(sqlquery)
    records = cur.fetchall()
    match = re.findall("FROM (\S+\S)", sqlquery)
    tablename = match[0]
    listwithvals = retinfogui(records, tablename)
    return listwithvals




def retreivali(aadharnum):
    database = r"Apollo_Systems.db"
    x = input("Validate Retrieval By entering Organisation Password")

    if x == '1234':
        hkey = hashfun.hashalgorithm(aadharnum)
        con = create_connection(database)

        cur = con.cursor()
        sqlquery = ''''''
        whatWant = input(
            "What data is to be retrieved? \n 1]Patient Information \n 2]General Medical Information \n 3]Previous Surgeries \n 4]Medical Conditions \n 5]Treatments \n ")
        if whatWant == 1:
            sqlquery = '''SELECT * FROM Patient WHERE ID=\'''' + hkey + '''\''''
        elif whatWant == 2:
            sqlquery = '''SELECT * FROM General_Medical_Information WHERE PID=\'''' + hkey + '''\''''
        elif whatWant == 3:
            sqlquery = '''SELECT * FROM Previous_Surgeries WHERE PID=\'''' + hkey + '''\''''
        elif whatWant == 4:
            sqlquery = '''SELECT * FROM Medical_Conditions WHERE PID=\'''' + hkey + '''\''''
        elif whatWant == 5:
            sqlquery = '''SELECT * FROM Treatments WHERE PID=\'''' + hkey + '''\''''
        else:
            "Please Select A Valid Option! Process will Start Again."
        cur.execute(sqlquery)
        records = cur.fetchall()
        match = re.findall("FROM (\S+\S)", sqlquery)
        tablename = match[0]
        retinfo(records, tablename)
    else:
        print("Entered password is wrong")


def retinfo (record,tablename):
    conn = sqlite3.connect('Apollo_Systems.db')
    cursor = conn.execute('select * from '+tablename)
    colnames = cursor.description

    for i in range(1,len(colnames)):
        print(colnames[i][0],":",record[0][i])


def retinfogui(record,tablename):

    conn = sqlite3.connect('Apollo_Systems.db')
    cursor = conn.execute('select * from ' + tablename)
    colnames = cursor.description
    l=[]
    for i in range(1, len(colnames)):
        l.append(str(colnames[i][0])+ " : "+ str(record[0][i]))
    return l


#General Medical Information

def general_medical_information(conn, info):

    sql = """INSERT INTO General_Medical_Information(PID,Height,Weight,BP,HeartRate,Hemoglobin,
                                                    RespirationRate)
                  VALUES(?,?,?,?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, info)
    conn.commit()
    return cur.lastrowid


def insert_general_medical_information(aadharnum):
    database = r"Apollo_Systems.db"
    hkey = hashfun.hashalgorithm(aadharnum)
    HeightIP = input("Enter height of patient in cm: ")
    WeightIP = input("Enter weight of patient in kg: ")
    BPIP = input("Enter BP of patient last measured: ")
    HeartRateIP = input("Enter heart rate of patient last measured: ")
    HemoglobinIP = input("Enter hemoglobin count of patient: ")
    RespirationRateIP = input("Enter rate of respiration of patient: ")

    conn = create_connection(database)
    with conn:
        info = (hkey,HeightIP, WeightIP, BPIP, HeartRateIP, HemoglobinIP, RespirationRateIP)
        general_medical_information(conn, info)


#Medical Conditions
def medical_conditions(conn,med_con):
    sql = """INSERT INTO Medical_Conditions(PID,Name,Intensity,ConsultationDate,VascularSystemEffected)
                  VALUES(?,?,?,?,?) """

    cur = conn.cursor()
    cur.execute(sql, med_con)
    conn.commit()
    return cur.lastrowid

def insert_medical_conditions(aadharnum):
    database = r"Apollo_Systems.db"

    hkey = hashfun.hashalgorithm(aadharnum)
    NAMEIP = input("ENTER THE NAME OF MEDICAL CONDITION: ")
    IntensityIP = input("Enter intensity scale of your medical condition on scale of 4(0:no life threating and 4:extreme life threatning): ")
    LastConsultationIP = input("Enter DATE of last consultation (YYYY-MM-DD):")
    VacularSystemEffectedIP = input("Enter vascular system effected:")

    conn = create_connection(database)
    with conn:
        med_con= (hkey,NAMEIP, IntensityIP, LastConsultationIP, VacularSystemEffectedIP)
        medical_conditions(conn, med_con)

#Known Allergies
def known_allergies(conn, allen):

    sql = """INSERT INTO Known_Allergies(PID,Allergen,Effect,Fatal)
              VALUES(?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, allen)
    conn.commit()
    return cur.lastrowid

def insert_known_allergies(aadharnum):
    database = r"Apollo_Systems.db"
    hkey = hashfun.hashalgorithm(aadharnum)
    AllergenIP = input("Enter known allergies: ")
    EffectIP = input("Enter effects of those allergies: ")
    FatalIP = input("Is/Are those allergies Fatal(0,1): ")

    conn = create_connection(database)
    with conn:
        allen = (hkey, AllergenIP, EffectIP, FatalIP)
        known_allergies(conn, allen)


#PREVIOUS SURGERIES
def previous_surgeries(conn, surgeries):
    sql = """INSERT INTO Previous_Surgeries(PID,Speciality,ProcedureName,DateTime,
                                            HospitalPerformedAt,Surgeon)
                      VALUES(?,?,?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, surgeries)
    conn.commit()
    return cur.lastrowid

def insert_previous_surgeries(aadharnum):
    database = r"Apollo_Systems.db"
    hkey = hashfun.hashalgorithm(aadharnum)
    SpecialityIP = input("Enter speciality of surgery: ")
    ProcedureNameIP = input("Enter Name of Procedure performed on the patient: ")
    DateTimeIP = input("Enter date and time details: ")
    HospitalPerformedAtIP = input("Enter Name of Hospital where surgery was performed: ")
    SurgeonIP = input("Enter name of surgeon: ")

    conn = create_connection(database)
    with conn:
        # create a new project
        surgeries = (hkey, SpecialityIP, ProcedureNameIP, DateTimeIP, HospitalPerformedAtIP, SurgeonIP)
        previous_surgeries(conn, surgeries)

#TREATMENTS
def treatments(conn, treatment):
    sql = """INSERT INTO Treatments(PID,Name,UndergoingTreatmentFor,MedicationAdministered,
                                            PrescribedOn,Duration,PrescribedBy,Status)
                          VALUES(?,?,?,?,?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, treatment)
    conn.commit()
    return cur.lastrowid

def insert_treatments(aadharnum):
    database = r"Apollo_Systems.db"
    hkey = hashfun.hashalgorithm(aadharnum)
    NameIP = input("Enter name of treatment: ")
    UndergoingTreatmentForIP = input("Enter Treatment reason: ")
    MedicationAdministeredIP = input("Enter the details of medication administered to the patient: ")
    PrescribedOnIP = input("Enter the Date of medication prescription(YYYY-MM-DD): ")
    DurationIP = input("Enter the duration of medication prescribed: ")
    PrescribedByStatusIP = input("Enter name of medical professional who prescribed medication: ")
    StatusIP = input("Enter status of mentioned medication: ")

    conn = create_connection(database)
    with conn:
        treatment = (hkey, NameIP,  UndergoingTreatmentForIP, MedicationAdministeredIP, PrescribedOnIP, DurationIP,
                     PrescribedByStatusIP, StatusIP)
        treatments(conn, treatment)

#VACCINATION


def vaccin(conn, vaccination):
    sql = """INSERT INTO Vaccinations(PID,TechnicalName,DOI,Doses,State,City,Status,SideEffect)
                  VALUES(?,?,?,?,?,?,?,?) """

    cur = conn.cursor()
    cur.execute(sql, vaccination)
    conn.commit()
    return cur.lastrowid


def insert_vaccination(aadharnum):
    database = r"Apollo_Systems.db"
    hkey = hashfun.hashalgorithm(aadharnum)

    TechnicalIP = input("Enter technical name of the vaccine: ")
    DateofInno = input("Enter date of innoculation: ")
    DosesIP = input("Enter doses taken: ")
    StateIP = input("From which state did you take the vaccine: ")
    CityIP = input("Enter from city did you take the vaccine: ")
    StatusIP = input("Enter status of the vaccine(Ongoing/Completed): ")
    SideEffectsIP = input("Enter any side-effects of vaccines: ")

    conn = create_connection(database)
    with conn:
        vaccination = (hkey, TechnicalIP, DateofInno, DosesIP, StateIP, CityIP, StatusIP, SideEffectsIP)
        vaccin(conn, vaccination)


def remarks(conn, remark):
    sql = """INSERT INTO Remarks(PID,Remark,Author,AuthorDesignation,Pertaining)
                  VALUES(?,?,?,?,?) """

    cur = conn.cursor()
    cur.execute(sql, remark)
    conn.commit()
    return cur.lastrowid


def insert_remarks(aadharnum):
    database = r"Apollo_Systems.db"
    hkey = hashfun.hashalgorithm(aadharnum)
    RemarkIP = input("Enter remarks: ")
    AuthorIP = input("Enter author name: ")
    AuthorDesignationIP = input("Enter Author designation: ")
    PertainingIP = input("Pertaining Condition/Treatment/Surgery: ")

    conn = create_connection(database)
    with conn:
        remark = (hkey, RemarkIP, AuthorIP, AuthorDesignationIP, PertainingIP)
        remarks(conn, remark)

#DEFICIENCIES
def deficiencies(conn , deficiency):
    sql = """INSERT INTO Deficiencies(PID,Deficiency)
                      VALUES(?,?) """

    cur = conn.cursor()
    cur.execute(sql, deficiency)
    conn.commit()
    return cur.lastrowid


def insert_deficiency(aadharnum):
    database = r"Apollo_Systems.db"
    hkey = hashfun.hashalgorithm(aadharnum)
    DeficiencyIP = input("Enter name of deficiency: ")

    conn = create_connection(database)
    with conn:
        deficiency = (hkey, DeficiencyIP)
        deficiencies(conn, deficiency)

def insertoneinstance(aadharnum):


    # if x == '1234':
    loffunc = [insert_known_allergies,insert_deficiency,insert_vaccination,insert_previous_surgeries,
             insert_medical_conditions, insert_treatments,insert_remarks]

    whatWant = int(input(
        "What data is to be inserted? \n 1]Known Allergies \n 2]Deficiencies \n 3]Vaccinations \n 4]Previous Surgeries \n 5]Medical Conditions \n 6]Treatments \n 7]Remarks\n"))
    loffunc[whatWant-1](aadharnum)

#################################################################################################################################################

def newMOrganisation(conn, org):
    sql = """INSERT INTO MOrganisations(Name,AccessCode,RPassword,IPassword,UPassword)
                  VALUES(?,?,?,?,?) """

    cur = conn.cursor()
    cur.execute(sql, org)
    conn.commit()
    return cur.lastrowid

def insert_newMOrganisation():
    database = r"C:\Users\Aryan-PC\PycharmProjects\testproject\Apollo_Systems_User.db"
    NameIP = input("Enter name of Organisation: ")

    AccessCodeIP = input("Enter Access Code for your organization: ")
    RPasswordIP = input("Enter a retrieval password for your organization: ")
    IPasswordIP = input("Enter an insertion password for your organization: ")
    UPasswordIP = input("Enter an updation password for your organization: ")


    conn = create_connection(database)
    with conn:
        org = (NameIP, AccessCodeIP, RPasswordIP, IPasswordIP, UPasswordIP)
        newMOrganisation(conn, org)


#NEW INSURANCE ORGANISATION
def newIOrganisation(conn, orgI):
    sql = """INSERT INTO IOrganisation(Name,AccessCode,RPassword,UPassword)
                  VALUES(?,?,?,?) """

    cur = conn.cursor()
    cur.execute(sql, orgI)
    conn.commit()
    return cur.lastrowid

def insert_newIOrganisation():
    database = r"C:\Users\Aryan-PC\PycharmProjects\testproject\Apollo_Systems_User.db"
    NameIP = input("Enter name of Organisation: ")
    RPasswordIP = input("Enter a retrieval password for your organization: ")

    UPasswordIP = input("Enter an updation password for your organization: ")
    AccessCodeIP = input("Enter Access Code for your organization: ")


    conn = create_connection(database)
    with conn:
        orgI = (NameIP,AccessCodeIP,RPasswordIP,UPasswordIP)
        newIOrganisation(conn, orgI)



def Mcheck_value(hasvalue):
    database = r"C:\Users\Aryan-PC\PycharmProjects\testproject\Apollo_Systems_User.db"
    con = create_connection(database)
    cur = con.cursor()
    cur.execute("SELECT * from MOrganisations where AccessCode = \'"+hasvalue+"\'")
    returner = False
    if cur.fetchone():
        returner = True
    else:
        pass
    guifunc.accesscode = hasvalue
    return returner

def Icheck_value(hasvalue):
    database = r"C:\Users\Aryan-PC\PycharmProjects\testproject\Apollo_Systems_User.db"
    con = create_connection(database)
    cur = con.cursor()
    cur.execute("SELECT * from IOrganisations where AccessCode = \'"+hasvalue+"\'")
    returner = False
    if cur.fetchone():
        returner = True
    else:
        pass
    return returner

def check_valueID(hasvalue):
    database = r"C:\Users\Aryan-PC\PycharmProjects\testproject\Apollo_Systems.db"
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT * from Patient where ID = \'" + hasvalue + "\'")
    returner = False
    if cur.fetchone():
        returner = True

    else:
        pass
    return returner



def check_mrpass(hasvalue,accesscode):
    database = r"C:\Users\Aryan-PC\PycharmProjects\testproject\Apollo_Systems_User.db"
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT * from MOrganisations where RPassword = \'" + hasvalue + "\' AND AccessCode = \'"+accesscode+"\'")
    returner = False
    if cur.fetchone():
        returner = True

    else:
        pass
    return returner

