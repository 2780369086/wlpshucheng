from django.conf.urls import url

from bookstore.comments import views

urlpatterns = [
	# 评论内容
	url(r'comment/(?P<books_id>\d+)/$', views.comment, name='comment'),
]

# wlp