#include <iostream>
using namespace std;

int main()
{
int t,i;
  cin>>t;
  for(i=0;i<t;i++)
  {
      int d,c;
      cin>>d>>c;
      int a1,a2,a3;
      cin>>a1>>a2>>a3;
      int b1,b2,b3;
      cin>>b1>>b2>>b3;
      int day1cost=0;
      day1cost=a1+a2+a3;
      int day2cost=0;
      day2cost=b1+b2+b3;
     int totalcost=day1cost+day2cost+d+d;
      int costwith;
      if(day1cost<150)
      {
      day1cost=day1cost+d;
      costwith=day1cost+day2cost+d+c;
      }
      if(day2cost<150)
      {
      day2cost=day2cost+d;
      costwith=day1cost+day2cost+d+c;
      }
      costwith=day1cost+day2cost+c;
      if(totalcost>costwith)
      {
      cout<<"yes"<<endl;
      }
      else
      cout<<"no"<<endl;
  }
  return 0;