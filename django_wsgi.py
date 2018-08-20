#!/usr/bin/env python
# coding: utf-8

import os
import importlib


importlib.reload(sys)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")#mysite替换为自己的项目名

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
