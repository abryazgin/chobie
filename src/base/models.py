# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

from django.db import models


@python_2_unicode_compatible
class Role(models.Model):
    def __str__(self):
        return u'{name} ({code})'.format(name=self.name, code=self.code)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=50)


@python_2_unicode_compatible
class Scope(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)


@python_2_unicode_compatible
class UserScope(models.Model):
    def __str__(self):
        return u'{role} {user} в {scope}'.format(user=self.user, scope=self.scope, role=self.role.name)
    scope = models.ForeignKey(Scope, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
