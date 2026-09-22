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
