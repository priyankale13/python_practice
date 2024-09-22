num=input("Enter a number: ")
digits=list(num)
count=len(digits)
print("no of digits :",count)
sum=0

for i in range(count):
    sum=sum+int(digits[i])

print("Sum of digits: ",sum)
