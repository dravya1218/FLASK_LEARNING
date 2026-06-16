from form_handler import *
from Database_handeling import *

def get_expense(id):
    expense=get_expense_by_id(id)
    if not expense:
        return None
    return expense

def handle_add_update_expense(form,mode,id):
    name,amount,category=get_input_expense(form)
    error=validate_expense(name,amount,category)
    if error:
        return error
    if mode=="add":
        insert_expense(name,float(amount),category)
        return None
    if mode=="update":
        update_expense_(id,name,float(amount),category)
        return None
    return None

def handle_delete_expense(id):
    expense=get_expense_by_id(id)
    if expense is None:
        return False
    delete_expense(int(id))
    return True

def handle_filtering(name, category, min_amount, max_amount):
    expenses = filter_in_expense(name, category, min_amount, max_amount)
    return expenses

def get_total_expense(name,category,min_amount,max_amount):
    result=total_expense(name,category,min_amount,max_amount)
    if result["count"]==0:
        result["total"]=0
        result["count"]=0
    return result

def get_category_summary(name,category,min_amount,max_amount):
    categorys=total_summary(name,category,min_amount,max_amount)
    if not categorys:
        return []
    return categorys
