import read
import datetime
def display_essentials():
    print("\t\t-----------------------------------------------")
    print("\t\t\tLIBRARY MANAGEMENT SYSTEM")
    print("\t\t-----------------------------------------------")
    print("\nHello! Welcome to the Library\n")
    
def display_items(prep_list):
    print("--------------------------------------------------------------------------------------------")
    print("CodeNO.\t\tBook Name\t\tAuthor\t\t\tQuantiy\t\tPrice($)")
    print("--------------------------------------------------------------------------------------------")
    for i in range(len(prep_list)):
        print(i+1,end="\t\t")
        for j in range(len(prep_list[i])):
            print(prep_list[i][j],end="\t\t")                                                                                                                                                                                                                          
        print("\n")
                                                               
def borrow_book1(name,book1,ref_no,borrow_dt,return_dt):
    L=read.list_conversion()
    print("\n\t\t--------------------RECEPIET------------------------")
    print("Full Name:",name)
    print("Book Reference NO:",ref_no)
    print("Book Title:",L[book1-1][0])
    print("Author:",L[book1-1][1])
    print("Price:$",L[book1-1][3])
    print("Date Borrowed:",borrow_dt)
    print("Loan Period:",return_dt)

def borrow_book2(name,book1,book2,ref_no,borrow_dt,return_dt):
    L=read.list_conversion()
    print("\t\t--------------------RECEPIET------------------------")
    print("Full Name:",name)
    print("Book Reference NO:",ref_no)
    print("First Book Title:",L[book1-1][0])
    print("Author:",L[book1-1][1])
    print("Price:$",L[book1-1][3])
    print("Second Book Title:",L[book2-1][0])
    print("Author:",L[book2-1][1])
    print("Price:$",L[book2-1][3])
    print("Total Price:$",float(L[book1-1][3])+float(L[book2-1][3]))
    print("Date Borrowed:",borrow_dt)
    print("Loan Period:",return_dt)

def return1(list1):
    print("\n\t\t Thank you for returning the book")
    print("\n\t\t--------------------RECEPIET------------------------")
    print("Full Name",list1[0])
    print("Book Name",list1[3])
    print("Borrowed Date",list1[4])
    print("Return Date",list1[5])
    print("Date Returned",datetime.datetime.now())
    
def return2(list1):
    print("\n\t\t Thank you for returning the book")
    print("\n\t\t--------------------RECEPIET------------------------")
    print("Full Name:",list1[0])
    print("First Book Name:",list1[4])
    print("Second Book Name:",list1[5])
    print("Borrowed Date:",list1[6])
    print("Return Date:",list1[7])
    print("Date Returned:",datetime.datetime.now())
   
    
    

