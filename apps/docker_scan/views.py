from rest_framework.views import APIView
from rest_framework.response import Response


class Test(APIView):

    def get(self, request):
        dic = {'name': 'shj', 'age': 18, 'girl_friend': ['刘亦菲', '李一桐', '其他女友']}
        return Response(dic)
