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
    These rules are used to diagnose faults in the satellite, like a part malfunctioning or failing
    #== Power System Rules ==#

    # Battery Rules
    IF batter_voltage <20 THEN batter_status="Critical"
    IF battery_voltge <20 and batter_charge <20% THEN power_system_status="Failing"
    IF battery_charge <5 THEN power_mode="Emergency"
    IF battery_voltage >45 THEN battery_status="Overcharged"

    #Solar Panel Rules
    IF solar_panel_current <1 AND solar_panel_voltage <10 THEN solar_panel_status="Failed"
    IF solar_panel_current <3 AND solar_pnale_voltage <15 THEN solar_panel_status="Degraded"
    IF solar_panel_voltage <15 AND outside_temperature >0 THEN solar_panel_statis="Damaged"

    #Charging Rules
    IF batter_voltage <26 AND solar_panel_current >5 AND battery_charge <50 THEN charging_system_status="Fault"
    IF solar_panel_current >0 AND battery_charge=100 AND battery_voltage >40 THEn charging_system_status=" Overcharging"

    #Capacitor Rules
    IF capacitor_voltage <10 THEN capacitor_status="Depleted"
    IF capacitor_voltage >45 THEN capacitor_status="Overvoltage"
    IF battery_voltage >30 AND capacitor_voltage <15 THEN capacitor_status="Failed"

    #Combined Diagnosis Rules
    IF battery_status="Critical" AND solar_panel_status="Failed" THEN overall_power_system_status="Total Power Loss"
    IF power_system_status="Failing" AND charging_system_status="Fault" THEN overall_power_system_status="Major Fault"
    

    #== Thermal Rules ==#
    #Temperature Extremes
    IF internal_temperature >65 THEN thermal_status="Overheating"
    IF internal_temperature <30 THEN thermal_status="Temperature Low"
    IF outside_temperature <-100 THEN external_thermal_status="Extreme Cold"
    IF outside_temperature >100 THEN external_thermal_status="Extreme Heat"

    #CPU Temperature Rules
    IF CPU_temp >85 THEN CPU_thermal_status="Overheating"
    IF CPU_temp >90 THEN CPU_thermal_status="Critical Overheat"
    IF CPU_temp >95 THEN CPU_thermal_status="Shutdown System"
    IF CPU_temp >75 AND internal_temperature >60 THEN CPU_thermal_status="Thermal Issue"

    #Thermal Control System Rules
    IF internal_temperatrue >60 AND outside_temperature <0 THEN thermal_control_status="Failed"
    IF internal_temperature <35 AND outside_temperature >50 THEN thermal_control_status="Inefficient"

    #Combined Thermal Diagnosis Rules
    IF CPU_thermal_status="Overheating" AND thermal_status="Overheating" THEN thermal_subsystem_status="Emergency"
    IF external_thermal_status="Extreme Heat" AND internal_temperature >70 THEN thermal_subsystem_status="Comprimised"
    
    #== Communication System Rules ==#

    #Antenna Signal Rules
    IF antenna_signal="none" AND antenna_orientation="earth_facing" THEN communication_status="Failed"
    IF antenna_signal="none" AND antenna_orientation="space_facing" THEN communication_status="Antenna Misaligned"
    IF antenna_signal="none" AND antenna_orientation="unknown" THEN communication_status="Antenna Fault"
    IF antenna_signal="weak" AND antenna_orientation="earth_facing" THEN communication_status="Degraded Signal"
    IF antenna_signal="weak" AND battery_charge <5% THEN communication_status="Insufficient Power"

    #Communication With Power Rules
    IF antenna_signal="none" AND battery_voltage <22 THEN communication_status="Power Failure"
    IF communication_status="Failed" AND battery_voltage >28 THEN communication_status="Antenna Failure"

    #== Attitude Control Rules ==#

    #Stability Rules
    IF attitude_stable=False AND reaction_wheel <1000 THEN attitude_status="Unstable - RW Low"
    IF attitude_stable=False AND reaction_wheel >4000 THEN attitude_status="Unstable - RW High"
    
    #Reaction Wheel Rules
    
    #== Onboard Computer Rules ==#
    #CPU Usage Rules
    IF CPU_usage >90 THEN CPU_status="Overloaded"
    IF CPU_usage >85 AND CPU_temp >80 THEN CPU_status="Critical Load"
    
    #Memory Usage Rules
    IF memory_usage >90 THEN system_status="Low Memory"
    IF memory_usage >85 AND CPU_temp >70 THEN system_status="System Strain"

    #Storage Rules
    IF storage_available <10 THEN storage_status="Low Storage"
    IF storage_available <5 AND memory_usage >90 THEN storage_status="Full Storage"

    #Computer Health Diagnosis Rules
    
"""



def forward_chaining():
    pass

def display_rules():
    pass


def main():
    pass

if __name__ == "__main__":
    main()