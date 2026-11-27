from thermometer import Thermometer


def main():
    # 1. Create a thermometer
    thermometer = Thermometer()

    # 1.1 Turn thermometer on
    thermometer.turn_on()

    # 1.2 Measure temperature
    thermometer.measure()

    # 1.3 Display temperature
    thermometer.display()

    # 1.4 Turn thermometer off
    thermometer.turn_off()


if __name__ == "__main__":
    main()