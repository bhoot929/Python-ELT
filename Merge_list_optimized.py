#this code will merge two list optimized way.

'''Create an array arr3[] of size n1 + n2.
Simultaneously traverse arr1[] and arr2[].
Pick smaller of current elements in arr1[] and arr2[], copy this smaller element to next position in arr3[] and move ahead in arr3[] and the array whose element is picked.
If there are are remaining elements in arr1[] or arr2[], copy them also in arr3[].'''

a = [3, 4, 6, 10, 11, 18]
b = [1, 5, 7, 12, 13, 19, 21]

def mergearray(a,b):
    l1 = len(a)
    l2 = len(b)
    i=0
    j=0
    k=0
    final_array = [None]* (l1 + l2)
    while i < l1 and j < l2:
        if(a[i] < b[j]):
            final_array[k] = a[i]
            i = i+1
            k = k+1
        else:
            final_array[k] = b[j]
            j = j+1
            k = k+1
    print(final_array)
    
    #add remaining elements
    
    while i <l1  :
        final_array[k] = a[i]
        k = k+1
        i = i+1
    while j < l2:
        final_array[k] = b[j]
        k = k+1
        j = j+1
    print(final_array)

if __name__ == "__main__":
    mergearray(a,b)
