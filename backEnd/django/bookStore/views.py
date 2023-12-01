from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ModelViewSet

from bookStore.models import Books
from bookStore.serializers import BooksSerializer


# Create your views here.
def index(request):
    return JsonResponse({"index": "testIndex"})


class BooksViewSet(ModelViewSet):
    """
        This ViewSet automatically provides
        `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

    @action(methods=['get'], detail=False)
    def latest(self, request):
        """
        返回最新的图书信息
        """
        book = Books.objects.latest('book_id')
        serializer = self.get_serializer(book)
        return Response(serializer.data)

    @action(detail=True, methods=['put'])
    def modifyPrice(self, request, pk):
        """
        修改图书价格
        """
        book = self.get_object()
        serializer = self.get_serializer(book)
        new_price = request.data.get('price')
        if new_price is not None:
            book.price = new_price
            book.save()
            serializer = self.get_serializer(book)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
