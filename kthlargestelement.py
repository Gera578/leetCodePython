class Solution:
    # This function partitions the array segment between indices 'first' and 'last'
    # so that all elements less than the pivot are to its left,
    # and all elements greater than or equal to the pivot are to its right.
    def partition(self, arr, first, last):
        # Choose the pivot element as the last element in the segment.
        pivot = arr[last]
        
        # 'smallest_element' marks the index where the next element smaller than
        # the pivot should be placed. It starts at 'first'.
        smallest_element = first
        
        # Iterate over the array segment (excluding the pivot)
        for j in range(first, last):
            # If the current element is less than the pivot,
            # swap it with the element at the 'smallest_element' index.
            if arr[j] < pivot:
                arr[j], arr[smallest_element] = arr[smallest_element], arr[j]
                # Move the boundary to the right.
                smallest_element += 1
        
        # After processing, swap the pivot element with the element at the boundary.
        # This puts the pivot in its correct sorted position.
        arr[smallest_element], arr[last] = arr[last], arr[smallest_element]
        
        # Return the index where the pivot is now located.
        return smallest_element
    
    # This function implements the QuickSelect algorithm to find the kth smallest
    # element in the array segment between indices 'first' and 'last'.
    def quickSelect(self, arr, first, last, k):
        if first <= last:
            # Partition the array and get the pivot index.
            pivotId = self.partition(arr, first, last)
            
            # Calculate the number of elements in the left partition,
            # including the pivot itself.
            leftCount = pivotId - first + 1
            
            # If the left partition contains exactly k elements,
            # then the pivot element is the kth smallest.
            if leftCount == k:
                return arr[pivotId]
            # If there are more than k elements in the left partition,
            # the kth smallest element is in the left partition.
            elif leftCount > k:
                return self.quickSelect(arr, first, pivotId - 1, k)
            # Otherwise, the kth smallest is in the right partition.
            # Adjust k by subtracting the number of elements in the left partition.
            else:
                return self.quickSelect(arr, pivotId + 1, last, k - leftCount)
        # In case the segment is invalid, return None.
        return None
        
    # This function finds the kth largest element in the list 'nums'.
    # It converts the problem into finding the (n - k + 1)th smallest element,
    # because the kth largest is the same as the (n - k + 1)th smallest.
    def findKthLargest(self, nums: list[int], k: int) -> int:
        n = len(nums)
        # Convert kth largest to kth smallest order.
        kth_smallest_order = n - k + 1
        # Call quickSelect to find the kth smallest element in the entire array.
        return self.quickSelect(nums, 0, n - 1, kth_smallest_order)

# Example usage:
solution = Solution()
nums = [3, 2, 1, 5, 6, 4]
k = 2

# Expected output: 5 (because 5 is the 2nd largest element in the array)
print(solution.findKthLargest(nums, k))
