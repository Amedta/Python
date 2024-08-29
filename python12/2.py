sales = [100, 121, 120, 130, 140, 120, 122, 123, 190, 125]
reduced_sales_days = [i for i in range(1, len(sales)) if sales[i] < sales[i - 1]]
print("Days with reduced sales:", reduced_sales_days)