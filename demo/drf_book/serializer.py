"""
这里自定义序列化器时需要继承drf框架自带的模型
"""


from rest_framework import serializers

"""
由一到多的访问语法：
一对应的模型类对象.多对应的模型类名小写_set 例：
>>> book = BookInfo.objects.get(id=1)
>>> book.peopleinfo_set.all()
<QuerySet [<PeopleInfo: 郭靖>, <PeopleInfo: 黄蓉>, <PeopleInfo: 黄药师>, <PeopleInfo: 欧阳锋>, <PeopleInfo: 梅超风>]>

由多到一的访问语法:
多对应的模型类对象.多对应的模型类中的关系类属性名 例：
person = PeopleInfo.objects.get(id=1)
person.book
<BookInfo: 射雕英雄传>

访问一对应的模型类关联对象的id语法:
多对应的模型类对象.关联类属性_id
例：
>>> person = PeopleInfo.objects.get(id=1)
>>> person.book_id
1
"""


# 自定义序列化器,创建序列化器类
class BookSerializer(serializers.Serializer):

    """
        图书序列化器
    """
    # 1.定义字段
    # 默认每个字段都有required=True的选项参数,这个参数就是要求前端必须传递参数
    # todo allow_null表明该字段是否允许传入为None, 默认为false, 需要配合form表单进行提交,不能使用json数据形式提交
    # id = serializers.IntegerField(required=False)
    id = serializers.IntegerField(read_only=True)  # 表示该字段只参数序列化返回
    btitle = serializers.CharField(max_length=20, min_length=5)
    # bpub_date = serializers.DateField(default="1999-10-10")
    # 这里可以使用default默认值,前端可以不传递参数
    bpub_date = serializers.DateField(default="2019-07-07")
    bread = serializers.IntegerField(min_value=5, max_value=200)
    bcomment = serializers.IntegerField(write_only=True)  # 表示该字段只参与反序列化过程
    is_delete = serializers.BooleanField(required=False)
    # h_name = serializers.BooleanField(write_only=True)

    # todo 关联对象嵌套序列化返回    父表返回时嵌套子表内容进行序列化返回
    # 在父表的序列化器中如何用字段表示子表的内容?  用子表的小写形式 + _set 来表示
    # 方法1: PrimaryKeyRelatedField 返回关联对象的id值\
    # heroinfo_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # 方法2: SrtingRelatedField 返回关联对象模型类中的__str__的结果
    # heroinfo_set = serializers.StringRelatedField(many=True)
    # 如果想将关联的英雄信息全部(所有字段)都返回,那么需要再定义一个英雄序列化器,如下所示:
    # 方法3: HeroSerializer
    # heroinfo_set = HeroSerializer(many=True)

    # 如果子表模型类中的外键有写related_name=",那么可以使用这个名字代替字表模型类名小写_set
    # related_name 即指定父表查询子表时使用什么字段
    # hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书', related_name='hero')  # 外键
    # hero = HeroSerializer(many=True)

    # 自定义验证字段的方法
    # ① 单一字段验证(validate后面跟验证字段名, attrs便是要验证的字段传入的内容)
    def validate_btitle(self, attrs):
        if attrs == 'python':
            raise serializers.ValidationError('书名不能为python')
        return attrs

    # ② 对多个字段进行验证, 这里的attrs指的是所有要验证的数据集合
    def validate(self, attrs):
        if attrs['bcomment'] > attrs['bread']:
            raise serializers.ValidationError('评论量不能大于阅读量')
        return attrs



# 自定义序列化器
class HeroSerializer(serializers.Serializer):
    """
        英雄序列化器
    """
    # 1.定义字段
    hname = serializers.CharField()
    hgender = serializers.IntegerField()
    hcomment = serializers.CharField()
    is_delete = serializers.BooleanField()

    # todo 关联对象嵌套序列化返回    子表返回时嵌套父表内容进行序列化返回
    # 方法1: PrimaryKeyRelatedField 返回关联对象的id值\
    # hbook = serializers.PrimaryKeyRelatedField(read_only=True)
    # 方法2: SrtingRelatedField 返回关联对象模型类中的__str__的结hbook = serializers.PrimaryKeyRelatedField(many=True, read_only=True)果
    # hbook = serializers.StringRelatedField()
    # 如果想将关联的英雄信息全部(所有字段)都返回
    # 方法3: HeroSerializer
    hbook = BookSerializer()





