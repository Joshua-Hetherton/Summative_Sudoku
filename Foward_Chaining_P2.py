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

        self.facts={}
        self.facts_range={}
        
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

    def create_label(self, text, x_pos, y_pos, parent, font_size=12, sticky=None):
        label=tk.Label(parent, text=text, font=("Arial",font_size), bg=parent["bg"])
        label.grid(row=y_pos, column=x_pos)

    def create_entry(self,x_pos, y_pos, parent):
        entry=tk.Entry(parent, width=30)
        entry.grid(row=y_pos, column=x_pos)
        return entry


    #Welcome/Main Menu Implementation
    def main_menu(self):
        self.create_label("Satellite Fault Diagnosis Using Forward Chaining", 1, 2, self.main_menu_frame, font_size=20)
        self.create_label("""In this Interface, you can either change the facts or, load a preset fact set to test the different diagnosis the Satellite Gives 
                        WARNING: Ensure all inputs are accurate before running diagnosis, This GUI was implemented for usability only!"""
                          , 1, 3, self.main_menu_frame, font_size=12, sticky="w")
        
        
        
        #Input Area
        self.display_facts_output= scrolledtext.ScrolledText(self.main_menu_frame, width=40, height=16)
        self.display_facts_output.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky="w")

        #Show Range for facts
        self.display_facts_range= scrolledtext.ScrolledText(self.main_menu_frame, width=60, height=16,)
        self.display_facts_range.grid(row=5, column=1, columnspan=3, padx=10, pady=10,sticky="e")
        self.facts_range=get_preset("Range For Facts")
        for key, value in self.facts_range.items():
            self.display_facts_range.insert(tk.END, f"{key}: {value} \n")
        self.display_facts_range.config(state=tk.DISABLED, wrap=tk.WORD)

        #Output Area (Showing the diagnosis results)
        self.display_diagnosis= scrolledtext.ScrolledText(self.main_menu_frame, width=100, height=15)
        self.display_diagnosis.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

        #Buttons and Labels for Diagnosis and Clearing Entry
        self.create_button("Run Diagnosis", 0,7, lambda: "run diagnosis", "lightgrey",self.main_menu_frame, sticky="w")
        self.create_label("Runs the Forward Chaining Algorithms to find a diagnosis based on the inputs entered", 1,7, self.main_menu_frame, font_size=10)

        self.create_button("Clear Entry", 0,8, lambda: self.clear_facts(), "lightgrey",self.main_menu_frame, sticky="w")
        self.create_label("Clears All inputs entered", 1,8, self.main_menu_frame, font_size=10)

    #Sidebar Implementation
    """Allows the User to easily navigate between the different algorithms implemented"""
    def sidebar(self, parent):
        self.create_button("Load Preset 1", 0, 0 , lambda: self.load_preset("Power System Failure"), "lightgrey", parent, sticky="w")
        self.create_button("Load Preset 2", 0, 1 , lambda: self.load_preset("Thermal System Failure"), "lightgrey", parent, sticky="w")
        self.create_button("Load Preset 3", 0, 2 , lambda: self.load_preset("Communication System Failure"), "lightgrey", parent, sticky="w")


    def load_preset(self, preset_name):
        self.facts = get_preset(preset_name)
        self.display_facts()
        self.display_diagnosis.delete(1.0, tk.END)

    def display_facts(self):
        self.display_facts_output.delete(1.0, tk.END)
        for key, value in self.facts.items():
            self.display_facts_output.insert(tk.END, f"{key}: {value} \n")


    def run_diagnosis(self):
        pass

    def display_diagnosis_results(self):
        pass
    
    def clear_facts(self):
        self.load_preset(4)
        self.display_diagnosis.delete(1.0, tk.END)




