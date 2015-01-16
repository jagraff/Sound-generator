import math

def main():
	while True:
		for z in range(-5, 5):
			for x in range(int(1*math.fabs(z)), int(10*math.fabs(z))):
				freq = x
				for i in range(0, 100*int(math.log10(freq))):
					raw_num = math.sin(6.28*(float(i)/float(freq)))
					converted_num = int(128*(raw_num + 1))
					print chr(converted_num)
		


main()
