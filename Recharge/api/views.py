from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Plans
from api.serializers import CompanySerializer,PlansSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer
    #companies/{company_id}/plans
    @action(detail=True,methods=['get'])
    def plans(self,request,pk=None):
        try:    
            company=Company.objects.get(pk=pk)
            plns=Plans.objects.filter(company=company)
            plns_serializer=PlansSerializer(plns,many=True,context={'request':request})
            return Response(plns_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Company might not exists'
            })
class PlanViewSet(viewsets.ModelViewSet):
    queryset=Plans.objects.all()
    serializer_class=PlansSerializer
