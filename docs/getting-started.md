# Getting Started 

## Welcome to Reporting

The Fiserv Reporting APIs are built on the foundation of REST. The APIs accept standard JSON requests and return JSON encoded responses while leveraging industry standard [HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) for a seamless integration. Reporting through CLX APIs provides the developer community the ability to retrieve transaction, chargeback, funding and settlement information in a simple and intuitive manner. You will find that access to itemized or summary data can be quickly initiated programmatically for statistical analysis purposes. 

## Authentication
Fiserv Reporting API authentication is based on the API keys concept. Each consumer will be assigned their own set of API keys that allow message passing to and from the exposed RESTful interface. Your API keys restrict data to only the owners of that data set. 

Your assigned API keys perform an [HTTP Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication) by passing the assigned key via the request header. 

### Authenticated Request
```javascript
curl -X GET "https://cat.api.firstdata.com/reporting/fraud/search/getMetaData" -H "accept: application/json" -H "apikey: YOURAPIKEY"
```

For more information on creating and using API keys for your organization, please click [here](https://www.google.com). 

# Domain Models

## What are Domain Models?
Domain models represent the type of data that you may be interested in.  IE authorization transactions, chargebacks, etc. Reporting supports the following domain models. 

### Authorizations 
>Authorizations refers to the transactions as soon as they are received by the receiving end point. An authorization can either be Approved or Declined. There are many details associated with the transaction that will determine where the authorization is ultimately routed to. The transaction details are captured in this report.

### Chargebacks
>The Disputes Overview provides an overview of Outstanding, Reversed, and Closed Chargebacks. Merchants can quickly see the total number of Open, Fulfilled, and Expired Retrievals, as well as the total number of Chargebacks that are Open, Closed, and Reversed.

### Disbursements
>Fiserv’s Digital Disbursement product allows a business to create a payment to a consumer (B2C) or another business (B2B) electronically.  Likewise, the product allows the recipient to select the method to be used to disburse the payment.
>
>The basic steps used to complete a Digital Disbursement are as follows:
> - Merchant Identifies the Recipient(s)
> - Merchant Initiates the Payment(s)
> - Merchant Approves the Payment(s) via Workflow Management 
> - Merchant Notifies the Recipient(s)
> - Recipient accepts the Payment (Acceptance Process)
> - Recipient selects a Disbursement Method
> - Fiserv disburses Funds to the recipient  via the chosen method.

### Fraud Detect
>Fraudsters are continually becoming more sophisticated and discovering new ways to steal sensitive customer data. As businesses and financial institutions strive to find fraud mitigation strategies, First Data provides an integrated and powerful solution that can address total loss prevention needs for payment and non-payment fraud.
>
>Fraud Detect is an ecommerce solution that enables merchants to reduce chargebacks while driving profits and providing a frictionless customer experience.  Based on machine learning that uses complex rules and algorithms, it provides real time, risk-based scoring decisions.  Fraud Detect’s machine learning solution utilizes decisions made by artificial intelligence and human analysis to improve accuracy and effectiveness.  

### Funding
>TBD

### Retrievals
>While there are many reasons an issuing bank may send a retrieval request, the notification process can be very simple. The Retrievals selection will help you facilitate the process of retrieving and fulfilling sales draft requests. In some instances, unanswered retrieval requests can result in a chargeback being initiated by the issuing bank.

### Settlements
>The Search option allows you to perform searches on specific card numbers over time. This report option provides a list of transactions associated with a specific cardholder account number for up to 13 months.

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

# API Structure

## Data Retrieval
>Data can be accessed in two ways. Each domain model supports both itemized transaction download as well as summarized data. In order to utilize the API for the data that you are interested, the developer will need to retrieve the meta data associated with that domain model. 
