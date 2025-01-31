from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def turn_on(self):
        ...

    @abstractmethod
    def turn_off(self):
        ...

    @abstractmethod
    def set_volume(self, volume:int):
        ...
    
    @abstractmethod
    def is_enable(self) -> bool:
        ...

class TV(Device):
    __on = False
    __volume = 30

    def turn_on(self):
        self.__on = True
        print("TV is now ON")
    
    def turn_off(self):
        self.__on = False
        print("TV is now OFF")
    
    def set_volume(self, volume:int):
        self.__volume = volume
        print(f"TV volume set to {volume}")
    
    def is_enable(self)->bool:
        return self.__on

class Radio(Device):
    __on = False
    __volume = 30

    def turn_on(self):
        self.__on = True
        print("RADIO is now ON")
    
    def turn_off(self):
        self.__on = False
        print("RADIO is now OFF")
    
    def set_volume(self, volume:int):
        self.__volume = volume
        print(f"RADIO volume set to {volume}")
    
    def is_enable(self)->bool:
        return self.__on
    
class Remote(ABC):
    device:Device

    def __init__(self, device:Device):
        self.device = device
    
    @abstractmethod
    def power(self):
        ...
    
    def volume_up(self):
        self.device.set_volume(1 if self.device.is_enable() else 0)
    
    def volume_down(self):
        self.device.set_volume(-1 if self.device.is_enable() else 0)

class BasicRemote(Remote):
    def __init__(self, device:Device):
        super().__init__(device)

    def power(self):
        if self.device.is_enable():
            self.device.turn_off()
        else:
            self.device.turn_on()

class AdvancedRemote(Remote):
    def __init__(self, device:Device):
        super().__init__(device)
    
    def power(self):
        if self.device.is_enable():
            self.device.turn_off()
        else:
            self.device.turn_on()
        
    def mute(self):
        self.device.set_volume(0)
        print("device is muted")

if __name__ == "__main__":
    tv:Device = TV()
    basic_remote:BasicRemote = BasicRemote(tv)

    basic_remote.power()
    basic_remote.volume_up()

    print()

    radio:Device = Radio()
    advanced_remote:AdvancedRemote = AdvancedRemote(radio)
    
    advanced_remote.power()
    advanced_remote.mute()