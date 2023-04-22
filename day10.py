# Simple calculator
print("""
 _____________________
|  _________________  |
| |                 | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
)

def add(n1,n2):
	return n1+n2
def sub(n1,n2):
	return n1-n2
def mul(n1,n2):
	return n1*n2
def divi(n1,n2):
	return n1/n2
operations={
	"+": add,
	"-": sub,
	"*": mul,
	"/": divi}
def calculator():
	num1=float(input("Enter the first number: \n"))
	for i in operations:
		print(i)
	flag=True
	while flag:
		op=input("Pick any operation: ")
		num2=float(input("Enter the next number: "))
		val=operations[op](num1,num2)
		print(f'{num1} {op} {num2} = {val}')
		cont=input("Type 'y' to continue calculating with {val}, or type 'n' to start a new calculation:").lower()
		if cont=="y":
			num1=val
		else:
			flag=False
			calculator()
calculator()
 
