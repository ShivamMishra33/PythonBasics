k = input('enter your text here')
d = k.find('.')
i = k.find('[')
j = k.find(']')
while(d>j):
 p = k[i+1:j]
print(p)
