import MySQLdb as sql
import classbank
ba=classbank.Banker()
ba.get_con()

Con = sql.Connect(host="127.0.0.1", port=3306, user="<Your Username>", passwd="<Password>", db="Your Database Name")
Cursor = Con.cursor()

c2=Con.cursor()
c3=Con.cursor()


print("Welcome To  XYZ Bank")
print("Press 1 to login")
print("Press 2 to signup")
num=int(raw_input("Number:"))
if num==1:
    
    us=raw_input("Enter Username")
    pa=raw_input("Enter Password")
    try:
        sql ="Select * from login Where Username='" + us + "' and Password='" + pa + "'";
        count=Cursor.execute(sql)
        Con.commit()
        
        if count==1:
            print("Press 1 for Savings Account")
            print("Press 2 for Current Account")
            nu=int(raw_input("Number:"))
            if nu==1:
                print("Press 1 for details")
                print("Press 2 for adding amount")
                am=int(raw_input("Number:"))
                if am==1:
                    ids=raw_input("Enter Account number")
                    c = Con.cursor()
                       
                    try:
                        sql1 ="Select * from login Where id="+ids  
                        c.execute(sql1)
                        res=c.fetchone()
                        print res
                        Con.commit()
                        
                    except:
                        Con.rollback()
                else:
                    
                    amo=raw_input("Enter Amount:")
                    c1=Con.cursor()
                    try:
                        idst=raw_input("Enter Account number")
                        sql2="UPDATE login SET savings=('"+amo+"') Where id="+idst
                        cont=c1.execute(sql2)
                        Con.commit()
                        if cont==1:
                            print("Amount added Successfully")
                        else:
                            print("Error in adding Amount")
                    except:
                        Con.rollback()
            else:
                print("Press 1 for detalis")
                print("Press 2 for adding amount")
                amt=int(raw_input("Number:"))
                if amt==1:
                    ids2=raw_input("Enter The account number")
                    try:
                        sql3="Select * from login Where id="+ids2 
                        c2.execute(sql3)
                        rest=c2.fetchall()
                        print rest
                        Con.commit()
                    except:
                        Con.rollback()
                else:
                    amou=raw_input("Enter The amount:")
                    c3=Con.cursor()
                    try:
                        ids3=raw_input("Enter The Account Number")
                        sql4="UPDATE login SET current=('"+amou+"') Where id="+ids3
                        cou=c3.execute(sql4)
                        Con.commit()
                        if cou==1:
                            print("Amount Added Successfully")
                        else:
                            print("Error in adding amount")
                    except:
                        Con.rollback()
        else:
            print("Login Failed")
        
        
            
    except:
        Con.rollback()

else:
    Conn = sql.Connect(host="127.0.0.1", port=3306, user="root", passwd="root", db="bank")
    cur=Conn.cursor();
    try:
        us=raw_input("Enter Username")
        pa=raw_input("Enter Password")
        ph=raw_input("Enter Phone Number")
        Id=raw_input("Enter Account Number")
        print("Generating New Client.....")
        sql5 ="INSERT INTO login (id,Username,Password,Phone) VALUES('"+Id+"','"+us+"','"+pa+"','"+ph+"')"
        cur.execute(sql5)
        Conn.commit()
        Conn.close()
        print("Congratulations!!!!")
        print("Thank You For Signing With Us,Reload the Program")
    except:
        Conn.rollback()
        
    
