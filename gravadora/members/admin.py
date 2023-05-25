from django.contrib import admin

from members.models import Musico, Musica, Banda

class ListandoMusicas(admin.ModelAdmin):
    list_display = ("titulo", "autores")        
    list_display_links = ("titulo", "autores")  
    search_fields = ("titulo", "autores",)
    list_filter = ("autores",)
    list_per_page = 10



admin.site.register(Musica, ListandoMusicas)


admin.site.register(Musico)
admin.site.register(Banda)
