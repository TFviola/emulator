import os


switched_off = """
            *   The screen displays "Switched OFF".
*   The instruction on the screen is "Send START to switch ON."

```json
{
  "screen_state": "OFF",
  "instructions": "Send START to switch ON"
}
```
        """

login = """
{
  "os_name": "Red Hat Enterprise Linux release 8.5 (Ootpa) (x86_64)",
  "kernel_version": "Linux PPR-ELDHCS01 4.18.0-348.12.2.e18_5.x86_64 x86_64",
  "logged_in_user": "mdoddegowd",
  "application_title": "HCS CORRECTIONAL MANAGEMENT LLC",
  "menu_options": [
    {
      "selection_key": "1",
      "selection_value": "HEALTHpac 4.0 Production"
    },
    {
      "selection_key": "9",
      "selection_value": "Logout"
    }
  ],
  "input_prompt": "Enter selection please >",
  "screen_type": "Menu"
}
"""

# login_prompt = "You are a senior business process executive trainer that uses Mainframe application. Your task is to analyse the given screen and generate a properly formatted JSON data (all in first level plain key-value pair). Assume your output will be consumed by automation tools and junior executives. Give importance to navigation options, notification, alerts and currently selected or focussed input fields with one liner tooltip instruction so tools can make proper decision. Put tabular data or list of items in an array of object. Have one field that has a concise summary (just a sentence) of what this screen is meant for and what user is expected to do. Below is the screenshot:"

# login="""
# {
#   "application_title": "Healthpac Systems",
#   "company_name": "Eldorado Computing, Inc.",
#   "screen_title": "WELCOME",
#   "system_name": "Healthpac IV Health Care Management System",
#   "company_division": "Health Cost Solutions, Inc. A Division of MPHASIS Inc.",
#   "release_version": "4.21.01",
#   "login_prompt": "PLEASE LOG INTO THE SYSTEM",
#   "login_instructions": "ENTER YOUR USERCODE AND YOUR PASSWORD",
#   "username_field_label": "USERCODE",
#   "username_field_focus": true,
#   "password_field_label": "PASSWORD",
#   "copyright_notice": "(c) Copyright 2003 - Eldorado Computing, Inc. All Rights Reserved",
#   "notifications": [],
#   "alerts": [],
#   "input_fields": [
#     {
#       "field_name": "username",
#       "field_type": "text",
#       "is_focused": true,
#       "data": ""
#     },
#     {
#       "field_name": "password",
#       "field_type": "password",
#       "is_focused": false,
#       "data": ""
#     }
#   ],
#   "navigation_options": []
# }
# """

main_menu = """
{
  "application_name": "HEALTHpac",
  "application_version": "4.21.01",
  "screen_title": "HCS CCS Processing",
  "current_date": "Wed Feb 19 2025",
  "current_time": "6:06",
  "user": "MANJUNATHA DODDEGOWD EL",
  "organization": "HCS CORRECTIONAL MGMT WELLPAT",
  "summary": "This is the main menu screen for HCS CCS Processing where users can select various options to manage claims, access workflows, generate reports and other administrative tasks.",
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
  "input_field_label": "Enter:",
  "input_field": "",
  "input_field_tooltip": "Enter the number corresponding to the desired menu option and press Enter.",
  "navigation_options": {
    "M": "Main Menu",
    "P": "Previous Menu",
    "I": "Information",
    "E": "Electronic Messages"
  },
  "notifications": [],
  "alerts": []
}
"""

first_workflow_queue = """
{
  "screenTitle": "WORKFLOW QUEUES",
  "screenFocus": "***SELECT***",
  "applicationName": "HCS CORRECTIONAL MGMT WELLPATH",
  "userQueuesHeader": "MDODDE'S QUEUES",
  "summary": "This screen displays a list of workflow queues for the user 'MDODDE', allowing the user to select a queue to access its associated jobs. User can use the number 1 to 5, or the arrow up or down keys to navigate.",
  "queueList": [
    {
      "selectionNumber": "1",
      "queueName": "CCH-790136",
      "queueDescription": "PA DOC P1",
      "jobs": "T",
      "isFocussed": true
    },
    {
      "selectionNumber": "2",
      "queueName": "CCH-ARDOC",
      "queueDescription": "ARDOC EFF 1/1/2020 NO BCBS"
    },
    {
      "selectionNumber": "3",
      "queueName": "CCH-CA",
      "queueDescription": "ALL CA SITES HCFA'S"
    },
    {
      "selectionNumber": "4",
      "queueName": "CCH-CA UB",
      "queueDescription": "ALL CA SITES UB'S"
    },
    {
      "selectionNumber": "5",
      "queueName": "CCH-MDCARE",
      "queueDescription": "MEDICARE SITES HCFA AND UBS"
    }
  ],
  "navigationHelp": "Arrow up/down",
  "accessInstruction": "1 Enter to access",
  "footerOptions": {
    "main": "(M)ain",
    "prior": "(P)rior",
    "resume": "(R)esume",
    "detail": "(D)etail",
    "jobCount": "(J)ob count",
    "search": "(S)earch",
    "list": "(L)ist"
  }
}
"""

