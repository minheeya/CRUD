# 자세한 실행 방법(endpoint 호출방법) & api 명세
------------
- 게시물 목록 조회 : GET / 생성: POST
- endpoint: localhost:8000/blog/
------------------
- 게시물 디테일 조회 GET / 수정 PUT / 삭제 DELETE
- endpoint: localhost:8000/blog/id 
- 위 endpoint의 id는 게시물 고유 값
---------------
- 회원가입 POST
- endpoint: localhost:8000/user/signup/
----------------
- 로그인 => 기존 장고 기능 활용
- endpoint: localhost:8000/user/api_auth/login/?next=/blog/


