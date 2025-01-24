
def canPlaceFlowers(flowers, n) -> bool:
    count = 0
    length = len(flowers)
    for flower in range(len(flowers)):
        if flowers[flower] == 0:
            previous = (flower==0) or (flowers [flower-1] == 0)
            next = (flower == length -1) or (flowers[flower + 1] == 0)
            
            if previous and next:
                flowers[flower] = 1
                count += 1
        if count >= n:
            return True
    return count >=n
            
flowers = [1,0,0,0,0,0,1]
n = 2
 
print(canPlaceFlowers(flowers, n))