def fractional_knapsack_allocation(items, capacity):

    items.sort(key=lambda x: (-x[1] / x[2], x[0]))

    selected = []
    total_profit = 0.0
    total_weight = 0.0
    remaining = capacity

    for item in items:
        item_id, value, weight = item

        if remaining <= 0:
            break

        if weight <= remaining:
            fraction = 1.0
            used_weight = weight
            profit = value
        else:
            fraction = remaining / weight
            used_weight = remaining
            profit = value * fraction

        selected.append(
            f"{item_id} {value:.2f} {weight:.2f} {fraction:.2f} {profit:.2f}"
        )

        total_weight += used_weight
        total_profit += profit
        remaining -= used_weight

    result = []

    result.append("Fractional Knapsack Report")
    result.append("Selected Items")
    result.append("Item Value Weight Fraction Profit")

    for item in selected:
        result.append(item)

    result.append(f"Maximum Profit: {total_profit:.2f}")
    result.append(f"Total Weight Used: {total_weight:.2f}")
    result.append("Selection Strategy: Highest value-to-weight ratio first")

    return result