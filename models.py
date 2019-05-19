#!C:\Users\rina\AppData\Local\Programs\Python\Python37-32\bin\python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import User




# Create your models here.
@python_2_unicode_compatible
class Book(models.Model):
    book_sn = models.CharField(max_length=10, null=True, blank=True)
    book_ln = models.CharField(max_length=75, null=True, blank=True)
    book_order = models.IntegerField(null=True, blank=True)
    book_color = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = 'zr_bb_book'
        verbose_name_plural = "zr_bb_book"        

    def __str__(self):
        return str(self.book_sn)
    

@python_2_unicode_compatible
class Tag(models.Model):
    tag = models.CharField(max_length=250, null=True, blank=True)
    
    class Meta:
        db_table = 'zr_bb_user_tag'
        verbose_name_plural = "zr_bb_user_tag"        

    def __str__(self):
        return str(self.tag_ln)


@python_2_unicode_compatible
class Book_contents(models.Model):
    book = models.ForeignKey(Book, null=True, blank=True, on_delete=models.CASCADE)
    book_chapiter = models.IntegerField(null=True, blank=True)
    book_verset = models.IntegerField(null=True, blank=True)
    book_contents = models.TextField(null=True, blank=True)
    
    class Meta:
        db_table = 'zr_bb_book_contents'
        verbose_name_plural = "zr_bb_book_contents"        

    def __str__(self):
        return str(self.book_verset)


@python_2_unicode_compatible
class Zr_ref(models.Model):
    book = models.ForeignKey(Book, null=True, blank=True, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, null=True, blank=True, on_delete=models.CASCADE)
    book_chapiter = models.IntegerField(null=True, blank=True)
    book_verset_begin = models.IntegerField(null=True, blank=True)
    book_verset_end = models.IntegerField(null=True, blank=True)
    
    
    class Meta:
        db_table = 'zr_bb_ref'
        verbose_name_plural = "zr_bb_ref"        

    def __str__(self):
        return str(self.book_chapiter)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    #photo = models.ImageField(upload_to="images")
    attachment = models.FileField(upload_to="attachments")
    phone = models.CharField(max_length=10)
