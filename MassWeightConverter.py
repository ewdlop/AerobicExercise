# Constants
EARTH_GRAVITY = 9.81  # m/s²
MOON_GRAVITY = 1.62   # m/s²
MARS_GRAVITY = 3.72   # m/s²
JUPITER_GRAVITY = 24.79  # m/s²

class MassWeightConverter:
    def __init__(self, mass_kg):
        self.mass = mass_kg
    
    def calculate_weight(self, gravity):
        """Calculate weight (force) given gravity"""
        return self.mass * gravity
    
    def compare_weights(self):
        """Compare weights on different celestial bodies"""
        weights = {
            "Earth": self.calculate_weight(EARTH_GRAVITY),
            "Moon": self.calculate_weight(MOON_GRAVITY),
            "Mars": self.calculate_weight(MARS_GRAVITY),
            "Jupiter": self.calculate_weight(JUPITER_GRAVITY)
        }
        return weights

# Example calculations for a 70 kg person
person = MassWeightConverter(70)
weights = person.compare_weights()

print(f"For a person with mass of 70 kg:")
print("\nWeight (in Newtons) on different bodies:")
for body, weight in weights.items():
    print(f"{body}: {weight:.2f} N")

print("\nTo convert to pounds, divide Newtons by 4.448")
print("Weights in pounds:")
for body, weight in weights.items():
    pounds = weight / 4.448
    print(f"{body}: {pounds:.2f} lbs")

# Demonstrate that mass stays constant
print("\nMass remains constant:")
locations = ["Earth", "Moon", "Mars", "Jupiter"]
for location in locations:
    print(f"Mass on {location}: 70 kg")

# Example of weight vs mass in everyday scenarios
print("\nPractical Examples:")
grocery_mass = 1  # 1 kg of apples
grocery_weight_earth = grocery_mass * EARTH_GRAVITY

print(f"1 kg of apples:")
print(f"Mass: Always 1 kg")
print(f"Weight on Earth: {grocery_weight_earth:.2f} N")
print(f"Weight on Moon: {grocery_mass * MOON_GRAVITY:.2f} N")

# Demonstrate weightlessness in space
print("\nIn space (zero gravity):")
print(f"Mass: Still 1 kg")
print(f"Weight: 0 N (weightless)")
