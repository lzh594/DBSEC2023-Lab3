from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Users, Authors, Publishers, Category, Books, Shoppingcarts, Shoppinghistory, Collection
from .serializers import UsersSerializer, AuthorsSerializer, PublishersSerializer, CategorySerializer, \
    BooksSerializer, ShoppingcartsSerializer, ShoppinghistorySerializer, CollectionSerializer


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
    """
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer


class PublishersViewSet(ModelViewSet):
    """
        list: 获取全部 publisher 数据
        create: 创建新 publisher 数据
        retrieve: 检索 publisher 数据
        update: 更新 publisher 数据
        delete: 删除 publisher 数据
    """
    queryset = Publishers.objects.all()
    serializer_class = PublishersSerializer


class CategoryViewSet(ModelViewSet):
    """
        list: 获取全部 category 数据
        create: 创建新 category 数据
        retrieve: 检索 category 数据
        update: 更新 category 数据
        delete: 删除 category 数据
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BooksViewSet(ModelViewSet):
    """
        list: 获取全部 books 数据
        create: 创建新 books 数据
        retrieve: 检索 books 数据
        update: 更新 books 数据
        delete: 删除 books 数据
    """
    queryset = Books.objects.select_related('authors', 'publishers', 'category').all()
    serializer_class = BooksSerializer

    @action(methods=['get'], detail=False)
    def latest(self, request):
        """
        返回最新的 books 信息
        """
        book = Books.objects.latest('book_id')
        serializer = self.get_serializer(book)
        return Response(serializer.data)


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
