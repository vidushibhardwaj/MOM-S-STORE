list_product_name={"dant kanti toothpaste":[59,10],"hair bands pair(2)":[10,50]};
def add_product():
    prod_list=[]
    n=input("enter the product name: ")
    p=int(input("enter the product price: "))
    prod_list.append(p)
    q=int(input("enter the quantity: "))
    prod_list.append(q)
    list_product_name[n]=prod_list

def modify_price():
    n=input("enter the name of the product: ")
    for i in list_product_name:
        if(i==n):
            print ("previous price: "+str(list_product_name[i][0]))
            p=int(input("updated price: "))
            list_product_name[i][0]=p
            see_list()

def modify_quantity():
    n=input("enter the name of the product: ")
    for i in list_product_name:
        if(i==n):
            print ("previous quantity: "+str(list_product_name[i][1]))
            q=int(input("updated quantity: "))
            list_product_name[i][1]=q
            see_list()

def see_list():
    print ("PRODUCT NAME\t\t\tPRICE\t\t\tQUANTITY")
    for i in list_product_name:
        print (i+"\t\t\t"+str(list_product_name[i][0])+"\t\t\t"+str(list_product_name[i][1])+"\n")
 
New_cust_list={};
list_admin=[]
list_admin.append("add product")
list_admin.append("modify price")
list_admin.append("modify quantity")
list_admin.append("see list")
def admin():
    for i in list_admin:
        print (i+"\n")
    n=int(input("enter: "))
    if(n==1):
        add_product()
    elif(n==2):
        modify_price()
    elif(n==3):
        modify_quantity()
    else:
        see_list()
    menu()


def new_customer():
    n=input("enter your name: ")
    phone_num=input("enter your phone_number: ")
    cust_list=[]
    cust_list.append(n);
    New_cust_list[phone_num]=cust_list
    return phone_num

def old_customer():
    p=input("enter your phone_number: ")
    f=0
    for i in New_cust_list:
        if(i==p):
            f=1
            print ("customer name: "+str(New_cust_list[i][0])+" customer phone number: "+i+" your current points: "+str(New_cust_list[i][1]) )
            return p
    if(f==0):
        print ("customer with "+p+" not found ")
        return -1



def cust_prod_list(phone_num):
    ch=1
    pro_list={};
    while (ch==1):
        n=input("enter the product name: ")
        for i in list_product_name:
            if(i==n):
                q=int(input("enter the quantity: "))
                if(list_product_name[i][1]<q):
                    print (str(list_product_name[i][1])+" is only available")
                else:
                    pro_list[i]=q
                    list_product_name[i][1]=list_product_name[i][1]-q  
        ch=int(input("wanna have more products to basket: "))
    for j in New_cust_list:
        if(j==phone_num):
            New_cust_list[j].append(pro_list)

def cust_prod_remove(phone_num):
    print ("\nYOUR BASKET: \n")
    for i in New_cust_list[phone_num][1]:
         print (i)
    n=input("enter the product to be removed: ")
    for j in New_cust_list[phone_num][1]:
        if(j==n):
            print ("****product found****")
            break
    del New_cust_list[phone_num][1][j]


def cust_qty_modify(phone_num):
    n=input("enter the product whose quantity to be modified: ")
    for i in New_cust_list[phone_num][1]:
        if(i==n):
            print ("YOUR CURRENT QUANTITY TAKEN IS: "+str(New_cust_list[phone_num][1][i]))
            q=int(input("updated quantity needed: "))
            if(list_product_name[n][1]<q):
                print ("quantity entered exceeded the present quantity which is: "+str(list_product_name[n][1]))
                cust_qty_modify(phone_num)
            else:
                list_product_name[n][1]=list_product_name[n][1]+New_cust_list[phone_num][1][i]
                New_cust_list[phone_num][1][i]=q;
                list_product_name[n][1]=list_product_name[n][1]-q
                see_list()
    print ("YOUR UPDATED BASKET:")
    print ("PRODUCT\t\t\tQUANTITY")
    for i in New_cust_list[phone_num][1]:
        print (i+"\t\t\t"+str(New_cust_list[phone_num][1][i]))
    
def cust_bill(phone_num):
    for i in New_cust_list:
        if(i==phone_num):
            print ("\n\n\n\t\t\t********************************************BILL**********************************************\n")
            print ("CUSTOMER NAME: "+New_cust_list[i][0]+"\nPHONE NUMBER: "+phone_num+"\n")
            print("PRODUCT NAME\t\tQUANTITY\t\tPER PRICE\t\tTOTAL PRICE\n")
            sum=0
            for j in New_cust_list[i][1]:
                for k in list_product_name:
                    if(j==k):
                        print (""+j+"\t\t"+str(New_cust_list[i][1][j])+"\t\t\t"+str(list_product_name[k][0])+"\t\t\t"+str((list_product_name[k][0])*New_cust_list[i][1][j]))
                        sum+=list_product_name[k][0]*New_cust_list[i][1][j]
            print ("\n\t\t\t\t\t\t\t\tTOTAL AMOUNT DUE:      "+str(sum))
            print ("\n\t\t\t****************************************************************************************************\n")
                
    
##                
##
list_user=[]
list_user.append("new customer")
list_user.append("old customer") 
def user():
    for i in list_user:
        print(i)
    o=int(input("enter the option: "))
    if(o==1):
       pn= new_customer()
    elif(o==2):
       pn= old_customer()
       if(pn==-1):
           user()
    ch=1
    while(ch==1):
        print ("1. see product list\n2. add a product\n3. remove a product\n4.modify the quantity\n5.take the bill\n")
        n=int(input("enter the option"))
        if(n==1):
            see_list()
        elif(n==2):
            cust_prod_list(pn)
        elif(n==3):
            cust_prod_remove(pn)
        elif(n==4):
            cust_qty_modify(pn)
        else:
            cust_bill(pn)
        ch=int(input("wanna look more into products: "))
    menu()
    
print("\t\t\t\t******************************WELCOME TO MOM'S STORE*********************************\n\n")
def menu():
    print ("\t\t\t\t1.CUSTOMER\n\t\t\t\t2.ADMIN\n\t\t\t\t3.EXIT")
    n=int(input("enter : "))
    if(n==1):
        user()
    elif(n==2):
        admin ()
    else:
        print ("\t\t\t\t****************************THANK YOU FOR VISIT*************************************")
menu()

