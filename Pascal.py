def base(n):
    base = "1"
    blist = [[1],[1,1]]
    for i in range(n):
        slist = blist[-1]
        sslist = [1,1]
        length = len(slist)
        for j in range(len(slist)):
            sslist.insert(1,slist[j]+slist[j+1])
            if j == length-2:
                break
        blist.append(sslist)
    return blist
    
def Pascal(aura):
    def mycenter(string,length):
        center = (int(length)*" ")+string+(int(length)*" ")
        return center
    def blocklength():
        pee = 0
        for aung in aura[-1]:
            aunglength = len(str(aung))
            if aunglength > pee:
                pee = aunglength
        return pee
                
    def adjust(n):
        while len(n) != blocklength():
            n += " "
        return n
    
    def middle():   
        ss = " "
        for uu in aura[-1]:
            ss += adjust(str(uu))+(blocklength())*" " 
        return len(ss)
    
    def tostring():
        bigstring = ""
        cent = middle()
        for aung in aura:
            smallstring = ""
            cent -= blocklength()
            for huang in aung:
                smallstring += adjust(str(huang)) + (blocklength())*" "
            ccc = mycenter(smallstring ,cent)+"\n"
            bigstring += ccc
        return bigstring
    return tostring()

print("Pascal's Triangle")
while True:
    n = int(input("Number of lines:"))
    print(Pascal(base(n)))
    g = input("Do you want to go again?Y/n:")
    if g.lower() == "n":
        break
    
