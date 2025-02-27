import os
import random
import json
from datetime import datetime
import time

# Constants
STORE_IDS = ['001', '002', '003']
PRODUCTS = {
    "Refrigerator": 6500000,
    "Air Conditioner": 4750000,
    "LED TV": 5000000,
    "Blender": 650000,
    "Speaker": 1250000,
    "Microwave": 1600000,
    "Washing Machine": 4000000,
    "Rice Cooker": 650000,
    "Water Dispenser": 1250000,
    "Electric Stove": 1000000
}
USER_RATINGS = range(1, 6)
QUANTITY_RANGE = range(1, 11)
OUTPUT_DIR = "generated_data"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Function to generate 1,000 records
def generate_records():
    records = []
    for _ in range(1000):
        store_id = random.choice(STORE_IDS)
        product_name, price = random.choice(list(PRODUCTS.items()))
        user_rating = random.choice(USER_RATINGS)
        quantity = random.choice(QUANTITY_RANGE)
        sale_amount = price * quantity

        record = {
            "store_id": store_id,
            "product_name": product_name,
            "price": price,
            "user_rating": user_rating,
            "purchase_quantity": quantity,
            "sale_amount": sale_amount,
            "timestamp": datetime.utcnow().isoformat()
        }
        records.append(record)
    return records

# Main function
def main():
    while True:
        # Generate 1,000 records
        new_records = generate_records()

        # Save to a local JSON file
        file_name = f"{OUTPUT_DIR}/data_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"
        with open(file_name, "w") as file:
            json.dump(new_records, file)

        print(f"Generated new data file: {file_name}")

        # Wait for 15 second before generating the next batch
        time.sleep(12)

if __name__ == "__main__":
    main()
