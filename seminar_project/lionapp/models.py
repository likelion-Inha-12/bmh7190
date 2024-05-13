from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=20,verbose_name="이름")
    email = models.EmailField(unique=True, verbose_name="이메일")

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(Member,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=50,verbose_name="제목") # 100글자가 최대인 문자열
    content = models.TextField(verbose_name="내용", null=True, blank=True) # 글자 수 제한이 없는 긴 문자열
    create_at = models.DateTimeField(auto_now_add=True,verbose_name="생성시간") # 처음 Post 생성시, 현재시간 저장
    def __str__(self):
        return self.title
    


class Comment(models.Model):
    content = models.CharField(max_length=200, null=True, blank=True)
    post_id = models.ForeignKey(Post, verbose_name="Post", on_delete=models.CASCADE,related_name="comments")
    member_id = models.ForeignKey(Member, verbose_name="Member", on_delete=models.CASCADE)
    

    def __str__(self):
        return self.content

class UserPost(models.Model):
    user_id = models.ForeignKey(Member, verbose_name="유저", on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, verbose_name="글", on_delete=models.CASCADE)