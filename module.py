def convert_arabic_roman(arabic):

	try:
	   Arabic = int(arabic)					#will cause ValueError if not correct input
	   if(Arabic<=0):
	   		return 'SignError'
	   if (Arabic >3999):						    #Makes sure > 0 and < 4000
	   		return 'RangeError'	
	except ValueError:							#Makes sure int is entered

	   return 'ValueError'	

	Roman = ""
	while (Arabic > 0):
		if(Arabic>=1000):
			Arabic=Arabic-1000
			Roman= Roman + 'M'
			continue
		if(Arabic>=900):
			Arabic=Arabic-900
			Roman= Roman + 'CM'
			continue
		if(Arabic>=500):
			Arabic=Arabic-500
			Roman= Roman + 'D'
			continue
		if(Arabic>=400):
			Arabic=Arabic-400
			Roman= Roman + 'CD'
			continue
		if(Arabic>=100):
			Arabic=Arabic-100
			Roman= Roman + 'C'
			continue
		if(Arabic>=90):
			Arabic=Arabic-90
			Roman= Roman + 'XC'
			continue
		if(Arabic>=50):
			Arabic=Arabic-50
			Roman= Roman + 'L'
			continue
		if(Arabic>=40):
			Arabic=Arabic-40
			Roman= Roman + 'XL'
			continue
		if(Arabic>=10):
			Arabic=Arabic-10
			Roman= Roman + 'X'
			continue
		if(Arabic>=9):
			Arabic=Arabic-9
			Roman= Roman + 'IX'
			continue
		if(Arabic>=5):
			Arabic=Arabic-5
			Roman= Roman + 'V'
			continue
		if(Arabic>=4):
			Arabic=Arabic-4
			Roman= Roman + 'IV'
			continue
		if(Arabic>=1):
			Arabic=Arabic-1
			Roman= Roman + 'I'
	return Roman 