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
        fields=[Field(name=name_field, required=True, location="query")]
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


class AuthorsViewSet(ModelViewSet):
    """
        list: 获取全部 author 数据
        create: 创建新 author 数据
        retrieve: 检索 author 数据
        update: 更新 author 数据
        delete: 删除 author 数据
        last: 最后一个 author 数据
    """
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer

    last = get_last(Authors)
    get_id = get_id_by_name(Authors, 'author_id', 'aname')


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


class CollectionViewSet(ModelViewSet):
    """
        list: 获取全部 shoppinghistory 数据
        create: 创建新 shoppinghistory 数据
        retrieve: 检索 shoppinghistory 数据
        update: 更新 shoppinghistory 数据
        delete: 删除 shoppinghistory 数据
   """
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
