from rest_framework import serializers
from django.contrib.auth.models import User
from vendortraining.models.serializers import userInfoSerializer,vendorSerializer, memberSerializer, eventSerializer
from vendortraining.models import UserInfo, Vendor, Member, Event

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email']
        depth = 2
  
    def getUserInfo(self,id):
        return userInfoSerializer.UserInfoSerializer(UserInfo.objects.get(id=id)).data
    def getVendorInfo(self, id):
        return vendorSerializer.VendorSerializer(Vendor.objects.get(id=id)).data
    def getMemberInfo(self, id):
        data = memberSerializer.MemberSerializer(Member.objects.get(user_id=id)).data
        vendor_info = {}
        vendor_info['vendor_info'] = self.getVendorInfo( data.get('vendor_id'))
        vendor_info['events'] = self.getVendorEvents(data.get('vendor_id'))
        return {
            'vendor_info':self.getVendorInfo( data.get('vendor_id')),
            'events':self.getVendorEvents(data.get('vendor_id'))
        }
    def getVendorEvents(self, id):
        return eventSerializer.EventSerializer(Event.objects.filter(vendor_id=id), many=True).data