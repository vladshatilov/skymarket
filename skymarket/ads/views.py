import django_filters
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.utils import json

from ads.models import Ad, Comment
from ads.permissions import IsAdminOrOwner, UserPermission
from ads.serializers import AdDetailSerializer, AdSerializer, CommentSerializer

from django_filters import rest_framework as filters

# class AdsFilter(filters.FilterSet):
#     # title = django_filters.CharFilter(lookup_expr='iexact')
#     min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
#     max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
#
#     class Meta:
#         fields = ['title', 'author', 'min_price', 'max_price']
#         # fields = ['min_price', 'max_price']


class MyModelFilter(django_filters.rest_framework.FilterSet):
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains", )

    class Meta:
        model = Ad
        fields = ("title",)


class AdPagination(pagination.PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 10


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    pagination_class = AdPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MyModelFilter     # Do not work. To do fix
    permission_classes = (UserPermission,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def post(self, request, *args, **kwargs):
        file = request.data['image']
        # file = request.FILES['image']
        image = Ad.objects.create(image=file)
        return HttpResponse(json.dumps({'message': "Uploaded"}), status=200) # error import maybe

    # retrieve break image.url
    # def retrieve(self, request, pk=None):
    #     queryset = Ad.objects.all()
    #     one_ad = get_object_or_404(queryset, pk=pk) # maybe error import
    #     serializer = AdDetailSerializer(one_ad)
    #     return Response(serializer.data)  # maybe error import


# @method_decorator(csrf_exempt, name='dispatch')
class AdsMine(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = (IsAdminOrOwner,)

    def get_queryset(self):
        queryset = super(AdsMine, self).get_queryset()
        print(self.request.user)
        return queryset.filter(author=self.request.user)



# approved method of adding images for testing
# @method_decorator(csrf_exempt, name='dispatch')
class AdsImageView(UpdateView):
    pass
#     model = Ad
#     fields = ['image']
#
#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         self.object.image = request.FILES['image']
#         self.object.save()
#
#         return JsonResponse({
#             "id": self.object.id,
#             "title": self.object.title,
#             "author": self.object.author.first_name,
#             "price": self.object.price,
#             "description": self.object.description,
#             "created_at": self.object.created_at,
#             "image": self.object.image.url
#         }, status=201)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (UserPermission,)

    def get_queryset(self):
        queryset = super(CommentViewSet, self).get_queryset()
        # return queryset.filter(professor__pk=self.kwargs.get('pk'))
        return queryset.filter(ad=self.kwargs.get('pk'))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        serializer.save(ad=Ad.objects.get(pk=self.kwargs.get('pk')))
        serializer.save(ad=self.request.data.id)

