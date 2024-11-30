from decimal import *

s = "ткаченкоелизаветаденисовна"

letters = []
probability = []
length = 0

getcontext().prec = 35

for c in s:
    if c in letters:
        for i in range(length):
            if c == letters[i]:
                probability[i] = probability[i] + 1
                break
    else:
        letters.append(c)
        probability.append(Decimal(1))
        length = length + 1



for i in range(length-1):
    for j in range(length-i-1):
        if probability[j] > probability[j+1]:
            probability[j], probability[j+1] = probability[j+1], probability[j]
            letters[j], letters[j+1] = letters[j+1], letters[j]

for i in range(length):
    probability[i] = probability[i]/len(s)

for i in range(length):
    print("Вероятность", letters[i], "=", probability[i])

left = Decimal(0)
right = Decimal(1)


for c in s:
    tmpl = left
    for i in range(length):
      tmpr = tmpl +  probability[i]*(right-left)
      if c == letters[i]:
        left = tmpl
        right = tmpr
        print("Границы буквы", c, ": левая =" , left, "правая =", right)
        break
      else:
        tmpl = tmpr

q = (right-left).ln()/Decimal(2).ln() * Decimal(-1)
q = q.quantize(Decimal('1'), ROUND_CEILING)
print("q =", q)

print("Границы для p:", left*Decimal(2)**q, right*Decimal(2)**q)
