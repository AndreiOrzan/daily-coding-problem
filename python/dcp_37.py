"""    def listlist():
        list ,super ,inter = [1,2,3] , [] , []
        a = len(list) 

        for i in range (a) : 
            for j in range(i):
                for z in list:
                    inter.append(z)
                super.append(inter)
                    
                
        print super,"test"
                
listlist()"""

def set(s):
    if not s:
        return[[]]
    result = set(s[1:])
    return result + [sub + [s[0]] for sub in result ]
    
print set([1,2,3])