bill_input = input("What is the bill total? ")

bill_input_clean = bill_input.replace("$", "")
# .replace() to remove $ if that is entered by user
bill_input_clean = float(bill_input_clean)

ten_percent = bill_input_clean * .10
fifteen_percent = bill_input_clean * .15
twenty_percent = bill_input_clean * .20

tip_input = input('''How much would you like to tip?
Press 1 for 10%
Press 2 for 15%
Press 3 for 20% 
''')

if tip_input == str(1):
 	print(f"Your total bill with 10% tip is: ${ten_percent:.2f}")
elif tip_input == str(2):
	print(f"Your total bill with 15% tip is: ${fifteen_percent:.2f}")
elif tip_input == str(3):
	print(f"Your total bill with 20% tip is: ${twenty_percent:.2f}")
else:
	print("invalid input")