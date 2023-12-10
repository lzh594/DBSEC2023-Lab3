from coreapi import Field
from django.db import IntegrityError
from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema
from rest_framework.viewsets import ModelViewSet

from .models import Users, Authors, Publishers, Category, Books, Shoppingcarts, Shoppinghistory, Collection
from .serializers import UsersSerializer, AuthorsSerializer, PublishersSerializer, CategorySerializer, \
    BooksSerializer, ShoppingcartsSerializer, ShoppinghistorySerializer, CollectionSerializer


def generate_fields_from_model(model):
    fields = []
    for field in model._meta.fields:
        field_name = field.name
        # field_type = field.type  # 你可能需要根据实际情况设置不同的类型
        description = f"{field_name} field of {model.__name__} model"
        example = ''  # 你可以根据需要设置示例值
        fields.append(Field(name=field_name, required=False, location="query", description=description,
                            example=example, schema=''))
    return fields


def get_custom_filter(model):
    """
    返回最新的 model 实例信息
    Args:
        model: 模型类
    Returns:
        Response: 复合查询条件下的 model 实例的响应对象
    """

    @action(methods=['get'], detail=False, schema=ManualSchema(
        description=f"复合查询",
        fields=generate_fields_from_model(model)
    ))
    def custom_filter(self, request):
        # 获取前端提供的参数集合
        filter_params = dict(request.query_params)
        filter_params = {key: value[0] for key, value in filter_params.items()}
        # 在这里根据参数集合进行自定义筛选逻辑
        queryset = model.objects.all().filter(**filter_params)
        # 序列化结果并返回
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    return custom_filter


def get_last(model):
    """
    返回最新的 model 实例信息
    Args:
        model: 模型类
    Returns:
        Response: 包含 model 实例的响应对象
    """

    @action(methods=['get'], detail=False)
    def last(self, request):
        instance = model.objects.last()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    return last


def get_id_by_name(model, id_field, name_field):
    """
    通过名称获取相应模型对象的 ID 字段值。
    Args:
        model: 模型类
        id_field: ID 参数的名称
        name_field: 名称字段的名称
    Returns:
        Response: 包含 ID 字段值的响应对象
    """

    @action(methods=['get'], detail=False, schema=ManualSchema(
        description=f"通过 {name_field} 获取 {id_field}",
        fields=[Field(name=name_field, required=True, location="query",
                      description=name_field, type='string', example='', schema='')]
    ))
    def get_id(self, request):
        name_value = request.query_params.get(name_field, None)
        if not name_value:
            return Response({'error': f'Please provide {name_field} parameter'}, status=400)
        try:
            instance = model.objects.get(**{name_field: name_value})
            return Response({id_field: getattr(instance, id_field)})
        except model.DoesNotExist:
            last_instance = model.objects.last()
            new_id = getattr(last_instance, id_field) + 1
            try:
                instance = model.objects.create(**{name_field: name_value}, **{id_field: new_id})
                return Response({id_field: getattr(instance, id_field)})
            except IntegrityError:
                return Response({'created': False, 'error': f'Creating {model.__name__} instacnce failed'}, status=400)

    return get_id


def index(request):
    return JsonResponse(
        {"index": "Welcome to bookStore!please access '/bookStore/api' or '/bookStore/docs'"})


class UsersViewSet(ModelViewSet):
    """
        list: 获取全部 user 数据
        create: 创建新 user 数据
        retrieve: 检索 user 数据
        update: 更新 user 数据
        delete: 删除 user 数据
    """
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    custom_filter = get_custom_filter(Users)
    get_id = get_id_by_name(Users, 'uid', 'uname')


class AuthorsViewSet(ModelViewSet):
    """
        list: 获取全部 author 数据
        create: 创建新 author 数据
        retrieve: 检索 author 数据
        update: 更新 author 数据
        delete: 删除 author 数据
        last: 最后一个 author 数据
        custom_filter : 自定义筛选
    """
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer

    last = get_last(Authors)
    get_id = get_id_by_name(Authors, 'author_id', 'aname')
    custom_filter = get_custom_filter(Authors)


class PublishersViewSet(ModelViewSet):
    """
        list: 获取全部 publisher 数据
        create: 创建新 publisher 数据
        retrieve: 检索 publisher 数据
        update: 更新 publisher 数据
        delete: 删除 publisher 数据
        last: 最后一个 publisher 数据

    """
    queryset = Publishers.objects.all()
    serializer_class = PublishersSerializer

    get_id = get_id_by_name(Publishers, 'pub_id', 'pname')
    last = get_last(Publishers)
    custom_filter = get_custom_filter(Publishers)


class CategoryViewSet(ModelViewSet):
    """
        list: 获取全部 category 数据
        create: 创建新 category 数据
        retrieve: 检索 category 数据
        update: 更新 category 数据
        delete: 删除 category 数据
        last: 最后一个 category 数据
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    get_id = get_id_by_name(Category, 'category_id', 'category_name')
    last = get_last(Category)
    custom_filter = get_custom_filter(Category)


class BooksViewSet(ModelViewSet):
    """
        list: 获取全部 books 数据
        create: 创建新 books 数据
        retrieve: 检索 books 数据
        update: 更新 books 数据
        delete: 删除 books 数据
        last: 最后一个 books 数据
    """
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

    last = get_last(Books)
    custom_filter = get_custom_filter(Books)


class ShoppingcartsViewSet(ModelViewSet):
    """
        list: 获取全部 shoppingcarts 数据
        create: 创建新 shoppingcarts 数据
        retrieve: 检索 shoppingcarts 数据
        update: 更新 shoppingcarts 数据
        delete: 删除 shoppingcarts 数据
   """
    queryset = Shoppingcarts.objects.all()
    serializer_class = ShoppingcartsSerializer
    custom_filter = get_custom_filter(Shoppingcarts)


class ShoppinghistoryViewSet(ModelViewSet):
    """
        list: 获取全部 shoppinghistory 数据
        create: 创建新 shoppinghistory 数据
        retrieve: 检索 shoppinghistory 数据
        update: 更新 shoppinghistory 数据
        delete: 删除 shoppinghistory 数据
   """
    queryset = Shoppinghistory.objects.all()
    serializer_class = ShoppinghistorySerializer
    custom_filter = get_custom_filter(Shoppinghistory)


class CollectionViewSet(ModelViewSet):
    """
        list: 获取全部 collection 数据
        create: 创建新 collection 数据
        retrieve: 检索 collection 数据
        update: 更新 collection 数据
        delete: 删除 collection 数据
   """
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    custom_filter = get_custom_filter(Collection)
