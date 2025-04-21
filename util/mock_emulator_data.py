import os

eligibility_main_menu = """
{
  "screenTitle": "HCS CCS PROCESSING",
  "applicationTitle": "HCS CORRECTIONAL MGMT WELLPATH",
  "current_date": "Thu Apr 10 2025",
  "current_time": "9:27",
  "user": "MANJUNATHA DODDEGOWD EL",
  "summary": "This is the main menu screen for HCS CCS Processing where users can select various options for claims and eligibility processing.",
  "menu_options": [
    {
      "option_number": "1",
      "option_text": "ACCESS WORKFLOW"
    },
    {
      "option_number": "2",
      "option_text": "CLAIMS/ELIGIBILITY"
    },
    {
      "option_number": "3",
      "option_text": "PROVIDER UTILITIES"
    },
    {
      "option_number": "4",
      "option_text": "GROUP MASTER"
    },
    {
      "option_number": "5",
      "option_text": "AUTHORIZATIONS"
    },
    {
      "option_number": "6",
      "option_text": "REPORTS"
    },
    {
      "option_number": "7",
      "option_text": "PRINT REPRICING SHEETS (801)"
    },
    {
      "option_number": "8",
      "option_text": "CHANGE UNDERWRITERS"
    },
    {
      "option_number": "9",
      "option_text": "LOG OFF SYSTEM"
    }
  ],
  "input_field": {
    "label": "Enter:",
    "value": "",
    "focus": true
  },
  "navigation_options": {
    "M": "Main Menu",
    "P": "Previous Menu",
    "I": "Information",
    "E": "Electronic Messages"
  }
}
"""

patient_search_selection = """
{
  "screenTitle": "PATIENT SEARCH SELECTION",
  "applicationTitle": "EMPLOYEE MASTER",
  "reviewStatus": "*REVIEW ONLY*",
  "organization": "HCS CORRECTIONAL MGMT WELLPATH",
  "summary": "This screen allows searching for patients by entering search criteria and pressing F3 to begin the search.",
  "search_fields": {
    "UNDERWRITER": "790",
    "GROUP": "***",
    "SSN/CERT": "",
    "LAST NAME": "",
    "FIRST NAME": "",
    "DATE OF BIRTH": "",
    "ADDRESS ONE": "",
    "ADDRESS TWO": "",
    "CITY": "",
    "STATE": "",
    "ZIP CODE": "",
    "ALTERNATE ID 1": "",
    "ALTERNATE ID 2": ""
  },
  "department_info": {
    "label": "DEPARTMENT",
    "options": "(E)MP/(B)OTH",
    "value": "B"
  },
  "input_field": {
    "label": "Press Credentials to begin searching for patient",
    "value": "",
    "focus": true
  },
  "navigation_options": {
    "F3": "Credentials",
    "back": "Return to Previous Screen"
  }
}
"""

patient_details = """
{
  "screenTitle": "GROUP INFO",
  "applicationTitle": "EMPLOYEE MASTER",
  "reviewStatus": "*REVIEW ONLY*",
  "organization": "HCS CORRECTIONAL MGMT WELLPATH",
  "summary": "This screen displays detailed patient information including demographics, status, and coverage details.",
  "group_info": {
    "GROUP": "136 790136",
    "ORGANIZATION": "PA DOC"
  },
  "patient_info": {
    "SOC SEC NBR": "997-13-3338",
    "CERT NUMBER": "BASLP1830",
    "FIRST NAME": "MARTWON",
    "GENDER": "M",
    "LAST NAME": "JOHNSON",
    "SUFFIX": "",
    "ADDRESS 1": "2500 LISBURN ROAD",
    "ADDRESS 2": "",
    "CITY/ST/ZIP": "CAMP HILL, PA 17001-",
    "DEPARTMENT": "0471",
    "WORK PHONE": "",
    "HOME PHONE": ""
  },
  "status_info": {
    "SEX": "M",
    "BIRTHDAY": "07/20/1992",
    "AGE": "32",
    "HIRED ON": "",
    "LST EFF DATE": "06/09/2021",
    "M/S": "",
    "MARRIED ON": "",
    "DEP": "N",
    "MC": "N",
    "TOV": "N",
    "UND": "N"
  },
  "status_history": [
    {
      "STATUS": "Active",
      "EFF DATE": "06/09/2021"
    },
    {
      "STATUS": "Termed",
      "EFF DATE": "02/12/2019"
    },
    {
      "STATUS": "Active",
      "EFF DATE": "02/01/2017"
    },
    {
      "STATUS": "Active",
      "EFF DATE": "01/01/2016"
    }
  ],
  "required_items": {
    "CARDS": "N",
    "CERTS": "N",
    "LABEL": "N",
    "HIPAA": "N"
  },
  "navigation_options": {
    "F6": "Notes",
    "F8": "HIPAA",
    "F7": "COBRA",
    "F3": "Continue",
    "back": "Return to Search"
  }
}
"""

