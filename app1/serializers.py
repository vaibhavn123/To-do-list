# from djoser import serializers
from rest_framework import serializers

from app1.models import tbl_todolist


class todolistserilizers(serializers.ModelSerializer):
    class Meta:
        model=tbl_todolist
        fields='__all__'

class todolistupdateserilizers(serializers.ModelSerializer):
    class Meta:
        model=tbl_todolist
        fields='__all__'