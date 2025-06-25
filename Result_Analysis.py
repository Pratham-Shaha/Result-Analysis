#Step 1


import pdfplumber
import re

# Open the PDF file
with pdfplumber.open("Final_result.pdf") as pdf:
    with open("temp.txt", "w") as file1:  # Create temp.txt to store extracted text
        for page in pdf.pages:  # Loop through each page
            text = page.extract_text()  # Extract text from the page
            if text:  # Check if text is not None
                for line in text.split('\n'):  # Split the text into lines
                    file1.write(line + "\n")  # Write each line with a newline
                    
                    
#Step 2
import re
import csv
row=[]
count=0
with open("temp.txt","r") as file1:
    with open("AI_miniproject.csv","a",newline="") as file2:
        writer=csv.writer(file2)
        line=file1.readline()
        while line:  
            match1=re.findall(r'T\d{10}',line)
            row.extend(match1)
            match2=re.findall(r'NAME : (\D+) MOTHER',line)
            row.extend(match2)
            match31=re.findall(r'310241\D+\* (?:\d{3}|AB)/030 (?:\d{3}|AB|\d{2}\W)/070 (\d{2,3}|AB)\W?/100',line)    #Oring condition should be in bracket and ?: specifies group which shouldnt be captured
            if match31:
                match32=re.findall(r'310241\D+\* (?:\d{3}|AB)/030 (?:\d{3}|AB|\d{2}\W)/070 (?:\d{2,3}|AB)\W?/100(?:\s+---){4} (\d{2}|FF)',line)
                count+=1
                row.extend(match31)
                row.extend(match32)
            match41=re.findall(r'310242\D+\* (?:\d{3}|AB)/030 (?:\d{3}|AB|\d{2}\W)/070 (\d{2,3}|AB)\W?/100',line)
            if match41:
                match42=re.findall(r'310242\D+\* (?:\d{3}|AB)/030 (?:\d{3}|AB|\d{2}\W)/070 (?:\d{2,3}|AB)\W?/100(?:\s+---){4} (\d{2}|FF)',line)
                count+=1
                row.extend(match41)
                row.extend(match42)
            match51=re.findall(r'310243\D+\* (?:\d{3}|AB)/030 (?:\d{3}|AB|\d{2}\W)/070 (\d{2,3}|AB)\W?/100',line)
            if match51:
                match52=re.findall(r'310243\D+\* (?:\d{3}|AB)/030 (?:\d{3}|AB|\d{2}\W)/070 (?:\d{2,3}|AB)\W?/100(?:\s+---){4} (\d{2}|FF)',line)
                count+=1
                row.extend(match51)
                row.extend(match52)
            match61=re.findall(r'310244\D+\* (?:\d{3}|AB)/030 (?:\d{3}|AB|\d{2}\W)/070 (\d{2,3}|AB)\W?/100',line)
            if match61:
                match62=re.findall(r'310244\D+\* (?:\d{3}|AB)/030 (?:\d{3}|AB|\d{2}\W)/070 (?:\d{2,3}|AB)\W?/100(?:\s+---){4} (\d{2}|FF)',line)
                count+=1
                row.extend(match61)
                row.extend(match62)
            match71=re.findall(r'310245\D+\* (?:\d{3}|AB)/030 (?:\d{3}|AB|\d{2}\W)/070 (\d{2,3}|AB)\W?/100',line) 
            #In case of marks of endsem there can be possibilities like 059/070 or AB/070 or 28$/070 so we had written regex according to it
            if match71:
                match72=re.findall(r'310245\D+\* (?:\d{3}|AB)/030 (?:\d{3}|AB|\d{2}\W)/070 (?:\d{2,3}|AB)\W?/100(?:\s+---){4} (\d{2}|FF)',line)
                count+=1
                row.extend(match71)
                row.extend(match72)
            match8=re.findall(r'310246\D+\*',line)
            if match8:
                count+=1
            match9=re.findall(r'310247\D+\*',line)
            if match9:
                count+=1
            match10=re.findall(r'310248\D+\*',line)
            if match10:
                count+=1
            match11=re.findall(r'310249\D+\*',line)
            if match11:
                count+=1
            match12=re.findall(r'310250\D+\*',line)
            if match12:
                count+=1
            match13=re.findall(r'SGPA1\D+(\d+\.\d+|--)',line)
            if match13:                                               #Ikde yeunch count 0 reset zhala pahije mhanun condn check karaychi
                row.extend(match13)
                if(count==10):
                    writer.writerow(row)
                row.clear()
                count=0
            match14=re.findall(r'THIRD YEAR SGPA : ',line)
            if match14:   #For backlog students , we dont even want to mention their names and seat_nos in .csv file
                row.clear()
                count=0
            line=file1.readline()
       
