#include <stdio.h>
int main(void)
{
	int t;
	scanf("%d", &t);
	for(int i = 0; i < t; i++)
	{
	    int n,x,s,r,m=0;
	    scanf("%d %d", &n , &x);
	    for(int j = 0; j < n; j++)
	    {
	        scanf("%d %d",&s,&r);
	        if(s <= x)
	        {
	            if(r > m)
	            {
	                m = r;
	            }
	        }
	    }
	    printf("%d\n",m);
	}
	return 0;
}