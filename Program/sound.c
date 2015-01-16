#include <math.h>
#include <stdio.h>
#define PI 3.14159265
#define sampleRate 41800
int main(void)
{
	double i = 0;
	for (i = 0;;i+=.1)
	{
		
		putchar(128*(sin(i)+1));
	}
	
	
	return 0;	
}
