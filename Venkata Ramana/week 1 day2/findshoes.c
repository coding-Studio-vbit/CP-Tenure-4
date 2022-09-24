#include <stdio.h>

int main(void) {
	// your code goes here
	int T;
	scanf("%d",&T);
	while(T--)
	{
	    int N,M;
	    scanf("%d %d",&N,&M);
	    if(N>M)
	    {
	        printf("%d\n",N*2-M);
	    }
	    else
	    {
	        printf("%d\n",N);
	    }
	}
	return 0;
}