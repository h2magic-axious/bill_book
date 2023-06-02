from django.contrib import admin
from django.utils.html import format_html

from .models import Category, Bill


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent", "direction")
    search_fields = ("name", "parent__name")
    list_filter = ("parent", "direction")


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    change_list_template = "admin/bill_change_list.html"

    list_display = ["created_time", "title", "direction", "category", "display_amount"]
    search_fields = ("title",)
    list_filter = ("user", "category", "created_time")
    ordering = ["-created_time"]

    @admin.display(description="方向")
    def direction(self, obj: Bill):
        if obj.amount > 0:
            return format_html(f"<span style='color: #28B55F'>收入</span>")
        return "支出"

    @admin.display(description="金额: 元")
    def display_amount(self, obj: Bill):
        amount = f"{round(abs(obj.amount) / 100, 2)}"
        if obj.amount > 0:
            return format_html(f"<span style='color: #28B55F'>{amount}</span>")

        return amount
