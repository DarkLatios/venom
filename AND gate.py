lis_a=[]

def calc_c(or_li):
    
    p=1
    for x in or_li:
        p=p*x
    if(p==1):
        lis_a.append(1)
    else:
        lis_a.append(0)


        


T=int(raw_input("Enter the number"))
for a in xrange(0,T):
    
    or_li = []
    a=int(raw_input("Enter the set"))
    if a:
        inputs=raw_input("Enter the list").split(' ')
        or_li = []
        for i in inputs:
            try:
                or_li.append(int(i))
              
              
            except:
                pass
                  
        calc_c(or_li)       
    
      
      
                
               
            
        
    
    
        
        
        
    
for xi in lis_a:
    print xi

        
