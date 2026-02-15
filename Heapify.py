import heapq
arr = [1, 100, 27, 103, 109, 1, 2, 53, 2]
# Converting arr into a min-heap
heapq.heapify(arr)
print("Heapified array:", arr)
n = len(arr)
for i in range(n):
    parent = (i - 1) // 2 if i > 0 else None #For Parent Node
    left = 2 * i + 1 if 2 * i + 1 < n else None #For Left Child
    right = 2 * i + 2 if 2 * i + 2 < n else None #For Right Child
    print(f"Index {i}, Value {arr[i]}, Parent {parent}, Left {left}, Right {right}")
