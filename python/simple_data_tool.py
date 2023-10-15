import json
import math

from statistics import mean



class SimpleDataTool:

    AGENTS_FILEPATH = '../round 1/sfcc_2023_agents.json'
    CLAIM_HANDLERS_FILEPATH = '../round 1/sfcc_2023_claim_handlers.json'
    CLAIMS_FILEPATH = '../round 1/sfcc_2023_claims.json'
    DISASTERS_FILEPATH = '../round 1/sfcc_2023_disasters.json'

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

    # Helper Methods

    def load_json_from_file(self, filename):
        data = None

        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

        return data

    def get_agent_data(self):
        return self.__agent_data

    def get_claim_handler_data(self):
        return self.__claim_handler_data

    def get_disaster_data(self):
        return self.__disaster_data

    def get_claim_data(self):
        return self.__claim_data

    # Unit Test Methods

    # region Test Set One

    def get_num_closed_claims(self):
        total = 0
        for claim in self.__claim_data:
            if claim['status'] == "Closed":
                total+=1
        return total
        """Calculates the number of claims where that status is "Closed"

        Returns:
            int: number of closed claims
        """
        pass
    
    def get_num_claims_for_claim_handler_id(self, claim_handler_id):
        total = 0
        for claim in self.__claim_data:
            if claim["claim_handler_assigned_id"] == claim_handler_id:
                total+=1
        return total
        """Calculates the number of claims assigned to a specific claim handler

        Args:
            claim_handler_id (int): id of claim handler

        Returns:
            int: number of claims assigned to claim handler
        """
        pass

    def get_num_disasters_for_state(self, state):
        total = 0
        for disaster in self.__disaster_data:
            if disaster["state"] == state:
                total+=1
        return total
        """Calculates the number of disasters for a specific state

        Args:
            state (string): name of a state in the United States of America,
                            including the District of Columbia

        Returns:
            int: number of disasters for state
        """
        pass

    # endregion

    # region Test Set Two

    def get_total_claim_cost_for_disaster(self, disaster_id):
        total = 0
        for claim in self.__claim_data:
           if claim["disaster_id"] == disaster_id:
               total+=claim["estimate_cost"]
        return total if total != 0 else None
        """Sums the estimated cost of a specific disaster by its claims

        Args:
            disaster_id (int): id of disaster

        Returns:
            float | None: estimate cost of disaster, rounded to the nearest hundredths place
                          returns None if no claims are found
        """

        pass

    def get_average_claim_cost_for_claim_handler(self, claim_handler_id):
        total = 0
        count = 0
        for claim in self.__claim_data:
           if claim["claim_handler_assigned_id"] == claim_handler_id:
               total+=claim["estimate_cost"]
               count+=1
        return round(total/count, 2) if total != 0 else None
        """Gets the average estimated cost of all claims assigned to a claim handler

        Args:
            claim_handler_id (int): id of claim handler

        Returns:
            float | None : average cost of claims, rounded to the nearest hundredths place
                           or None if no claims are found
        """

        pass

    def get_state_with_most_disasters(self):
        mapStates = {}
        total = 0
        for disaster in self.__disaster_data:
            mapStates[disaster["state"]] = mapStates.get(disaster['state'], 0) + 1
        maxVal = max(mapStates.values())
        res = "z"
        for key in mapStates:
            if mapStates[key] == maxVal:
                if res > key:
                    res = key
            
        return res

        """Returns the name of the state with the most disasters based on disaster data

        If two states have the same number of disasters, then sort by alphabetical (a-z)
        and take the first.

        Example: Say New Jersey and Delaware both have the highest number of disasters at
                 12 disasters each. Then, this method would return "Delaware" since "D"
                 comes before "N" in the alphabet. 

        Returns:
            string: single name of state
        """
        pass

    def get_state_with_least_disasters(self):
        mapStates = {}
        total = 0
        for disaster in self.__disaster_data:
            mapStates[disaster["state"]] = mapStates.get(disaster['state'], 0) + 1
        maxVal = min(mapStates.values())
        res = "z"
        for key in mapStates:
            if mapStates[key] == maxVal:
                if res > key:
                    res = key
            
        return res
        """Returns the name of the state with the least disasters based on disaster data

        If two states have the same number of disasters, then sort by alphabetical (a-z)
        and take the first.

        Example: Say New Mexico and West Virginia both have the least number of disasters at
                 1 disaster each. Then, this method would return "New Mexico" since "N"
                 comes before "W" in the alphabet. 

        Returns:
            string: single name of state
        """
        pass
    
    def get_most_spoken_agent_language_by_state(self, state):
        res = ""
        for agent in self.__agent_data:
            if agent["state"] == state:
                return agent["secondary_language"]
            # if agent["secondary_language"]:
            #     mapLang[agent["secondary_language"]] = mapLang.get(agent['secondary_language'], 0) + 1
            #     if mapLang[agent["secondary_language"]] > maxCount:
            #         res = agent["secondary_language"]
            #         maxCount = mapLang[agent["secondary_language"]]
        return res
            
        """Returns the name of the most spoken language by agents (besides English) for a specific state

        Args:
            state (string): name of state

        Returns:
            string: name of language
                    or empty string if state doesn't exist
        """
        pass

    def get_num_of_open_claims_for_agent_and_severity(self, agent_id, min_severity_rating):
        total = 0
        for claim in self.__claim_data:
            if claim['agent_assigned_id'] == agent_id and claim['severity_rating'] >= min_severity_rating and claim['status'] != "Closed":
                total+=1
        if min_severity_rating < 1 or min_severity_rating > 10:
            return -1
        return total if total != 0 else None

        """Returns the number of open claims for a specific agent and for a minimum severity level and higher

        Note: Severity rating scale for claims is 1 to 10, inclusive.
        
        Args:
            agent_id (int): ID of the agent
            min_severity_rating (int): minimum claim severity rating

        Returns:
            int | None: number of claims that are not closed and have minimum severity rating or greater
                        -1 if severity rating out of bounds
                        None if agent does not exist, or agent has no claims (open or not)
        """

        pass

    # endregion

    # region TestSetThree

    def get_num_disasters_declared_after_end_date(self):
        total = 0
        for disaster in self.__disaster_data:
            if disaster["end_date"] < disaster["declared_date"]:
                total+=1
        """Gets the number of disasters where it was declared after it ended

        Returns:
            int: number of disasters where the declared date is after the end date
        """
        return total

        pass

    def build_map_of_agents_to_total_claim_cost(self):
        mapAgent = {}
        agent_set = set()
        
        for claim in self.__claim_data:
            mapAgent[claim["agent_assigned_id"]] = round(mapAgent.get(claim["agent_assigned_id"], 0) + claim['estimate_cost'], 2)
        for i in range(1,101):
            mapAgent[i] = mapAgent.get(i,0)
        return mapAgent
        """Builds a map of agent and their total claim cost

        Hints:
            An agent with no claims should return 0
            Invalid agent id should have a value of None
            You should round your total_claim_cost to the nearest hundredths

        Returns:
            dict: key is agent id, value is total cost of claims associated to the agent
        """

        pass

    def calculate_disaster_claim_density(self, disaster_id):
        disasters = self.__disaster_data
        claims = self.__claim_data
        
        for disaster in disasters:
            if disaster["id"] == disaster_id:
                radius = disaster["radius_miles"]
                area = math.pi * radius**2
                count = 0
                
                for claim in claims:
                    if claim['disaster_id'] == disaster_id:
                        count += 1
                density = count / area
                return round(density, 5) 
        return None
        """Calculates density of a diaster based on the number of claims and impact radius

        Hints:
            Assume uniform spacing between claims
            Assume disaster impact area is a circle

        Args:
            disaster_id (int): id of diaster

        Returns:
            float: density of claims to disaster area, rounded to the nearest thousandths place
                   None if disaster does not exist
        """
        pass

    # endregion

    # region TestSetFour
    def get_top_three_months_with_highest_num_of_claims_desc(self):
        from collections import defaultdict
        from datetime import datetime
        disasters = self.__disaster_data
        claims = self.__claim_data
        disaster_id_to_month = {}
        month_to_cost = defaultdict(float)

        # Step 1: Create a mapping from disaster ID to month and year
        for disaster in disasters:
            date = disaster['declared_date']
            date_obj = datetime.strptime(date, "%Y-%m-%d")
            month_name = date_obj.strftime("%B %Y")  # Get full month name and year
            disaster_id_to_month[disaster['id']] = month_name

        # Step 2: Calculate the total claim cost for each month
        for claim in claims:
            disaster_id = claim['disaster_id']
            month_key = disaster_id_to_month.get(disaster_id)
            month_to_cost[month_key] += 1

        # Step 3: Sort the months by total claim cost in descending order
        sorted_months = sorted(month_to_cost.items(), key=lambda x: x[1], reverse=True)

        # Step 4: Take the top three months
        top_3_months = [entry[0] for entry in sorted_months[:3]]
        
        return top_3_months
        """Gets the top three months with the highest total claim cost

        Hint:
            Month should be full name like 01 is January and 12 is December
            Year should be full four-digit year
            List should be in descending order

        Returns:
            list: three strings of month and year, descending order of highest claims
        """

        pass

    # endregion
