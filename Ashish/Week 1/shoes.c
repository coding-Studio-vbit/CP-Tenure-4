#include <stdio.h>
int main(void) {
	int t;
	scanf("%d",&t);
	for(int i = 0; i < t; i++)
	{
	    int n,m;
	    scanf("%d %d",&n,&m);
	    if(m >= n)
	    {
	        printf("%d\n",n);
	    }
	    else
	    {
	        int nl = n-m;
	        nl = nl + n;
	        printf("%d\n",nl);
	    }
	}
	return 0;
}

