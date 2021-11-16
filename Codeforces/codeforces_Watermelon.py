'''sketch
figure out whether even number or odd number is

- if weight == 2: divided into odd number => exclude this case
'''
weight = int(input())
if weight % 2 is 0 and weight is not 2:
    print("YES")
else:
    print("NO")