def get_preset(preset_value):
    """
    Loads a specific preset of facts that induce an intended error. 
    This is used for convenience to easily see if the fault can be accurately diagnosed by the "satellite"
    
    Args:
    preset_value (int): A number used by the switch case statement to load the specific preset selected by the user.

    Returns:
    preset (dict): A dictionary that contains all facts and values for the selcted preset, to induce the error in the "satellite"
    """
    
    """
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
    """
    preset={}
    match preset_value:
        case "Basic Preset":
            #Basic Preset
            preset={
                #Power
                "battery_voltage": 0 ,       #0-50V
                "battery_charge": 0 ,         #0-100%
                "solar_panel_voltage": 0 ,        #0-50V
                "solar_panel_current": 0,        #0-10A
                "capacitor_voltage": 0,      #0-50V

                #Temperature/ Thermal
                "outside_temperature": 0 ,        #-150C - 120C
                "internal_temperature": 0 ,       #30-70C

                #Communication
                "antenna_signal": "none" ,        #strong, weak, none
                "antenna_orientation": "unknown" ,        #earth_facing, space_facing, unknown

                #Attitude Control
                "attitude_stable": True,        #True/False
                "reaction_wheel": 0,        #0-6000RPM

                #Onboard Computer
                "CPU_temp": 0 ,       #0-100C
                "CPU_usage": 0 ,      #0-100%
                "memory_usage": 0 ,       #0-100%
                "storage_available": 0 ,      #0-100%

            }
            return preset
        
        case "Range For Facts":

            preset={
                #Power
                "battery_voltage": "0-50V",
                "battery_charge":  "0-100%",         
                "solar_panel_voltage": "0-50V",        
                "solar_panel_current": "0-10A",        
                "capacitor_voltage": "0-50V",     

                #Temperature/ Thermal
                "outside_temperature": "-150C - 120C",        
                "internal_temperature": "30-70C",       
                #Communication
                "antenna_signal": "strong, weak, none" ,        
                "antenna_orientation": "earth_facing, space_facing, unknown" ,        

                #Attitude Control
                "attitude_stable": "True/False",        
                "reaction_wheel": "0-6000RPM",        

                #Onboard Computer
                "CPU_temp": "0-100C",       
                "CPU_usage": "0-100%",      
                "memory_usage": "0-100%",       
                "storage_available": "0-100%",      

            }
            return preset
        
        case "Power System Failure":
            #Power System Failure Preset
            preset={
                #Power
                "battery_voltage":3  ,       #0-50V
                "battery_charge":10 ,         #0-100%
                "solar_panel_voltage":30 ,        #0-50V
                "solar_panel_current": 10,        #0-10A
                "capacitor_voltage": 0,      #0-50V

                #Temperature/ Thermal
                "outside_temperature": -50,        #-150C - 120C
                "internal_temperature": 50,       #30-70C

                #Communication
                "antenna_signal": "strong" ,        #strong, weak, none
                "antenna_orientation": "earth_facing" ,        #earth_facing, space_facing, unknown

                #Attitude Control
                "attitude_stable": True,        #True/False
                "reaction_wheel": 3500,        #0-6000RPM

                #Onboard Computer
                "CPU_temp": 40,       #0-100C
                "CPU_usage": 50,      #0-100%
                "memory_usage": 50,       #0-100%
                "storage_available": 37,      #0-100%

            }
            return preset
        case "Thermal System Failure":
            #Thermal System Failure Preset
            preset={
                #Power
                "battery_voltage":40  ,       #0-50V
                "battery_charge":90 ,         #0-100%
                "solar_panel_voltage":25 ,        #0-50V
                "solar_panel_current": 9,        #0-10A
                "capacitor_voltage": 40,      #0-50V

                #Temperature/ Thermal
                "outside_temperature": 120,        #-150C - 120C
                "internal_temperature": 70,       #30-70C

                #Communication
                "antenna_signal": "weak" ,        #strong, weak, none
                "antenna_orientation": "earth_facing" ,        #earth_facing, space_facing, unknown

                #Attitude Control
                "attitude_stable": True,        #True/False
                "reaction_wheel": 3500,        #0-6000RPM

                #Onboard Computer
                "CPU_temp": 90,       #0-100C
                "CPU_usage": 90,      #0-100%
                "memory_usage": 75,       #0-100%
                "storage_available": 77,      #0-100%
            }
            return preset
        case "Communication System Failure":
            #Communication System Failure Preset
            preset={
                #Power
                "battery_voltage":3  ,       #0-50V
                "battery_charge":10 ,         #0-100%
                "solar_panel_voltage":30 ,        #0-50V
                "solar_panel_current": 10,        #0-10A
                "capacitor_voltage": 0,      #0-50V

                #Temperature/ Thermal
                "outside_temperature": -50,        #-150C - 120C
                "internal_temperature": 30,       #30-70C

                #Communication
                "antenna_signal": "none" ,        #strong, weak, none
                "antenna_orientation": "unknown" ,        #earth_facing, space_facing, unknown

                #Attitude Control
                "attitude_stable": True,        #True/False
                "reaction_wheel": 3500,        #0-6000RPM

                #Onboard Computer
                "CPU_temp": 40,       #0-100C
                "CPU_usage": 50,      #0-100%
                "memory_usage": 50,       #0-100%
                "storage_available": 37,      #0-100%
            }
            return preset
        
        


