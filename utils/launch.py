import datetime

class Launch:
    """Class that stores the data associated to a launch: date, max_payload, fixed_cost and variable_cost"""

    def __init__(self, date, max_payload, fixed_cost, variable_cost):
        self.date = date
        self.max_payload = max_payload
        self.fixed_cost = fixed_cost
        self.variable_cost = variable_cost

    def __str__(self):
        return "launch: %s %s %s %s" % (self.date, str(self.max_payload), str(self.fixed_cost), str(self.variable_cost))

class Launches:
    """Class that stores a list and dictionary with the launches ordered by date"""

    def __init__(self):
        self.launch_list = []
        self.launch_dict = {}

    def ordered_insertion_on_list(self, launch):
        """method that receives an instance of Launch an inserts it on the list ordered by date"""

        #check if the date on the launch object is in a valid format
        try:
            launch_date_to_insert = datetime.date(int(launch.date[4:]),int(launch.date[2:4]),int(launch.date[:2]))
        except:
            return

        iteration_count = 0
        #empty list case, insert in the begging of the list
        if len(self.launch_list) == 0:
            self.launch_list.append(launch)
            return

        #ordered insertion o self.launch_list by date of launch
        for x in self.launch_list:
            launch_date_to_compar = datetime.date(int(x.date[4:]),int(x.date[2:4]),int(x.date[:2]))
            if launch_date_to_insert <= launch_date_to_compar:
                self.launch_list.insert(iteration_count,launch)
                return
            iteration_count = iteration_count + 1

        #insert in the end of the list
        self.launch_list.append(launch)
        return

    def generate_dictionary_trough_list(self):
        """method that through the launch_list fills in the launches dictionary(self.launch_dict), only call this method after the method ordered_insertion_on_list() has been called"""
        iteration_count = 1
        for x in self.launch_list:
            self.launch_dict[iteration_count] = x
            iteration_count = iteration_count + 1
        return

    def __str__(self):
        return_str = "Launches dictionary:"

        for key, value in self.launch_dict.items():
            return_str += " key-- " + str(key) + " value-- "+ str(value)
        return return_str
