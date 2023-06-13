def create_spend_chart(categories):
  total_withdrawals = 0
  category_names = []
  spent_percentages = []

  for category in categories:
    total_withdrawals += category.get_withdrawals()
    category_names.append(category.name)

  for category in categories:
    spent_percentage = category.get_withdrawals() / total_withdrawals * 100
    spent_percentages.append(spent_percentage)

  chart = "Percentage spent by category\n"
  for i in range(100, -10, -10):
    chart += f"{i:3}| "
    for percentage in spent_percentages:
      if percentage >= i:
        chart += "o  "
      else:
        chart += "   "
    chart += "\n"

  chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

  max_category_name_length = max([len(name) for name in category_names])
  for i in range(max_category_name_length):
    chart += "     "
    for name in category_names:
      if i < len(name):
        chart += name[i] + "  "
      else:
        chart += "   "
    chart += "\n"

  return chart
