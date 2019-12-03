from django.shortcuts import render_to_response,render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect,FileResponse
from .models import *
from django.urls import reverse
import json
import pymysql
import re
import time
import os
import paramiko

class DB():
	def __init__(self,host,user,passwd,port,db):
		self.conn=pymysql.connect(host=host,user=user,password=passwd,port=int(port),database=db,charset="utf8")
		self.cursor=self.conn.cursor()
	def select_sql(self,sql):
		try:
			self.cursor.execute(sql)
			data=self.cursor.fetchall()
			return data
		except:
			return False

	def execute_sql(self,sql):
		try:
			self.cursor.execute(sql)
			self.conn.commit()
		except:
			self.conn.rollback()


def myssh(host,localfile,remotefile):
	private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
	transport = paramiko.Transport((host, 22))
	transport.connect(username='root', pkey=private_key )
	sftp = paramiko.SFTPClient.from_transport(transport)
	sftp.get(remotefile, localfile)
	transport.close()


def base(request):
	return render_to_response("base.html",locals())

def dml(request):
	if request.method=="POST" and request.POST:
		flag=(request.POST.get("plat"))
		db=(request.POST.get("db"))
		sql=request.POST.get("sql")
		gzip_model=request.POST.get("gzip")

		#if re.match('select',sql).group():
		if not flag or flag=="0" or not db or not sql or not gzip_model:
			error="请选择选项"
		else:
			flag,gzip_model=int(flag),int(gzip_model)
			db_ms="slave"
			one_data=db_info.objects.filter(platform_id=flag).filter(db_id=db).filter(db_type=db_ms)[0]
			host,name,user,passwd,port=one_data.db_host,one_data.db_name,one_data.usename,one_data.password,one_data.port
			getdb=DB(host,user,passwd,port,name)
			if gzip_model==1:
				selectdata=getdb.select_sql(sql)	
			elif gzip_model==2:
				base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
				TIME=time.strftime("%Y%m%d%H%M%S", time.localtime())
				sqlname=time.strftime("%Y%m%d%H%M%S", time.localtime())+".csv"
				remotepath="/tmp/%s" %sqlname
				localpath=os.path.join(base_dir, 'polls',"download",sqlname)
				sql=sql+" into outfile '%s' " %remotepath
				getdb.execute_sql(sql)
				myssh(host,localpath,remotepath)

			elif gzip_model==3:
				pass

	dbs_num=dbs.objects.order_by('db_id')
	platform_num=platform.objects.order_by('platform_id')
	
	
	return render_to_response("dml.html",locals())


def bak(request):
	return render_to_response("bak.html",locals())

def install(request):
	return render_to_response("install.html",locals())


def download(request,filename):
	base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	file_path = os.path.join(base_dir, 'polls',"download",filename)
	file=open(file_path,'rb')
	response=FileResponse(file)
	response['Content-Type'] = 'application/octet-stream'
	response['Content-Disposition'] = 'attachment;filename="BatchPayTemplate.xls"'
	return response



# def index(request):
# 	# select * from polls_question order by pub_date desc limit 5;
# 	latest_question_list=Question.objects.order_by('-pub_date')[:5]  #(数据的集合)
# 	#output=', '.join([q.question_text for q in latest_question_list])
# 	#context={'latest_question_list':latest_question_list}
# 	#return HttpResponse(output)
# 	# return HttpResponse("hello world")
# 	return render_to_response('index.html', locals())


# def backupage(request):
# 	test="备份"
# 	return render_to_response("backupage.html",locals())

# def pages(request):
# 	name=FirstPage.objects.order_by('id')[:5]
# 	return render_to_response("pages.html",locals())


# def detail(request,question_id):
# 	# try:
# 	# 	question=Question.objects.get(pk=question_id)
# 	# except Question.DoesNotExist:
# 	# 	raise Http404("Question does not exist")
# 	# # return HttpResponse("you look young %s" %question_id)
# 	# return render_to_response('detail.html',locals())
# 	question=get_object_or_404(Question,pk=question_id)
# 	return render_to_response('detail.html',locals())

# def results(request,question_id):
# 	#response ="result of the question %s"
# 	question = get_object_or_404(Question, pk=question_id)
# 	#return HttpResponse(response %question_id)
# 	return render_to_response('results.html',locals())

# def vote(request,question_id):
# 	question=get_object_or_404(Question,pk=question_id)
# 	try:
# 		selected_choice=question.choice_set.get(pk=request.POST['choice'])
# 	except (KeyError, Choice.DoesNotExist):
# 		error_message="You didn't select a choice."
# 		return render_to_response('detail.html',locals())
# 	else:
# 		selected_choice.votes+=1
# 		selected_choice.save()
# 		return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))


