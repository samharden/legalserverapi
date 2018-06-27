## Legal Server API Package

### Example:
#### >>> from legalserverapi import LegServ
#### >>> query = LegServ('username', 'password', 'domain')
#### (Note: make sure your username and password don't contain special characters)
#### >>> query.get_basic_case_info_by_name('John Doe', 'id')

### Parameters For All Methods
  - output_format – Optional – json|xml – defaults to json

### Basic Case Information Lookup

#### URL: /matter/api/basic_case_info/
#### Permissons Required: API Basic Case Information
#### Parameters:
- caseid – Optional – LegalServer Case ID
- client_name – Optional – Client's name (First, Middle, and Last Name, with suffix)
- ssn – Optional – Client's Social Security Number (SSN)
- dob – Optional – Client's Date of Birth (DOB)
#### Examples:
- /matter/api/basic_case_info/?caseid=17-00000255
- /matter/api/basic_case_info/?client_name=Jane+Doe
- /matter/api/basic_case_info/?caseid=17-00000255&client_name=Jane+Doe
- /matter/api/basic_case_info/?ssn=123-45-6789&dob=1/23/1945

### List most recently viewed matters

#### URL: /matter/api/recent_matters/
#### Permissons Required: N/A


### Search for a case by id or name

#### URL: /matter/api/matter_search/
#### Permissons Required: N/A
#### Parameters:
- token – Required – Search query
#### Examples:
- /matter/api/matter_search/?token=smith
- /matter/api/matter_search/?token=17-00000255

### Caller ID Search

#### URL: /matter/api/caller_id_search/
#### Permissons Required: API Search Cases By Phone
#### Parameters:
- number – Required – Phone number to search for. Anything non-numeric is ignored.
#### Examples:
- /matter/api/caller_id_search/?number=1-212-555-1212&output_format=json

### Create Case Note

#### URL: /matter/api/create_case_note/
#### Permissons Required: API Create Case Note
#### Parameters:
- case_number – Optional – The case number to write the note to.
- note – Required – The contents of the note to create.
#### Examples:
- /matter/api/create_case_note?output_format=json

### Online Intake Trigger

#### URL: /matter/api/online_intake_trigger/
#### Permissons Required: API Create Online Intake
#### Parameters:
- first – Optional – First name
- middle – Optional – Middle name
- last – Optional – Last name
- suffix – Optional – Suffix
- phone_mobile – Optional – Mobile phone
#### Examples:
- /matter/api/online_intake_trigger?output_format=json

### Pro Bono Opportunities

#### URL: /matter/api/pro_bono_opportunities/
#### Permissons Required: API Search Pro Bono Opportunities
#### Parameters:
- county – Optional – The county to search within.
- organization – Optional – Only show PBOs within a given organization.
- problem – Optional – Only show PBOs with this legal problem code.
- status – Optional – Only show PBOs with this status.
- offset – Optional – Start after N records. (Useful for pagination.)
- limit – Optional – How many results to fetch. (Default: 20)
#### Examples:
/matter/api/pro_bono_opportunities/?county=King&problem=01&output_format=json


### Get My Case Status by Phone

#### URL: /matter/api/ivr_case_status/
#### Permissons Required: API Search Cases By Phone
#### Parameters:
- case_number – Optional – The case number to search for.
- client_ssn – Optional – The client's social security number to search for.
- client_ssn_last4 – Optional – The last 4 digits of the client's social security number.
- client_dob – Optional – The clients date of birth to search for.
#### Examples:
- /matter/api/ivr_case_status?output_format=json


### Get Available Appointments for Online Intake Scheduling.

#### URL: /matter/api/oi_appt_slots/
#### Permissons Required: API Search Cases By Phone
#### Parameters:
- identification_number – Optional – Online Intake Matter ID.
- etransfer_id – Optional – The clients E­Transfer ID.
- slot_id – Optional – Calendar Slot ID (that it is taking).
- action – Optional – An optional paramater for custom use.
#### Examples:
- /matter/api/oi_appt_slots?output_format=json


### Get Available Event Slots for Clinics Scheduling.

#### URL: /matter/api/oi_clinic_event_appointments/
#### Permissons Required: API Search Cases By Phone
#### Parameters:
- identification_number – Optional – Online Intake Matter ID.
- start_date – Optional – The date to search after
- problem_code_id – Optional – The Clients Problem Code ID.
- slot_id – Optional – Event Slot ID (that it is taking).
- action – Optional – An optional paramater for custom use.
#### Examples:
- /matter/api/oi_clinic_event_appointments?output_format=json


### My Cases

