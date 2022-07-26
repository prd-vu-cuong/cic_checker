#  Copyright (c) 2022,
#  CIC Checker
#  __author = "cuong"
#  __date_time = "7/24/22, 5:41 PM"

from rest_framework import viewsets, status
from rest_framework.response import Response

from cic_single.services.single import SingleService


class SingleCheckViewSet(viewsets.ViewSet):
    def list(self, request):
        init_data = SingleService().get_init_data()
        return Response(data=init_data, status=status.HTTP_200_OK)
