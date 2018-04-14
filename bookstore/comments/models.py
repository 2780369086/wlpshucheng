from django.db import models

from bookstore.db.base_model import BaseModel


# Create your models here.

class Comments(BaseModel):
	disabled = models.BooleanField(default=False,verbose_name='禁止评论')
	user = models.ForeignKey('bookstore.users.Passport', verbose_name='用户ID')
	book = models.ForeignKey('bookstore.books.Books', verbose_name='书籍ID')
	content = models.CharField(max_length=1000,verbose_name='评论内容')

	class Meta:
		db_table = 's_comment_table'
# wlp