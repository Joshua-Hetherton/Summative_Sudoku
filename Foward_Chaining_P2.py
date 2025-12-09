"""
Users can change the facts at any point, allowing the user to test diagnosing different problems
Facts:
    #Power
    battery_voltage=0-50V
    battery_charge=0-100%
    solar_panel_voltage= 0-50V
    solar_panel_current=0-10A
    capacitor_voltage=0-50V

    #Temperature/ Thermal
    outside_temperature = -150C - 120C
    internal_temperature= 30-70C

    #Communication
    antenna_signal= strong, weak, none
    antenna_orientation= earth_facing, space_facing, unknown

    #Attitude Control
    attitude_stable= True/False
    reaction_wheel= 0-6000RPM

    #Onboard Computer
    CPU_temp= 0-100C
    CPU_usage= 0-100%
    memory_usage= 0-100%
    storage_available=0-100%


Rules:
    #== Power System Rules ==#

    #== Thermal Rules ==#

    #== Communication System Rules ==#

    #== Attitude Control Rules ==#

    #== Onboard Computer Rules ==#
"""



def forward_chaining():
    pass

def display_rules():
    pass


def main():
    pass

if __name__ == "__main__":
    main()