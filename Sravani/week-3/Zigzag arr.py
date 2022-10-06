class Solution:

	def zigZag(self,arr, n):
		# code here
		flag = 1
		for i in range(0,n-1):
		    if flag ==1:
		        if (arr[i]>arr[i+1]):
		            arr[i],arr[i+1] = arr[i+1],arr[i]
            else:
		        if (arr[i]<arr[i+1]):
		             arr[i],arr[i+1] = arr[i+1],arr[i]
            flag = not flag
		            