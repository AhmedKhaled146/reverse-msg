message = str(input("Enter your message to reverse : "))
print(len(message))
inverse = '' 
i = len(message) - 1

while i >= 0:
   inverse = inverse + message[i]
   i = i - 1
print(inverse)