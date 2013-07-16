from django.contrib import admin
from IP.models import List

class ListAdmin(admin.ModelAdmin):
        list_display = ('ip', 'user', 'machine', 'status', 'date', 'location', 'note')

admin.site.register(List, ListAdmin)
