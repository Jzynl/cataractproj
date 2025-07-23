from django.contrib import admin
from django.urls import path
from django.template.response import TemplateResponse
from django.db.models import Count
from django.utils.html import format_html
from .models import CataractScan, UserProfile, DashboardStats

@admin.register(CataractScan)
class CataractScanAdmin(admin.ModelAdmin):
    list_display = ('user', 'diagnosis', 'confidence_display', 'scan_preview', 'created_at')
    list_filter = ('diagnosis', 'created_at')
    search_fields = ('user__username',)
    ordering = ('-created_at',)

    def scan_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" style="border-radius:6px;" />', obj.image.url)
        return "-"
    scan_preview.short_description = "Scan Image"

    def confidence_display(self, obj):
        return f"{obj.confidence:.2%}"
    confidence_display.short_description = "Confidence"

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_image')

# ✅ Fixed version of DashboardStatsAdmin
@admin.register(DashboardStats)
class DashboardStatsAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        # Add your custom chart data
        data = CataractScan.objects.values('diagnosis').annotate(count=Count('id'))
        labels = [entry['diagnosis'] for entry in data]
        counts = [entry['count'] for entry in data]

        # Get default admin context
        context = self.admin_site.each_context(request)

        # Merge in your chart data
        context.update({
            'labels': labels,
            'counts': counts,
            'title': 'Diagnosis Statistics Chart'
        })

        return TemplateResponse(request, "admin/diagnosis_chart.html", context)
