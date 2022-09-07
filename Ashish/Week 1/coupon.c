#include <stdio.h>

int main(void) {
	int t;
	scanf("%d",&t);
	for(int i = 0; i < t; i++)
	{
	    int d,c,a[3],b[3],sa=0,sb=0;
	    scanf("%d %d",&d,&c);
	    scanf("%d %d %d",&a[0],&a[1],&a[2]);
	    scanf("%d %d %d",&b[0],&b[1],&b[2]);
	    int swc,sc;
	    for(int j = 0; j < 3; j++)
	    {
	        sa = sa + a[j];
	        sb = sb + b[j];
	    }
	    swc = sa + sb + 2*d;
	    sc = sa + sb + c;
	    if(sa < 150)
	    {
	        sc = sc + d;
	    }
	    if(sb < 150)
	    {
	        sc = sc + d;
	    }
	    if(sc < swc)
	    {
	        printf("YES\n");
	    }
	    else
	    {
	        printf("NO\n");
	    }
	}
	return 0;
}

