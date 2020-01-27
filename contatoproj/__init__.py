from __future__ import absolute_import, unicode_literals
 
# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
# noqa: indicates that the linter (a program that automatically checks code quality) 
# should not check this line

from .celery import app as celery_app  # noqa
 
__all__ = ['celery_app']
