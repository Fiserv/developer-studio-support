# Meta Data

### What is Meta Data?
Meta data are the fields and pivots that comprise a report.  What fields a user would like to be shown in an itemized report or what pivots a user would like to use in a summary report. By calling the `metaData` API for a particular report type, the developer will get access to all the available fields and pivots to build their own customizable report. 

### Example Meta Data
```json
{
  "fields": [
    {
      "id": "a_approvalCode",
      "name": "Approval Status",
      "type": "Map",
      "description": "Identifies if the authorization was approved or declined.",
      "mapping": {
        "0": "Unknown",
        "1": "Approved",
        "2": "Declined"
      }
    },
    {
      "id": "a_transactionDateTime",
      "name": "Txn Date & Time",
      "type": "Time",
      "description": "Date & Time of the authorization transaction."
    },
    {
      "id": "a_accountNumber",
      "name": "Account #",
      "type": "String",
      "description": "Card number used for authorization transaction."
    },
    {
      "id": "a_amount",
      "name": "Amount",
      "type": "Double",
      "description": "Amount requested for the authorization transaction."
    }
  ],
  "filters": [
    {
      "field": "a_accountNumber",
      "type": "Text"
    },
    {
      "field": "a_network",
      "type": "Choice",
      "mapping": {
        "0": "Unknown",
        "1": "American Express",
        "2": "Visa",
        "3": "Mastercard",
        "4": "Discover",
        "5": "Pulse",
        "6": "Accel",
        "7": "Interlink",
        "8": "Jeanie",
        "9": "Maestro",
        "10": "NYCE",
        "11": "CU Alliance",
        "12": "Shazam",
        "13": "EBT",
        "14": "AFFN",
        "15": "Telecheck",
        "16": "Diners Club",
        "17": "PayPal",
        "18": "ValueLink",
        "19": "Private Label",
        "20": "Debit/Other",
        "21": "Voyager",
        "22": "ATH",
        "23": "JCB",
        "24": "Star",
        "25": "Star SE",
        "26": "Star W",
        "27": "Star Access",
        "28": "Fleet",
        "29": "Stored Value Systems (SVS)",
        "30": "Wright Express (WEX)",
        "31": "Incomm",
        "32": "Canadian Debit (Interac)",
        "33": "Not Applicable",
        "34": "Moneris",
        "35": "Vaulted Card",
        "36": "Pin-Authenticated Visa Debit (PAVD)",
        "37": "Mastercard MoneySend",
        "38": "Union Pay",
        "39": "Fraud FlexDetect",
        "40": "Certegy",
        "41": "MCI"
      }
    }
  ]
}
```
