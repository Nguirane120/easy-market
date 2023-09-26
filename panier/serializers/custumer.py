
from rest_framework import serializers
from ..models import Custumer

class CustumerSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)
    # user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user')
    class Meta:
        model = Custumer
        fields =('id','firstName','lastName','phone','email','adress','birthday','archived')