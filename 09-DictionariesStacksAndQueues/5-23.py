import json

with open("euro.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print(f"{'Date':<16}{'Buying Rate':<16}{'Selling Rate'}")
print("=" * 44)

for rate in data["rates"]:
    date = rate["effectiveDate"]
    buying = rate["bid"]
    selling = rate["ask"]
    print(f"{date:<16}{buying:<16.4f}{selling:.4f}")