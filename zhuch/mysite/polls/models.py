from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Question(models.Model):
	question_text=models.CharField(max_length=200)
	pub_date=models.DateTimeField('date published')
	def __str__(self):
		return self.question_text
	def was_published_recently(self):
		return self.pub_date>=timezone.now()-datetime.timedelta(days=1)

class Choice(models.Model):
	question=models.ForeignKey(Question,on_delete=models.CASCADE)
	choice_text=models.CharField(max_length=200)
	votes=models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text


class FirstPage(models.Model):
	project_name=models.CharField(max_length=50)
	def __str__(self):
		return self.project_name


class dbs(models.Model):
	db_name=models.CharField(max_length=10)
	db_id=models.IntegerField(default=1)
	def __str__(self):
		return self.db_name

class platform(models.Model):
	platform_name=models.CharField(max_length=20)
	platform_id=models.IntegerField()
	# platform_db=models.ManyToManyField(dbs)
	def __str__(self):
		return self.platform_name

class db_info(models.Model):
	db_host=models.CharField(max_length=50,default='')
	db_type=models.CharField(max_length=10)
	usename=models.CharField(max_length=10)
	password=models.CharField(max_length=20)
	port=models.IntegerField(default=3306)
	db_name=models.CharField(max_length=10)
	platform_id=models.IntegerField()
	db_id=models.IntegerField(default=0)

# Question.objects.all()   select * from Question
# Question.objects.filter(id=1) select * from polls_question where id=1;
# Question.objects.filter(question_text__startswith='what') select * from polls_question where question_text like "what%";



#Question.objects.order_by('-pub_date')[:5]  select * from polls_question order by pub_date desc limit 5;