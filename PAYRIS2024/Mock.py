import pandas as pd
import random
from datetime import datetime, timedelta
import time

def generate_mock_data(file_path):
    countries = ['USA', 'Canada', 'France', 'Germany', 'UK', 'China', 'Japan', 'Australia']
    sports = ['Swimming', 'Running', 'Cycling', 'Gymnastics', 'Basketball', 'Soccer', 'Tennis', 'Boxing']
    age_groups = ['18-25', '26-35', '36-45', '46-55', '56-65']
    events = ['Opening Ceremony', 'Closing Ceremony', 'Gold Medal Match', 'Qualifying Round']
    response_codes = [200, 404, 500, 301, 302]
    
    data = {
        'Timestamp': [],
        'Country': [],
        'Sport': [],
        'Visit Duration': [],
        'Response Code': [],
        'Age Group': [],
        'Event': []
    }

    while True:
        timestamp = datetime.now()
        country = random.choice(countries)
        sport = random.choice(sports)
        visit_duration = random.randint(1, 300)  # visit duration in seconds
        response_code = random.choice(response_codes)
        age_group = random.choice(age_groups)
        event = random.choice(events)
        
        data['Timestamp'].append(timestamp)
        data['Country'].append(country)
        data['Sport'].append(sport)
        data['Visit Duration'].append(visit_duration)
        data['Response Code'].append(response_code)
        data['Age Group'].append(age_group)
        data['Event'].append(event)
        
        df = pd.DataFrame(data)
        df.to_csv(file_path, index=False, encoding="ISO-8859-1")
        
        time.sleep(5)  # Generate data every 5 seconds

# Specify the path to save the CSV file
mock_data_file = "mock_paris2024.csv"
generate_mock_data(mock_data_file)
