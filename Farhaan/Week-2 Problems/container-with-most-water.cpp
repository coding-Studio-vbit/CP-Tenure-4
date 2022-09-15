class Solution {
public:
int maxArea(vector<int>& height) {
	int n=height.size();
	int maxx=0,left = 0,right=n-1;
	while(left<right){
		
		int area = abs(left-right)*min(height[left],height[right]);
		
		if(height[left]<=height[right]){
			left++;
		}else
			right--;
			//cout<<left<<" "<<right<<" "<<area<<endl;
		maxx = max(area,maxx);
	}
	return maxx;

	}
};

