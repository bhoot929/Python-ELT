'''
nums1 = [1, 3]
nums2 = [2]

The median is 2.0

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''

def findMedianSortedArrays(self, nums1, nums2):
        new_list = sorted(nums1+ nums2)
        len_list = len(new_list)


        if(len_list%2==0):
            num =  len_list/2
            int_num = int(num)

            median = (new_list[int_num-1]+new_list[int_num]) / 2
        else:
            num =  (len_list+1) / 2
            int_num = int( num)
            median = new_list[int_num-1]
        return(median)
