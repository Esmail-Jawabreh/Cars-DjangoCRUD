from django.contrib import admin

# Register your models here.
from .models import Cars


class CustomCarsAdmin(admin.ModelAdmin):
    model = Cars
    list_display = [
        "name",
        "purchaser",
        "desc",
    ]
    fieldsets = (
        ("Owner", {"fields": ("purchaser",)}),
        (
            "snack info",
            {
                "fields": (
                    "name",
                    "desc",
                )
            },
        ),
    )


admin.site.register(Cars, CustomCarsAdmin)
