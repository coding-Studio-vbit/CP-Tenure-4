class Solution {
public:
    int maxArea(vector<int>& height)
    {
        int i=0;
        int j=height.size()-1;
        int max_area=0,m1;
        while(i<j)
        {
            m1=min(height[i],height[j])*(j-i);
            max_area=max(max_area,m1);
            height[i]<height[j]?i++:j--;
        }
        return max_area;
    }
};