from django.db import models

# Create your models here.
class Users(models.Model):
    uphone = models.CharField(max_length=11,verbose_name="手机号")
    upwd = models.CharField(max_length=50,verbose_name='密码')
    uemail = models.CharField(max_length=245,verbose_name='邮箱')
    uname = models.CharField(max_length=20,verbose_name='姓名')
    isActive = models.BooleanField(default=True)
    def __str__(self):
        return self.uname

    class Meta:
        db_table = 'users'
        verbose_name = "用户"
        verbose_name_plural = verbose_name
