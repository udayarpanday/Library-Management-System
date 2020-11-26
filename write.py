
def overwrite_borrow1(name,Code_No1,book_name,borrow_dt,return_dt):
    user_data1=open(str(name)+".txt","w")
    user_data1.write(str(name))
    user_data1.write(",")
    user_data1.write("1")
    user_data1.write(",")
    user_data1.write(str(Code_No1))
    user_data1.write(",")
    user_data1.write(str(book_name))
    user_data1.write(",")
    user_data1.write(str(borrow_dt))
    user_data1.write(",")
    user_data1.write(str(return_dt))
    user_data1.write(",")
    user_data1.close()
def overwrite_borrow2(name,Code_No1,Code_No2,book_name1,book_name2,borrow_dt,return_dt):
    user_data2=open(str(name)+".txt","w")
    user_data2.write(str(name))
    user_data2.write(",")
    user_data2.write("2")
    user_data2.write(",")
    user_data2.write(str(Code_No1))
    user_data2.write(",")
    user_data2.write(str(Code_No2))
    user_data2.write(",")    
    user_data2.write(str(book_name1))
    user_data2.write(",")
    user_data2.write(str(book_name2))
    user_data2.write(",")
    user_data2.write(str(borrow_dt))
    user_data2.write(",")
    user_data2.write(str(return_dt))
    user_data2.write(",")
    user_data2.close()
def overwrite_book1(overlist,book1):
    overlist[book1][2]=int(overlist[book1][2])-1
    return overlist
def overwrite_book2(overlist,book1,book2):
    overlist[book1][2]=int(overlist[book1][2])-1
    overlist[book2][2]=int(overlist[book2][2])-1
    return overlist
def overwrite_return1(name,book_name,actual_return_dt):
    user_data1=open(str(name)+".txt","w")
    user_data1.write(str(name))
    user_data1.write(",")
    user_data1.write(str(book_name))
    user_data1.write(",")
    user_data1.write(str(actual_return_dt))
    user_data1.write(",")
    user_data1.close()
def overwrite_return2(name,book_name1,book_name2,actual_return_dt):
    user_data2=open(str(name)+".txt","w")
    user_data2.write(str(name))
    user_data2.write(",")   
    user_data2.write(str(book_name1))
    user_data2.write(",")
    user_data2.write(str(book_name2))
    user_data2.write(",")
    user_data2.write(str(actual_return_dt))
    user_data2.write(",")
    user_data2.close()
def return_book1(overlist,book1):
    overlist[book1][2]=int(overlist[book1][2])+1
    return overlist
def return_book2(overlist,book1,book2):
    overlist[book1][2]=int(overlist[book1][2])+1
    overlist[book2][2]=int(overlist[book2][2])+1
    return overlist

def overwrite_quantity(overlist):
    file=open("OverWrite.txt","w")
    for i in range(len(overlist)):
        counter=1
        for j in range(len(overlist[i])):
            file.write(str(overlist[i][j]))
            if counter<=3:
                file.write(",")
            counter+=1
        file.write("\n")
    file.close()
            
