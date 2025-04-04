# Sub System 정의
class Thermostat:
    def set_temperature(self, temperature: int):
        print(f"setting thermostat to {temperature} degree")
    
class Lights:
    def on(self):
        print("Lights are on.")
    
    def off(self):
        print("Ligths are off.")

class CoffeeMaker:
    def brew_coffee(self):
        print("brewing coffee")

# Facade 정의
class SmartHomeFacade:
    thermostat:Thermostat
    lights:Lights
    coffee_maker:CoffeeMaker

    def __init__(self, thermostat:Thermostat, lights: Lights, coffee_maker: CoffeeMaker):
        self.thermostat = thermostat
        self.lights = lights
        self.coffee_maker = coffee_maker
    
    def wake_up(self):
        print("waking up")
        self.thermostat.set_temperature(22)
        self.lights.on()
        self.coffee_maker.brew_coffee()
    
    def leave_home(self):
        print("leaving home")
        self.thermostat.set_temperature(18)
        self.lights.off()

if __name__ == "__main__":
    thermostat = Thermostat()
    lights = Lights()
    coffee_maker = CoffeeMaker()

    smart_home = SmartHomeFacade(thermostat, lights, coffee_maker)

    smart_home.wake_up()
    smart_home.leave_home()