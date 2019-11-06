from django.contrib import admin

# Register your models here.
from .models import Question,platform,dbs

class QuestionAdmin(admin.ModelAdmin):
	fields=['pub_date','question_text']

class platformAdmin(admin.ModelAdmin):
	fields=['platform_name','platform_id']


admin.site.register(Question,QuestionAdmin)
admin.site.register(platform)
admin.site.register(dbs)

