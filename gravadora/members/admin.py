from django.contrib import admin

# Register your models here.
from members.models import Musico, Musica, Banda, Disco, Produtor, Instrumento

class ListandoMusicas(admin.ModelAdmin):
    list_display = ("titulo", "autores")        
    list_display_links = ("titulo", "autores")  
    search_fields = ("titulo", "autores",)
    list_filter = ("autores",)
    list_per_page = 10

    def bandas(self, obj):
        return ", ".join([banda.nome for banda in obj.esta.all()])
    def instrumentos(self, obj):
        return ", ".join([instrumento.nome for instrumento in obj.toca.all()])
    
    bandas.short_description = "Bandas"
    instrumentos.short_description = "Instrumentos"

admin.site.register(Musica, ListandoMusicas)

class ListandoBandas(admin.ModelAdmin):
    list_display = ("nome")        
    list_display_links = ("nome")  
    search_fields = ("nome",)
    list_filter = ("nome",)
    list_per_page = 10

admin.site.register(Banda)

class ListandoDiscos(admin.ModelAdmin):
    list_display = ("titulo", "data", "musicos", "bandas")
    list_display_links = ("titulo",)
    search_fields = ("titulo", "data",)
    list_filter = ("titulo", "data",)
    list_per_page = 10

    def musicos(self, obj):
        return ", ".join([musico.nome for musico in obj.disco_musico.all()])

    def bandas(self, obj):
        return ", ".join([banda.nome for banda in obj.disco_banda.all()])

    musicos.short_description = "Músicos"
    bandas.short_description = "Bandas"

admin.site.register(Disco, ListandoDiscos)

class ListandoProdutores(admin.ModelAdmin):
    list_display = ("nome")        
    list_display_links = ("nome")  
    search_fields = ("nome",)
    list_filter = ("nome",)
    list_per_page = 10    

admin.site.register(Produtor)

class ListandoInstrumentos(admin.ModelAdmin):
    list_display = ("nome")        
    list_display_links = ("nome")  
    search_fields = ("nome",)
    list_filter = ("nome",)
    list_per_page = 10    

admin.site.register(Instrumento)