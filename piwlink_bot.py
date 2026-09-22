# PIWLink - Water Marketplace

suppliers = {
    "Juba": [
        {
            "name": "Juba Water Supplier 1",
            "location": "Juba",
            "phone": "000000000",
            "price": 20000,
            "available": 10000,
            "delivery_fee": 5000
        }
    ],

    "Kampala": [
        {
            "name": "Kampala Water Supplier 1",
            "location": "Kampala",
            "phone": "000000000",
            "price": 20000,
            "available": 10000,
            "delivery_fee": 5000
        }
    ],

    "Gulu": [
        {
            "name": "Gulu Water Supplier 1",
            "location": "Gulu",
            "phone": "000000000",
            "price": 20000,
            "available": 10000,
            "delivery_fee": 5000
        }
    ],

    "Nairobi": [
        {
            "name": "Nairobi Water Supplier 1",
            "location": "Nairobi",
            "phone": "000000000",
            "price": 20000,
            "available": 10000,
            "delivery_fee": 5000
        }
    ],

    "Mombasa": [],
    "Kisumu": [],
    "Nakuru": [],
    "Thika": [],
    "Limuru": []
}
}

print("Welcome to PIWLink 💧")
print("Connect with trusted water suppliers near you.")

print("\nAvailable cities:")
for city in suppliers:
    print("-", city)
    print("\nChoose your city:")
city = input("Enter city name: ")

if city in suppliers:
    print(f"\nWater suppliers in {city}:")

    if suppliers[city]:
        for supplier in suppliers[city]:
            print("\nSupplier:", supplier["name"])
            print("Location:", supplier["location"])
            print("Phone:", supplier["phone"])
            print("Price:", supplier["price"], "UGX")
            print("Available:", supplier["available"], "litres")
            print("Delivery fee:", supplier["delivery_fee"], "UGX")
    else:
        print("No suppliers registered in this city yet.")

else:
    print("Sorry, PIWLink is not available in that city yet.")
