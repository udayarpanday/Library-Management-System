import datetime
import random
from datetime import timedelta
import read
import display
import write
menu="LibraryMenu.txt"
display.display_essentials()
menu_dis=read.Lab_Menu(menu)
main_dis=read.list_conversion()
def display_option():
    option=int(input("\nChoose An Above Option:")) #Taking Input from User
    try:
        #Checking using options
        if option==1:#This option will print the books in the library
            display.display_items(main_dis)#Displays the main file of books
            read.Lab_Menu(menu)#Displays the library menu
            display_option()
        elif option==2:#This option will enable a user to borrow books from the list
            success="false"
            while success=="false":
                name=input("\nEnter your full name:")#Taking Input from User
                if name.replace(" ","").isalpha()==True:
                    success="true"
                else:
                    print("\nInvalid input\nPlease enter your name properly")
            display.display_items(main_dis)
            borrow_dt=datetime.datetime.now()#To set the book borrow date 
            return_dt=borrow_dt+timedelta(days=10)#To set the return date of the borrowed book of duration 10 days
            ref_no=random.randint(1,10) #Random number for Reference
            book1=int(input("\nEnter the Book Code NO. of the book you want to borrow."))#Taking Input from User
            if book1>5:
                print("Please select a appropriate Code No.")
                read.Lab_Menu(menu)
                display_option()
            else:
                extra_book=input("\nDo you want to borrow two books?(y/n)")#Asking the user for an extra book
                if extra_book=="y":
                    book2=int(input("\nEnter another Book Code NO. of the book you want to borrow."))#Taking Input from User
                    if book2==book1:
                        print("\nYou have entered the same Code NO.\nPlease try a different Code NO.")#Since the input is same as the previous input,asking for a different input 
                        book2=int(input("\nEnter the Book Code NO. of the book you want to borrow:"))
                    if book2>5:
                        print("Please select a appropriate Code No.")
                        book2=int(input("\nEnter the Book Code NO. of the book you want to borrow:"))
                    else:
                        display.borrow_book2(name,book1,book2,ref_no,borrow_dt,return_dt)#Printing the receipt for the user for two books
                        print("\n\t\t---------NOTE---------\n\nPlease return the books before ",return_dt," to avoid fine.")
                        list_book2=write.overwrite_book2(main_dis,(book1-1),(book2-1))#Passing the values to the parameter
                        write.overwrite_quantity(list_book2)#Overwriting the main file
                        write.overwrite_borrow2(name,(book1-1),(book2-1),main_dis[book1-1][0],main_dis[book2-1][0],borrow_dt,return_dt)#Passing values to the parameter and displaying them in a new file
                        read.Lab_Menu(menu)
                        display_option()
                if extra_book=="n" :
                    display.borrow_book1(name,book1,ref_no,borrow_dt,return_dt)#Printing the receipt for the user for a single book
                    print("\n\t\t---------NOTE---------\nPlease return the books before ",return_dt," to avoid fine.")
                    list_book1=write.overwrite_book1(main_dis,(book1-1))#Passing the values to the parameter
                    write.overwrite_quantity(list_book1)#Overwriting main file
                    write.overwrite_borrow1(name,(book1-1),main_dis[book1-1][0],borrow_dt,return_dt)#Passing values to the parameter and displaying them in a new file
                    read.Lab_Menu(menu)
                    display_option()
        elif option==3:
            success="false"
            while success=="false":
                name=input("\nEnter your full name:")#Taking user input
                if name.replace(" ","").isalpha()==True:
                    success="true"
                else:
                    print("\nInvalid input\nPlease input your name properly")
            return_list=read.Return_Books(name)#Reading borrow note file    
            ref_number=int(return_list[1])#Book quantity
            book_list1=int(return_list[2])#Book Code No.
            bookno1=return_list[3]
            bookno2=return_list[5]
            
            if ref_number==1:
                display.return1(return_list)
                file=open(str(name)+".txt","w")
                returnbook1=write.return_book1(main_dis,book_list1)#Passing the values to the parameter
                write.overwrite_quantity(returnbook1)#Overwriting main file
                write.overwrite_return1(name,bookno1,datetime.datetime.now())
                file.close()
                read.Lab_Menu(menu)
                display_option()
            elif ref_number==2:
                book_list2=int(return_list[3])#Book Code No.
                display.return2(return_list)
                file=open(str(name)+".txt","w")
                returnbook1=write.return_book2(main_dis,book_list1,book_list2)#Passing the values to the parameter
                write.overwrite_quantity(returnbook1)#Overwriting main file
                write.overwrite_return2(name,bookno1,bookno2,datetime.datetime.now())
                file.close()
                read.Lab_Menu(menu)
                display_option()
        elif option==4:
            print("\t\t\tThank you!")
            
        else:
            print("Please choose an above option")
            read.Lab_Menu(menu)
            display_option()
    except ValueError:
        print("Please choose an above option")
display_option()

