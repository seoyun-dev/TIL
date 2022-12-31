## 1. HTTP 정의 : HyperText Transfer Protocol
<span style="color:red">**HTTP**</span>는 **HTML파일<span style="color:red">(Hyper Text)</span>를 전송<span style="color:red">(Transfer)</span>하기 위한 컴퓨터끼리 어떻게 HTML파일을 주고 받을지에 대한 약속이자 애플리케이션 레이어의 프로토콜<span style="color:red">(Protocol)**</span>이다.  
여기서 모르는 단어, 프로토콜이다. 프로토콜은 무엇일까?  
**Protocol**은 **상호 합의된 규칙으로, 데이터 통신을 원활하게 하기 위해 필요한 통신 규칙**이다.  
HTTP는 신호 송신의 순서, 데이터의 표현법 등을 정한다.  
이 HTTP를 쉽게 풀어보면 "**나는 이렇게 줄 테니 넌 이렇게 받고 
난 너가 준거 이런 식으로 받을 수 있으니 참고해줘**"이다.  
## 2. HTTP의 두 가지 특징
### 2-1. HTTP request & HTTP response
![](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview/client-server-chain.png)  

![](https://velog.velcdn.com/images/tiger/post/bc3550b3-595d-43d4-a507-4e19395de815/image.png)

우리가 URL로 특정 사이트를 접속한다고 생각해보자.  
그 후에 일어나는 일을 간단하게 말하자면 아래 두 줄로 정리가 가능하다.
>브라우저: 서버님 html 주세요 <요청 request>  
서버: html 여기 있습니다 <응답 response>

무슨 말인지 모르겠다면 아래의 추가 설명을 보자.  
**< request >**  
그 사이트의 URL을 누름과 동시에 우리의 브라우저는 서버에게 html, css, js같은 파일을 달라고 요청한다.  
즉, 해당 사이트를 브라우저에 표현하기 위해 해당 사이트의 자료를 달라고 요청하는 것이다.  
**<  response >**  
'요청'받은 해당사이트 관련 자료들을 브라우저에게 '응답'으로 전달해주는 것이다.
### 2-2. stateless
**State(상태) + less(없음)**  
HTTP에 대한 설명 중 절대 잊어서는 안 될 HTTP의 특징이 바로 Stateless 이다. 문자 그대로 번역하면 State(상태) + less(없음) 을 의미한다.

각각의 HTTP 통신(요청/응답)은 독립적 이기 때문에 과거의 통신(요청/응답)에 대한 내용을 전혀 알지 못한다. 이전의 상태를 전혀 알지 못 한다는 것은 무엇을 의미할까?

예시로 stateful과 stateless의 카페를 들어보자.
![](https://velog.velcdn.com/images/tiger/post/1013df0d-f967-4ba7-be3d-4aac9fd36a85/image.png)
steateful할 때는 점원(서버)이 한 번 준 정보를 가지고 있어서, 전에 준 정보를 다시 줄 필요가 없다.  

![](https://velog.velcdn.com/images/tiger/post/e0b124b1-dc47-4735-901f-65c2e98b2582/image.png)  
하지만 stateless 통신의 점원은 전에 준 정보를 기억하지 못하므로, 매 통신마다 필요한 정보를 다시 보내줘야 한다.

따라서, 만일 여러번의 통신(요청/응답)의 진행과정에서 연속된 데이터 처리가 필요한 경우(ex. 온라인 쇼핑몰에서 로그인 후 장바구니 기능)를 위해 로그인 토큰 또는 브라우저의 쿠키, 세션, 로컬스토리지 같은 기술이 필요에 의해 만들어졌다.  

예로 Youtube를 들어보자.
![](https://velog.velcdn.com/images/tiger/post/c0e204ba-4558-42db-8a49-352a254613b5/image.png)  

유튜브 로그인페이지에서 로그인을 한 후, 메인페이지로 오면 실제로 서버는 클라가 로그인을 했다는 것을 기억하지 못한다. 
그러므로 내가 로그인한 후 메인페이지에서 영상을 보려고하면, 사용자는 다시 로그인이 되어있지 않은 상태가 되는 것이다.  
이러한 번거로움을 방지하기 위해 사용자가 로그인을 성공하면, 서버는 로그인을 성공했다라는 해당 서버 전용 토큰을 사용자에게 보내준다.  
그럼 사용자는 그 토큰을 저장소에 저장해두었다가 통신을 할 때 서버에게 같이 보내줌으로써, 중복된 정보를 전송하지 않게 해준다.  

 **stateful 사용 안 하는 이유**  
채팅같이 내용을 보존해야하는 것은 stateful을 사용한다.  
하지만 대부분의 서버에서 stateless를 사용하는 이유는 서버가 많은 데이터를 가지고 있으면 서버가 무거워지고, 그로 인해 요청을 빨리 처리하기 힘들기 때문이다.

## 3. Request/Response
### 3-1. HTTP request
이번엔 HTTP request를 자세히 뜯어보자.
Chrome의[개발자도구]-[검사]-[Network]탭 통해 브라우저와 서버가 통신하는 내용 감청이 가능하다.  

아래는 **HTTP request** 형식이다.  

![](https://velog.velcdn.com/images/tiger/post/868459f0-9013-4770-88cc-eacb5e6f0c04/image.png)  
1. **Start Line**: 요청의 첫번째 줄. 이 시작 줄도 세 부분으로 구성되어있다.
- HTTP Method
- Request target
- HTTP Version
2. **Headers**: 해당 요청에 대한 추가 정보(메타 데이터)를 담고있는 부분.  
- Host: 요청을 보내는 목표(타겟)의 주소. 즉, 요청을 보내는 웹사이트의 기본 주소가 된다. (ex. www.apple.co.kr)
- User-Agent: 요청을 보내는 클라이언트(웹 브라우저)의 대한 정보 (ex. chrome, firefox, safari, ~~explorer~~)
-Accept-Encoding: 웹 브라우저에서 가능한 압축방식. 서버는 브라우저가 알려준 압축방식들 중에서 가능한 압축방식을 골라서 사용한다.
- Content-Type: 해당 요청이 보내는 메세지 body의 타입 (ex. application/json)
- Content-Length: body 내용의 길이
- Authorization: 회원의 인증/인가를 처리하기 위해 로그인 토큰을 Authroization 에 담는다.
- If-Modified-Since: 현재 파일이 언제 마지막으로 다운받은 파일인지를 나타낸다.  
서버는 자신이 가지고 있는 파일과 비교하여 무엇이 더 최신인지 알아내고, 서버가 가지고 있는 것이 최신이면 서버의 파일을 브라우저에게 전송한다.
서버의 파일보다 브라우저의 파일이 최신이거나 같다면 불필요한 다운을 하지 않기 위해 전송하지 않는다. 
3. **Body**: 해당 요청의 실제 내용. 주로 Body를 사용하는 메소드는 POST이다.  
ex) 로그인 시에 서버에 보낼 요청의 내용
```python
Body: {
"user_email":"wecode@gmail.com" 
"user_password": "wecode"
}
```
아래는 HTTP request의 실제 예시이다. 보면서 이해해보자.
![](https://velog.velcdn.com/images/tiger/post/d069bc9e-9d54-4044-a50d-6eadafbdd7df/image.png)  

### 3-2. HTTP response
아래는 HTTP response의 형식이다.  

![](https://velog.velcdn.com/images/tiger/post/776fb4b9-36a9-4e9a-ada2-d1be3f35aff4/image.png)_(Header 부분의 User-Agent는 request 헤더에만 존재한다. 오타..)_

아래는 HTTP response의 실제 예시이다. 보면서 이해해보자.
![](https://velog.velcdn.com/images/tiger/post/806241c3-690c-48f7-8415-e6930c5062f9/image.png)

1. **Status Line**: 응답의 첫 번째 줄. 첫 줄은 버전 상태코드와 상태 메세지로 구성되어 있다.
- HTTP Version: 요청의 HTTP버전과 동일
- status code: 응답 결과(상태코드)
- phrase: 응답 결과를 사람이 이해하기 쉽도록 말로 풀어쓴 것
  
2. **Headers**: 요청의 헤더와 동일. 응답의 추가 정보를 담고 있다.
- 응답에서만 사용되는 헤더의 정보들이 있다. (ex. 요청하는 브라우저의 정보가 담긴 User-Agent 대신, Server 헤더가 사용된다.)

3. **Body**: 요청의 Body와 일반적으로 동일
- 요청의 메소드에 따라 Body가 항상 존재하지 않듯이 응답도 응답의 형태에 따라 데이터를 전송할 필요가 없는 경우엔 Body가 없을 수도 있다.
- 가장 많이 사용되는 Body 의 데이터 타입은 JSON(JavaScript Object Notation/JS 객체 문법을 따르는 문자 기반의 데이터 포맷) 이다.
- 로그인 요청에 대해 성공했을 때 응답의 내용
```python
Body: {
    "message": "SUCCESS"
    "token": "kldiduajsadm@9df0asmzm" 
    (암호화된 유저의 정보)
}
```
 ## 4. HTTP Request Methods
프론트엔드에서 요청의 의도를 담기 위해선 어떻게 해야할까?   
바로 **HTTP 요청 메서드(Http Request Methods**)를 이용하면 된다. 대표적인 HTTP요청 메서드를 살펴보자.
- **GET** : 자료를 **요청**
데이터를 서버로부터 받아올 때 사용. 
데이터를 받아오기만 할 때 사용된다.
> e.g. 장바구니에 담은 제품을 조회한다.

- **POST** : 자료의 **생성**을 요청
데이터 생성 수정에 사용하므로 대부분 body가 포함되어 보내진다.
> e.g. 장바구니에 맘에 드는 상품을 담는다.

- **PUT(전체), PATCH(일부)** : 데이터의 **수정**을 요청
- **DELETE** : 서버 데이터의 **삭제**를 요청
> e.g. 장바구니에서 제품을 삭제한다.

## 5. HTTP 상태코드
상태 코드에는 굉장히 많은 종류가 있지만, HTTP 상태 코드는 크게 다섯 부류로 나눌 수 있다.
1.  **1XX (조건부 응답)** : 요청을 받았으며 작업을 계속한다.
2. **2XX (성공)** : 클라이언트의 요청을 성공적으로 처리했음을 가리킨다.
- 200: OK
가장 자주 보게되는 Status Code  
문제없이 요청에 대한 처리가 백엔드 서버에서 이루어지고 나서 오는 응답코드
- 201: Created  
무언가가 잘 생성되었을 때에(Successfully Created) 오는 Status Code.  
대게 POST 메소드의 요청에 따라 백엔드 서버에 데이터가 잘 생성 또는 수정 되었을 때에 보내는 코드
- 204: No Content  
요청이 성공했으며 제공할 응답메세지가 없을 경우 사용하는 Status Code  
주로 DELETE 메소드의 요청으로 성공적으로 삭제되어서 응답으로 제공할 컨텐츠가 없을 때 사용
3. **3XX (리다이렉션 완료)** : 클라이언트는 요청을 마치기 위해 추가 조치가 필요하다.  
4. **4XX (요청 오류)** : 클라이언트에 오류가 있음을 나타낸다.
- 400: Bad Request  
해당 요청이 잘못되었을 때 보내는 Status Code  
주로 요청의 Body에 보내는 내용이 잘못되었을 때 사용되는 코드  
ex) 전화번호를 보내야 하는데 숫자가 아닌 문자열의 주소가 대신 Body에 담겼을 경우
- 401: Unauthorized  
유저가 해당 요청을 진행하려면 먼저 로그인을 하거나 회원가입이 필요하다는 의미를 나타내는 Status Code  
ex) wish list, 좋아요 기능은 회원이 아니면 요청을 보낼 수 없음.
- 403: Forbidden  
유저가 해당 요청에 대한 권한이 없다는 의미를 나타내는 Status Code  
접근 불가능한 정보에 접근했을 경우  
ex) 오직 유료회원만 접근할 수 있는 데이터를 요청 했을 때
- 404: Not Found  
요청된 URI 가 존재하지 않는다는 의미를 나타내는 Status Code  
5. **5XX (서버 오류)** : 서버가 유효한 요청을 수행하는 것에 실패했다.  
-  500: Internal Server Error  
서버에서 에러가 났을 때의 Status Code
## 6. HTTP vs. HTTPS
**HTTP**가 처음 나왔을 땐, 세상은 아직 통신으로 많은 정보들을 나누지 않았다. 
그래서 HTTP는 **암호화 기능을 가지고 있지 않았다**.  
하지만 지금은 군사, 금융, 사생활 등 중요한 정보들을 통신으로 주고 받는다.  
만약 현재 HTTP를 사용하여 통신한다면 어떻게 될까?  
'HTTP를 이용한다'의 위험성을 쉽게 말하자면,
'누군가 우리가 통신을 통해 주고받는 데이터를 들여다볼 수 있다'는 것이다.  

이를 막기 위해 HTTPS가 탄생했다. 그렇다면 HTTPS란 무엇일까?  
**HTTPS = HTTP over Secure socket layer**로 **HTTP에 데이터 암호화가 추가된 프로토콜로, 
안전한 HTTP**라고 볼 수 있다.
(Secure Socket Layer(SSL): 데이터를 암호화하여 인터넷 연결을 보호하기 위한 표준 기술)  
즉, HTTP와 달리 HTTPS로 통신하고 있는 우리를 누가 들여본다고 해도 
데이터가 암호화가 되어있어 무슨 내용인지 알 수 없다.

## 7. HTTP 통신 모니터링 도구
- developer tools > Network
- Wireshark

## ➕ 추가로 공부하면 좋은 것들
- **Cache**  
cache는 **어떤 웹사이트에 접속했을 때 이미 다운 받은 파일을 읽어 성능을 향상시키는 기법**이다.   
cache의 문제점은 내용이 갱신되었을때도 웹브라우저가 그 사실을 알아차리지 못한다는 것이다.  
이 때, 윈도우: ctrl+f5, mac: cmd+r, linux:f5 을 누르면 캐시가 갱신된다.
- **cookie**  
우리는 이용했던 사이트에 다시 들어갔을 때 로그인 혹은 장바구니의 상태가 유지되어 있음을 자주 볼 수 있다.  
이게 가능한 이유는 무엇일까?  
사이트에 로그인을 했었던 기록, 예전에 했던 장바구니 담기 등의 기록들을 
웹사이트와 웹 브라우저가 기억하고있기 때문이다.  
이걸 가능하게 하는 것이 **쿠키**다.
HTTP 쿠키(웹 쿠키, 브라우저 쿠키)는 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각이다.   
쿠키값을 웹브라우저에 설정하면 그걸 서버에 전송함으로 인해 사용자 상태를 저장하고 식별이 가능해진다.
## 📑 참고 자료
[생활코딩 - HTTP](https://opentutorials.org/course/4848)  
[Wikipedia - HTTP 상태코드](https://ko.wikipedia.org/wiki/HTTP_%EC%83%81%ED%83%9C_%EC%BD%94%EB%93%9C)  
[MDN Web Docs - HTTP](https://developer.mozilla.org/ko/docs/Web/HTTP)  
https://joshua1988.github.io/web-development/http-part1/
https://www.zerocho.com/category/HTTP/post/5b344f3af94472001b17f2da  
https://velog.io/@surim014/HTTP%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80  
wecode 2주차 자료