

def main():
    list ,max_list = [10,5,2,7,8,7,8,1,1,1,2,3,4] , []
    k = 9
    i = 0

    while i+k < len(list)+1 :
        sub = list[i:i+k]
        i += 1 
        max_list.append(max(sub))
        
    print max_list
main()