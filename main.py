num = int(input("Multiplication table you want: "))
o = int(input("Till which number you want your table to be: "))
for i in range(1, o + 1):
  y = num*i
  print(f"{num} x {i} = {y}")
