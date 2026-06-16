def get_input_expense(form):
    name=form["Name"]
    amount=form["Amount"]
    category=form["Category"]
    return name,amount,category


def validate_expense(name, amount, category):

    if not name.strip():
        return "Name cannot be empty"

    if name.isdigit():
        return "Name cannot be all digits"

    if len(name) < 2:
        return "Name must be at least 2 characters"

    if len(name) > 50:
        return "Name cannot be more than 50 characters"

    if not amount.strip():
        return "Amount cannot be empty"

    if "." in amount:
        part = amount.split(".")

        if len(part[1]) > 2:
            return "Maximum 2 decimal places allowed"

    try:
        amount = float(amount)

        if amount <= 0:
            return "Amount must be greater than 0"

        if amount > 1000000:
            return "Amount is too large"

    except ValueError:
        return "Amount must be a real number"

    allowed_categories = [
        "food",
        "travel",
        "enterteiment",
        "sport"
    ]

    if category not in allowed_categories:
        return "Invalid category"

    return None