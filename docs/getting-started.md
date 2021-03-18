# Getting Started

## Welcome to Reporting

Reporting through CLX APIs provides the developer community the ability to retrieve transaction, chargeback, funding and settlement information in a simple and intuitive manner. You will find that access to itemized or summary data can be initiated programmatically for statistical analysis purposes. 

# Domain Models

## What are Domain Models?
Domain models represent the type of data that you may be interested in.  IE authorization transactions, chargebacks, etc. Reporting supports the following domain models. 

### Authorizations 
>Authorizations refers to the transactions as soon as they are received by the receiving end point. An authorization can either be Approved or Declined. There are many details associated with the transaction that will determine where the authorization is ultimately routed to. The transaction details are captured in this report.

### Chargebacks
>The Disputes Overview provides an overview of Outstanding, Reversed, and Closed Chargebacks. Merchants can quickly see the total number of Open, Fulfilled, and Expired Retrievals, as well as the total number of Chargebacks that are Open, Closed, and Reversed.

### Disbursements
>TBD

### Fraud Detect
>TBD

### Funding
>TBD

### Retrievals
>While there are many reasons an issuing bank may send a retrieval request, the notification process can be very simple. The Retrievals selection will help you facilitate the process of retrieving and fulfilling sales draft requests. In some instances, unanswered retrieval requests can result in a chargeback being initiated by the issuing bank.

### Settlements
>The Search option allows you to perform searches on specific card numbers over time. This report option provides a list of transactions associated with a specific cardholder account number for up to 13 months.

# Meta Data

### What is Meta Data?
Meta data are the fields and pivots that comprise a report.  What fields a user would like to be shown in an itemized report or what pivots a user would like to use in a summary report. By calling the `metaData` API for a particular report type, the developer will get access to all the available fields and pivots to build their own customizable report. 

# API Structure

## Data Retrieval
>Data can be accessed in two ways. Each domain model supports both itemized transaction download as well as summarized data. In order to utilize the API for the data that you are interested, the developer will need to retrieve the meta data associated with that domain model. 
