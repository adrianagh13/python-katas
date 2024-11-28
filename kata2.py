def cost_calculation(costs_dict, products_bought, tax):
    missing_items = []
    missing_items = [item for item in products_bought if item not in costs_dict]

    total_costs = sum(costs_dict[item] for item in products_bought if item in costs_dict)

    total_with_tax = total_costs * ( 1 + tax)

    if missing_items:
        print(f"The following items were not found: {', '.join(missing_items)}")
    
    return f"The total cost calculation with taxes is: {round(total_with_tax, 2)}"