from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase
from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    fields = [
        'img',
        'get_img_preview',
    ]
    readonly_fields = ['get_img_preview']

    def get_img_preview(self, obj):
        return format_html(
            '<img src="{url}" style="max-height: 200px;"/>',
            url=obj.img.url
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = (ImageInline, )

    search_fields = ['title']


admin.site.register(Image)
