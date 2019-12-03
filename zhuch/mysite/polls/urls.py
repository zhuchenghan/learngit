from django.urls import path
from .import views

app_name = 'polls'
urlpatterns=[
	path('',views.base,name='base'),
	#ex:/polls/5/
	# path('<int:question_id>',views.detail,name='detail'),
	#ex:/polls/5/results
	# path('<int:question_id>/results/',views.results,name='results'),
	#ex:/polls/5/vote
	# path('<int:question_id>/vote/',views.vote,name='vote'),
	####
	# path('pages',views.pages,name='pages'),
	####
	# path('backupage',views.pages,name='backupage'),
	####
	path('dml',views.dml,name='dml'),
	###
	path('bak',views.bak,name='bak'),
	####
	path('install',views.install,name='install'),
	####
	path('download/<*.?csv>$',views.download,name='download'),

]