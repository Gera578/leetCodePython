import heapq

def findKthLargest(nums, k):
    # Create an empty min-heap
    min_heap = []
    
    # Process each number in the array
    for num in nums:
        heapq.heappush(min_heap, num)
        # If heap grows larger than k, remove the smallest element
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    # The root of the heap is the kth largest element
    return min_heap[0]

# Example usage:
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(findKthLargest(nums, k))  # Expected output: 5
