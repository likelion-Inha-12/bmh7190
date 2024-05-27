from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self, userid, email, name, generation, gender, password=None):
        user =self.model(
            userid = userid,
            email = self.normalize_email(email),
            name = name,
            generation = generation,
            gender = gender
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, userid, email, name, generation, gender, password):
        user = self.create_user(
            userid,
            email,
            name=name,
            password=password,
            generation=generation,
            gender = gender
            
        )

        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    GENDER_CHOICES = [
        ('M','Male'),
        ('F', 'Female'),
    ]

    userid = models.CharField(max_length=10, verbose_name='아이디',unique=True)
    email = models.EmailField(
        verbose_name='email',
        max_length=100,
        unique=True,
    )
    name = models.CharField(max_length=30)
    generation = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'userid'
    REQUIRED_FIELDS = ['name','email','generation','gender']

    def __str__(self):
        return self.userid

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
    class Meta:
        db_table = 'user' # 테이블명을 user로 설정