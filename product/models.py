from django.db import models

# Create your models here.

class ProductUpdate(models.Model):    # 상품등록 클래스 모델
    product_img = models.ImageField(verbose_name="프로필 사진" , upload_to="images/%Y/%m/%d", null=True, blank=True)
    product_name = models.CharField(max_length=100, verbose_name="상품명")
    product_price = models.IntegerField(verbose_name="가격")
    product_info = models.TextField(verbose_name="상품설명")

    def __str__(self):
        return f"{self.id}. {self.product_name}"
