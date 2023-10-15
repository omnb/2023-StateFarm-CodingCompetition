import json
import math
import pandas as pd
import matplotlib.pyplot as plt
import folium
import plotly.express as px
from statistics import mean

class Enhancements:
    AGENTS_FILEPATH = 'round 1/sfcc_2023_agents.json'
    CLAIM_HANDLERS_FILEPATH = 'round 1/sfcc_2023_claim_handlers.json'
    CLAIMS_FILEPATH = 'round 1/sfcc_2023_claims.json'
    DISASTERS_FILEPATH = 'round 1/sfcc_2023_disasters.json'

    REGION_MAP = {
        'west': 'Alaska,Hawaii,Washington,Oregon,California,Montana,Idaho,Wyoming,Nevada,Utah,Colorado,Arizona,New Mexico',
        'midwest': 'North Dakota,South Dakota,Minnesota,Wisconsin,Michigan,Nebraska,Iowa,Illinois,Indiana,Ohio,Missouri,Kansas',
        'south': 'Oklahoma,Texas,Arkansas,Louisiana,Kentucky,Tennessee,Mississippi,Alabama,West Virginia,Virginia,North Carolina,South Carolina,Georgia,Florida',
        'northeast': 'Maryland,Delaware,District of Columbia,Pennsylvania,New York,New Jersey,Connecticut,Massachusetts,Vermont,New Hampshire,Rhode Island,Maine'
    }
    # reads in the data from the json files

    def __init__(self):
        self.__agent_data = self.load_json_from_file(self.AGENTS_FILEPATH)
        self.__claim_handler_data = self.load_json_from_file(
            self.CLAIM_HANDLERS_FILEPATH)
        self.__claim_data = self.load_json_from_file(self.CLAIMS_FILEPATH)
        self.__disaster_data = self.load_json_from_file(
            self.DISASTERS_FILEPATH)
        self.severity_visualization()
        self.heatMap()

    # Helper Methods

    def load_json_from_file(self, filename):
        data = None

        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

        return data
    def severity_visualization(self):
        print('he')
        df = pd.DataFrame(self.__claim_data)

        # Plot a bar chart of severity_rating
        plt.figure(figsize=(8, 6))
        plt.bar(df['id'], df['severity_rating'])
        plt.xlabel('Record ID')
        plt.ylabel('Severity Rating')
        plt.title('Severity Rating for Each Record')
        plt.show()
        
if __name__ == '__main__':
    enhancements = Enhancements()
