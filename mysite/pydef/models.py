#-*- coding: utf-8 -*-
from django.db import models

# 函数的主数据存储
class func(models.Model):
	fname 			= models.CharField(max_length = 80)		# 函数名： 由字母，符号， 数字， 和下划线构成
	fformat			= models.CharField(max_length = 200)
	fversion		= models.ManyToManyField(version)		# 函数的版本说明
	fcotegory 		= models.ManyToManyField(category)
	fintroduction 	= models.ManyToManyField(introduction)
	fparams 		= models.ManyToManyField(params)
	freturns 		= models.ManyToManyField(returns)
	fdemo 			= models.ManyToManyField(demo)
	fcode 			= models.ManyToManyField(code)
	fpublisher 		= models.CharField(max_length = 20)		#发布人
	fpublishtime	= models.DateTimeField()				#发布时间
		
# 函数类别的详细内容
class category(models.Model):
	cname 	= models.CharField(max_length = 20)	  			#函数类别名称
	ceditor = models.CharField(max_length = 20) 			#修改人
	ctime 	= models.DateTimeField()						#修改时间
	
# 函数的介绍部分
# 函数说明的详细内容（每个函数包含了多条说明记录，
# 其中最早的一条记录是创建时间，最近的一条记录用于显示显示）
class introduction(models.Model): 
	ccontent= models.TextField()   							#函数说明的内容
	ceditor = models.CharField(max_length = 20) 			#修改人
	ctime 	= models.DateTimeField()						#修改时间
	
# 函数的参数部分
class params(models.Model):
	ccontent= models.TextField()   							#函数的参数说明
	ceditor = models.CharField(max_length = 20) 			#修改人
	ctime 	= models.DateTimeField()						#修改时间

# 函数的范例部分
class returns(models.Model):
	ccontent= models.TextField()   							#函数的输出说明
	ceditor = models.CharField(max_length = 20) 			#修改人
	ctime 	= models.DateTimeField()						#修改时间

# 函数的范例部分
class demo(models.Model):
	ccontent= models.TextField()   							#函数的输出说明
	ceditor = models.CharField(max_length = 20) 			#修改人
	ctime 	= models.DateTimeField()						#修改时间
	
# 函数的源码部分
class code(models.Model):
	ccontent= models.TextField()   							#函数的源码
	ceditor = models.CharField(max_length = 20) 			#修改人
	ctime 	= models.DateTimeField()						#修改时间
	
	