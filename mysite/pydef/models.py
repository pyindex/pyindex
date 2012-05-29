#-*- coding: utf-8 -*-
from django.db import models

# �����������ݴ洢
class func(models.Model):
	fname 			= models.CharField(max_length = 80)		# �������� ����ĸ�����ţ� ���֣� ���»��߹���
	fformat			= models.CharField(max_length = 200)
	fversion		= models.ManyToManyField(version)		# �����İ汾˵��
	fcotegory 		= models.ManyToManyField(category)
	fintroduction 	= models.ManyToManyField(introduction)
	fparams 		= models.ManyToManyField(params)
	freturns 		= models.ManyToManyField(returns)
	fdemo 			= models.ManyToManyField(demo)
	fcode 			= models.ManyToManyField(code)
	fpublisher 		= models.CharField(max_length = 20)		#������
	fpublishtime	= models.DateTimeField()				#����ʱ��
		
# ����������ϸ����
class category(models.Model):
	cname 	= models.CharField(max_length = 20)	  			#�����������
	ceditor = models.CharField(max_length = 20) 			#�޸���
	ctime 	= models.DateTimeField()						#�޸�ʱ��
	
# �����Ľ��ܲ���
# ����˵������ϸ���ݣ�ÿ�����������˶���˵����¼��
# ���������һ����¼�Ǵ���ʱ�䣬�����һ����¼������ʾ��ʾ��
class introduction(models.Model): 
	ccontent= models.TextField()   							#����˵��������
	ceditor = models.CharField(max_length = 20) 			#�޸���
	ctime 	= models.DateTimeField()						#�޸�ʱ��
	
# �����Ĳ�������
class params(models.Model):
	ccontent= models.TextField()   							#�����Ĳ���˵��
	ceditor = models.CharField(max_length = 20) 			#�޸���
	ctime 	= models.DateTimeField()						#�޸�ʱ��

# �����ķ�������
class returns(models.Model):
	ccontent= models.TextField()   							#���������˵��
	ceditor = models.CharField(max_length = 20) 			#�޸���
	ctime 	= models.DateTimeField()						#�޸�ʱ��

# �����ķ�������
class demo(models.Model):
	ccontent= models.TextField()   							#���������˵��
	ceditor = models.CharField(max_length = 20) 			#�޸���
	ctime 	= models.DateTimeField()						#�޸�ʱ��
	
# ������Դ�벿��
class code(models.Model):
	ccontent= models.TextField()   							#������Դ��
	ceditor = models.CharField(max_length = 20) 			#�޸���
	ctime 	= models.DateTimeField()						#�޸�ʱ��
	
	