# Step 3
import pandas as pd
pf=pd.read_csv('AI_miniproject.csv')
print("Select appropriate number to perform task\n1)Get your result\n2)Subject-wise Toppers\n3)Topper in overall SGPA\n4)Top 5 highest SGPA's\n5)List of backlogs in DBMS\n6)List of backlogs in TOC\n7)List of backlogs in SPOS\n8)List of backlogs in CNS\n9)List of backlogs in Elective-I\n10)Chart displaying subject performance in %")
a=int(input("\nEnter your input:- "))
if(a==1):
    b=str(input("Enter your seat number:- "))
    pfa=pf[pf['Seat_number']==b][['Seat_number','Name','DBMS','TOC','SPOS','CNS','Elective-I','SGPA']]
    if(pfa.empty):
        print("Please enter valid seat number")
    else:
        print("\n\n",pfa)
elif(a==2):
    print("\nDBMS Topper:- ","\n",pf[pf['DBMS']==pf['DBMS'].max()][['Name','DBMS']])
    print("\nTOC Topper:- ","\n",pf[pf['TOC']==pf['TOC'].max()][['Name','TOC']])
    print("\nSPOS Topper:- ","\n",pf[pf['SPOS']==pf['SPOS'].max()][['Name','SPOS']])
    print("\nCNS Topper:- ","\n",pf[pf['CNS']==pf['CNS'].max()][['Name','CNS']])
    print("\nElective-I Topper:- ","\n",pf[pf['Elective-I']==pf['Elective-I'].max()][['Name','Elective-I']])

elif(a==3):
    pfb=pf
    pfb['SGPA']=pfb['SGPA'].replace('--','0.0')  #Replacing -- with 0
    pfb['SGPA']=pfb['SGPA'].astype(float)        #Converting dtype from object to float
    print("\nTopper in overall SGPA:- ","\n",pfb[pfb['SGPA']==pfb['SGPA'].max()][['Seat_number','Name','DBMS','TOC','SPOS','CNS','Elective-I','SGPA']])
    
elif(a==4):
    pfc=pf
    pfc['SGPA']=pfc['SGPA'].replace('--','0.0')  #Replacing -- with 0
    pfc['SGPA']=pfc['SGPA'].astype(float)        #Converting dtype from object to float
    pfc=pfc.sort_values(by='SGPA',ascending=False)   #We sorted the dataframe as per SGPA in descending order
    print("\nTop 5 highest SGPA scorer:- ","\n",pfc[['Name','SGPA']].head(5))

elif(a==5):
    print("\n","Total backlogs in DBMS are:- ",pf[pf['DBMS_Tot%']=='FF']['DBMS_Tot%'].count(),"\n",pf[pf['DBMS_Tot%']=='FF'][['Seat_number','Name','DBMS']])

elif(a==6):
     print("\n","Total backlogs in TOC are:- ",pf[pf['TOC_Tot%']=='FF']['TOC_Tot%'].count(),"\n",pf[pf['TOC_Tot%']=='FF'][['Seat_number','Name','TOC']])

elif(a==7):
     print("\n","Total backlogs in SPOS are:- ",pf[pf['SPOS_Tot%']=='FF']['SPOS_Tot%'].count(),"\n",pf[pf['SPOS_Tot%']=='FF'][['Seat_number','Name','SPOS']])

elif(a==8):
     print("\n","Total backlogs in CNS are:- ",pf[pf['CNS_Tot%']=='FF']['CNS_Tot%'].count(),"\n",pf[pf['CNS_Tot%']=='FF'][['Seat_number','Name','CNS']])

elif(a==9):
     print("\n","Total backlogs in Elective-I are:- ",pf[pf['Elective_Tot%']=='FF']['Elective_Tot%'].count(),"\n",pf[pf['Elective_Tot%']=='FF'][['Seat_number','Name','Elective-I']])

elif(a==10):
    import matplotlib.pyplot as plt
    DBMS_Pass=pf['Seat_number'].count()-pf[pf['DBMS_Tot%']=='FF']['Seat_number'].count()
    DBMS_score=(DBMS_Pass*100)/pf['Seat_number'].count()
    TOC_Pass=pf['Seat_number'].count()-pf[pf['TOC_Tot%']=='FF']['Seat_number'].count()
    TOC_score=(TOC_Pass*100)/pf['Seat_number'].count()
    SPOS_Pass=pf['Seat_number'].count()-pf[pf['SPOS_Tot%']=='FF']['Seat_number'].count()
    SPOS_score=(SPOS_Pass*100)/pf['Seat_number'].count()
    CNS_Pass=pf['Seat_number'].count()-pf[pf['CNS_Tot%']=='FF']['Seat_number'].count()
    CNS_score=(CNS_Pass*100)/pf['Seat_number'].count()
    Elective_Pass=pf['Seat_number'].count()-pf[pf['Elective_Tot%']=='FF']['Seat_number'].count()
    Elective_score=(Elective_Pass*100)/pf['Seat_number'].count()


    subjects = ['DBMS','TOC','SPOS','CNS','Elective-I']
    results = [DBMS_score,TOC_score,SPOS_score,CNS_score,Elective_score]  

    plt.bar(subjects,results, color='skyblue')
    plt.ylabel('Result %')
    plt.title('Subject-wise Result Percentage')
    plt.show()

else:
    print("Please enter proper value")
