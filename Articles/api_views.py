from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from extensions.articles import topArticles
from .models import Articles,ArticlesLikes
from rest_framework import generics
from rest_framework import status
from django.db.models import Q
from .serializers import *




class articles_list(generics.ListAPIView):
    serializer_class = ArticlesSerializers

    def get_queryset(self):
        return Articles.objects.all().order_by('id')



class article_detail(generics.ListAPIView):
    serializer_class = ArticlesSerializers

    def get_queryset(self):
        id = self.request.query_params.get('id')
        slug = self.request.query_params.get('slug')
        return [get_object_or_404(Articles,id=id,slug=slug)]


class search_articles(generics.ListAPIView):
    serializer_class = ArticlesSerializers

    def get_queryset(self):
        q = self.request.query_params.get('q')
        return Articles.objects.filter(title__icontains=q).all().order_by('id')





class latest_articles(generics.ListAPIView):
    serializer_class = ArticlesSerializers

    def get_queryset(self):
        return Articles.objects.all().order_by('-id')[:5]


class top_articles(generics.ListAPIView):
    serializer_class = ArticlesSerializers

    def get_queryset(self):
        return Articles.objects.filter(id__in=topArticles())



class add_articles_comment(generics.CreateAPIView):
    serializer_class = ArticlesCommentsSerializers
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = ArticlesCommentsSerializers(data=request.data)
        if data.is_valid():
            user_token = str(request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            article_comment_check = ArticlesComments.objects.filter(user_id=token_info.user.id,article_id=data.validated_data['article'].id,status=False).first()
            if article_comment_check is None:
                ArticlesComments.objects.create(article_id=data.validated_data['article'].id,user_id=token_info.user.id,comment=data.validated_data['comment'],status=False)
                return Response({"message": "created"})
            else:
                return Response({"message": "has been created"},status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(data.errors)






class add_article_like(generics.CreateAPIView):
    serializer_class = ArticlesLikesializers
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = ArticlesLikesializers(data=request.data)
        if data.is_valid():
            article_id = data.validated_data['article'].id
            user_token = str(request.headers['Authorization']).split('Token')[1].strip()
            token_info = Token.objects.filter(key=user_token).first()
            print(article_id)
            check_like = ArticlesLikes.objects.filter(user_id=token_info.user.id, article_id=article_id).first()
            if check_like is None:
                add_like = ArticlesLikes.objects.create(user_id=token_info.user.id, article_id=article_id)
                return Response({"message": "created"})
            else:
                return Response({"message": "has been created"})
        else:
            return Response(data.errors)



