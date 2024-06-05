from tkinter import *
from tkinter import ttk 
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        self.NameofMedicines=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.IssueDate=StringVar()
        self.ExpiryDate=StringVar()
        self.DailyDose=StringVar()
        self.SideEffect=StringVar()
        self.FurtherInFormation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsnumber=StringVar()
        self.Patientname=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()

        lbltitle=Label(self.root,bd=25,relief=RAISED,text="+ HOSPITAL MANAGEMENT SYSTEM +",fg="white",bg="light blue",font=("Helvetica",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        #     DATAFRAME
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)

        DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RAISED,padx=20,font=("times new roman",12,"bold"),text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=980,height=350)

        DataframeRight=LabelFrame(Dataframe,bd=10,relief=RAISED,padx=20,font=("times new roman",12,"bold"),text="Prescription")
        DataframeRight.place(x=990,y=5,width=480,height=350)

        #    BUTTONS FRAME
        Buttonframe=Frame(self.root,bd=10,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)

        #     DETAILS FRAME
        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)

        #     DATA_FRAME_LEFT
        lbl_name_med=Label(DataframeLeft,text="Name of Medicine",font=("Helvetica",12,"bold"),padx=2,pady=6)
        lbl_name_med.grid(row=0,column=0,sticky=W)

        com_med_name=ttk.Combobox(DataframeLeft,font=("Helvetica",12,"bold"),state="readonly",textvariable=self.NameofMedicines,width=33)
        com_med_name["values"]=("Paracetamol","Rosuvasstatin","Acetaminophen","Aspirin","Atvin")
        com_med_name.current(0)
        com_med_name.grid(row=0,column=1)

        lbl_ref=Label(DataframeLeft,font=("Helvetica",12,"bold"),text="Refrence No:",padx=2)
        lbl_ref.grid(row=1,column=0,sticky=W)
        txt_ref=Entry(DataframeLeft,font=("Helvetica",13,"bold"),textvariable=self.ref,width=35)
        txt_ref.grid(row=1,column=1)

        lbl_dose=Label(DataframeLeft,font=("Helvetica",12,"bold"),text="Dose:",padx=2,pady=4)
        lbl_dose.grid(row=2,column=0,sticky=W)
        txt_dose=Entry(DataframeLeft,font=("Helvetica",13,"bold"),textvariable=self.Dose,width=35)
        txt_dose.grid(row=2,column=1)

        lbl_noOf_Tablets=Label(DataframeLeft,font=("Helvetica",12,"bold"),text="No. of tablets:",padx=2,pady=6)
        lbl_noOf_Tablets.grid(row=3,column=0,sticky=W)
        txt_noOf_Tablets=Entry(DataframeLeft,font=("Helvetica",13,"bold"),textvariable=self.NumberofTablets,width=35)
        txt_noOf_Tablets.grid(row=3,column=1)

        lbl_Lot=Label(DataframeLeft,font=("Helvetica",12,"bold"),text="Lot:",padx=2,pady=6)
        lbl_Lot.grid(row=4,column=0,sticky=W)
        txt_Lot=Entry(DataframeLeft,font=("Helvetica",13,"bold"),textvariable=self.Lot,width=35)
        txt_Lot.grid(row=4,column=1)

        lbl_issue_date=Label(DataframeLeft,font=("Helvetica",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lbl_issue_date.grid(row=5,column=0,sticky=W)
        txt_issue_date=Entry(DataframeLeft,font=("Helvetica",13,"bold"),textvariable=self.IssueDate,width=35)
        txt_issue_date.grid(row=5,column=1)

        lbl_expiry_date=Label(DataframeLeft,font=("Helvetica",12,"bold"),text="Expiry Date:",padx=2,pady=6)
        lbl_expiry_date.grid(row=6,column=0,sticky=W)
        txt_expiry_date=Entry(DataframeLeft,font=("Helvetica",13,"bold"),textvariable=self.ExpiryDate,width=35)
        txt_expiry_date.grid(row=6,column=1)

        lbl_daily_dose=Label(DataframeLeft,font=("Helvetica",12,"bold"),text="Daily Dose:",padx=2,pady=4)
        lbl_daily_dose.grid(row=7,column=0,sticky=W)
        txt_daily_dose=Entry(DataframeLeft,font=("Helvetica",13,"bold"),textvariable=self.DailyDose,width=35)
        txt_daily_dose.grid(row=7,column=1)

        lbl_side_effect=Label(DataframeLeft,font=("Helvetica",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lbl_side_effect.grid(row=8,column=0,sticky=W)
        txt_side_effect=Entry(DataframeLeft,font=("Helvetica",13,"bold"),textvariable=self.SideEffect,width=35)
        txt_side_effect.grid(row=8,column=1)

        lbl_further_info=Label(DataframeLeft,font=("Helvetica",12,"bold"),text="Further Information:",padx=2)
        lbl_further_info.grid(row=0,column=2,sticky=W)
        txt_further_info=Entry(DataframeLeft,font=("Helvetica",13,"bold"),textvariable=self.FurtherInFormation,width=35)
        txt_further_info.grid(row=0,column=3)

        lbl_driving_machine=Label(DataframeLeft,font=("Helvetica",12,"bold"),text="Blood Pressure:",padx=2,pady=6)
        lbl_driving_machine.grid(row=1,column=2,sticky=W)
        txt_driving_machine=Entry(DataframeLeft,font=("Helvetica",13,"bold"),textvariable=self.DrivingUsingMachine,width=35)
        txt_driving_machine.grid(row=1,column=3)

        lbl_storage=Label(DataframeLeft,font=("Helvetica",12,"bold"),text="Storage Advice:",padx=2,pady=6)
        lbl_storage.grid(row=2,column=2,sticky=W)
        txt_storage=Entry(DataframeLeft,font=("Helvetica",13,"bold"),textvariable=self.StorageAdvice,width=35)
        txt_storage.grid(row=2,column=3)

        lbl_medicine=Label(DataframeLeft,font=("Helvetica",12,"bold"),text="Medication:",padx=2,pady=6)
        lbl_medicine.grid(row=3,column=2,sticky=W)
        txt_medicine=Entry(DataframeLeft,font=("Helvetica",13,"bold"),textvariable=self.HowToUseMedication,width=35)
        txt_medicine.grid(row=3,column=3)

        lbl_patient_id=Label(DataframeLeft,font=("Helvetica",12,"bold"),text="Patient ID:",padx=2,pady=6)
        lbl_patient_id.grid(row=4,column=2,sticky=W)
        txt_patient_id=Entry(DataframeLeft,font=("Helvetica",13,"bold"),textvariable=self.PatientId,width=35)
        txt_patient_id.grid(row=4,column=3)

        lbl_nhs_no=Label(DataframeLeft,font=("Helvetica",12,"bold"),text="NHS No.:",padx=2,pady=6)
        lbl_nhs_no.grid(row=5,column=2,sticky=W)
        txt_nhs_no=Entry(DataframeLeft,font=("Helvetica",13,"bold"),textvariable=self.nhsnumber,width=35)
        txt_nhs_no.grid(row=5,column=3)

        lbl_patient_name=Label(DataframeLeft,font=("Helvetica",12,"bold"),text="Patient Name:",padx=2,pady=6)
        lbl_patient_name.grid(row=6,column=2,sticky=W)
        txt_patient_name=Entry(DataframeLeft,font=("Helvetica",13,"bold"),textvariable=self.Patientname,width=35)
        txt_patient_name.grid(row=6,column=3)

        lbl_dob=Label(DataframeLeft,font=("Helvetica",12,"bold"),text="Date Of Birth:",padx=2,pady=6)
        lbl_dob.grid(row=7,column=2,sticky=W)
        txt_dob=Entry(DataframeLeft,font=("Helvetica",13,"bold"),textvariable=self.DateOfBirth,width=35)
        txt_dob.grid(row=7,column=3)

        lbl_patient_add=Label(DataframeLeft,font=("Helvetica",12,"bold"),text="Patient Address:",padx=2,pady=6)
        lbl_patient_add.grid(row=8,column=2,sticky=W)
        txt_patient_add=Entry(DataframeLeft,font=("Helvetica",13,"bold"),textvariable=self.PatientAddress,width=35)
        txt_patient_add.grid(row=8,column=3)

       #         DATA_FRAME_RIGHT
        self.txt_prescription=Text(DataframeRight,font=("Helvetica",12,"bold"),width=46,height=16,padx=2,pady=6)
        self.txt_prescription.grid(row=0,column=0)

        #          BUTTONS
        
        button_prescription=Button(Buttonframe,command=self.iprescription,text="Prescription",fg="black",bg="light blue",font=("Helvetica",12,"bold"),width=23,height=16,padx=2,pady=6)
        button_prescription.grid(row=0,column=0)
        
        button_prescriptionData=Button(Buttonframe,text="Prescription Data",fg="black",bg="light blue",font=("Helvetica",12,"bold"),width=23,height=16,padx=2,pady=6,command=self.iPrescriptionData)
        button_prescriptionData.grid(row=0,column=1)

        button_update=Button(Buttonframe,text="Update",command=self.Update,fg="black",bg="light blue",font=("Helvetica",12,"bold"),width=23,height=16,padx=2,pady=6)
        button_update.grid(row=0,column=2)

        button_delete=Button(Buttonframe,command=self.idelete,text="Delete",fg="black",bg="light blue",font=("Helvetica",12,"bold"),width=23,height=16,padx=2,pady=6)
        button_delete.grid(row=0,column=3)

        button_clear=Button(Buttonframe,text="Clear",command=self.iclear,fg="black",bg="light blue",font=("Helvetica",12,"bold"),width=23,height=16,padx=2,pady=6)
        button_clear.grid(row=0,column=4)

        button_exit=Button(Buttonframe,command=self.iexit,text="Exit",fg="black",bg="light blue",font=("Helvetica",12,"bold"),width=23,height=16,padx=2,pady=6)
        button_exit.grid(row=0,column=5)
        
        #            TABLE
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL) # scroll
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,column=("nameOfMed","refNo.","dose","NO.ofTablets",
                                                               "Lot","IssueDate","ExpiryDate","DailyDose","SideEffect",
                                                               "FurtherInfo","BP","Storage","Medicine","PatientID","NHSno.","PatientName","DOB","PatientADD")
                                                               ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameOfMed",text="Name of Medicine")
        self.hospital_table.heading("refNo.",text="Reference No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("NO.ofTablets",text="No. of Tablets")
        self.hospital_table.heading("Lot",text="Lot")
        self.hospital_table.heading("IssueDate",text="Issue Date")
        self.hospital_table.heading("ExpiryDate",text="Expiry Date")
        self.hospital_table.heading("DailyDose",text="Daily Dose")
        self.hospital_table.heading("SideEffect",text="Side Effect")
        self.hospital_table.heading("FurtherInfo",text="Further Information")
        self.hospital_table.heading("BP",text="Blood Pressure")
        self.hospital_table.heading("Storage",text="Storage")
        self.hospital_table.heading("Medicine",text="Medicine")
        self.hospital_table.heading("PatientID",text="Patient ID")
        self.hospital_table.heading("NHSno.",text="NHS No.")
        self.hospital_table.heading("PatientName",text="Patient Name")
        self.hospital_table.heading("DOB",text="Date of Birth")
        self.hospital_table.heading("PatientADD",text="Patient Address")

        self.hospital_table["show"]="headings"


        self.hospital_table.column("nameOfMed",width=100)
        self.hospital_table.column("refNo.",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("NO.ofTablets",width=100)
        self.hospital_table.column("Lot",width=100)
        self.hospital_table.column("IssueDate",width=100)
        self.hospital_table.column("ExpiryDate",width=100)
        self.hospital_table.column("DailyDose",width=100)
        self.hospital_table.column("Storage",width=100)
        self.hospital_table.column("NHSno.",width=100)
        self.hospital_table.column("PatientName",width=100)
        self.hospital_table.column("DOB",width=100)
        self.hospital_table.column("PatientADD",width=100)
   
        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.cursor_get)
        self.fetch_data()


        #       FUNCTIONALITY DECLARATION
    def iPrescriptionData(self):
        if self.NameofMedicines.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error","ALL FIELDS MUST BE FILLED")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="keerat123",database="managementsys")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.NameofMedicines.get(),
                                                                                                       self.ref.get(),
                                                                                                       self.Dose.get(),
                                                                                                       self.NumberofTablets.get(),
                                                                                                       self.Lot.get(),
                                                                                                       self.IssueDate.get(),
                                                                                                       self.ExpiryDate.get(),
                                                                                                       self.DailyDose.get(),
                                                                                                       self.StorageAdvice.get(),
                                                                                                       self.nhsnumber.get(),
                                                                                                       self.Patientname.get(),
                                                                                                       self.DateOfBirth.get(),
                                                                                                       self.PatientAddress.get()
                                                                                                       ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","information successfull inserted")
    def Update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="keerat123",database="managementsys")
        my_cursor=conn.cursor()
        sql="update hospital set Name_of_med = %s,Dose = %s,Numberoftabs = %s,Lot= %s,Issuedate = %s,Expdate = %s,Dailydose = %s,Storage = %s,nhsnumber = %s,pname = %s,dob = %s,paddress = %s where Reference_no. = %s"
        val=(self.NameofMedicines.get(),
            self.Dose.get(),
            self.NumberofTablets.get(),
            self.Lot.get(),
            self.IssueDate.get(),
            self.ExpiryDate.get(),
            self.DailyDose.get(),
            self.StorageAdvice.get(),
            self.nhsnumber.get(),
            self.Patientname.get(),
            self.DateOfBirth.get(),
            self.PatientAddress.get(),
            self.ref.get()
            )
                            
        my_cursor.execute(sql,val)
        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Update","Information has been updated successfully!")
    
    
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="keerat123",database="managementsys")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital ")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    def cursor_get(self,event=""):
        cursorRow=self.hospital_table.focus()
        content=self.hospital_table.item(cursorRow)
        row=content["values"]
        self.NameofMedicines.set(row[0])
        self.ref.set(row[1]),
        self.Dose.set(row[2]),
        self.NumberofTablets.set(row[3]),
        self.Lot.set(row[4]),
        self.IssueDate.set(row[5]),
        self.ExpiryDate.set(row[6]),
        self.DailyDose.set(row[7]),
        self.StorageAdvice.set(row[8]),
        self.nhsnumber.set(row[9]),
        self.Patientname.set(row[10]),
        self.DateOfBirth.set(row[11]),
        self.PatientAddress.set(row[12])
    

    def iprescription(self):
        self.txt_prescription.insert(END,"Name of Medicine:\t\t\t"+self.NameofMedicines.get()+"\n")
        self.txt_prescription.insert(END,"Reference no.:\t\t\t"+self.ref.get()+"\n")
        self.txt_prescription.insert(END,"Dose:\t\t\t"+self.Dose.get()+"\n")
        self.txt_prescription.insert(END,"Number of Tablets:\t\t\t"+self.NumberofTablets.get()+"\n")
        self.txt_prescription.insert(END,"Lot:\t\t\t"+self.Lot.get()+"\n")
        self.txt_prescription.insert(END,"Issue Date:\t\t\t"+self.IssueDate.get()+"\n")
        self.txt_prescription.insert(END,"Exp Date:\t\t\t"+self.ExpiryDate.get()+"\n")
        self.txt_prescription.insert(END,"Daily Dose:\t\t\t"+self.DailyDose.get()+"\n")
        self.txt_prescription.insert(END,"Side Effect:\t\t\t"+self.SideEffect.get()+"\n")
        self.txt_prescription.insert(END,"Further Information:\t\t\t"+self.FurtherInFormation.get()+"\n")
        self.txt_prescription.insert(END,"storage advice:\t\t\t"+self.StorageAdvice.get()+"\n")
        self.txt_prescription.insert(END,"Drivin using machine:\t\t\t"+self.DrivingUsingMachine.get()+"\n")
        self.txt_prescription.insert(END,"PatientID:\t\t\t"+self.PatientID.get()+"\n")
        self.txt_prescription.insert(END,"NHS Number:\t\t\t"+self.nhsnumber.get()+"\n")
        self.txt_prescription.insert(END,"Patient Name:\t\t\t"+self.Patientname.get()+"\n")
        self.txt_prescription.insert(END,"Date of Birth:\t\t\t"+self.dob.get()+"\n")
        self.txt_prescription.insert(END,"Patient Address:\t\t\t"+self.PatientAddress.get()+"\n")
    

    def idelete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="keerat123",database="managementsys")
        my_cursor=conn.cursor()
        query="delete from hospital where Reference_no. = %s"
        values=(self.ref.get(),)
        my_cursor.execute(query,values)

        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete","info has been deleted successfully")
    
    def iclear(self):
        self.NameofMedicines.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.IssueDate.set("")
        self.ExpiryDate.set("")
        self.DailyDose.set("")
        self.SideEffect.set("")
        self.FurtherInFormation.set("")
        self.StorageAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.HowToUseMedication.set("")
        self.PatientId.set("")
        self.nhsnumber.set("")
        self.Patientname.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txt_prescription.delete("1.0",END)
    
    def iexit(self):
        iexit=messagebox.askyesno("HOSPITAL MANAGEMENT SYSTEM","Are you sure you want to exit?")
        if iexit>0:
            root.destroy()
            return




root=Tk()
ob=Hospital(root)
root.mainloop()