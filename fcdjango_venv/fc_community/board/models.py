from django.db import models

# Create your models here.

class Board(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=128, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    writer = models.ForeignKey('fcuser.Fcuser', on_delete=models.CASCADE, verbose_name='작성자')
    tags = models.ManyToManyField('tag.Tag', verbose_name='태그')
    registered_dtt = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'fastcampus_board'
        verbose_name = '패스트캠퍼스 게시글'
        verbose_name_plural = '패스트캠퍼스 게시글'