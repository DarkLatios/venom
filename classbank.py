import MySQLdb as sql 
class Banker:
    def get_con(self):
        Cont = sql.Connect(host="127.0.0.1", port=3306, user="root", passwd="root", db="bank")
        try:
            
            Cu = Cont.cursor()
            tbl="login"
            sql7="SELECT COUNT(*) FROM information_schema.tables WHERE table_name = '"+tbl+"'";
            cont=Cu.execute(sql7)
            res=Cu.fetchone()
            if True:
                print("HELLO")
                Cont.commit()
                Cont.close()
            else:
                Contt = sql.Connect(host="127.0.0.1", port=3306, user="root", passwd="root", db="bank")
                tbl="login"
                sql6="CREATE TABLE "+tbl+" (id VARCHAR(255) NOT NULL , Username VARCHAR(255),Password VARCHAR(255),Phone VARCHAR(255),savings VARCHAR(255),current VARCHAR(255), PRIMARY KEY ( id ))";
                Cu.execute(sql6)
                Contt.commit()
                Contt.close()

        except:
            Cont.rollback()







    

    
