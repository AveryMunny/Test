#O(1)
#array
nums = [1,2,3]
nums.append(4)  #push to end
nums.pop() #pop from end
nums[0]  #lookup
nums[1]
nums[2]

#Hashmap
hashMap = {}
hashMap["key"] = 10 #insert
print("key" in hashMap) #lookup
print(hashMap["key"]) #lookup
hashMap.pop("key") #remove

#O(n)
nums = [1,2,3]
sum(nums) #sum of array
for n in nums: #looping
    print(n)

nums.insert(1,100) #inserting 100 in the middle
nums.remove(100) #removing 100
print(100 in nums) #searching

import heapq
heapq.heapify(nums) #building a heap

#sometimes even nested loops can be O(n)
# (e.g. monotonic stack or sliding window)

#O(n^2)
#traverse a square grid 
nums = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(nums)):
    for j in range(len(nums)):
        print(nums[i][j])

#get every pair of elements in the array
nums = [1,2,3]
for i in range(len(nums)):
    for j in range(len(nums)):
        print(nums[i], nums[j])

#insertion sort (insert in middle n times-> n^2)

#O(n*m)
#get every pair of elements from two arrays
nums1, nums2 = [1,2,3],[4,5]
for i in range(len(nums1)):
    for j in range(len(nums2)):
        print(nums1[i], nums2[j])