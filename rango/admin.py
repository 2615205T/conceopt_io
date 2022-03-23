from django.contrib import admin

from rango.models import Project,Image,Page,Tag,Category


admin.site.register(Image)

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

admin.site.register(Page, PageAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Tag)
admin.site.register(Category)
