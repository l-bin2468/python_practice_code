from django.db import models as db

# Create your models here.
from django.utils import timezone


class BaseModel(db.Model):
    id = db.AutoField("ID", primary_key=True)  # 自增列。主键
    create_time = db.DateTimeField(verbose_name="创建时间", auto_now=True)  # 创建时，自动生成时间
    update_time = db.DateTimeField("更新时间", auto_now_add=True)  # 更新时，自动更新为当前时间
    delete_time = db.DateTimeField("删除时间", default=timezone.now)  # 修改字段保存当前时间

    class Meta:
        # 抽象基类，生成时不会创建该表
        abstract = True


class Info(BaseModel):
    name = db.CharField(max_length=255, null=False)  # 字段长度。是否为空

    class Meta:
        # 自定义表名。没有时，表名为：应用名称_类名
        db_table = "Info"

    def __str__(self):
        """将模型类以字符串的方式输出"""
        return self.name


class Detail(BaseModel):
    execute_machine = db.CharField(max_length=255, blank=True)  # 是否为空
    log = db.CharField(max_length=255, null=False, default="")  # 默认值
    # text = db.TextField("正文")

    class Meta:
        # 自定义表名。没有时，表名为：应用名称_类名
        db_table = "detail"


