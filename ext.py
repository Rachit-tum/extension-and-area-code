dict={"py":"python file","docx":"word file","pdf":"adobe reader file"}
z=0
while True:
    q=""
    b=[]
    a=input("give the file name with extension: ")
    for i in a:
        b.append(i)
    for e in a:
        b.remove(e)
        if e==".":
            break
    if b==[]:
        print("no extension is given with the file name")
    else:    
        for w in b:
            q=q+w    
        if q in dict:    
            print("file name" ,a,"  " ,"extension:",q,"  ", dict[q])
        else :
            print("unkown extension")
    z+=1    
        
