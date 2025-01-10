def calculate_bmr(weight_lbs, height_inches, age, gender):
    """
    Calculate Basal Metabolic Rate using the Mifflin-St Jeor Equation
    
    Parameters:
    weight_lbs (float): Weight in pounds
    height_inches (float): Height in inches
    age (int): Age in years
    gender (str): 'M' for male, 'F' for female
    
    Returns:
    float: BMR in calories per day
    """
    # Convert to metric
    weight_kg = weight_lbs * 0.453592
    height_cm = height_inches * 2.54
    
    # Base BMR calculation
    bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age)
    
    # Gender adjustment
    if gender.upper() == 'M':
        bmr += 5
    else:
        bmr -= 161
        
    return round(bmr, 1)

def calculate_tdee(bmr, activity_level):
    """
    Calculate Total Daily Energy Expenditure
    
    Parameters:
    bmr (float): Basal Metabolic Rate
    activity_level (str): Sedentary, Light, Moderate, Very Active, or Extremely Active
    
    Returns:
    float: TDEE in calories per day
    """
    activity_multipliers = {
        'sedentary': 1.2,        # Little or no exercise
        'light': 1.375,          # Light exercise 1-3 times/week
        'moderate': 1.55,        # Moderate exercise 3-5 times/week
        'very active': 1.725,    # Hard exercise 6-7 times/week
        'extremely active': 1.9   # Very hard exercise & physical job
    }
    
    multiplier = activity_multipliers.get(activity_level.lower(), 1.2)
    return round(bmr * multiplier, 1)

def calculate_exercise_calories(weight_lbs, activity, duration_mins, fitness_level, intensity):
    """
    Calculate calories burned during exercise with metabolic factors
    
    Parameters:
    weight_lbs (float): Weight in pounds
    activity (str): Type of exercise
    duration_mins (float): Duration in minutes
    fitness_level (str): beginner, intermediate, or advanced
    intensity (str): low, medium, or high
    
    Returns:
    float: Calories burned
    """
    # Base MET values
    base_met_values = {
        'walking': {'low': 2.5, 'medium': 3.5, 'high': 4.5},
        'swimming': {'low': 4.0, 'medium': 6.0, 'high': 8.0},
        'cycling': {'low': 4.0, 'medium': 7.0, 'high': 10.0},
        'running': {'low': 6.0, 'medium': 9.0, 'high': 12.0},
        'dancing': {'low': 4.0, 'medium': 6.5, 'high': 8.0}
    }
    
    # Fitness level adjustments (more fit = more efficient)
    fitness_multipliers = {
        'beginner': 1.1,
        'intermediate': 1.0,
        'advanced': 0.9
    }
    
    # Get base MET value for activity and intensity
    activity_mets = base_met_values.get(activity.lower(), base_met_values['walking'])
    met = activity_mets.get(intensity.lower(), activity_mets['medium'])
    
    # Apply fitness level adjustment
    met *= fitness_multipliers.get(fitness_level.lower(), 1.0)
    
    # Calculate calories
    weight_kg = weight_lbs * 0.453592
    duration_hrs = duration_mins / 60
    calories = met * weight_kg * duration_hrs
    
    return round(calories, 1)

def analyze_metabolism(weight_lbs, height_inches, age, gender, activity_level, 
                      exercise_type, exercise_duration, fitness_level, exercise_intensity):
    """
    Comprehensive metabolism and exercise analysis
    """
    # Calculate BMR
    bmr = calculate_bmr(weight_lbs, height_inches, age, gender)
    
    # Calculate TDEE
    tdee = calculate_tdee(bmr, activity_level)
    
    # Calculate exercise calories
    exercise_cals = calculate_exercise_calories(weight_lbs, exercise_type, 
                                              exercise_duration, fitness_level, 
                                              exercise_intensity)
    
    return {
        'bmr': bmr,
        'tdee': tdee,
        'exercise_calories': exercise_cals,
        'total_daily_with_exercise': tdee + exercise_cals
    }

# Example usage
if __name__ == "__main__":
    # Example person
    results = analyze_metabolism(
        weight_lbs=155,
        height_inches=68,
        age=30,
        gender='M',
        activity_level='moderate',
        exercise_type='running',
        exercise_duration=30,
        fitness_level='intermediate',
        exercise_intensity='medium'
    )
    
    print(f"BMR: {results['bmr']} calories/day")
    print(f"TDEE: {results['tdee']} calories/day")
    print(f"Calories burned in exercise: {results['exercise_calories']}")
    print(f"Total daily calories with exercise: {results['total_daily_with_exercise']}")
