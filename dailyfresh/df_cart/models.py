from django.db import models


class CartInfo(models.Model):
    user = models.ForeignKey('df_user.UserInfo')
    goods = models.ForeignKey('df_goods.GoodsInfo')
    count = models.IntegerField()

    def __str__(self):
        return str(self.user)
