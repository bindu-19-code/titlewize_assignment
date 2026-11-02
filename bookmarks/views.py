from rest_framework import viewsets
from collections import Counter
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from .models import Bookmark
from .serializers import BookmarkSerializer


class BookmarkPagination(PageNumberPagination):
    page_size = 10


class BookmarkViewSet(viewsets.ModelViewSet):

    serializer_class = BookmarkSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = BookmarkPagination

    def get_queryset(self):

        queryset = Bookmark.objects.filter(
            user=self.request.user
        ).order_by('-created_at')

        tag = self.request.query_params.get('tag')

        if tag:
            queryset = queryset.filter(tags__icontains=tag)

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def stats(self, request):

        tag_counts = Counter()

        bookmarks = self.get_queryset()

        for bookmark in bookmarks:

            tags = bookmark.tags.split(',')

            for tag in tags:
                tag = tag.strip()

                if tag:
                    tag_counts[tag] += 1

        return Response(dict(tag_counts))