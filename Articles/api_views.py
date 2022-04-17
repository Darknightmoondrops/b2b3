from rest_framework.decorators import api_view,permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from extensions.articles import topArticles
from rest_framework.response import Response
from .models import Articles,ArticlesLikes
from rest_framework import status
from django.db.models import Q
from .serializers import *



@api_view(["GET"])
def articles_list(request):
    paginator = PageNumberPagination()
    paginator.page_size = 12
    articles = Articles.objects.all().order_by('id')
    result_page = paginator.paginate_queryset(articles, request)
    data = ArticlesSerializers(result_page,many=True).data
    return paginator.get_paginated_response(data)

@api_view(["GET"])
def search_articles(request):
    try:
        q = request.GET['q']
        articles = Articles.objects.filter(Q(title__icontains=q)).all().order_by('id')
        paginator = PageNumberPagination()
        paginator.page_size = 12
        result_page = paginator.paginate_queryset(articles, request)
        data = ArticlesSerializers(result_page, many=True).data
        return paginator.get_paginated_response(data)
    except:
        return Response({'message': 'error'},status=status.HTTP_400_BAD_REQUEST)





@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_articles_comment(request):
    data = ArticlesCommentsSerializers(data=request.data)
    if data.is_valid():
        user_token = str(request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        article_comment_check = ArticlesComments.objects.filter(user_id=token_info.user.id,article_id=data.validated_data['article'].id,status=False).first()
        if article_comment_check is None:
            ArticlesComments.objects.create(article_id=data.validated_data['article'].id,user_id=token_info.user.id,comment=data.validated_data['comment'],status=False)
            return Response({"message": "created"})
        else:
            return Response({"message": "has been created"})

    else:
        return Response(data.errors)





@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_article_like(request):
    try:
        article_id = request.POST['id']
        user_token = str(request.headers['Authorization']).split('Token')[1].strip()
        token_info = Token.objects.filter(key=user_token).first()
        check_like = ArticlesLikes.objects.filter(like_id=token_info.user, article_id=article_id).first()
        if check_like is  None:
            add_like = ArticlesLikes.objects.create(like_id=token_info.user, article_id=article_id)
            return Response({"message": "created"})
        else:
            return Response({"message": "has been created"})
    except:
        return Response({"message": "error"},status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET"])
def latest_articles(request):
    articles = Articles.objects.all().order_by('-id')[:5]
    data = ArticlesSerializers(articles,many=True).data
    return Response(data)

@api_view(["GET"])
def top_articles(request):
    articles = Articles.objects.filter(id__in=topArticles())
    data = ArticlesSerializers(articles,many=True).data
    return Response(data)