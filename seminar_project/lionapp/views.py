import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import *

def create_post(request):

    if request.method == 'POST':
        data = json.loads(request.body)

        title = data.get('title')
        content = data.get('content')

        post = Post(
            title = title,
            content = content
        )
        post.save()
        return JsonResponse({'message':'success'})
    return JsonResponse({'message':'POST 요청만 허용됩니다.'})
    


def get_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # 원하는 pk값이 있으면 Post, 없으면 404

    data = {
        'id' : post.pk,
        '제목' : post.title,
        '내용' : post.content,
        '메세지' : '조회 성공'
    }

    return JsonResponse(data, status = 200)


def delete_post(request, pk):
    if request.method == 'DELETE':
        post = get_object_or_404(Post, pk = pk)
        post.delete()
        data = {
            "message" : f"id: {pk} 포스트 삭제 완료"
        }
        return JsonResponse(data, status = 200)
    return JsonResponse({'message':'DELETE 요청만 허용됩니다.'})

# 심화과제 1
def like_post(request, user_id, post_id):
    
    # 사용자와 게시물을 가져오기
    user_id = get_object_or_404(Member, pk=user_id)
    post_id  = get_object_or_404(Post, pk=post_id)

    # 사용자가 게시물에 좋아요를 남겼는지 확인
    # .filter(user_id=user_id, post_id=post_id) : url로 넘어온 user_id와 post_id와 일치하는 객체를 선택
    # .exists() : 쿼리셋이 비어있는지 확인 / 존재한다면 = True 반환 , 없다면 False 반환
    existing_like = UserPost.objects.filter(user_id=user_id, post_id=post_id).exists()
    if existing_like:
        return JsonResponse({'message' : '좋아요가 이미 눌렸습니다.'}, status = 400)

    # 사용자가 좋아요를 남기지 않았다면 / UserPost를 통해 좋아요라는 객체를 생성
    like = UserPost.objects.create(user_id = user_id, post_id = post_id)

    return JsonResponse({'message' : '좋아요가 눌렸습니다.'}, status = 200)

# 심화과제 2
def like_count(request, post_id):

    like_count = UserPost.objects.filter(post_id = post_id).count()

    return JsonResponse({'like_count' : like_count})

# 심화과제 3
def sort_posts(request):

    # 댓글이 많이 달린 순으로 포스트를 정렬
    # Post.object : Post 모델의 데이터베이스 테이블에 대한 추가 쿼리 수행
    # .annotate(comment_count=models.Count('comments')) : Post 객체들에 대한 추가적인 필드 구성 -> 댓글 수
    # .order_by('-comment_count') : comment_count를 기준으로 내림차순 정렬

    sorted_posts = Post.objects.annotate(comment_count=models.Count('comments')).order_by('-comment_count')

    # 포스트를 리스트로 변환하여 반환
    post_list = [{'title': post.title, 'content': post.content, 'author': post.author.name, 'comment_count': post.comment_count} for post in sorted_posts]
    
    return JsonResponse({'comment_list': post_list})