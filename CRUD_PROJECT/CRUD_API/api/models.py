from django.db import models
from account.models import User

class Blog(models.Model):
    #게시글 id값 => AutoField으로 자동 부여
    id = models.AutoField(primary_key=True, null=False, blank=False)
    #게시글 제목
    title = models.CharField(max_length=100)                          
    #게시글 작성 날짜 => 작성 시점을 자동으로 저장하기 위해 auto_now_add를 True로 설정
    created_at = models.DateTimeField(auto_now_add=True)              
    #게시글 작성 user => on_delete=models.CASCADE이면 user가 삭제되었을때 해당 게시글도 함께 삭제
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE) 
    #게시글 내용
    body = models.TextField() 