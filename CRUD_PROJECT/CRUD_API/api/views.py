from .models import Blog
from .serializers import BlogSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly


# Blog의 CRUD모두 가능
class BlogViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication, SessionAuthentication]   # authentication 추가
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]     # permission 추가
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
   
   	# serializer.save() 재정의
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)