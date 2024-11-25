from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cliente


class CustomUserAdmin(UserAdmin):
    model = Cliente
    list_display = ('email', 'nome', 'sobrenome', 'is_staff', 'ativo')
    list_filter = ('is_staff', 'ativo')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informação Pessoal', {'fields': ('nome', 'sobrenome')}),
        ('Permissões', {'fields': ('is_staff', 'ativo', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nome', 'sobrenome', 'password1', 'password2', 'is_staff', 'ativo')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(Cliente, CustomUserAdmin)