record_details = """
{
  "screenTitle": "Workflow Queues",
  "applicationTitle": "HCS Correctional Mgmt Wellpath",
  "screenPurpose": "This screen displays a list of workflow queues for the HCS Correctional Management system, allowing the user to select a queue for further action.",
  "instructionBanner": "***SELECT***",
  "columnHeaders": [
    "SEL",
    "ORG DATE",
    "DT TO",
    "Q TIME",
    "TYPE",
    "PA DOC",
    "P1",
    "RECORD DETAIL",
    "EX EX/ TP",
    "PND DUE DT",
    "IMG"
  ],
  "queueItems": [
    {
      "SEL": "A",
      "ORG DATE": "04/07/25",
      "DT TO": "04/14/25",
      "Q TIME": "06:29",
      "TYPE": "RPC",
      "PA DOC": "790",
      "P1": "136",
      "RECORD DETAIL": "225-050468-00",
      "EX EX/ TP": "PV NPR",
      "PND DUE DT": null,
      "IMG": "Y"
    },
    {
      "SEL": "B",
      "ORG DATE": "04/07/25",
      "DT TO": "04/08/25",
      "Q TIME": "06:19",
      "TYPE": "RPC",
      "PA DOC": "790",
      "P1": "136",
      "RECORD DETAIL": "225-050470-00",
      "EX EX/ TP": "PV NPR",
      "PND DUE DT": null,
      "IMG": "Y"
    },
    {
      "SEL": "C",
      "ORG DATE": "04/07/25",
      "DT TO": "04/08/25",
      "Q TIME": "06:19",
      "TYPE": "RPC",
      "PA DOC": "790",
      "P1": "136",
      "RECORD DETAIL": "225-050473-00",
      "EX EX/ TP": "PV NPR",
      "PND DUE DT": null,
      "IMG": "Y"
    },
    {
      "SEL": "D",
      "ORG DATE": "04/07/25",
      "DT TO": "04/14/25",
      "Q TIME": "06:28",
      "TYPE": "RPC",
      "PA DOC": "790",
      "P1": "136",
      "RECORD DETAIL": "225-050474-00",
      "EX EX/ TP": "EP EMM",
      "PND DUE DT": null,
      "IMG": "Y"
    },
    {
      "SEL": "E",
      "ORG DATE": "04/07/25",
      "DT TO": "04/08/25",
      "Q TIME": "06:19",
      "TYPE": "RPC",
      "PA DOC": "790",
      "P1": "136",
      "RECORD DETAIL": "224-408504-00",
      "EX EX/ TP": "PV NPR",
      "PND DUE DT": null,
      "IMG": "Y"
    },
    {
      "SEL": "F",
      "ORG DATE": "04/07/25",
      "DT TO": "04/08/25",
      "Q TIME": "06:19",
      "TYPE": "RPC",
      "PA DOC": "790",
      "P1": "136",
      "RECORD DETAIL": "225-050480-00",
      "EX EX/ TP": "PV NPR",
      "PND DUE DT": null,
      "IMG": "Y"
    },
    {
      "SEL": "G",
      "ORG DATE": "04/07/25",
      "DT TO": "04/08/25",
      "Q TIME": "06:19",
      "TYPE": "RPC",
      "PA DOC": "790",
      "P1": "136",
      "RECORD DETAIL": "225-050481-00",
      "EX EX/ TP": "PV NPR",
      "PND DUE DT": null,
      "IMG": "Y"
    },
    {
      "SEL": "H",
      "ORG DATE": "04/07/25",
      "DT TO": "04/08/25",
      "Q TIME": "06:19",
      "TYPE": "RPC",
      "PA DOC": "790",
      "P1": "136",
      "RECORD DETAIL": "225-050482-00",
      "EX EX/ TP": "PV NPR",
      "PND DUE DT": null,
      "IMG": "Y"
    },
    {
      "SEL": "I",
      "ORG DATE": "04/07/25",
      "DT TO": "04/08/25",
      "Q TIME": "06:19",
      "TYPE": "RPC",
      "PA DOC": "790",
      "P1": "136",
      "RECORD DETAIL": "225-050484-00",
      "EX EX/ TP": "PV NPR",
      "PND DUE DT": null,
      "IMG": "Y"
    },
    {
      "SEL": "J",
      "ORG DATE": "04/07/25",
      "DT TO": "04/08/25",
      "Q TIME": "06:19",
      "TYPE": "RPC",
      "PA DOC": "790",
      "P1": "136",
      "RECORD DETAIL": "225-050486-00",
      "EX EX/ TP": "PV NPR",
      "PND DUE DT": null,
      "IMG": "Y"
    },
    {
      "SEL": "K",
      "ORG DATE": "04/07/25",
      "DT TO": "04/08/25",
      "Q TIME": "06:19",
      "TYPE": "RPC",
      "PA DOC": "790",
      "P1": "136",
      "RECORD DETAIL": "225-050487-00",
      "EX EX/ TP": "PV NPR",
      "PND DUE DT": null,
      "IMG": "Y"
    },
    {
      "SEL": "L",
      "ORG DATE": "04/07/25",
      "DT TO": "04/08/25",
      "Q TIME": "06:19",
      "TYPE": "RPC",
      "PA DOC": "790",
      "P1": "136",
      "RECORD DETAIL": "225-050488-00",
      "EX EX/ TP": "PV NPR",
      "PND DUE DT": null,
      "IMG": "Y"
    },
    {
      "SEL": "M",
      "ORG DATE": "04/07/25",
      "DT TO": "04/08/25",
      "Q TIME": "06:19",
      "TYPE": "RPC",
      "PA DOC": "790",
      "P1": "136",
      "RECORD DETAIL": "225-050490-00",
      "EX EX/ TP": "PV NPR",
      "PND DUE DT": null,
      "IMG": "Y"
    },
    {
      "SEL": "N",
      "ORG DATE": "04/07/25",
      "DT TO": "04/08/25",
      "Q TIME": "06:19",
      "TYPE": "RPC",
      "PA DOC": "790",
      "P1": "136",
      "RECORD DETAIL": "225-050491-00",
      "EX EX/ TP": "PV NPR",
      "PND DUE DT": null,
      "IMG": "Y"
    },
    {
      "SEL": "O",
      "ORG DATE": "04/07/25",
      "DT TO": "04/08/25",
      "Q TIME": "06:19",
      "TYPE": "RPC",
      "PA DOC": "790",
      "P1": "136",
      "RECORD DETAIL": "225-050493-00",
      "EX EX/ TP": "PV NPR",
      "PND DUE DT": null,
      "IMG": "Y"
    }
  ],
  "inputFieldLabel": "ENTER SELECTION:",
  "inputFieldValue": null,
  "inputFieldTooltip": "Enter the selection code (A-O) corresponding to the desired workflow queue and press Enter.",
  "urgencyNote": "* = Urgent"
}
"""


