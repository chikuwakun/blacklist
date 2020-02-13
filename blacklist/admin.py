from django.contrib import admin

from .models import BlackUrl


class BlackUrlModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'id', 'comment', 'created_at')
    ordering = ('-created_at',)
    readonly_fields = ('id', 'created_at')


admin.site.register(BlackUrl, BlackUrlModelAdmin)
