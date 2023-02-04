from rest_framework.viewsets import ModelViewSet
from .models import Account
from .serializers import AccountSerializer

class AccountView(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