# claim_details= """
# json
# {
#   "summary": "This screen contains claim information and details for a patient. It includes claim status, dates, amounts, and provider information.",
#   "CLAIM INFORMATION": {
#     "TY": "MM",
#     "CLAIM NUMBER": "222-483371-00",
#     "STATUS OF CLAIM": "PAID 11/15/22 KARRIE",
#     "RECEIVED": "11/04/22",
#     "INCURRED": "10/22/22",
#     "PLAN ID": "790216A",
#     "EFFECTIVE": "02/01/17",
#     "DGN": "S01",
#     "DESCRIPTION": "Open wound of h",
#     "ICD": "s01.01XA",
#     "YEAR": "2022",
#     "UND/GROUP CODES": "790 790216",
#     "NETWK": "CMA",
#     "CLAIM SOURCE": "EDI 11/07/22"
#   },
#   "CLAIM DETAILS": [
#     {
#       "BEN": "780",
#       "FROM DOS": "10/22/22",
#       "VISIT": "1",
#       "CHARGE AMT": "1025.00",
#       "DISALLOWED": "1025.00",
#       "DEDUCTIBLE": ".00",
#       "PCT": "0",
#       "PAYMENT": ".00",
#       "type": "P"
#     },
#     {
#       "BEN": "780",
#       "FROM DOS": "10/22/22",
#       "VISIT": "1",
#       "CHARGE AMT": "750.00",
#       "DISALLOWED": "750.00",
#       "DEDUCTIBLE": ".00",
#       "PCT": "0",
#       "PAYMENT": ".00",
#       "type": "P"
#     }
#   ],
#   "TOTALS": {
#     "CHARGE AMT": "1775.00",
#     "DISALLOWED": "1775.00",
#     "DEDUCTIBLE": ".00",
#     "PAYMENT": ".00"
#   },
#   "ADJUSTMENTS": {
#     "ADJ": ".00",
#     "COB ADJ": ".00",
#     "W/HOLD": ".00",
#     "TOT": ".00"
#   },
#   "PARTY INFORMATION": {
#     "PATIENT": {
#       "TAX ID": "593677604",
#       "EMPLOYEE/PATIENT": "TAMPA BAY EMERGENCY PHYSICIANS / (self)"
#     },
#     "PROVIDER": {
#       "TAX ID": null,
#       "PROVIDER": "TAMPA BAY EMERGENCY PHYSICIANS"
#     },
#     "ALT PAYEE": null,
#     "CHECK NO": null,
#     "NET PAYMENT": [
#       ".00",
#       ".00",
#       ".00",
#       ".00"
#     ]
#   },
#   "NAVIGATION": {
#     "Back": ScreenNames.AW_Jobs,
#     "SELECT": "Choose an option",
#     "OPTIONS": [
#       "(M)ain",
#       "(P)rior",
#       "(R)esume",
#       "(V)iew",
#       "(0)ptions",
#       "(F)ind"
#     ],
#     "focussed": null
#   },
#   "ALERTS": {
#     "IMAGE AVAILABLE": true,
#     "E-PAY INFO": "--->",
#     "CLAIM NOTES EXIST": true
#   }
# }
# """

