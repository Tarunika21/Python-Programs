class solution:
    def twosum(self,list,target):
        list.sort()
        left = 0
        right = len(list)-1
        tempsum =0
        while left<right:
            tempsum = list[left]+list[right]
            if tempsum == target:
                return [left,right]
            elif tempsum<target:
                left+=1
            else:
                right-=1
        return [-1,-1]
    
n = int(input("Enter the number of elements:"))
list = []
for i in range(n):
    ele = int(input())
    list.append(ele)
target = int(input("Enter the target:")) 
obj = solution()
print(obj.twosum(list,target))

