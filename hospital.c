#include <stdio.h>
int main(){
	double vol,t;
	double rate;
	printf("enter the volume and time in (minutes) \n");
	scanf("%lf",&vol);
	scanf("%lf",&t);
        t=t/60;
	rate=vol/t;
	printf("the rate is %f",rate);
}

