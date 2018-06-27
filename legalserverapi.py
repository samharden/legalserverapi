import requests

class LegServ:
    ## Example:
    ## query = LegServ('username', 'password', 'domain')
    ## Note: make sure your username and password don't contain special characters

    def __init__(self, username, password, domain):
        self.un = username
        self.pw = password
        self.dm = domain
        self.initial_domain = "https://"+username+":"+password+"@"+domain

    def check_for_cases(self, name_to_query):

        name_to_query = name_to_query.replace(" ", "+")
        r = requests.get(self.initial_domain+"/matter/api/matter_search/?token="+name_to_query)
        r_json = r.json()
        results_list = r_json['results']
        final_list = []
        if len(results_list) > 0:
            for result in results_list:
                final_list.append(r_json['results'][0]['label'])

        print("List = ", final_list)
        return final_list


    def get_basic_case_info_by_name(self, name_to_query, return_value):

        ## Usage:
        ## query.get_basic_case_info_by_name('John Doe', 'id')

        ## returns the requested value(s) in a list

        name_to_query = name_to_query.replace(" ", "+")
        r = requests.get(self.initial_domain+"/matter/api/basic_case_info/?client_name="+name_to_query)
        r_json = r.json()
        results_list = r_json['results']
        final_list = []
        if len(results_list) > 0:
            for result in results_list:
                final_list.append(r_json['results'][0][return_value]['text_value'])
            # LegServ.json_values_to_list(final_list, return_value, results_list, r_json)
        else:
            final_list.append("Sorry, no results")

        return final_list

    def create_case_note(self, case_number, note):
        try:
            r = requests.post(self.initial_domain+"/matter/api/create_case_note/?case_number="+case_number+"&note="+note)
        except Exception as e:
            print(str(e))

    def help_me(self):
        print("""
        Available methods: \n
        create_case_note(self, case_number, note)
        get_basic_case_info_by_name(self, name_to_query, return_value)
        check_for_cases(self, name_to_query)
        \n
        Available return_value(s) for get_basic_case_info_by_name:\n
        "id"
        "full_name"
        "county"
        "addr1"
        "phone_home"
        "phone_business"
        "phone_fax"
        "phone_mobile"
        "phone_other"
        "legal_problem_code"
        "unique_id"
        "dob"\n
        "identification_number"
        "email"
        "current_disposition"
        "date_open"
        "close_date"
        "close_reason"
        "disposition_status"
        "disposition_date"
        "primary_advocate"
        "url"
        """)
