'''
Name: Ramya
Date: 21/01/24
Task: TV Task
'''

# Created a base class called TVClass
class TVClass:
    # Created a constructor of class TVClass
    def __init__(self, brand, price, inches, OnOff_status):
        self.brand = brand
        self.channel = 1
        self.price = price
        self.inches = inches
        self.OnOff_status = OnOff_status
        self.volume = 50
    
    # Crearted a method to print the on or off status of TV
    def on_off_status(self):
        if self.OnOff_status == True:
            print("TV On/Off Status: TV is on")
        else:
            print("TV On/Off Status: TV is off")
        
    # Created a method to increase volume of TV
    def increase_volume(self):
        if self.volume < 100:
            self.volume = self.volume + 1
            print("Volume increased to ", self.volume)
    
    # Created a method to decrease volume of TV
    def decrease_volume(self):
        if self.volume > 0:
            self.volume = self.volume - 1
            print("Volume decreased to ", self.volume)
    
    # Created a method to set channel between 1 and 50
    def set_channel(self):
        if 1 <= self.channel <=50:
            print("Channel is set at ", self.channel)
        else:
            print("Channel should be between 1 and 50, channel returns back to", self.channel)
        
   # Created a method to reset TV to channel 1 and volume 50
    def reset_tv(self):
        self.channel = 1
        self.volume = 50
        print("TV reset to channel 1 and volume 50")
    
    # Created a method to show the status info for TV
    def tv_status(self):
        print(f"\nTV Info: {self.brand} at channel {self.channel}, volume {self.volume}.")

# Created a sub class which will inherit the properties from base class
class LedTV(TVClass):
    # Created constructor for sub class
    def __init__(self, brand, price, inches, OnOff_status, screen_thickness, energy_usage, lifespan, refresh_rate, viewing_angle, backlight, display_details):
        super().__init__(brand, price, inches, OnOff_status)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = viewing_angle
        self.backlight = backlight
        self.display_details = display_details
    
    # Created a method to show the LED TV info
    def tv_status(self):
        led_status = super().tv_status()
        ledtv_info = f"LED TV Info: \nScreen Thickness: {self.screen_thickness} inches\nEnergy Usage = {self.energy_usage}\nLifespan: {self.lifespan}\nRefresh Rate: {self.refresh_rate}\nViewing Angle: {self.viewing_angle}\nBacklight: {self.backlight}\nDisplay Details: {self.display_details}"
        return ledtv_info

# Created a sub class which will inherit the properties from base class
class PlasmaTV(TVClass):
    # Created constructor for sub class
    def __init__(self, brand, price, inches, OnOff_status, screen_thickness, energy_usage, lifespan, refresh_rate, viewing_angle, backlight, display_details):
        super().__init__(brand, price, inches, OnOff_status)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = viewing_angle
        self.backlight = backlight
        self.display_details = display_details
    
    # Created a method to show the Plasma TV info
    def tv_status(self):
        PlasmaTV_status = super().tv_status()
        PlasmaTV_info = f"Plasma TV Info: \nScreen Thickness: {self.screen_thickness} inches\nEnergy Usage = {self.energy_usage}\nLifespan: {self.lifespan}\nRefresh Rate: {self.refresh_rate}\nViewing Angle: {self.viewing_angle}\nBacklight: {self.backlight}\nDisplay Details: {self.display_details}"
        return PlasmaTV_info

# Main method execution
if __name__ == "__main__":
    # Created object for base class TVClass and passing arguments to the parameters
    tv = TVClass("Samsung", 50000, 65, True)
    # Calling the methods from TVClass
    tv.tv_status()
    tv.on_off_status()
    tv.increase_volume()
    tv.decrease_volume()
    tv.set_channel()
    tv.reset_tv()

    # Created an object for sub class LedTV and passing arguments
    led_tv = LedTV("Samsung", 50000, 65, True, 2.4, "Optimum", "10 years", "60 Hz", "Straight", "LED", "4K")
    print(led_tv.tv_status())

    # Created an object for sub class PlasmaTV and passing arguments
    plasma_tv = PlasmaTV("Samsung", 50000, 65, True, 2.4, "Low", "8 years", "100 Hz", "160 degrees", "No Backlight", "4K HDR")
    print(plasma_tv.tv_status())