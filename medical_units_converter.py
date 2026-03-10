def glucose_mg_dl_to_mmol_l(glucose_mg_dl):
    """
    Convert glucose from mg/dL to mmol/L.

    Parameters:
    glucose_mg_dl (float): Glucose level in mg/dL.

    Returns:
    float: Glucose level in mmol/L.
    """
    return glucose_mg_dl * 0.0555

def glucose_mmol_l_to_mg_dl(glucose_mmol_l):
    """
    Convert glucose from mmol/L to mg/dL.

    Parameters:
    glucose_mmol_l (float): Glucose level in mmol/L.

    Returns:
    float: Glucose level in mg/dL.
    """
    return glucose_mmol_l * 18.018
def cholesterol_mg_dl_to_mmol_l(cholesterol_mg_dl):
    """Convert cholesterol from mg/dL to mmol/L.

    Parameters:
    cholesterol_mg_dl (float): Cholesterol level in mg/dL.

    Returns:
    float: Cholesterol level in mmol/L.
    """
    return cholesterol_mg_dl / 38.67
def cholesterol_mmol_l_to_mg_dl(cholesterol_mmol_l):
    """Convert cholesterol from mmol/L to mg/dL.

    Parameters:
    cholesterol_mmol_l (float): Cholesterol level in mmol/L.

    returns:
    float: Cholesterol level in mg/dL.
    """
    return cholesterol_mmol_l * 38.67

def blood_pressure_mm_hg_to_kpa(mm_hg):
    """Convert blood pressure from mmHg to kPa.

    Parameters:
    mm_hg (float): Blood pressure in mmHg.

    Returns:
    float: Blood pressure in kPa.
    """
    return mm_hg * 0.133322
def blood_pressure_kpa_to_mm_hg(kpa):
    """Convert blood pressure from kPa to mmHg.

    Parameters:
    kpa (float): Blood pressure in kPa.

    Returns:
    float: Blood pressure in mmHg.
    """
    return kpa / 0.133322

def weight_kg_to_lb(weight_kg):
    """Convert weight from kg to lb.

    Parameters:
    weight_kg (float): Weight in kg.

    Returns:
    float: Weight in lb.
    """
    return weight_kg * 2.20462
def weight_lb_to_kg(weight_lb):
    """Convert weight from lb to kg.

    Parameters:
    weight_lb (float): Weight in lb.

    Returns:
    float: Weight in kg.
    """
    return weight_lb / 2.20462

def height_cm_to_in(height_cm):
    """Convert height from cm to inches.

    Parameters:
    height_cm (float): Height in cm.

    Returns:
    float: Height in inches.
    """
    return height_cm * 0.393701
def height_in_to_cm(height_in):
    """Convert height from inches to cm.

    Parameters:
    height_in (float): Height in inches.

    Returns:
    float: Height in cm.
    """
    return height_in / 0.393701
def temperature_c_to_f(temperature_c):
    """Convert temperature from Celsius to Fahrenheit.

    Parameters:
    temperature_c (float): Temperature in Celsius.

    Returns:
    float: Temperature in Fahrenheit.
    """
    return (temperature_c * 9/5) + 32
def temperature_f_to_c(temperature_f):
    """Convert temperature from Fahrenheit to Celsius.

    Parameters:
    temperature_f (float): Temperature in Fahrenheit.
    
    Returns:
    float: Temperature in Celsius.
    """
    return (temperature_f - 32) * 5/9

def show_menu():
    """Display the conversion options menu."""
    print("Welcome to the Medical Units Converter. \nPlease select a conversion option:")
    print("1. Glucose (mg/dL to mmol/L)")
    print("2. Glucose (mmol/L to mg/dL)")
    print("3. Cholesterol (mg/dL to mmol/L)")
    print("4. Cholesterol (mmol/L to mg/dL)")
    print("5. Blood Pressure (mmHg to kPa)")
    print("6. Blood Pressure (kPa to mmHg)")
    print("7. Weight (kg to lb)")
    print("8. Weight (lb to kg)")
    print("9. Height (cm to inches)")
    print("10. Height (inches to cm)")
    print("11. Temperature (Celsius to Fahrenheit)")
    print("12. Temperature (Fahrenheit to Celsius)")
    print("13. Exit")

def main():
    """Main function to handle user input and perform conversions."""
    while True:
        choice = input("Enter your choice (1-13): ")
        if choice == '1':
            glucose_mg_dl = float(input("Enter glucose level in mg/dL: "))
            print(f"Glucose level in mmol/L: {glucose_mg_dl_to_mmol_l(glucose_mg_dl):.2f}")
        elif choice == '2':
            glucose_mmol_l = float(input("Enter glucose level in mmol/L: "))
            print(f"Glucose level in mg/dL: {glucose_mmol_l_to_mg_dl(glucose_mmol_l):.2f}")
        elif choice == '3':
            cholesterol_mg_dl = float(input("Enter cholesterol level in mg/dL: "))
            print(f"Cholesterol level in mmol/L: {cholesterol_mg_dl_to_mmol_l(cholesterol_mg_dl):.2f}")
        elif choice == '4':
            cholesterol_mmol_l = float(input("Enter cholesterol level in mmol/L: "))
            print(f"Cholesterol level in mg/dL: {cholesterol_mmol_l_to_mg_dl(cholesterol_mmol_l):.2f}")
        elif choice == '5':
            mm_hg = float(input("Enter blood pressure in mmHg: "))
            print(f"Blood pressure in kPa: {blood_pressure_mm_hg_to_kpa(mm_hg):.2f}")
        elif choice == '6':
            kpa = float(input("Enter blood pressure in kPa: "))
            print(f"Blood pressure in mmHg: {blood_pressure_kpa_to_mm_hg(kpa):.2f}")
        elif choice == '7':
            weight_kg = float(input("Enter weight in kg: "))
            print(f"Weight in lb: {weight_kg_to_lb(weight_kg):.2f}")
        elif choice == '8':
            weight_lb = float(input("Enter weight in lb: "))
            print(f"Weight in kg: {weight_lb_to_kg(weight_lb):.2f}")
        elif choice == '9':
            height_cm = float(input("Enter height in cm: "))
            print(f"Height in inches: {height_cm_to_in(height_cm):.2f}")
        elif choice == '10':
            height_in = float(input("Enter height in inches: "))
            print(f"Height in cm: {height_in_to_cm(height_in):.2f}")
        elif choice == '11':
            temperature_c = float(input("Enter temperature in Celsius: "))
            print(f"Temperature in Fahrenheit: {temperature_c_to_f(temperature_c):.2f}")
        elif choice == '12':
            temperature_f = float(input("Enter temperature in Fahrenheit: "))
            print(f"Temperature in Celsius: {temperature_f_to_c(temperature_f):.2f}")
        elif choice == '13':
            print("Thank you for using the Medical Units Converter!")
            break
        else:
            print("Invalid choice. Please try again.")
# Run the program
show_menu()
main()