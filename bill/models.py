from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    class Meta:
        db_table = "category"
        verbose_name = "账单类目"
        verbose_name_plural = verbose_name

    name = models.CharField("类名", max_length=16)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, default=None)

    class Direction(models.TextChoices):
        INCOME = "income", "收入"
        EXPEND = "expend", "支出"

    direction = models.CharField("类型", choices=Direction.choices, max_length=6)

    def __str__(self):
        return f"{'' if self.parent is None else f'{self.parent.name}-'}{self.name}"


class Bill(models.Model):
    class Meta:
        db_table = "bill"
        verbose_name = "账单"
        verbose_name_plural = verbose_name

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateField("账单时间")
    amount = models.IntegerField("金额", help_text="单位: 分")
    title = models.CharField("标题", max_length=32)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="类目")
