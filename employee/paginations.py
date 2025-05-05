from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    page_query_param= 'page_num' # by default it is page
    max_page_size= 1 
    page_size = 1 # number of records per page

    def get_paginated_response(self, data):
        return Response({
            'next':self.get_next_link(),
            'previous':self.get_previous_link(),
            'count':self.page.paginator.count,
            'page_size':self.page_size,
            'results':data
        })

