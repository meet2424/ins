P = int(input('Enter value of P: '))#23
Q = int(input('Enter value of Q: '))#9
a = int(input('Enter value of a: '))#4
b = int(input('Enter value of b: '))#3

x = int(pow(Q,a,P))
y = int(pow(Q,b,P))

ka = int(pow(y,a,P))
kb = int(pow(x,b,P))

if ka==kb:
  print('Done!')
else:
  print('Failed!')

print('Secret key for the Jhon is : %d'%(ka))
print('Secret Key for the Tom is : %d'%(kb))