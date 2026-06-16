from flask import Flask,render_template,request,redirect,url_for
from Handlers import *
app=Flask(__name__)

create_table()
@app.route("/",methods=["GET","POST"])
def home():
    mode=request.args.get("mode","add")
    if request.method=="POST":
        error=handle_add_update_expense(request.form,mode,None)
        if error:
            return render_template("index.html",error=error,mode=mode)
        return redirect(url_for("expense"))
    return render_template("index.html",mode=mode)

@app.route("/update/<int:id>",methods=["GET","POST"])
def update_expense(id):
    expense=get_expense(id)
    mode=request.args.get("mode","update")
    if expense is None:
        return "Expense not found"
    
    if request.method=="POST":     
        error=handle_add_update_expense(request.form,mode,id)
        if error:
            return render_template("index.html",error=error,mode=mode,expense=expense)
        
        return redirect(url_for("expense",mode=mode))
    return render_template("index.html",mode=mode,expense=expense)

@app.route("/view_expense")
def expense():
    mode = request.args.get("mode", "view")
    name = request.args.get("name")
    category = request.args.get("category")
    min_amount = request.args.get("min_amount")
    max_amount = request.args.get("max_amount")

    result=None
    categorys=None
    if mode=="view":
        result=get_total_expense(name,category,min_amount,max_amount)
        categorys=get_category_summary(name,category,min_amount,max_amount)

    
    expenses=handle_filtering(name, category, min_amount, max_amount)

    return render_template(
        "view_expense.html",
        expenses=expenses,
        mode=mode,
        result=result,
        categorys=categorys
    )

@app.route("/delete_confirm/<int:id>")
def delete_confirm(id):
    expense=get_expense(id)
    mode=request.args.get("mode","delete_confirm")
    if expense is None:
        return"Expense not found"
    return render_template("index.html",mode=mode,expense=expense)

@app.route("/delete/<int:id>",methods=["POST"])
def delete_page(id):
    mode=request.args.get("mode","delete_confirm")
    success=handle_delete_expense(id)
    if not success:
        return"Cannot delete"
    return redirect(url_for("expense",mode=mode))

if __name__ == "__main__":
    app.run(debug=True)
    