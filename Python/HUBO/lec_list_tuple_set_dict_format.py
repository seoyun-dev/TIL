###################### 리스트
print("============리스트===============")
list1 = [1, 2, 3, 4, 'a', 'b']
list2 = [3, 1, 2, 0]
# 변경
list1[0] = 'hi'
print(list1)

# 내장 함수 len sum max
print("list1 길이:", len(list1))
print("list2 합:", sum(list2))
print("list2 max값:", max(list2))

# 슬라이싱
list3 = [1, 2, 3, 4, 5, 6]
print(list3[-1])
print(list3[2:])

# 리스트 메소드
l = [2, 3, 5, 4, 5]
l.append(6)             # 끝에 6 추가
l.insert(1, 0)          # index 1 자리에 0 추가
print(l)

l.pop()                 # 마지막꺼 삭제
l.pop(2)                # index 2를 삭제
print(l)

l.remove(5)             # 처음 만난 5 삭제
print(l)

l.append(5)
print(l.index(4))       # 처음 발견된 숫자 4의 index 반환

a = [2, 3, 2, 3, 4, 4, 5]
print(a.count(3))       # 숫자 3의 개수 반환
a.extend([7, 8])        # 이어붙이기 
print(a)
a.reverse()             # 역순 정렬
print(a)
a. sort()               # 오름차순 정렬
print(a)



###################### 튜플
# 리스트와 튜플은 매우 비슷 (서로 형변환 가능)
# 차이점: 튜플은 값 변경 X
print("============튜플===============")
t = (1, 3, 2, 'a')
print(t[-1])



###################### 집합(set)
# 중복되는 요소 제거, 순서가 없음
print("============집합(set)===============")

# 집합 생성
odds = {1, 3, 5, 7, 9}
emptyset = set() # 빈 집합 생성

# 자료형 변환
print(set("Good morning!"))
print(set([1, 3, 5, 6, 7]))

# 순서가 없으므로 인덱싱 불가 -> in 사용
nums = {1, 2}
print(3 in nums)
print(2 in nums)
for num in nums:
    print(num)

# 메소드
print(odds)
odds.add(11)                    # 숫자 11 추가
odds.remove(3)                  # 숫자 3 제거
print("pop:",odds.pop())       # 임의 값 pop 후 반환
print(odds)

# {5, 7, 9, 11}
print(odds.intersection({5, 6, 7}))   # {5,6,7}과 교집합 반환
print(odds.union({5,6,7}))            # 합집합
print(odds.difference({5,6,7}))       # odds - {5, 6, 7}




###################### 사전(dict)
# key, value 구조 (key는 값 변경 불가)
# 순서 X
print("============사전(dict)===============")

# 빈 딕셔너리 생성
d1 = dict()
d1 = {}

# 값 변경 및 생성
majors = {"CS" : "Computer", "EE" : "Electrical Engineering", "ME": "Mechanical Engineering"}
print(majors['EE'])
majors["CS"] = "Compute Science"    # 값 변경
majors["PH"] = "physics"            # 값 생성
print(majors)

# 메소드
print(len(majors))              # majors의 길이
print("ME" in majors)           # key 존재 유무 반환
print(majors.get("CS"))         # "CS" Key의 value 반환
print(majors.keys())            # key 값들 리스트로 반환
print(majors.values())          # value 값들 리스트로 반환
print(majors.items())           # key, value 값들 리스트로 반환
del majors['PH']                # 'PH' key에 해당하는 key-value 삭제
print(majors)

# loop 실행
print("-----dict loop-----")
for key in majors:
    print("%s is %s" % (key, majors[key]))
for key, value in majors.items():
    print("%s is %s" % (key, value))



################# 포맷팅
list = [1, 2.0, 3]
print("첫번째는 " + str(list[0]) + "야.")
print("첫번째는 %d 이고 두번째는 %g 야." % (list[0], list[1]))      # %d 정수, %g 실수, %.2f 소숫점둘째자리의 실수, %s 문자열
print("우선 리스트는 {}개고 리스트의 세번째 값은 {}야.".format(1, list[2]))