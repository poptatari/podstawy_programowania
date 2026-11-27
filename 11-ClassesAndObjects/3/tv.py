# tv.py file
# class definition
class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0

    def turn_off(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def show_status(self):
        if self.is_on:
            print('The TV is on')
            print(f'channel {self.channel_no} ({self.channels[self.channel_no - 1]})')
            print(f'Volume: {self.volume}')
        else:
            print('The TV is off')

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no

    def set_channels(self, channel_list):
        for channel in channel_list:
            self.channels.append(channel)

    def show_channels(self):
        if len(self.channels) > 0:
            i = 1
            for channel in self.channels:
                print(f'{i}. {channel}')
                i += 1
        else:
            print('No available channels')

    def increase_vol(self):
        if self.volume < 10:
            self.volume += 1
            
    def decrease_vol(self):
        if self.volume > 0:
            self.volume -= 1

