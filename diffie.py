import math
array = []
private = []
key = []
p = int(input("Choose a public key p: "))
n = int(input("Enter number of users: "))
for i in range(0,n):x = int(input("Choose private key of user"+str(i)+": "))
private.append(x)
for g in range(1,p-1):
for j in range(0,p-1):
array.append(0)
for i in range(1,p):
x = int(pow(g,i))
x = int(math.fmod(x,p))
if (int(array[x])==1):
break
else:
array[x] = 1
if i==p-1:
break
print("Primitive root is ",g)
for i in range(0,n):
x = pow(g,private[i])
x = int(math.fmod(x,p))
key.append(x)
print("Key generated by user"+str(i)+" before key
exchange: ",key[i])
exc = int(input("Enter number of exchanges: "))
for i in range(0,exc):
x1 = int(input("Enter first user number: "))
x2 = int(input("Enter second user number: "))
ka = pow(key[x2],private[x1])
ka = int(math.fmod(ka,p))kb = pow(key[x1],private[x2])
kb = int(math.fmod(kb,p))
print("Key generated by user"+str(x1)+" after key
exchange: ",ka)
print("Key generated by user"+str(x2)+" after key
exchange: ",kb)
