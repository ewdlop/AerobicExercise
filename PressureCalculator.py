class PressureCalculator:
    def __init__(self):
        # Constants
        self.SEA_LEVEL_PRESSURE = 1013.25  # millibars (1 atm)
        self.WATER_PRESSURE_PER_METER = 98.1  # millibars per meter depth
        self.PRESSURE_PSI = 14.7  # pounds per square inch at sea level
        self.WATER_DENSITY = 1000  # kg/m³
        self.GRAVITY = 9.81  # m/s²

    def calculate_water_pressure(self, depth_meters):
        """Calculate pressure at given water depth"""
        # Atmospheric pressure + water pressure
        water_pressure = depth_meters * self.WATER_PRESSURE_PER_METER
        total_pressure = self.SEA_LEVEL_PRESSURE + water_pressure
        return total_pressure

    def pressure_effects(self, pressure_mb):
        """Determine effects of pressure on human body"""
        atmospheres = pressure_mb / self.SEA_LEVEL_PRESSURE
        
        effects = {
            1: "Normal breathing, no effects",
            2: "Slight increase in nitrogen absorption",
            3: "Increased breathing resistance",
            4: "Significant nitrogen narcosis risk",
            5: "Severe breathing difficulty",
            6: "Critical pressure - immediate danger"
        }
        
        return effects.get(int(atmospheres), "Extreme pressure - fatal conditions")

    def calculate_lung_volume(self, initial_volume, depth_meters):
        """Calculate lung volume changes with depth (Boyle's Law)"""
        pressure_ratio = self.calculate_water_pressure(depth_meters) / self.SEA_LEVEL_PRESSURE
        return initial_volume / pressure_ratio

# Create calculator instance
calc = PressureCalculator()

# Test different scenarios
print("Pressure Analysis at Different Levels:\n")

# Sea level
print("At Sea Level:")
print(f"Pressure: {calc.SEA_LEVEL_PRESSURE:.2f} millibars")
print(f"Effects: {calc.pressure_effects(calc.SEA_LEVEL_PRESSURE)}")
print(f"Lung Volume: 100% of normal\n")

# Different water depths
depths = [0, 10, 20, 30, 40, 50]
initial_lung_volume = 6.0  # liters

print("Pressure at Different Water Depths:")
for depth in depths:
    pressure = calc.calculate_water_pressure(depth)
    lung_vol = calc.calculate_lung_volume(initial_lung_volume, depth)
    print(f"\nAt {depth}m depth:")
    print(f"Total Pressure: {pressure:.2f} millibars")
    print(f"Atmospheres: {pressure/calc.SEA_LEVEL_PRESSURE:.1f}")
    print(f"Effects: {calc.pressure_effects(pressure)}")
    print(f"Lung Volume: {lung_vol:.2f} liters")

# Calculate safe breathing limits
max_safe_depth = 30  # meters, typical recreational diving limit
safe_pressure = calc.calculate_water_pressure(max_safe_depth)
print(f"\nSafe Breathing Limit:")
print(f"Maximum recommended depth: {max_safe_depth}m")
print(f"Pressure at max depth: {safe_pressure:.2f} millibars")
print(f"Atmospheres: {safe_pressure/calc.SEA_LEVEL_PRESSURE:.1f}")
