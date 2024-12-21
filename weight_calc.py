# Function to calculate weight of Y-angle

def calculate_y_angle_weight():
    # Input dimensions from user
    print("Enter dimensions:")
    length_i_section = float(input("Length of I-section (vertical part) in inches: ")) * 25.4  # Convert inches to mm
    length_arm1 = float(input("Length of Arm 1 (V-section) in inches: ")) * 25.4  # Convert inches to mm
    length_arm2 = float(input("Length of Arm 2 (V-section) in inches: ")) * 25.4  # Convert inches to mm
    width = float(input("Width of flat bars in mm: "))  # e.g., 40
    thickness = float(input("Thickness of flat bars in mm: "))  # e.g., 6

    # Constants
    density_iron = 7.85e-6  # Corrected density of iron in kg/mm^3

    # Calculating volumes
    # I-section (2 perpendicular bars)
    volume_i_section = 2 * length_i_section * width * thickness

    # V-section arms (each with 2 perpendicular bars)
    volume_arm1 = 2 * length_arm1 * width * thickness  # Arm 1
    volume_arm2 = 2 * length_arm2 * width * thickness  # Arm 2

    # Total volume
    total_volume = volume_i_section + volume_arm1 + volume_arm2

    # Convert volume to weight (kg)
    total_weight = total_volume * density_iron

    # Display results
    print(f"\nResults:")
    print(f"Volume of I-section: {volume_i_section:.2f} mm^3")
    print(f"Volume of Arm 1: {volume_arm1:.2f} mm^3")
    print(f"Volume of Arm 2: {volume_arm2:.2f} mm^3")
    print(f"Total Volume: {total_volume:.2f} mm^3")
    print(f"Total Weight of Y angle is {total_weight:.2f} kg")

# Call the function
calculate_y_angle_weight()
