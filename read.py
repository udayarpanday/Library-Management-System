def Return_Books(name):
    Returnbooks_file=open(str(name)+".txt","r")
    Returnfile=Returnbooks_file.read().split(",")
    return Returnfile
def Lab_Menu(menu):
    Library_file=open(menu,"r")
    print(Library_file.read())
    return menu  
def Books():
    Books_file=open("Books.txt","r")
    option=Books_file.readlines()
    return option

def list_conversion():
    list2D=[ ]
    list2=Books()
    for item in list2:
        list2D.append(item.replace("\n","").split(","))
    return list2D
