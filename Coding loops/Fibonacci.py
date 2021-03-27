n = int(input("Enter the number till where fibonacci should be printed : "))
p = 1
q = 0
for i in range(n):
    print(p, end =' ' )
    temp = p
    p = p + q
    q = temp