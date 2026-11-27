import tv

def main():
    tv_set = tv.TV()
    tv_set.show_status()
    tv_set.turn_on()
    tv_set.show_channels()
    tv_set.set_channels(['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox', 'Discovery'])
    tv_set.show_channels()
    tv_set.increase_vol()
    tv_set.show_status()
    tv_set.turn_off()

if __name__ == "__main__":
    main()