import sqlite3

DATABASE = "piwlink.db"


def connect_db():
    return sqlite3.connect(DATABASE)


def view_suppliers():
    conn = connect_db()

    rows = conn.execute("""
        SELECT id, name, location, area, phone, price, available, delivery_fee
        FROM suppliers
        ORDER BY id
    """).fetchall()

    conn.close()

    print("\n===== ALL WATER SUPPLIERS =====")

    if len(rows) == 0:
        print("No suppliers registered yet.")
        return

    print("Total suppliers:", len(rows))

    for supplier in rows:
        supplier_id, name, city, area, phone, price, available, delivery_fee = supplier

        print("\n------------------------------")
        print("ID:", supplier_id)
        print("Supplier:", name)
        print("City:", city)
        print("Area:", area)
        print("Phone:", phone)
        print("Price:", price)
        print("Available:", available, "litres")
        print("Delivery fee:", delivery_fee)


def find_supplier():
    city = input("\nEnter city: ").strip().title()
    area = input("Enter area: ").strip().title()

    conn = connect_db()

    rows = conn.execute("""
        SELECT id, name, location, area, phone, price, available, delivery_fee
        FROM suppliers
        WHERE location = ? AND area = ?
        ORDER BY name
    """, (city, area)).fetchall()

    conn.close()

    print(f"\n===== SUPPLIERS IN {area}, {city} =====")

    if not rows:
        print("No suppliers found in this area yet.")
        return

    for supplier in rows:
        supplier_id, name, city, area, phone, price, available, delivery_fee = supplier

        print("\n------------------------------")
        print("ID:", supplier_id)
        print("Supplier:", name)
        print("City:", city)
        print("Area:", area)
        print("Phone:", phone)
        print("Price:", price)
        print("Available:", available, "litres")
        print("Delivery fee:", delivery_fee)


def register_supplier():
    print("\n===== REGISTER AS SUPPLIER =====")

    name = input("Supplier name: ").strip()
    city = input("City: ").strip().title()
    area = input("Area: ").strip().title()
    phone = input("Phone number: ").strip()

    try:
        price = float(input("Price: "))
        available = int(input("Available litres: "))
        delivery_fee = float(input("Delivery fee: "))
    except ValueError:
        print("\nPlease enter valid numbers for price, litres and delivery fee.")
        return

    conn = connect_db()

    conn.execute("""
        INSERT INTO suppliers
        (name, location, area, phone, price, available, delivery_fee)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (name, city, area, phone, price, available, delivery_fee))

    conn.commit()
    conn.close()

    print("\nSupplier registered successfully!")


def order_water():
    print("\n===== ORDER WATER =====")

    try:
        supplier_id = int(input("Enter supplier ID: "))
        litres = int(input("Enter litres of water: "))
    except ValueError:
        print("\nPlease enter valid numbers.")
        return

    conn = connect_db()

    supplier = conn.execute("""
        SELECT id, name, location, area, phone, price, available, delivery_fee
        FROM suppliers
        WHERE id = ?
    """, (supplier_id,)).fetchone()

    if supplier is None:
        print("\nSupplier not found.")
        conn.close()
        return

    supplier_id, name, city, area, phone, price, available, delivery_fee = supplier

    if litres <= 0:
        print("\nLitres must be greater than zero.")
        conn.close()
        return

    if litres > available:
        print("\nNot enough water available.")
        print("Available:", available, "litres")
        conn.close()
        return

    water_cost = (price / 1000) * litres
    total_cost = water_cost + delivery_fee

    print("\n===== ORDER SUMMARY =====")
    print("Supplier:", name)
    print("City:", city)
    print("Area:", area)
    print("Phone:", phone)
    print("Water:", litres, "litres")
    print("Water cost:", water_cost)
    print("Delivery fee:", delivery_fee)
    print("TOTAL COST:", total_cost)

    confirm = input("\nConfirm order? (yes/no): ").strip().lower()

    if confirm == "yes":
        new_available = available - litres

        conn.execute("""
            UPDATE suppliers
            SET available = ?
            WHERE id = ?
        """, (new_available, supplier_id))

        conn.commit()

        print("\nOrder placed successfully!")
        print("Remaining water:", new_available, "litres")
    else:
        print("\nOrder cancelled.")

    conn.close()


print("\n===== PIWLink MENU =====")
print("1. Find water supplier")
print("2. Register as supplier")
print("3. View all suppliers")
print("4. Order water")
print("5. Exit")

choice = input("\nChoose an option: ").strip()

if choice == "1":
    find_supplier()

elif choice == "2":
    register_supplier()

elif choice == "3":
    view_suppliers()

elif choice == "4":
    order_water()

elif choice == "5":
    print("\nThank you for using PIWLink.")

else:
    print("\nInvalid option.")