from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import Request

admin.site.register(Request, SimpleHistoryAdmin)
