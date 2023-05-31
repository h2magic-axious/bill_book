from django.contrib import admin

from .models import Category, Bill


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("name", "parent__name")
    list_filter = ("parent",)


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ["created_time", "direction", "title", "category", "display_amount"]
    search_fields = ("title",)
    list_filter = ("user", "category", "created_time")
    ordering = ["-created_time"]

    @admin.display(description="方向")
    def direction(self, obj: Bill):
        return "收入" if obj.amount > 0 else "支出"

    @admin.display(description="金额")
    def display_amount(self, obj: Bill):
        return f"{round(obj.amount / 100, 2)}"
