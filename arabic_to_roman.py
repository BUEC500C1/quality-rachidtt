from module import convert_arabic_roman

print("Arabic to Roman converter \n")

Arabic = input("Please enter a number: ")
Roman = convert_arabic_roman(Arabic)

while(Roman=='SignError' or Roman=='RangeError' or Roman=='ValueError'):
	if(Roman=='SignError'):
		print("Sorry, number must be positive and non-zero, please try again\n")
		Arabic = input("Please enter a number: ")
		Roman = convert_arabic_roman(Arabic)
	elif(Roman=='RangeError'):
		print("Sorry, number cannot be larger than 3999, please try again\n")
		Arabic = input("Please enter a number: ")
		Roman = convert_arabic_roman(Arabic)
	else:
		print("Please enter a real number, try again\n")
		Arabic = input("Please enter a number: ")
		Roman = convert_arabic_roman(Arabic)

print('The number '+Arabic+' is '+Roman+' in roman numerals\n')