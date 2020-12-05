# django-rest-framework
 django-rest-framework tutorial

<br>

# REST ?
#### URL과 Http Method 를 사용하여 API 사용 가독성을 높인 구조화된 시스템 아키텍쳐

Representational status transfer의 약자로, 소프트웨어 프로그램 개발의 아키텍쳐의 한 형식이다. 

직역하면 '대표적인 상태 전달'... 무슨 말인지 와닿지가 않는데, 쉽게 정의하자면 '무언가'를 주고받는 제약 조건의 집합(프로토콜, 약속) 이라고 할 수 있다. 
RESTful이란, '무언가'를 주고 받을 때의 약속(프로토콜) 을 정의하고, 그것이 완벽히 이행되었을 때 그 상태를 RESTful 하다라고 한다. 

그렇다면 여기서 말하는 '무언가'는 무엇이며, 어떻게 주고 받는 것일까? 

## REST 의 구성 
- Resource (자원) : URL
- Verb (행위) : Http Method (GET, POST, PUT, DELETE)
- Representation (표현) : 데이터의 형태 (json, xml, ...)

URL과 Http Method 가 주어지면, 그에 대한 결과를 데이터의 형태에 맞추어 응답하는 방식으로 동작한다. 

## 왜 REST 인가? 
스마트폰의 탄생 이전 많은 IT 기업들은 웹 페이지를 사용자에게 렌더하기 위한 웹 서버만을 필요로 했다. 
그 웹 서버에서 DB 서버의 데이터를 읽어오거나(GET), DB 서버에 데이터를 저장, 수정, 삭제하는(POST, PUT, DELETE) 기능을 모두 담당했다. 

하지만 스마트폰 출시 이후 어플리케이션의 등장으로 더 이상 웹으로만은 서비스를 제공할 수 없었다. 
**즉, HTML로 렌더링하는 웹 서버가 아닌, JSON 혹은 XML과 같은 형식을 통해 데이터를 다루는 별도의 API 서버가 필요해진 것이다.** 

(스마트폰 어플과 웹에서 동일한 기능을 제공하는데 기존의 웹서버를 계속 사용하면 매번 HTML을 읽어서 해당 태그에 있는 정보를 찾아내는 비효율적인 프로세스를 준용하여야 하기 때문이다.)

따라서 RESTful한 아키텍쳐를 HTTP method와 함께 사용하여 웹, 앱, 데스크탑, 스마트폰 어플들까지 범용 가능한 하나의 API를 선호하게 되었다.


Django 또한 View 클래스 자체가 RESTful 한 서버를 만들기에 최적인 프레임워크이다. 

<br>

# DRF (Django Restful Framework) ?  
Django 안에서 RESTful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리이다. 


## DRF의 장점
1. Front-end와 Back-end의 완벽한 분리가 가능하다. (생산성 향상)
2. 코드의 재사용성 증가 (서로 다른 웹 페이지에서 동일한 API 호출이 가능=> 범용성, 멀티 플랫폼으로의 확장)
3. 인증 정책에 OAuth1, OAuth2 를 위한 추가적인 패키지가 추가되어 있는 경우
4. Serialize(시리얼라이즈) 기능을 제공해준다. (DB data -> JSON)

그 중 4번째, **Serialize** 야말로 DRF의 가장 매력적인 기능이라고 할 수 있다. 
Serializer란 DRF에서 직렬화를 담당하는 클래스로, queryset, model instance등의 복잡한 데이터를 python datatype으로 변환시켜 json, xml등의 컨텐츠 타입으로의 변환을 쉽게 만들어준다.

<br>


# And More.. 
1. [[JWT] 토큰 기반 인증에 대한 소개](https://velopert.com/2350)
2. [[JWT] JSON Web Token 소개 및 구조](https://velopert.com/2389)
3. [sentry로 에러탐지](https://velog.io/@lemontech119/DRF%EB%A1%9C-api-%EC%84%9C%EB%B2%84-%EA%B0%9C%EB%B0%9C7-%EC%97%90%EB%9F%AC%ED%83%90%EC%A7%80)

<br>

### References :
1) https://velog.io/@ifyouseeksoomi/DRF-Django-REST-Framework-%EA%B0%84%EB%8B%A8%ED%95%9C-%EC%98%88%EC%8A%B5-Serializer
2) https://butter-shower.tistory.com/50
3) https://blog.naver.com/pjok1122/221610282758


