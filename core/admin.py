from django.contrib import admin
from core import models

class CessaoAdmin(admin.ModelAdmin):
    list_display = ('item', 'data_hora_inicio', 'data_hora_final', 'local', 'raio', 'valor_item', 'valor_emprestimo')
    #list_display = ('data_hora_inicio', 'data_hora_final', 'local', 'raio', 'valor_item', 'valor_emprestimo')
    #list_display = models.Cessao._meta.get_all_field_names()

# Register your models here.
admin.site.register(models.Endereco)
admin.site.register(models.Pessoa)
admin.site.register(models.Status)
admin.site.register(models.Item)
admin.site.register(models.Cessao, CessaoAdmin)
#admin.site.register(models.Cessao)
admin.site.register(models.Emprestimo)





