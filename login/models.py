from django.db import models


class User(models.Model):
    """用户表"""

    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    # name必填，最长不超过128字符，唯一
    name = models.CharField(max_length=128, unique=True)
    # password必填，最长不超过256字符
    password = models.CharField(max_length=256)
    # sex只能选择男or女，默认为男
    sex = models.CharField(max_length=32, choices=gender, default='男')
    # create_time
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
