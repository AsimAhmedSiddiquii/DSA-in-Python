str1 = "999999"
str2 = "999999"
res = ''
carry = 0

str1 = str1[::-1]
str2 = str2[::-1]

for i in range(0, len(str1)):
    sum = int(str2[i]) + int(str1[i]) + carry
    if sum > 9:
        res += str(sum % 10)
        carry = 1
    else:
        carry = 0
        res += str(sum)

if carry == 1:
    res += str(carry)

print(res[::-1])