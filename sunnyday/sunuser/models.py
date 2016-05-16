# coding=utf-8
import uuid
import logging
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from utils.md5util import md5


class Job(models.Model):
    name = models.CharField('职业', max_length=20, blank=True, null=True, default='')

    def __unicode__(self):
        return self.name


class User(models.Model):
    username = models.CharField('用户名', max_length=50, blank=True, null=True, default='')
    nickname = models.CharField('昵称', max_length=20, blank=True, null=True, default='')
    password = models.CharField('密码', max_length=100, blank=False, null=False)
    email = models.CharField('邮箱', max_length=50, blank=True, null=True, default='')
    avatar = models.URLField('头像', blank=True, null=True, default='')
    mobile = models.CharField('移动电话', max_length=20, blank=True, null=True, default='')
    birthday = models.DateTimeField(default=timezone.now)
    gender = models.CharField('性别', max_length=10, default='男')
    QQ = models.CharField('QQ', max_length=50, blank=True, null=True, default='')
    weChat = models.CharField('微信', max_length=50, blank=True, null=True, default='')
    microBlog = models.CharField('微博', max_length=50, blank=True, null=True, default='')
    douban = models.CharField('豆瓣', max_length=50, blank=True, null=True, default='')
    country = models.CharField('目前所在国家', max_length=50, blank=True, null=True, default='中国')
    province = models.CharField('目前所在省', max_length=50, blank=True, null=True, default='北京')
    city = models.CharField('目前所在城市', max_length=50, blank=True, null=True, default='北京')
    ctime = models.DateTimeField(auto_now_add=True)
    utime = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    enable = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    pw_salt = models.CharField('密码盐', max_length=100, blank=False, null=False, default='')
    token = models.CharField('登录token', max_length=100, blank=True, null=True, default='')
    token_utime = models.DateTimeField('登录token更新时间', default=timezone.now)
#    job = models.ForeignKey(Job, blank=True, null=True, )
    uid = models.CharField('唯一识别id', max_length=50, blank=True, null=True, default='')
    sign = models.CharField('个性签名', max_length=200, blank=True, null=True, default='')

    def __unicode__(self):
        return self.username

    def set_password(self, pw):
        # 从客户端接收的密码就已经是md5后的密码
        salt = str(uuid.uuid4())
        encrypt_pw = md5(str(salt + pw))
        self.pw_salt = salt
        self.password = encrypt_pw

    def verify_password(self, input_pw):
#    	return self.password is input_pw
        encrypt_input_pw = md5(str(self.pw_salt + input_pw))
        return encrypt_input_pw == self.password

    def save_user(self, user_type=0):
        self.uid = str(uuid.uuid4())
        self.job_id = 1
        self.save()
        user_roles = UserRoles()
        user_roles.user_id = self.id
        if user_type == 0:  # 普通用户
            user_roles.roles_id = 1
        user_roles.save()

    def login(self):
        self.token = str(uuid.uuid4())
        self.token_utime = timezone.now()
        self.save()

    def verify_token(self, token):
        # 后续加上token过期判断,根据token_utime判断是否过期
        return token is self.token

    def as_json(self):
#        job = self.job.name if self.job else ''
        return dict(id=self.id, username=self.username, nickname=self.nickname,password=self.password,
                    token=self.token, avatar=self.avatar, gender=self.gender,
                    mobile=self.mobile, QQ=self.QQ, weChat=self.weChat,
                    user_id=self.uid, sign=self.sign)


class Roles(models.Model):
    description = models.CharField('角色描述', max_length=20, blank=False, null=False, default='')

    def __unicode__(self):
        return self.description


class Permission(models.Model):
    description = models.CharField('权限描述', max_length=20, blank=False, null=False, default='')

    def __unicode__(self):
        return self.description


class ThirdPartyRelation(models.Model):
    user = models.ForeignKey(User)
    third_party_id = models.CharField('三方登录识别id', max_length=50)
    third_party_type = models.IntegerField()  # 1qq2wexin3weibo


class UserRoles(models.Model):
    user_id = models.IntegerField()
    roles_id = models.IntegerField()


class RolesPermission(models.Model):
    roles_id = models.IntegerField()
    permission_id = models.IntegerField()