search_patient_details = """
{
  "screenTitle": "GLOBAL SEARCH",
  "applicationTitle": "HCS CORRECTIONAL MGMT WELLPATH",
  "summary": "This screen displays the search results for patients and allows selection of a patient to view their details.",
  "header_info": {
    "UNDERWRITER": "790",
    "GROUP": "***"
  },
  "search_results": [
    {
      "name": "JOHNSON, M.",
      "details": {
        "P UND": "790",
        "GROUP": "136 790136",
        "SSN": "997-13-3338",
        "DOB": "07/20/1992",
        "STATUS": "ACTIVE",
        "GEN/SEX": "/M",
        "organization": "PA DOC",
        "cert": "BASLP1830",
        "full_name": "MARTWON JOHNSON",
        "address": "2500 LISBURN ROAD",
        "city_state": "CAMP HILL, PA 17001"
      }
    }
  ],
  "coverage_info": {
    "coverage_date": "06/09/2021",
    "products": [
      {
        "type": "MEDICAL",
        "coverage": "Y",
        "benefit": "790136A",
        "dep": "N",
        "cob": "N",
        "product": "N",
        "volume": "0"
      },
      {
        "type": "DENTAL",
        "coverage": "Y",
        "benefit": "790136A",
        "dep": "N",
        "cob": "N",
        "product": "N",
        "volume": "0"
      },
      {
        "type": "RX DRUG",
        "coverage": "N",
        "dep": "N",
        "product": "N",
        "volume": "0"
      },
      {
        "type": "VISION",
        "coverage": "N",
        "dep": "N",
        "product": "N",
        "volume": "0"
      },
      {
        "type": "FLEX",
        "coverage": "N",
        "dep": "N",
        "product": "N",
        "volume": "0"
      }
    ],
    "additional_coverage": {
      "WKLY INC": {
        "coverage": "N",
        "volume": "0",
        "product": "N",
        "value": "0"
      },
      "LONG TRM": {
        "coverage": "N",
        "volume": "0",
        "product": "N",
        "value": "0"
      }
    }
  },
  "navigation_options": {
    "F3": "Continue to Review Details",
    "back": "Return to Patient Details"
  }
}
"""

review_details = """
{
  "screenTitle": "REVIEW DETAILS",
  "applicationTitle": "HCS CORRECTIONAL MGMT WELLPATH",
  "summary": "This screen shows the final review details for the selected patient including coverage and benefit information.",
  "patient_info": {
    "name": "MARTWON JOHNSON",
    "id": "BASLP1830",
    "ssn": "997-13-3338",
    "dob": "07/20/1992",
    "status": "ACTIVE"
  },
  "coverage_details": {
    "medical": {
      "status": "Active",
      "plan": "790136A",
      "effective_date": "06/09/2021"
    },
    "dental": {
      "status": "Active",
      "plan": "790136A",
      "effective_date": "06/09/2021"
    }
  },
  "benefit_info": {
    "group": "136 790136",
    "organization": "PA DOC",
    "underwriter": "790"
  },
  "navigation_options": {
    "back": "Return to Search Patient Details"
  }
}
"""
