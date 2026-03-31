# 💰 Livestock Cost Estimator
# FarmKit Tools - Free tool for farmers
# GitHub: github.com/farrakhimtiaz9/farmkit-tools

def estimate_costs():
    """Calculate total livestock farming costs and profit estimate."""

    print("\n💰 LIVESTOCK COST ESTIMATOR - FarmKit Tools")
    print("==========================================")

    # Input costs
    num_animals = int(input("Number of animals: "))
    feed_cost_per_day = float(input("Daily feed cost per animal (USD): "))
    medicine_cost_monthly = float(input("Monthly medicine cost total (USD): "))
    labor_cost_monthly = float(input("Monthly labor cost (USD): "))
    other_cost_monthly = float(input("Other monthly costs (USD): "))

    # Input income
    sale_price_per_animal = float(input("Expected sale price per animal (USD): "))
    months = int(input("Number of months until sale: "))

    # Calculations
    total_feed = feed_cost_per_day * num_animals * 30 * months
    total_medicine = medicine_cost_monthly * months
    total_labor = labor_cost_monthly * months
    total_other = other_cost_monthly * months
    total_cost = total_feed + total_medicine + total_labor + total_other

    total_income = sale_price_per_animal * num_animals
    profit = total_income - total_cost

    print("\n==========================================")
    print(f"Total feed cost      : ${total_feed:.2f}")
    print(f"Total medicine cost  : ${total_medicine:.2f}")
    print(f"Total labor cost     : ${total_labor:.2f}")
    print(f"Total other costs    : ${total_other:.2f}")
    print(f"------------------------------------------")
    print(f"TOTAL COST           : ${total_cost:.2f}")
    print(f"TOTAL INCOME         : ${total_income:.2f}")
    print(f"------------------------------------------")
    if profit > 0:
        print(f"✅ ESTIMATED PROFIT  : ${profit:.2f}")
    else:
        print(f"⚠️  ESTIMATED LOSS   : ${abs(profit):.2f}")
    print("==========================================")
    print("✅ Free tool by FarmKit Tools")

estimate_costs()
