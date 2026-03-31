# 🐄 Milk Yield Calculator
# FarmKit Tools - Free tool for dairy farmers
# GitHub: github.com/farrakhimtiaz9/farmkit-tools

def calculate_milk_yield(num_cows, avg_liters_per_cow):
    """Calculate total milk yield and estimated income."""
    
    daily_total = num_cows * avg_liters_per_cow
    weekly_total = daily_total * 7
    monthly_total = daily_total * 30

    # Estimated price per liter (can be changed)
    price_per_liter = 0.50  # USD

    daily_income = daily_total * price_per_liter
    monthly_income = monthly_total * price_per_liter

    print("\n🐄 MILK YIELD CALCULATOR - FarmKit Tools")
    print("==========================================")
    print(f"Number of cows      : {num_cows}")
    print(f"Avg yield per cow   : {avg_liters_per_cow} liters/day")
    print(f"Daily total yield   : {daily_total} liters")
    print(f"Weekly total yield  : {weekly_total} liters")
    print(f"Monthly total yield : {monthly_total} liters")
    print("------------------------------------------")
    print(f"Est. daily income   : ${daily_income:.2f}")
    print(f"Est. monthly income : ${monthly_income:.2f}")
    print("==========================================")
    print("✅ Free tool by FarmKit Tools")

# Run the calculator
print("Welcome to FarmKit Milk Yield Calculator!")
num = int(input("Enter number of cows: "))
avg = float(input("Enter average liters per cow per day: "))
calculate_milk_yield(num, avg)
