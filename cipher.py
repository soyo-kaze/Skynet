if __name__=="main":
    pass
    
            
def enc(password):
    #print("hello")
    grid = {}
    key = 33
    index = []
    for x in range(1, 4):
        c = x
        for y in range(1, 9):
            b = y
            for z in range(1, 5):
                a = z
                index = []
                for f in (c, b, a):
                    index.append(str(f))
                grid[chr(key)] = index
                key += 1
    #global grid
    encryption = []
    for p in range(0, len(password)):
        encryption.append("".join(grid[password[p]]))  # encrypts the pass
    return "".join(encryption)  # prints encrypted pass

def dec(sam):
    #print("hello")
    grid = {}
    key = 33
    index = []
    for x in range(1, 4):
        c = x
        for y in range(1, 9):
            b = y
            for z in range(1, 5):
                a = z
                index = []
                for f in (c, b, a):
                    index.append(str(f))
                grid[chr(key)] = index
                key += 1
    decryption = []
    #print(sam)
    ecn_pass = str(sam) #will be changed to a var taking ecrypted_pass as input
    n = 0
    dec = []
    for g in range(0, int(len(ecn_pass)/3)):
        dec = []
        for e in range(n, n+3):
            dec.append(ecn_pass[e])
        decryption.append(dec)
        n = n + 3
    #print(decryption)
    d = []
    for h in range(0, len(decryption)):
        d.append(list(grid.keys())[list(grid.values()).index(decryption[h])]) #prints decrypted pass
    return "".join(d)
