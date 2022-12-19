
from .models import Plan, RechagreHistory

def get_all_plans():
    plans = Plan.objects.all()
    plans_list = []

    for plan in plans:
        plan_data  = {
            'id' : plan.id,
            'data': plan.data,
            'validity': plan.validity,
            'price': plan.price,
            'created_At':plan.created_at
        }
        plans_list.append(plan_data)

    return plans_list

def get_all_recharge_history():
    recharge_historys = RechagreHistory.objects.all()
    recharge_historys_list = []

    for recharge_history in recharge_historys:
        recharge_historys_data  = {
            'id' : recharge_history.id,
            'Mobile Number': recharge_history.mobile_number,
            'Created_At': recharge_history.created_at
        }
        recharge_historys_list.append(recharge_historys_data)

    return recharge_historys_list

def create_new_recharge(data):
    plan = Plan.objects.filter(id = data.get('plan_id')).first()
    recharge_history = RechagreHistory.objects.create(
        plan = plan,
        mobile_number = data.get('mobile_number')
    )
    return recharge_history