# 🐔 Poultry Feed Calculator
# FarmKit Tools - Free tool for poultry farmers
# GitHub: github.com/farrakhimtiaz9/farmkit-tools

def calculate_feed(num_birds, bird_type):
    """Calculate daily feed requirement for poultry."""
    
    # Daily feed per bird in grams
    feed_per_bird = {
        "broiler": 150,
        "layer": 120,
        "chick": 50,
        "turkey": 250
    }
    
    if bird_type not in feed_per_bird:
        print("Unknown bird type. Choose: broiler, layer, chick, turkey")
        return
    
    daily_feed_grams = num_birds * feed_per_bird[bird_type]
    daily_feed_kg = daily_feed_grams / 1000
    weekly_feed_kg = daily_feed_kg * 7
    monthly_feed_kg = daily_feed_kg * 30
    
    print("\n🐔 POULTRY FEED CALCULATOR - FarmKit Tools")
    print("==========================================")
    print(f"Bird type     : {bird_type.capitalize()}")
    print(f"Number of birds: {num_birds}")
    print(f"Daily feed    : {daily_feed_kg:.2f} kg")
    print(f"Weekly feed   : {weekly_feed_kg:.2f} kg")
    print(f"Monthly feed  : {monthly_feed_kg:.2f} kg")
    print("==========================================")
    print("✅ Free tool by FarmKit Tools")

# Run the calculator
print("Welcome to FarmKit Poultry Feed Calculator!")
print("Bird types: broiler, layer, chick, turkey")
bird = input("Enter bird type: ").lower()
count = int(input("Enter number of birds: "))
calculate_feed(count, bird)
