
import re
# first step it to open file 

with open("contact_data_sample.txt",'r') as main_file:
    # let make list and keep all the contacts in ti 
    lines=main_file.readlines()
    
    regex_email=r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    regex_contact=r'\+91-\d{10}'
    regex_website=r'www\.[a-zA-Z0-9]+\.[a-zA-Z]+'

    # improvement
    """ 
        first collecting all the data a storing it in some for of list 


    """

    contact_list=[]
    website_list=[]
    Email_list=[]


    # now open a file write mode will make it in python it self 
    for text in lines:
        contact_list.extend(re.findall(regex_contact,text))
        website_list.extend(re.findall(regex_website,text))
        Email_list.extend(re.findall(regex_email,text))


# print(len(contact_list),"\t",len(Email_list),"\t",len(website_list))
   

with open("contact.txt",'w') as contact_file:
    for numbers in contact_list:
        contact_file.write(numbers + "\n")

with open("email.txt",'w') as email_file:
    for emails in Email_list:
        email_file.write(emails + "\n")

with open("website.txt",'w') as website_file:
    for websites in website_list:
        website_file.write(websites + "\n")

    
   

    
    

