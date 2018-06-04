#Simple program that takes in IP address, returns Subnet Mask, Broadcast/Network Address, Host Address Range
#Rohan Taneja
import math

def dec2binary(decimal): #NOTE: function already exists to convert decimal to binary, this is just for practice
    eightbit = ""
    while decimal > 0:
        eightbit = str(decimal%2) + eightbit
        decimal = decimal//2
    return int(eightbit.zfill(8))

def binarytodec(binary): #NOTE: function used only for 8 bit binary nums
    sum = 0
    for i in range(8):
        if binary[i] == '1':
            sum += math.pow(2,7-i)
    return int(sum)

def nsplit(s,n):#splits string into n groups, for example used to break up 32 bit ip address into individual bytes
    groups = []
    for i in range(0, len(s),n):
        groups.append((s[i:i+n]))
    return groups

address = input("Please enter a valid IP address with net mask (Ex: 192.168.2.64/26) : ")
ipaddress = address[:address.index('/')]
mask = int(address[address.index('/')+1:])
bytes = ipaddress.split('.')

##### Determining Subnet Mask#####
if(mask == 0): #random extreme case, not actually feasible
    subnetstring = "0"*32
else:
    subnetstring = '{:<032d}'.format(int("1"*mask))

subnetbytes = nsplit(subnetstring,8)
for x in range(len(subnetbytes)):
    subnetbytes[x] = str(binarytodec(subnetbytes[x]))
subnetmask = '.'.join(subnetbytes)
#print("Subnet Mask:", subnetmask)
##### Determining Network/Broadcast Addresses
for y in range(len(bytes)):
    #print(bytes[y],str(dec2binary(int(bytes[y]))).zfill(8))
    bytes[y] = str(dec2binary(int(bytes[y]))).zfill(8)
fullIPbinary = ''.join(bytes)
#print(fullIPbinary)
splicedaddress = fullIPbinary[:mask]
#print("SPL",splicedaddress)
networkaddress = '{:<032d}'.format(int(splicedaddress))
#print("Network Address",networkaddress)
broadcastaddress = splicedaddress + ("1"*(32-len(splicedaddress)))
#print("Broadcast Address",broadcastaddress)
networkad = nsplit(networkaddress,8)
broadcastad = nsplit(broadcastaddress,8)
#print(broadcastad)
for x in range(len(networkad)):
    networkad[x] = str(binarytodec(networkad[x]))
    broadcastad[x] = str(binarytodec(broadcastad[x]))
hostmin = int(networkad[-1])+1
hostmax = int(broadcastad[-1])-1
hostrangemin = networkad[:3]
hostrangemin.append(str(hostmin))
#print("HRM", hostrangemin)
hostrangemax = networkad[:3]
hostrangemax.append(str(hostmax))

#print("HOSTMIN",hostmin)
formattednetworkaddress = '.'.join(networkad)
formattedbroadcastaddress = '.'.join(broadcastad)
#print(formattednetworkaddress, formattedbroadcastaddress)
rangemin = '.'.join(hostrangemin)
rangemax = '.'.join(hostrangemax)
print("Subnet Mask:", subnetmask)
print("Network Address:",formattednetworkaddress)
print("Broadcast Address:",formattedbroadcastaddress)
print("Host Address Range: ",rangemin,'-', rangemax)