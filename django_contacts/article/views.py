from rest_framework.generics import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Article, Author
from .serializers import ArticleSerializer, AuthorSerializer


class ArticleView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        author = get_object_or_404(Author, id=self.request.data.get('author_id'))
        return serializer.save(author=author)


class SingleArticleView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    # 'aggregate', 'all', 'annotate', 'as_manager', 'bulk_create', 'bulk_update',
    # 'complex_filter', 'count', 'create', 'dates', 'datetimes', 'db', 'defer',
    # 'delete', 'difference', 'distinct', 'earliest', 'exclude', 'exists', 'explain',
    # 'extra', 'filter', 'first', 'get', 'get_or_create', 'in_bulk', 'intersection',
    # 'iterator', 'last', 'latest', 'model', 'none', 'only', 'order_by', 'ordered',
    # 'prefetch_related', 'query', 'raw', 'resolve_expression', 'reverse',
    # 'select_for_update', 'select_related', 'union', 'update', 'update_or_create',
    # 'using', 'values', 'values_list']
    serializer_class = ArticleSerializer


class AuthorView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    # def perform_create(self, serializer):
    #     print('start')
    #     author = get_object_or_404(Author, id=self.request.data.get('id'))
    #     print(author)
    #     print("ok3")
    #     return serializer.save(author=author)


class SingleAuthorView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