#### URL: /matter/api/my_cases/
#### Permissons Required: API Search Pro Bono Opportunities
#### Parameters:
- assignment – Optional – The person assigned to the case.
- county – Optional – The county to search within.
- organization – Optional – Only show PBOs within a given organization.
- problem – Optional – Only show PBOs with this legal problem code.
- status – Optional – Only show PBOs with this status.
- offset – Optional – Start after N records. (Useful for pagination.)
- limit – Optional – How many results to fetch. (Default: 20)
#### Examples:
- /matter/api/my_cases/?assignment=32&county=King&problem=01&output_format=json


### My Pro Bono Opportunities

#### URL: /matter/api/my_opportunities/
#### Permissons Required: API Search Pro Bono Opportunities
#### Parameters:
- assignment – Optional – The person assigned to the opportunity.
- county – Optional – The county to search within.
- organization – Optional – Only show PBOs within a given organization.
- problem – Optional – Only show PBOs with this legal problem code.
- status – Optional – Only show PBOs with this status.
- offset – Optional – Start after N records. (Useful for pagination.)
- limit – Optional – How many results to fetch. (Default: 20)
#### Examples:
- /matter/api/my_opportunities/?assignment=32&county=King&problem=01&output_format=json


### Basic Admin Information Lookup

#### URL: /matter/api/basic_admin_info/
#### Permissons Required: API Basic Case Information
#### Parameters:
- caseid – Optional – LegalServer Case ID
#### Examples:
- /matter/api/basic_admin_info/?caseid=255


### Pending Case List

#### URL: /matter/api/pending_case_info/
#### Permissons Required: API Basic Case Information
#### Parameters:
- caseid – Optional – LegalServer Case ID
#### Examples:
- /matter/api/pending_case_info/?caseid=255


### Case List by Disposition

#### URL: /matter/api/get_case_info/
#### Permissons Required: API Basic Case Information
#### Parameters:
- disposition – Required – LegalServer Case Disposition
#### Examples:
- /matter/api/get_case_info/?disposition=open


### Basic Information Lookup

#### URL: /matter/api/basic_bigsky_info/
#### Permissons Required: API Basic Case Information
#### Parameters:
- caseid – Optional – LegalServer Case ID
#### Examples:
- /matter/api/basic_bigsky_info/?caseid=255


### Get Pro Bono Opportunity

#### URL: /matter/api/get_opportunity/
#### Permissons Required: API Basic Case Information
#### Parameters:
- caseid – Optional – LegalServer Case ID
#### Examples:
- /matter/api/get_opportunity/?caseid=255


### Take Pro Bono Opportunity

#### URL: /matter/api/take_opportunity/
#### Permissons Required: API Basic Case Information
#### Parameters:
- caseid – Optional – LegalServer Case ID
- userid – Optional – LegalServer User ID
#### Examples:
- /matter/api/take_opportunity/?caseid=42&userid=32


### Release Pro Bono Opportunity

#### URL: /matter/api/release_opportunity/
#### Permissons Required: API Basic Case Information
#### Parameters:
- caseid – Required – LegalServer Case ID
#### Examples:
- /matter/api/release_opportunity/?caseid=47


### Take Pro Bono Opportunity

#### URL: /matter/api/answer_opportunity/
#### Permissons Required: API Basic Case Information
#### Parameters:
- caseid – Required – LegalServer Case ID
- userid – Required – LegalServer User ID
- problem – Optional – LegalServer Problem Code ID
- answer – Required – The volunteers answer to a client question
#### Examples:
- /matter/api/answer_opportunity/?caseid=42&userid=32&answer=my question response


### Get Pro Bono Opportunity Status Note

#### URL: /matter/api/get_opportunity_answer/
#### Permissons Required: API Basic Case Information
#### Parameters:
- caseid – Required – LegalServer Case ID
#### Examples:
- /matter/api/get_opportunity_answer/?caseid=42


### Set Pro Bono Opportunity

#### URL: /matter/api/set_opportunity/
#### Permissons Required: API Basic Case Information
#### Parameters:
- caseid – Required – LegalServer Case ID
- summary – Required – A breief summary of the question or issue
- question – Required – A detailed description of your question or issue
#### Examples:
- /matter/api/set_opportunity/?caseid=255&summary=summary of my question&question=my detailed question

### Create New User

#### URL: /matter/api/new_user/
#### Permissons Required: API Basic Case Information
#### Parameters:
- first – Required – User First Name
- last – Required – User Last Name
- login – Optional – User Login Name
#### Examples:
- /matter/api/new_user/?first=Lucious&last=DuFrain&login=ldufrain1
