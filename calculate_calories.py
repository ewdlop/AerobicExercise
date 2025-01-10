def calculate_calories(weight_lbs, activity, duration_mins):
    """
    Calculate calories burned during aerobic exercise.
    
    Parameters:
    weight_lbs (float): Weight in pounds
    activity (str): Type of exercise
    duration_mins (float): Duration in minutes
    
    Returns:
    float: Estimated calories burned
    """
    
    # MET (Metabolic Equivalent of Task) values for different activities
    met_values = {
        'walking': 3.5,      # Walking 3.5 mph
        'swimming': 6.0,     # Moderate swimming
        'cycling': 7.0,      # 12-14 mph
        'running': 9.0,      # 5 mph (12-min mile)
        'dancing': 6.5,      # Vigorous dancing
        'aerobic': 7.0       # General aerobic exercise
    }
    
    # Formula: Calories = (MET × weight in kg × duration in hours)
    # First convert weight to kg
    weight_kg = weight_lbs * 0.453592
    
    # Convert duration to hours
    duration_hrs = duration_mins / 60
    
    # Get MET value for activity (default to walking if activity not found)
    met = met_values.get(activity.lower(), met_values['walking'])
    
    # Calculate calories
    calories = met * weight_kg * duration_hrs
    
    return round(calories, 1)

# Example usage:
if __name__ == "__main__":
    # Example calculations for a 155 lb person doing different activities for 30 mins
    weight = 155
    duration = 30
    
    for activity in ['walking', 'swimming', 'cycling', 'running', 'dancing']:
        calories = calculate_calories(weight, activity, duration)
        print(f"{activity.capitalize()}: {calories} calories in {duration} minutes")
