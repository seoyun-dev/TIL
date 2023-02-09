## 1. Query parameter v.s. Path Variable

### 1) Query parameter

```python
/products?id=3 # Fetch a products that has id of 3
```

위에서 보는 것처럼 ? 뒤에  **`key=value`** 형식의 문자열이 붙는 방식이 Query parameter이다. 위에선 id란 변수에 3 이란 값을 담아 백엔드에 전달하는 것이다.  products에 담긴 정보 중 id 3번의 자료를 달라는 요청이다.

### 2) Path Variable

```python
/products/3 # Fetch a products that has id 3
```

위와 동일한 요청을 경로를 지정하여 요청할 수도 있는데 이것을 Path Variable이라고 한다.

### 3) Query parameter v.s. Path Variable
![](https://velog.velcdn.com/images/tiger/post/10dd0d5c-a04b-43cb-81d9-43953c138273/image.png)


- **우리가 어떤 자원(데이터)의 위치를 특정해서 보여줘야 할 경우 → Path variable**
- **정렬하거나 필터해서 보여줘야 할 경우 → Query parameter**

### 4) with HTTP Method

```python
/users                        # Fetch a list of users
/users?occupation=programer   # Fetch a list of programer user
/users/123                    # Fetch a user who has id 123
```

위의 방식으로 우리는 어디에 어떤 데이터(명사)를 요청하는 것인지 명확하게 정의할 수 있다. 하지만, 그 데이터를 가지고 뭘 하자는 것인지 동사는 빠져있다. 그 동사 역할을 하는 것이 GET, POST, PUT, DELETE 메소드이다.

즉, Query parameter와 Path variable이 이들 메소드와 결합함으로써 "특정 데이터"에 대한 CRUD 프로세스를 추가의 엔드포인트 없이 완결 지울 수 있게 되는 것인다.(가령, `users/create` 혹은 `users?action=create`를 굳이 명시해 줄 필요가 없다.)

```python
/users [GET]         # Fetch a list of users
/users [POST]        # Create new user
/users/123 [PUT]     # Update user
/users/123 [DELETE]  # remove user
```

물론 위와 같은 규칙을 지키지 않더라도 잘 돌아가는 API를 만들 수 있다. 하지만 지키지 않을 경우 서비스 엔드포인트는 복잡해 지고, 개발자간/외부와 커뮤니케이션 코스트가 높아져 큰 잠재적 손실을 초래할 수 있으니 이 규칙은 잘 지켜서 사용하는 것이 필수라 하겠다.

## 2. Path parameter 예시

![](https://velog.velcdn.com/images/tiger/post/a0f584e3-7dfb-43b5-bc39-925fc5695bf0/image.png)


![](https://velog.velcdn.com/images/tiger/post/7147de38-3f65-40d2-8399-c6dc3e9143dc/image.png)


## 3. Query parameter 예시

### 1) Filtering(필터링)

![](https://velog.velcdn.com/images/tiger/post/bf4c6186-45d6-47c1-97ae-eccb9f0692ae/image.png)


### 2) Ordering(정렬)

![](https://velog.velcdn.com/images/tiger/post/1a7f3d31-164d-400b-aa6d-c15f48baa941/image.png)


### 3) Pagination(쪽수 나누기)

![](https://velog.velcdn.com/images/tiger/post/f4b7b3a6-d4c7-448d-8778-3133df94f3ba/image.png)


### 4) Searching(검색)

![](https://velog.velcdn.com/images/tiger/post/a52f1854-4c2e-4eac-b798-281bab198512/image.png)


## 4. 실제 예시

[단편선](https://www.dpsnnn.com/reserve)

그없상 - 05부터 12까지 숫자 올릴때마다 한타임씩 미뤄짐

- 2월 12일 20:30 - [https://www.dpsnnn.com/reserve/?idx=11&day=2023-02-12](https://www.dpsnnn.com/reserve/?idx=11&day=2023-02-12)
- 2월 12일 22:00 - [https://www.dpsnnn.com/reserve/?idx=12&day=2023-02-12](https://www.dpsnnn.com/reserve/?idx=11&day=2023-02-12)