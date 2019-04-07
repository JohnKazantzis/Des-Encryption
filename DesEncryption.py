import binascii
import copy
import sys

def shifting1(listx,listy):
    for i in range(1,28):       #Shifting by 1
        listx.append(listy[i])
    listx.append(listy[0])


def shifting2(listx,listy):
    for i in range(2,28):       #Shifting by 2
        listx.append(listy[i])
    listx.append(listy[0])
    listx.append(listy[1])


def pc2Perm(listx,listy):       #Pc2 Permutation
    pc2 = [14,17,11,24,1,5,
            3,28,15,6,21,10,
            23,19,12,4,26,8,
            16,7,27,20,13,2,
            41,52,31,37,47,55,
            30,40,51,45,33,48,
            44,49,39,56,34,53,
            46,42,50,36,29,32]

    for x in pc2:
        listx.append(listy[x-1])

def addLeading0(oldbin):
    newbin = []
    if(len(oldbin) < 66):             #String to table with leading zeros
        for i in range(66 - len(oldbin)):
            newbin.append('0')
        for x in range(64 - (66 - len(oldbin))):
            newbin.append(oldbin[x + 2])
        oldbin = copy.copy(newbin)
        return oldbin
    else:
        for x in range(64 - (66 - len(oldbin))):
            newbin.append(oldbin[x + 2])
        oldbin = copy.copy(newbin)
        return oldbin

def plaintextPerm(pTextBin):
    permutedPlain = []
    permList = [58,50,42,34,26,18,10,2,
                60,52,44,36,28,20,12,4,
                62,54,46,38,30,22,14,6,
                64,56,48,40,32,24,16,8,
                57,49,41,33,25,17,9,1,
                59,51,43,35,27,19,11,3,
                61,53,45,37,29,21,13,5,
                63,55,47,39,31,23,15,7]

    for x in permList:
        permutedPlain.append(pTextBin[x-1])
    return permutedPlain

def expansion(rList): # expansion
    expandedList = []
    eBitSel = [32,1,2,3,4,5,
                4,5,6,7,8,9,
                8,9,10,11,12,13,
                12,13,14,15,16,17,
                16,17,18,19,20,21,
                20,21,22,23,24,25,
                24,25,26,27,28,29,
                28,29,30,31,32,1]
    for x in eBitSel:
        expandedList.append(rList[x-1])
    return expandedList

def xorOperation48(listx,listy): # 48 bit xor
    xorlist = []
    for x in range(0,48):
        if((listx[x] and not listy[x]) or (not listx[x] and listy[x])):
            xorlist.append('1')
        else:
            xorlist.append('0')
    return xorlist

def fourBitList(listx): # converting to 4bit list
    newlist = []
    if(4 - len(listx) > 0):
        for x in range(4 - len(listx)):
            newlist.append(0)
        for x in range(len(listx)):
            newlist.append(listx[x])
        return newlist
    else:
        return listx

def spliting8(kR): #Spliting the list in 8 parts
        b1 = []
        b2 = []
        b3 = []
        b4 = []
        b5 = []
        b6 = []
        b7 = []
        b8 = []
        for x in range(0,6):
            b1.append(kR[x])
            b1[x] = int(b1[x])
        for x in range(6,12):
            b2.append(kR[x])
            b2[x-6] = int(b2[x-6])
        for x in range(12,18):
            b3.append(kR[x])
            b3[x-12] = int(b3[x-12])
        for x in range(18,24):
            b4.append(kR[x])
            b4[x-18] = int(b4[x-18])
        for x in range(24,30):
            b5.append(kR[x])
            b5[x-24] = int(b5[x-24])
        for x in range(30,36):
            b6.append(kR[x])
            b6[x-30] = int(b6[x-30])
        for x in range(36,42):
            b7.append(kR[x])
            b7[x-36] = int(b7[x-36])
        for x in range(42,48):
            b8.append(kR[x])
            b8[x-42] = int(b8[x-42])

        return b1,b2,b3,b4,b5,b6,b7,b8