claim_details= """
{
  "summary": "This screen displays claim details and allows users to view information such as claim status, charges, payments, patient and provider details.",
  "CLAIM INFORMATION": {
    "TY": "MM",
    "CLAIM NUMBER": "225-050474-00",
    "STATUS OF CLAIM": "EXC 04/08/25 HAL",
    "RECEIVED": "04/07/25",
    "INCURRED": "03/31/25",
    "PLAN ID": "790136A",
    "EFFECTIVE": "02/01/17",
    "REPRICING METHOD": "External sent EDI",
    "ICD": "J01.90",
    "YEAR": "2025",
    "UND/GROUP CODES": "790 790136",
    "NETWORK": "CMA",
    "CLAIM SOURCE": "EDI 04/08/25"
  },
  "CLAIM DETAILS": [
    {
      "FROM DOS": "03/31/25",
      "PROCED": "36415",
      "UNITS": "1",
      "CHARGE AMT": "26.00",
      "DISCOUNT AMT": "26.00",
      "REPRICED AMT": ".00",
      "O.I. PAID": ".00"
    },
    {
      "FROM DOS": "03/31/25",
      "PROCED": "84484",
      "UNITS": "1",
      "CHARGE AMT": "144.00",
      "DISCOUNT AMT": "144.00",
      "REPRICED AMT": ".00",
      "O.I. PAID": ".00"
    },
    {
      "FROM DOS": "03/31/25",
      "PROCED": "83880",
      "UNITS": "1",
      "CHARGE AMT": "284.00",
      "DISCOUNT AMT": "284.00",
      "REPRICED AMT": ".00",
      "O.I. PAID": ".00"
    },
    {
      "FROM DOS": "03/31/25",
      "PROCED": "83690",
      "UNITS": "1",
      "CHARGE AMT": "55.00",
      "DISCOUNT AMT": "55.00",
      "REPRICED AMT": ".00",
      "O.I. PAID": ".00"
    },
    {
      "FROM DOS": "03/31/25",
      "PROCED": "83605",
      "UNITS": "1",
      "CHARGE AMT": "97.00",
      "DISCOUNT AMT": "97.00",
      "REPRICED AMT": ".00",
      "O.I. PAID": ".00"
    },
    {
      "FROM DOS": "03/31/25",
      "PROCED": "80053",
      "UNITS": "1",
      "CHARGE AMT": "122.00",
      "DISCOUNT AMT": "122.00",
      "REPRICED AMT": ".00",
      "O.I. PAID": ".00"
    },
    {
      "FROM DOS": "03/31/25",
      "PROCED": "85730",
      "UNITS": "1",
      "CHARGE AMT": "49.00",
      "DISCOUNT AMT": "49.00",
      "REPRICED AMT": ".00",
      "O.I. PAID": ".00"
    },
    {
      "FROM DOS": "03/31/25",
      "PROCED": "85610",
      "UNITS": "1",
      "CHARGE AMT": "38.00",
      "DISCOUNT AMT": "38.00",
      "REPRICED AMT": ".00",
      "O.I. PAID": ".00"
    },
    {
      "FROM DOS": "03/31/25",
      "PROCED": "85025",
      "UNITS": "1",
      "CHARGE AMT": "70.00",
      "DISCOUNT AMT": "70.00",
      "REPRICED AMT": ".00",
      "O.I. PAID": ".00"
    },
    {
      "FROM DOS": "03/31/25",
      "PROCED": "71046",
      "UNITS": "1",
      "CHARGE AMT": "298.00",
      "DISCOUNT AMT": "207.28",
      "REPRICED AMT": "90.72",
      "O.I. PAID": ".00"
    },
    {
      "FROM DOS": "03/31/25",
      "PROCED": "70486",
      "UNITS": "1",
      "CHARGE AMT": "1457.00",
      "DISCOUNT AMT": "1347.44",
      "REPRICED AMT": "109.56",
      "O.I. PAID": ".00"
    }
  ],
  "CLAIM TOTALS": {
    "CHARGE AMT": "5567.95",
    "DISCOUNT AMT": "4470.61",
    "REPRICED AMT": "1097.34",
    "O.I. PAID": ".00"
  },
  "PARTY INFORMATION": {
    "PATIENT": {
      "TAX ID": "997083174",
      "EMPLOYEE/PATIENT": "SEAY, BILLY (Self)"
    },
    "PROVIDER": {
      "TAX ID": "231352159",
      "PROVIDER": "PENN HIGHLANDS HUNTINGDON"
    }
  },
  "NAVIGATION": {
    "OPTIONS": [
      "(M)ain",
      "(P)rior",
      "(R)esume",
      "(F)ind",
      "(V)iew",
      "(O)ptions"
    ]
  },
  "ALERTS": {
    "IMAGE AVAILABLE": true,
    "CLM NOTES AVAILABLE": true
  }
}
"""