def get_rules():
    """
    List all the rules that are used in the forward chaining algorithm, to help determine what the fault is in the "satellite"
    
    Returns:
    rules (list): A list of dictionaries that contains all the rules needed to diagnose the faults in the "satellite"
    """

    rules=[
        #== Power System Rules ==#
        # Battery Rules
        {"conditions": [("battery_voltage","<",20)], "conclusion":("battery_status","Critical")},
        {"conditions": [("battery_voltage", "<", 20), ("battery_charge", "<", 20)], "conclusion":("power_system_status","Failing")},
        {"conditions": [("battery_charge", "<", 5)], "conclusion":("power_mode","Emergency")},
        {"conditions": [("battery_voltage",">",45)], "conclusion":("battery_status","Overcharged")},
        #Solar Panel Rules
        {"conditions": [("solar_panel_current","<",1), ("solar_panel_voltage", "<", 10)], "conclusion":("solar_panel_status","Failed")},
        {"conditions": [("solar_panel_current","<",3),("solar_panel_voltage","<",15)], "conclusion":("solar_panel_status","Degraded")},
        {"conditions": [("solar_panel_voltage","<",15),("outside_temperature",">",0)], "conclusion":("solar_panel_status","Damaged")},
        #Charging Rules
        {"conditions": [("battery_voltage","<",26),("solar_panel_current",">",5),("battery_charge","<",50)], "conclusion":("charging_system_status","Fault")},
        {"conditions": [("solar_panel_current",">",0),("battery_charge","==",100),("battery_voltage",">",40)], "conclusion":("charging_system_status","Overcharging")},
        #Capacitor Rules
        {"conditions": [("capacitor_voltage","<",10)], "conclusion":("capacitor_status","Depleted")},
        {"conditions": [("capacitor_voltage",">",45)], "conclusion":("capacitor_status","Overvoltage")},
        {"conditions": [("battery_voltage",">",30),("capacitor_voltage","<",15)], "conclusion":("capacitor_status","Failed")},
        #Combined Diagnosis Rules
        {"conditions": [("battery_status","==","Critical"),("solar_panel_status","==","Failed")], "conclusion":("overall_power_system_status","Total Power Loss")},
        {"conditions": [("power_system_status","==","Failing"),("charging_system_status","==","Fault")], "conclusion":("overall_power_system_status","Major Fault")},

        #== Thermal Rules ==#
        #Temperature Extremes
        {"conditions": [("internal_temperature",">",65)], "conclusion":("thermal_status","Overheating")},
        {"conditions": [("internal_temperature","<",30)], "conclusion":("thermal_status","Temperature Low")},
        {"conditions": [("outside_temperature","<",-100)], "conclusion":("external_thermal_status","Extreme Cold")},
        {"conditions": [("outside_temperature",">",100)], "conclusion":("external_thermal_status","Extreme Heat")},
        #CPU Temperature Rules
        {"conditions": [("CPU_temp",">",85)], "conclusion":("CPU_thermal_status","Overheating")},
        {"conditions": [("CPU_temp",">",90)], "conclusion":("CPU_thermal_status","Critical Overheat")},
        {"conditions": [("CPU_temp",">",75),("internal_temperature",">",60)], "conclusion":("CPU_thermal_status","Thermal Issue")},
        #Thermal Control System Rules
        {"conditions": [("internal_temperature",">",60),("outside_temperature","<",0)], "conclusion":("thermal_control_status","Failed")},
        {"conditions": [("internal_temperature","<",35),("outside_temperature",">",50)], "conclusion":("thermal_control_status","Inefficient")},
        #Combined Thermal Diagnosis Rules
        {"conditions": [("CPU_thermal_status","==","Overheating"),("thermal_status","==","Overheating")], "conclusion":("thermal_subsystem_status","Emergency")},
        {"conditions": [("external_thermal_status","==","Extreme Heat"),("internal_temperature",">",70)], "conclusion":("thermal_subsystem_status","Compromised")},
        #== Communication System Rules ==#
        {"conditions": [("antenna_signal","==","none"),("antenna_orientation","==","earth_facing")], "conclusion":("communication_status","Failed")},
        {"conditions": [("antenna_signal","==","none"),("antenna_orientation","==","space_facing")], "conclusion":("communication_status","Antenna Misaligned")},
        {"conditions": [("antenna_signal","==","none"),("antenna_signal","==","unknown")], "conclusion":("communication_status","Antenna Fault")},
        {"conditions": [("antenna_signal","==","weak"),("antenna_orientation","earth_facing",)], "conclusion":("communication_status","Degraded Signal")},
        
        {"conditions": [("antenna_signal","==","weak"),("battery_charge","<",5)], "conclusion":("communication_status","Insufficient Power")},
        {"conditions": [("antenna_signal","==","none"),("battery_voltage","<",22)], "conclusion":("communication_status","Power Failure")},
        {"conditions": [("communication_status","==","Failed"),("battery_voltage","<",28)], "conclusion":("communication_status","Antenna Failure")},
        
        #== Attitude Control Rules ==#
        #Stability Rules
        {"conditions": [("attitude_stable","==",False),("reaction_wheel","<",1000)], "conclusion":("attitude_status","Unstable - RW Low")},
        {"conditions": [("attitude_stable","==",False),("reaction_wheel",">",4000)], "conclusion":("attitude_status","Unstable - RW High")},
        #Reaction Wheel Rules
        {"conditions": [("reaction_wheel","==",0)], "conclusion":("reaction_wheel_status","Failed")},
        {"conditions": [("reaction_wheel",">",5500)], "conclusion":("reaction_wheel_status","Overheating")},
        #Orientation Rules
        {"conditions": [("attitude_stable","==",False),("atenna_orientation","==","unknown")], "conclusion":("craft_orientation","Tumbling")},
        {"conditions": [("attitude_stable","==",False)], "conclusion":("craft_orientation","Drifting")},
        #== Onboard Computer Rules ==#
        #CPU Usage Rules
        {"conditions": [("CPU_usage",">",90)], "conclusion":("CPU_status","Overloaded")},
        {"conditions": [("CPU_usage",">",85),("CPU_temp",">",80)], "conclusion":("CPU_status","Critical Load")},
        {"conditions": [("memory_usage",">",90)], "conclusion":("system_status","Low Memory")},
        {"conditions": [("memory_usage",">",85),("CPU_temp",">",70)], "conclusion":("system_status","System Strain")},
        {"conditions": [("storage_available","<",10)], "conclusion":("storage_status","Low Storage")},
        {"conditions": [("storage_available","<",5),("memory_usage",">",90)], "conclusion":("storage_status","Full Storage")},


        ]
    return rules

def eval_condition(fact_value, operator, condition_value):
    try:
        match operator:
            case "==":
                return fact_value == condition_value
            case ">":
                return fact_value > condition_value
            case "<":
                return fact_value < condition_value
    except Exception as e:
        print(f"Error evaluating condition: {e}")
        return False
    
def check_rule(rule, facts):
    """
    Checks if all the rules are satisfied based on the current facts.
    Args:
    dict rule: A dictonary that contains all the rules, containing conditions and conclusions "IF _ THEN ..."
    dict facts: A dictionary of the current facts and their values

    Returns:
    bool: True if all the conditions are met, False Otherwise
    """
    for condition in rule["conditions"]:
        fact, operator, condition_value = condition
        if fact not in facts or not eval_condition(facts[fact], operator, condition_value):
            return False
    return True


def forward_chaining():

    pass



if __name__ == "__main__":
    root=tk.Tk()
    app=GUI(root)
    root.mainloop()