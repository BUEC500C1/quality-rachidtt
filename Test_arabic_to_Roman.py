from module import convert_arabic_roman

def test_convert():
	assert convert_arabic_roman('1')=='I'
	assert convert_arabic_roman('1978')=='MCMLXXVIII'
	assert convert_arabic_roman('3989')=='MMMCMLXXXIX'
	assert convert_arabic_roman('-45')=='SignError'
	assert convert_arabic_roman('4500')=='RangeError'
	assert convert_arabic_roman('')=='ValueError'
	assert convert_arabic_roman('@@')=='ValueError'
