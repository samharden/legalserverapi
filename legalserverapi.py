import requests

class LegServ:

    ## Note: make sure your username and password don't contain special characters

    def __init__(self, username, password, domain):
        self.un = username
        self.pw = password
        self.dm = domain
        self.initial_domain = "https://"+username+":"+password+"@"+domain

    def __str__(self):
        return self.un, self.pw, self.initial_domain


class Person(LegServ):

    ## Example: new_client_1 = Person('username', 'password', 'domain.legalserver.org', 'John', 'Doe')

    def __init__(self, username, password, domain, firstname, lastname):
        LegServ.__init__(self, username, password, domain)
        self.firstname = firstname
        self.lastname = lastname

    def check_for_cases(self):

        ## new_client_1.check_for_cases()

        name_to_query = self.firstname+"+"+self.lastname
        r = requests.get(self.initial_domain+"/matter/api/matter_search/?token="+name_to_query)
        r_json = r.json()
        results_list = r_json['results']
        final_list = []
        if len(results_list) > 0:
            for result in results_list:
                final_list.append(r_json['results'][0])
        return final_list


    def get_basic_case_info_by_name(self, return_value):
        ## new_client_1.get_basic_case_info_by_name('id')
        ## returns the requested value(s) in a list

        name_to_query = self.firstname+"+"+self.lastname
        r = requests.get(self.initial_domain+"/matter/api/basic_case_info/?client_name="+name_to_query)
        r_json = r.json()
        results_list = r_json['results']
        final_list = []
        if len(results_list) > 0:
            for result in results_list:
                final_list.append(r_json['results'][0][return_value]['text_value'])

        else:
            final_list.append("Sorry, no results")

        return final_list

    def create_case_note(self, note):
        ## creates a case note
        ## new_client_1.create_case_note('Hi this is a note')

        case_number = Person.get_basic_case_info_by_name(self, 'identification_number')[0]
        try:
            r = requests.post(self.initial_domain+"/matter/api/create_case_note/?case_number="+case_number+"&note="+note)
        except Exception as e:
            print(str(e))

    def set_probono_opportunity(self, summary, question):
        case_number = Person.get_basic_case_info_by_name(self, 'id')[0]
        try:
            r = requests.post(self.initial_domain+"/matter/api/set_opportunity/?caseid="+case_number+"&summary="+summary+"&question="+question)
            print(r.json())
        except Exception as e:
            print(str(e))

    def basic_admin_info(self):
        case_number = Person.get_basic_case_info_by_name(self, 'id')[0]
        try:
            r = requests.get(self.initial_domain+"/matter/api/basic_admin_info/?caseid="+case_number)
            return r.json()['results']
        except Exception as e:
            print(str(e))

    def online_intake_trigger(self, firstname, middlename, lastname):
        ### creates an online intake
        try:
            r = requests.post(self.initial_domain+"/matter/api/online_intake_trigger/?first="+firstname+"&middle="+middlename+"&last="+lastname)
            print(r.json())
        except Exception as e:
            print(str(e))



    def help(self):
        print("""
        Available methods: \n
            create_case_note(self, case_number, note)
            get_basic_case_info_by_name(self, name_to_query, return_value)
            check_for_cases(self, name_to_query)
            create_case(xml_file)
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
