from django.shortcuts import render
from .models import Plan,RechagreHistory
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .controllers import get_all_plans, get_all_recharge_history, create_new_recharge

@api_view(['GET'])
def allPlans(request):
    plans=Plan.objects.all()
    if request.method == 'GET':
    
        plans = get_all_plans()
        return Response(
            {
                'Plans': plans
            }, 
            status=status.HTTP_200_OK
        )

    else:
        return Response(
            {
                'message': 'Method not allowed'
            }, 
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )

@api_view(['POST'])
def recharge(request):
    if request.method == 'POST':
        data = request.data
        recharge_data = create_new_recharge(data)
        
        if recharge_data:
            return Response(
                {
                    'message': 'Recharge Done successfully!',
                    'Rechage_id': recharge_data.id
                }, 
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    'message': 'Recharge Failed'
                }, 
                status=status.HTTP_404_NOT_FOUND
            )

    else:
        return Response(
            {
                'message': 'Method not allowed'
            }, 
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )



@api_view(['GET'])
def rechargeHistory(request):
    plans=Plan.objects.all()
    if request.method == 'GET':
    
        recharge_historys = get_all_recharge_history()
        return Response(
            {
                'Rechare Historys': recharge_historys
            }, 
            status=status.HTTP_200_OK
        )

    else:
        return Response(
            {
                'message': 'Method not allowed'
            }, 
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )
    pass
