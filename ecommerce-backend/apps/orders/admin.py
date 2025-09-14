from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'updated_at', 'status')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'status')
    ordering = ('-created_at',)
    pagination = True

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('user')  # Optimize database access by using select_related
