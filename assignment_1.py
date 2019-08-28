#importing libraries
import pandas as pd
import re


#importing data in "dataset" variable
dataset = pd.read_csv("sample_email.csv",encoding="latin1")
dataset_1=dataset.iloc[:,[0,1,10,11,12]]
dataset_1["Name"]=dataset_1["first_name"].str.cat(dataset["last_name"],sep=" ")
dataset_1=dataset_1.drop(["first_name","last_name"],axis=1)
dataset_1.columns=["Email","Subject","Email_body","Name"]

#creating csv file for email address in email body and blank list for email address
email_address=[]
email_add=pd.DataFrame(columns=["Email_Id"])

#creating csv file for phone number in email body and blank list for phone numbers
phone_numbers=[]
phone_nums=pd.DataFrame(columns=["Phone_number"])



#creating A which is going to use file handling and will write text file for every single person
def Email_temp(name,email_id,subject_line,email_body):
    file=open("F:/Python/test/"+name+".txt",'w')
    file.write("Email to : "+email_id+"\n"+"Subject Line:"+subject_line+"\n"+"Hi "+name+","+"\n"+email_body+"\nThanks\n"+"Rose Willison.")
    file.close()
    
    
#looping over the dataset_1 which will write the text file for everyone in the dataset_1    
for index,row in dataset_1.iterrows():
    #using regular expression for finding email from email body
    email=re.findall('\S+@\S+',row['Email_body'])
    email_address.append(email)
    
    #using regular ex[ression for finding phone number in email body
    phone=re.findall("\d\d\d-\d\d\d-\d\d\d\d",row["Email_body"])
    phone_numbers.append(phone)
    
    name=row['Name']
    email_id=row['Email']
    subject_line=row['Subject']
    email_body=row['Email_body']
    Email_temp(name,email_id,subject_line,email_body)


#adding the extracted emails and phone number from email body in two different csv file    
email_add["Email_Id"]=email_address
phone_nums["Phone_number"]=phone_numbers

#writing csv file
dataset_1.to_csv(r'F:/Python/test/csv/data.csv',index=False)
email_add.to_csv(r'F:/Python/test/csv/email.csv',index=False)
phone_nums.to_csv(r'F:/Python/test/csv/phone.csv',index=False)   

