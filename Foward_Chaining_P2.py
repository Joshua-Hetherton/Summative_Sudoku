import tkinter as tk
from tkinter import messagebox, scrolledtext

class GUI:
    
    #=== All GUI Tasks ===#
    def __init__(self, root):
        self.root =  root
        self.setup_window()
        self.create_frame()
        self.sidebar(self.sidebar_frame)

        self.main_menu()
        self.show_frame(self.main_menu_frame)
        
    def setup_window(self):
        self.root.title("Satellite Fault Diagnosis Using Forward Chaining")
        self.root.geometry("1080x720")

    def show_frame(self, frame):
        frame.tkraise()




    def create_frame(self):
        self.configure_grid_layout(self.root, 1, 2)
        #Main menu Frame
        self.main_menu_frame=tk.Frame(self.root, bg="white")

        #Sidebar Frame
        self.sidebar_frame=tk.Frame(self.root, bg="lightgrey")
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        # self.sidebar_frame.grid_propagate(False)


    
        
        #Setting frame positions
        self.main_menu_frame.grid(row=0, column=1, sticky="nsew")
        
        self.root.grid_columnconfigure(0, weight=1, minsize=150)   
        self.root.grid_columnconfigure(1, weight=4)                
        self.root.grid_rowconfigure(0, weight=1)



    #Configuring Grid Layout
    def configure_grid_layout(self, parent, rows, columns):
        for row in range(rows):
            parent.grid_rowconfigure(row, weight=1)
        for column in range(columns):
            parent.grid_columnconfigure(column, weight=1)




    #Creates a button that can be clicked to access anything (self, text, colour, position x, position y, command)
    def create_button(self, text, x_pos, y_pos, command, colour, parent,sticky=None, pad_x=5, pad_y=5):
        button = tk.Button(parent, text=text,bg=colour, command=command)
        #Change to grid format later
        if sticky:
            button.grid(row=y_pos, column=x_pos, padx=pad_x, pady=pad_y, sticky=sticky)
        else:
            button.grid(row=y_pos, column=x_pos, padx=pad_x, pady=pad_y)
        return button

    def create_label(self, text, x_pos, y_pos, parent, font_size=12):
        label=tk.Label(parent, text=text, font=("Arial",font_size), bg=parent["bg"])
        label.grid(row=y_pos, column=x_pos)

    def create_entry(self,x_pos, y_pos, parent):
        entry=tk.Entry(parent, width=30)
        entry.grid(row=y_pos, column=x_pos)
        return entry


    #Welcome/Main Menu Implementation
    def main_menu(self):
        self.create_label("Satellite Fault Diagnosis Using Forward Chaining", 1, 2, self.main_menu_frame, font_size=20)
        

    #Sidebar Implementation
    """Allows the User to easily navigate between the different algorithms implemented"""
    def sidebar(self, parent):
        self.create_button("Main Menu", 0, 0 , lambda: self.show_frame(self.main_menu_frame), "lightgrey", parent, sticky="w")
        # self.create_button("RSA", 0, 1 , lambda: self.show_frame(self.rsa_frame), "lightgrey", parent, sticky="w")


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
    IF reaction_wheel=0 THEN reaction_wheel_status="Failed"
    IF reaction_wheel >5500 THEN reaction_wheel_status="Overheating"
    IF attitude_stable=True AND reaction_wheel BETWEEN 2000 AND 4000 THEN attitude_status="Compensating"
    
    #Orientation Rules
    IF attitude_stable=False AND antenna_orientation="unknown" THEN craft_orientation="Tumbling"
    IF attitude_stable=False THEN craft_orientation="Drifting"

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



def get_facts():
    facts={
        #Power

        #Thermal

        #Communication

        #Attitude Control

        #Onboard Computer
    }

def get_rules():
    rules=[
        {"conditions": [], "conslusion":""},
        {"conditions": [], "conslusion":""},
        {"conditions": [], "conslusion":""},
        {"conditions": [], "conslusion":""},
        {"conditions": [], "conslusion":""},
        {"conditions": [], "conslusion":""},
        {"conditions": [], "conslusion":""},
        {"conditions": [], "conslusion":""},
        {"conditions": [], "conslusion":""},
        {"conditions": [], "conslusion":""},
        {"conditions": [], "conslusion":""},
        {"conditions": [], "conslusion":""},
        {"conditions": [], "conslusion":""},
        {"conditions": [], "conslusion":""},
        {"conditions": [], "conslusion":""},
        {"conditions": [], "conslusion":""},
        {"conditions": [], "conslusion":""},
        {"conditions": [], "conslusion":""},
        {"conditions": [], "conslusion":""},
        {"conditions": [], "conslusion":""},
        {"conditions": [], "conslusion":""},
        {"conditions": [], "conslusion":""},
        {"conditions": [], "conslusion":""},

        ]

def forward_chaining():
    pass



if __name__ == "__main__":
    root=tk.Tk()
    app=GUI(root)
    root.mainloop()