def sfunction(b1,b2,b3,b4,b5,b6,b7,b8):     #S box function
    s1 = [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
            [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
            [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
            [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]
    s2 = [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
            [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
            [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
            [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]]
    s3 = [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
            [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
            [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
            [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]]
    s4 = [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
            [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
            [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
            [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]]
    s5 = [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
            [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
            [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
            [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]]
    s6 = [[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
            [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
            [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
            [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]]
    s7 = [[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
            [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
            [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
            [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]]
    s8 = [[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
            [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
            [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
            [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]

    row = b1[0]*2 + b1[5]
    col = b1[1]*8 + b1[2]*4 + b1[3]*2 + b1[4]
    num = s1[int(row)][int(col)]
    sb1 = [int(x) for x in bin(num)[2:]]
    sb1 = fourBitList(sb1)

    row = b2[0]*2 + b2[5]
    col = b2[1]*8 + b2[2]*4 + b2[3]*2 + b2[4]
    num = s2[row][col]
    sb2 = [int(x) for x in bin(num)[2:]]
    sb2 = fourBitList(sb2)

    row = b3[0]*2 + b3[5]
    col = b3[1]*8 + b3[2]*4 + b3[3]*2 + b3[4]
    num = s3[row][col]
    sb3 = [int(x) for x in bin(num)[2:]]    #print(sb2)
    sb3 = fourBitList(sb3)

    row = b4[0]*2 + b4[5]
    col = b4[1]*8 + b4[2]*4 + b4[3]*2 + b4[4]
    num = s4[row][col]
    sb4 = [int(x) for x in bin(num)[2:]]
    sb4 = fourBitList(sb4)

    row = b5[0]*2 + b5[5]
    col = b5[1]*8 + b5[2]*4 + b5[3]*2 + b5[4]
    num = s5[row][col]
    sb5 = [int(x) for x in bin(num)[2:]]
    sb5 = fourBitList(sb5)

    row = b6[0]*2 + b6[5]
    col = b6[1]*8 + b6[2]*4 + b6[3]*2 + b6[4]
    num = s6[row][col]
    sb6 = [int(x) for x in bin(num)[2:]]
    sb6 = fourBitList(sb6)

    row = b7[0]*2 + b7[5]
    col = b7[1]*8 + b7[2]*4 + b7[3]*2 + b7[4]
    num = s7[row][col]
    sb7 = [int(x) for x in bin(num)[2:]]
    sb7 = fourBitList(sb7)

    row = b8[0]*2 + b8[5]
    col = b8[1]*8 + b8[2]*4 + b8[3]*2 + b8[4]
    num = s8[row][col]
    sb8 = [int(x) for x in bin(num)[2:]]
    sb8 = fourBitList(sb8)

    return sb1,sb2,sb3,sb4,sb5,sb6,sb7,sb8

def fPerm(f):
    fnew = []
    p = [16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]
    for x in p:
        fnew.append(f[x-1])
    return fnew

def xorOperation32(listx,listy): # 32 bit xor
    xorlist = []
    for x in range(0,32):
        if((listx[x] and not listy[x]) or (not listx[x] and listy[x])):
            xorlist.append('1')
        else:
            xorlist.append('0')
    return xorlist

def finalPerm(r16l16): # final permutation
    fnew = []
    p = [40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,37,
    5,45,13,53,21,61,29,36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,34,2,42,10,
    50,18,58,26,33,1,41,9,49,17,57,25]
    for x in p:
        fnew.append(r16l16[x-1])
    return fnew

def main():
    pKey = []
    c0 = []
    d0 = []
    c1 = []
    c2 = []
    c3 = []
    c4 = []
    c5 = []
    c6 = []
    c7 = []
    c8 = []
    c9 = []
    c10 = []
    c11 = []
    c12 = []
    c13 = []
    c14 = []
    c15 = []
    c16 = []
    d1 = []
    d2 = []
    d3 = []
    d4 = []
    d5 = []
    d6 = []
    d7 = []
    d8 = []
    d9 = []
    d10 = []
    d11 = []
    d12 = []
    d13 = []
    d14 = []
    d15 = []
    d16 = []

    cd1 = []
    cd2 = []
    cd3 = []
    cd4 = []
    cd5 = []
    cd6 = []
    cd7 = []
    cd8 = []
    cd9 = []
    cd10 = []
    cd11 = []
    cd12 = []
    cd13 = []
    cd14 = []
    cd15 = []
    cd16 = []

    k1 = []
    k2 = []
    k3 = []
    k4 = []
    k5 = []
    k6 = []
    k7 = []
    k8 = []
    k9 = []
    k10 = []
    k11 = []
    k12 = []
    k13 = []
    k14 = []
    k15 = []
    k16 = []

    newbin = []
    ip = []         #intitial m permutation
    l0 = []
    r0 = []
    l1 = []
    r1 = []
    newmbin = []

    m = raw_input("Please input a 64bit String (8 characters): ")
    mbin = bin(int(binascii.hexlify(m),16)) #Converting Text String to bin

    key = raw_input("Please input a 64bit hex (16 hexadecimal digits): ")
    print("\n")

    key = int(key,16)

    print("Plaintest Input: "),
    print(m)
    print("Key: "),
    print(hex(key).lstrip("0x").rstrip("L"))

    binKey = bin(key)               #Converting Hex to bin

    mbin = addLeading0(mbin)

    binKey = addLeading0(binKey)

    pc1 = [57,49,41,33,25,17,9,
        1,58,50,42,34,26,18,
        10,2,59,51,43,35,27,
        19,11,3,60,52,44,36,
        63,55,47,39,31,23,15,
        7,62,54,46,38,30,22,
        14,6,61,53,45,37,29,
        21,13,5,28,20,12,4]


    for x in pc1:                   #PC1
        pKey.append(binKey[x-1])

    for i in range(28):             #Subkey C0
        c0.append(pKey[i])

    for j in range(28,56):          #Subkey D0
        d0.append(pKey[j])

    shifting1(c1,c0)                #Shifting
    shifting1(c2,c1)
    shifting2(c3,c2)
    shifting2(c4,c3)
    shifting2(c5,c4)
    shifting2(c6,c5)
    shifting2(c7,c6)
    shifting2(c8,c7)
    shifting1(c9,c8)
    shifting2(c10,c9)
    shifting2(c11,c10)
    shifting2(c12,c11)
    shifting2(c13,c12)
    shifting2(c14,c13)
    shifting2(c15,c14)
    shifting1(c16,c15)

    shifting1(d1,d0)
    shifting1(d2,d1)
    shifting2(d3,d2)
    shifting2(d4,d3)
    shifting2(d5,d4)
    shifting2(d6,d5)
    shifting2(d7,d6)
    shifting2(d8,d7)
    shifting1(d9,d8)
    shifting2(d10,d9)
    shifting2(d11,d10)
    shifting2(d12,d11)
    shifting2(d13,d12)
    shifting2(d14,d13)
    shifting2(d15,d14)
    shifting1(d16,d15)

    cd1 = c1 + d1                   #Merging
    cd2 = c2 + d2
    cd3 = c3 + d3
    cd4 = c4 + d4
    cd5 = c5 + d5
    cd6 = c6 + d6
    cd7 = c7 + d7
    cd8 = c8 + d8
    cd9 = c9 + d9
    cd10 = c10 + d10
    cd11 = c11 + d11
    cd12 = c12 + d12
    cd13 = c13 + d13
    cd14 = c14 + d14
    cd15 = c15 + d15
    cd16 = c16 + d16

    pc2Perm(k1,cd1)                 #Pc2 Permuting
    pc2Perm(k2,cd2)
    pc2Perm(k3,cd3)
    pc2Perm(k4,cd4)
    pc2Perm(k5,cd5)
    pc2Perm(k6,cd6)
    pc2Perm(k7,cd7)
    pc2Perm(k8,cd8)
    pc2Perm(k9,cd9)
    pc2Perm(k10,cd10)
    pc2Perm(k11,cd11)
    pc2Perm(k12,cd12)
    pc2Perm(k13,cd13)
    pc2Perm(k14,cd14)
    pc2Perm(k15,cd15)
    pc2Perm(k16,cd16)

    ip = plaintextPerm(mbin)

    for x in range(0,32):
        l0.append(ip[x])

    for y in range(32,64):
        r0.append(ip[y])

    b1 = []
    b2 = []
    b3 = []
    b4 = []
    b5 = []
    b6 = []
    b7 = []
    b8 = []
    sb1 = []
    sb2 = []
    sb3 = []
    sb4 = []
    sb5 = []
    sb6 = []
    sb7 = []
    sb8 = []
    f = []

    Kiter = [k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11,k12,k13,k14,k15,k16]

    counter = 1

    for i in Kiter:     #16 rounds of key adding
        l1 = r0
        r0 = expansion(r0)
        for k in range(0,48):
            r0[k] = int(r0[k])
            i[k] = int(i[k])

        k1r0 = xorOperation48(i,r0)

        b1,b2,b3,b4,b5,b6,b7,b8 = spliting8(k1r0)
        sb1,sb2,sb3,sb4,sb5,sb6,sb7,sb8 = sfunction(b1,b2,b3,b4,b5,b6,b7,b8)
        f = sb1 + sb2 + sb3 + sb4 + sb5 + sb6 + sb7 + sb8

        f = fPerm(f)

        for n in range(0,32):
            l0[n] = int(l0[n])

        r1 = xorOperation32(l0,f)

        counter = counter + 1

        l0 = l1
        r0 = r1

    r16l16 = r1 + l1

    r16l16 = finalPerm(r16l16) #Final permutation

    str1 = ''.join(r16l16)
    ciphertext = hex(int(str1,2))
    print("Ciphertext: "),
    print(ciphertext.lstrip("0x").rstrip("L"))
main()
