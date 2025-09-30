import heapq

### 최소 힙
heap = []

heapq.heappush(heap, 50)
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)

print(heap) # 리스트를 출력해야함 #[10, 50, 20]


#이미 생성해둔 리스트가 있다면 heapify 함수를 통해 즉각적으로 힙 자료형으로 변환할 수 있다.

heap2 = [50, 10, 20]

heapq.heapify(heap2)

print(heap2) #[10, 50, 20 ]

# 힙에서 원소 삭제 - 가장 작은 원소를 힙에서 제거함과 동시에 그를 결과값으로 리텅한다.
result = heapq.heappop(heap)
print(result) #10
print(heap) #[20, 50]

## 최대 힙

heap_items = [1,3,5,7,9]

max_heap = []

# 튜플형태로 집어넣어준다.
for item in heap_items:
    heapq.heappush(max_heap, (-item, item))

print(max_heap) #[(-9, 9), (-7, 7), (-3, 3), (-1, 1), (-5, 5)]