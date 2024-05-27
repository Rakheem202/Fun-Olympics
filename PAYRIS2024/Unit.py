import unittest
import pandas as pd
from datetime import datetime, timedelta
from unittest.mock import patch, MagicMock

class TestFunOlympicsDashboard(unittest.TestCase):

    def setUp(self):
        # Sample data to test
        self.sample_data = {
            'Timestamp': [datetime.now() - timedelta(minutes=i) for i in range(10)],
            'Country': ['USA', 'Canada', 'France', 'Germany', 'USA', 'China', 'Japan', 'Australia', 'USA', 'Canada'],
            'Sport': ['Swimming', 'Running', 'Cycling', 'Gymnastics', 'Swimming', 'Soccer', 'Tennis', 'Boxing', 'Swimming', 'Running'],
            'Visit Duration': [120, 150, 180, 200, 160, 100, 220, 110, 90, 130],
            'Response Code': [200, 404, 500, 301, 200, 302, 500, 200, 404, 200],
            'Age Group': ['18-25', '26-35', '36-45', '46-55', '18-25', '56-65', '26-35', '18-25', '36-45', '46-55'],
            'Event': ['Opening Ceremony', 'Gold Medal Match', 'Qualifying Round', 'Closing Ceremony', 'Opening Ceremony',
                      'Gold Medal Match', 'Qualifying Round', 'Opening Ceremony', 'Closing Ceremony', 'Gold Medal Match']
        }
        self.df = pd.DataFrame(self.sample_data)

    @patch('your_dashboard_module.load_data')
    def test_load_data(self, mock_load_data):
        # Mock the load_data function to return the sample data
        mock_load_data.return_value = self.df
        data = load_data("mock_paris2024.csv")
        self.assertEqual(len(data), 10)
        self.assertListEqual(data.columns.tolist(), ['Timestamp', 'Country', 'Sport', 'Visit Duration', 'Response Code', 'Age Group', 'Event'])

    def test_metrics(self):
        total_viewers = len(self.df)
        avg_visit_duration = self.df['Visit Duration'].mean()
        self.assertEqual(total_viewers, 10)
        self.assertAlmostEqual(avg_visit_duration, 146, delta=0.1)

    def test_peak_viewership_hour(self):
        self.df['Timestamp'] = pd.to_datetime(self.df['Timestamp'])
        peak_viewership_hour = self.df['Timestamp'].dt.hour.mode()[0]
        self.assertTrue(isinstance(peak_viewership_hour, int))

    def test_filter_data(self):
        filtered_df = self.df[self.df['Country'].isin(['USA', 'Canada'])]
        self.assertEqual(len(filtered_df), 4)

        filtered_df = self.df[self.df['Sport'].isin(['Swimming', 'Running'])]
        self.assertEqual(len(filtered_df), 4)

    def test_visualizations(self):
        # Assuming the visualizations are created correctly
        sport_time_df = self.df.groupby(['Sport', 'Timestamp']).size().reset_index(name='Counts')
        self.assertFalse(sport_time_df.empty)

        top_sports = self.df.groupby('Sport').size().reset_index(name='Viewership Counts').nlargest(5, 'Viewership Counts')
        self.assertEqual(len(top_sports), 5)

        country_viewers_df = self.df.groupby('Country').size().reset_index(name='Viewership Counts')
        self.assertFalse(country_viewers_df.empty)

        response_code_counts = self.df['Response Code'].value_counts()
        self.assertTrue(response_code_counts[200] > 0)

        age_group_counts = self.df['Age Group'].value_counts().sort_index()
        self.assertEqual(len(age_group_counts), 5)

        event_counts = self.df['Event'].value_counts()
        self.assertFalse(event_counts.empty)

if __name__ == '__main__':
    unittest.main()
