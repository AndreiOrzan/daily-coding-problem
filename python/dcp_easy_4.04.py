def length_encoding():
    stri ,new = "AAAABBBCCDAA" ,""
    count = 1 
    for i in range(len(stri) - 1):
        if stri[i+1] != stri[i]:
            new += str(count) + stri[i]
            print stri[i]
            count = 1
        else:
            count += 1
    print new
            
length_encoding()
