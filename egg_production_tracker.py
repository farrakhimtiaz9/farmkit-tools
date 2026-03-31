# 🥚 Egg Production Tracker
# FarmKit Tools - Free tool for poultry farmers
# GitHub: github.com/farrakhimtiaz9/farmkit-tools

def track_egg_production(num_hens, eggs_collected, egg_price):
    """Track daily egg production and estimate income."""

    production_rate = (eggs_collected / num_hens) * 100
    weekly_eggs = eggs_collected * 7
    monthly_eggs = eggs_collected * 30

    daily_income = eggs_collected * egg_price
    weekly_income = weekly_eggs * egg_price
    monthly_income = monthly_eggs * egg_price

    print("\n🥚 EGG PRODUCTION TRACKER - FarmKit Tools")
    print("==========================================")
    print(f"Number of hens       : {num_hens}")
    print(f"Eggs collected today : {eggs_collected}")
    print(f"Production rate      : {production_rate:.1f}%")
    print("------------------------------------------")
    print(f"Weekly eggs          : {weekly_eggs}")
    print(f"Monthly eggs         : {monthly_eggs}")
    print("------------------------------------------")
    print(f"Daily income         : ${daily_income:.2f}")
    print(f"Weekly income        : ${weekly_income:.2f}")
    print(f"Monthly income       : ${monthly_income:.2f}")
    print("==========================================")

    if production_rate < 50:
        print("⚠️  WARNING: Low production rate! Check hen health.")
    elif production_rate < 75:
        print("📊 Production is average. Room for improvement.")
    else:
        print("✅ Excellent production rate!")

    print("✅ Free tool by FarmKit Tools")

# Run the tracker
print("Welcome to FarmKit Egg Production Tracker!")
hens = int(input("Enter number of hens: "))
eggs = int(input("Enter eggs collected today: "))
price = float(input("Enter price per egg (USD): "))
track_egg_production(hens, eggs, price)
