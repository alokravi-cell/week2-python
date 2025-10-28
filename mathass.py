#simple interest calculation
p=int(input("Please enter Principal :"))
r=float(input("Please enter rate of interest :"))
t=float(input("Please enter time in years :"))
SI = float((p*r*t)/100)
print(f"The Simple Interet is Rs.{SI:.2f}/-")