select_options = """
{
  "screen_title": "Select Details to View",
  "options": [
    {
      "key": "S",
      "description": "Service line details"
    },
    {
      "key": "G",
      "description": "Group Information"
    },
    {
      "key": "E",
      "description": "Employee Information"
    },
    {
      "key": "B",
      "description": "Benefit Accumulators"
    },
    {
      "key": "P",
      "description": "Provider Information"
    },
    {
      "key": "R",
      "description": "exception Reasons"
    },
    {
      "key": "I",
      "description": "claim Images"
    },
    {
      "key": "L",
      "description": "benefit pLan details"
    },
    {
      "key": "H",
      "description": "claims History"
    },
    {
      "key": "N",
      "description": "claim Notes"
    },
    {
      "key": "A",
      "description": "Audit history of claim changes"
    },
    {
      "key": "V",
      "description": "View additional service lines"
    }
  ],
  "right_panel": [
    {
      "key": "U",
      "description": "view previous service lines"
    },
    {
      "key": "Y",
      "description": "summary screen"
    }
  ],
  "input_field": {
    "label": "ENTER OPTION",
    "value": "",
    "focus": true
  },
  "patient_info": {
    "name": "SEAY, BILLY (Self)",
    "provider": "PENN HIGHLANDS HUNTINGDON"
  },
  "alerts": {
    "IMAGE": "AVAILABLE",
    "CLM NOTES": "AVAILABLE"
  }
}
"""

workflow_images = """
{
  "screenTitle": "WORKFLOW QUEUES",
  "applicationTitle": "HCS CORRECTIONAL MGMT WELLPATH",
  "screenPurpose": "This screen displays available images for the selected claim or workflow item.",
  "instructionBanner": "*** IMAGES ***",
  "columnHeaders": [
    "SEL",
    "RECEIVED",
    "IMAGE TYPE",
    "DESCRIPTION OF AVAILABLE IMAGE"
  ],
  "imageItems": [
    {
      "SEL": "A",
      "RECEIVED": "04/07/2025",
      "IMAGE_TYPE": "Unknown",
      "DESCRIPTION": "No further images available"
    }
  ],
  "inputFieldLabel": "ENTER SELECTION",
  "inputFieldValue": null,
  "inputFieldTooltip": "Enter the selection code (A) to view the image",
  "navigationOptions": {
    "back": "Return to previous screen",
    "main": "Return to main menu"
  }
}
"""








