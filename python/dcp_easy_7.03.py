def main():
    list = [10,15,3,7]
    k = 170
    
    for i in list: 
        rest = k - i 
        if rest in list :
            print True 
            break
        rest = 0
        
main()