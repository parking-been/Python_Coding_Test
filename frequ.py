from collections import Counter

print(Counter(["hi", "hey", "hi", "hi", "hello", "hey"]))
#Counter({'hi': 3, 'hey': 2, 'hello': 1})

print(Counter("hello world"))
#Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

#Counter를 dictionary 처럼 사용할 수 있다
# 대괄호를 이용하여 키로 값 읽기
counter = Counter("hello world")
print(counter["o"], counter["l"]) #(2, 3)

counter["l"] += 1
counter["h"] -= 1
print(counter) # Counter({'h': 0, 'e': 1, 'l': 4, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# Counter 클래스는 개수가 많은 순으로 정렬된 배열을 리턴함
# most_common
from collections import Counter

print(Counter('hello world').most_common())
# [('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]

#개수만큼 return
from collections import Counter

print(Counter('hello world').most_common(1))
# [('l', 3)]