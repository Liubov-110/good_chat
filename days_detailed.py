week = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')

day_night_parts = {
    'night': ['1-5', 'sleep'],
    'morning': ['5-9', 'get up, open the window'],
    'brunch': ['9-13', 'eat breakfast and lunch'],
    'day': ['13-17', 'enjoy life'],
    'tea': ['17-21', 'visit friend'],
    'evening': ['21-1', 'go to bed'],
}

suggestions = [day_night_parts.values().mapping[p][1] for p in day_night_parts.keys()]

added_todos = []
