import json


def load_reservations(filename):
    with open(filename, mode="r", encoding="utf-8") as file:
        data = json.load(file)
    return data["reservations"]


def count_rooms(reservations):
    unique_rooms = {res["room_number"] for res in reservations}
    return len(unique_rooms)


def count_by_payment_status(reservations, is_paid):
    return sum(1 for res in reservations if res["paid"] == is_paid)


def total_value_by_payment_status(reservations, is_paid):
    return sum(
        res["nights"] * res["price_per_night"]
        for res in reservations
        if res["paid"] == is_paid
    )


def print_summary(reservations):
    print(f"Number of rooms: {count_rooms(reservations)}")
    print(f"Number of paid reservations: {count_by_payment_status(reservations, True)}")
    print(f"Number of unpaid reservations: {count_by_payment_status(reservations, False)}")
    print(f"Total value of paid reservations: {total_value_by_payment_status(reservations, True):.2f}")
    print(f"Total value of unpaid reservations: {total_value_by_payment_status(reservations, False):.2f}")


def main():
    reservations = load_reservations("reservations.json")
    print_summary(reservations)


if __name__ == "__main__":
    main()