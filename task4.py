def temperature_converter():
    print("Temperature Converter")
    source_unit = input("Enter source unit (C for Celsius, F for Fahrenheit): ").upper()
    if source_unit not in ['C', 'F']:
        print("Invalid source unit.")
        return

    try:
        value = float(input("Enter the temperature value: "))
    except ValueError:
        print("Invalid input for temperature value.")
        return

    if source_unit == 'C':
        result = (value * 9/5) + 32
        target_unit = 'Fahrenheit'
    else:
        result = (value - 32) * 5/9
        target_unit = 'Celsius'

    print(f"{value} {source_unit} is equal to {result:.2f} {target_unit}.")

def length_converter():
    print("Length Converter")
    source_unit = input("Enter source unit (M for Meters, F for Feet): ").upper()
    if source_unit not in ['M', 'F']:
        print("Invalid source unit.")
        return

    try:
        value = float(input("Enter the length value: "))
    except ValueError:
        print("Invalid input for length value.")
        return

    if source_unit == 'M':
        result = value * 3.28084
        target_unit = 'Feet'
    else:
        result = value / 3.28084
        target_unit = 'Meters'

    print(f"{value} {source_unit} is equal to {result:.2f} {target_unit}.")

def weight_converter():
    print("Weight Converter")
    source_unit = input("Enter source unit (K for Kilograms, P for Pounds): ").upper()
    if source_unit not in ['K', 'P']:
        print("Invalid source unit.")
        return

    try:
        value = float(input("Enter the weight value: "))
    except ValueError:
        print("Invalid input for weight value.")
        return

    if source_unit == 'K':
        result = value * 2.20462
        target_unit = 'Pounds'
    else:
        result = value / 2.20462
        target_unit = 'Kilograms'

    print(f"{value} {source_unit} is equal to {result:.2f} {target_unit}.")

def main():
    print("Welcome to the Unit Converter!")
    print("1. Temperature Converter")
    print("2. Length Converter")
    print("3. Weight Converter")

    choice = input("Enter the number of your choice (1/2/3): ")

    if choice == '1':
        temperature_converter()
    elif choice == '2':
        length_converter()
    elif choice == '3':
        weight_converter()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
