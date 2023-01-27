# API, REST API
웹개발을 하는 사람이라면 누구나 API, REST API, RESTful API라는 단어들을 접하게 된다. 많은 개발자들이 '그래서 도대체 API가 뭔데?' 하고 찾아보면 이해 못하는 말 투성이였던 경험을 했을거라 생각한다. 좌절감을 느꼈을 나의 동지분들을 위해 열심히 찾아보고 정리하였다. 이번엔 이해가 되는 말 투성이이길 바란다.
(틀린 내용이 있다면 언제든지 지적하고 알려주시면 감사하겠다 😄)

##  API
> API(Application Programming Interface) : 클라이언트, 서버와 같은 서로 다른 프로그램에서 요청과 응답(+데이터)을 주고 받을 수 있게 만든 체계.  
서버 개발자가 개발하고, 클라이언트 개발자가 사용.

- 클라이언트 관점 → 데이터를 다루는 요청의 4가지 요소(CRUD)
(Create: 올려줘!, Read: 불러와줘!, Update: 바꿔줘!, Delete: 지워줘!)
- 서버 관점 → 서버는 응답. 응답에는 '잘 됐어', '잘 안 됐어'라는 2가지 경우가 있음 .  
'잘 됐어', '잘 안 됐어'를 컴퓨터가 알아 듣기 위해 코드로 표현.
  - 잘 됐어': 200번대 코드  
  - '잘 안 됐어': 400번대(클라이언트 요청 문제), 500번대(서버 문제)  
## REST API  
### REST API 탄생 배경
CRUD요청은 각각의 주소를 가졌었다. 하지만 이로 인해 아래 예시처럼 주소가 많아지는 단점이 생겼다.  
  
장바구니 생성:    /cart/create  
장바구니 읽기:    /cart/read  
장바구니 업데이트: /card/update  
장바구니 삭제:    /cart/delete  
이를 해결하기 위해 더 체계적인 API를 만들고자 했고, 그 결과 REST API가 탄생했다.  

### REST API 란
>REpresentational State Transfer API  
자원(resource)의 표현(representation)에 의한 상태 전달을 뜻한다.  
자원 : 해당 소프트웨어가 관리하는 모든 것 ( 문서, 그림, 데이터, 해당 소프트웨어 자체 등 )  
표현 : 그 자원을 표현하기 위한 이름 ( DB의 학생 정보가 자원이면, 'students'를 자원의 표현으로 정함 )  
상태 전달 : 데이터가 요청되는 시점에 자원의 상태를 전달한다. ( JSON 혹은 XML을 통해 데이터를 주고 받는 것이 일반적 )  

**이해하기 쉽게 설명하자면 ...**

- 웹상에서 사용되는 여러 리소스를 HTTP URI로 표현하고 그 리소스에 대한 행위를 HTTP Method로 정의하는 방식. 즉, 리소스(HTTP URI로 정의된)를 어떻게 한다(HTTP Method + Payload)를 구조적으로 깔끔하게 표현하는 방식.  
예) GET /users/101 : 101번 째 user의 정보(resource)를 GET(method) 즉, 가져온다.
- API 시스템을 구현하기 위한 아키텍처 중에 가장 널리 사용되는 형식
- CRUD를 하나의 주소로 관리하기 위해, 요청을 보낼 때 CRUD에 해당하는 메소드를 붙여 함께 전송
  - Create : POST
  - Read : GET
  - Update : PUT(전체), PATCH(일부)
  - Delete : DELETE  

예) 장바구니 POST, GET, DELETE, PATCH를 localhost:8080 주소 하나로 관리  

![](https://velog.velcdn.com/images/tiger/post/f7bbd654-9bf4-46d1-8494-6aedc67607be/image.png)


### REST API 설계 규칙
1. 의미를 바로 알아볼 수 있도록 작성하고, 소문자를 사용한다.  
❌ GET /users/writing  
❌ GET /users/Post-Comments  
⭕ GET /users/post-comments  

2. URI가 길어지는 경우 언더바(_) 대신 하이픈(-)을 사용한다.  
❌ GET /users/profile_image  
⭕ GET /users/profile-image  

3. 마지막에 슬래시(/)를 포함하지 않는다.  
후행 슬래시(/)는 의미가 전혀 없고 혼란을 야기할 수 있다.  
❌ GET /users/  
⭕ GET /users  

4. 리소스에 대한 행위를 HTTP Method로 표현한다.  
URI에 HTTP Method가 포함되서는 안된다.  
❌ get/users/  
⭕ GET /users/  
resource는 동사가 포함되서는 안되고 명사를 사용한다.  
❌ GET /users/show/1  
⭕ GET /users/1  
5. 파일 확장자는 URI에 포함시키지 않는다.  
❌ GET /users/photo.jpg  
⭕ GET /users/photo (이때, payload의 포맷은 headers에 accept를 사용한다.)  

6. URI 사이에 연관 관계가 있는 경우 /리소스/고유ID/관계 있는 리소스 순으로 작성한다.  
❌ GET /users/profile/{user_id}  
⭕ GET /users/{user_id}/profile  

7. URI에 작성되는 영어를 복수형으로 작성한다.  
❌ GET /product  
⭕ GET /products  

8. URI는 / 구분자를 사용하여 자원의 계층 관계를 나타내는데 사용한다.

![](https://velog.velcdn.com/images/tiger/post/30a59e44-c8b0-4a3b-bb9a-b151b26878f2/image.png)


#### RESTful 하지 못한 API 설계 예시

![](https://velog.velcdn.com/images/tiger/post/f8020287-662e-4efb-9402-3193f6129161/image.png)

- 1, 2 → 의미 바로 알아볼 수 있도록
- 3, 4 → 동사 금지
- 5 → 특정할 수 없음
- 6 → 쿼리파라미터

## RESTful API
>RESTful한 API: REST의 설계 규칙을 잘 지켜서 설계된 API  
즉, REST의 원리를 잘 따르는 시스템을 RESTful이란 용어로 지칭