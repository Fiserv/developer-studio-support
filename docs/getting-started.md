# Getting Started 

## Welcome to Reporting

The Fiserv Reporting APIs are built on the foundation of REST. The APIs accept standard JSON requests and return JSON encoded responses while leveraging industry standard [HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) for a seamless integration. Interaction through our Reporting APIs provides the developer community the ability to retrieve transaction, chargeback, funding and settlement information in a simple and intuitive manner. You will find that access to itemized or summary data can be quickly initiated programmatically for statistical analysis purposes. 

- Reporting through our APIs allows access to all of your transactional data within a well defined restful interface and clearly defined models. 
- Schedule your custom reports to be delivered at regular intervals. 
- Export data through csv, json or even have delivered on the cloud.

---
### Overview

Reporting information is available across data/information produced by the set of services a client uses. The following diagram depicts typical flow of information through the processes. Our APIs provide you with the ability to pull information across these various stages.

![reportingoverview](../assets/images/reportingoverview.png)

#### Authorizations

Authorizations refers to the transactions as soon as they are received by the receiving end point. An authorization can either be Approved or Declined. There are many details associated with the transaction that will determine where the authorization is ultimately routed to.

#### Settlement

Approved and eligible authorizations are sent over for settlement with the associations/issuers. The process is initiated the same day; however, the settlement process may take 1, 2 or more days.

#### Funding

Funding activity denotes what was transferred into the merchant account, broken down by deposit and various fees. Funding reports are used in the reconciliation process to the merchant bank account. Any adjustments will be shown as deductions made from the merchant's total sales (chargebacks, fees, interchange charges, etc.)

#### Chargebacks

The Disputes Overview provides an overview of Outstanding, Reversed, and Closed Chargebacks. Merchants can quickly see the total number of Open, Fulfilled, and Expired Chargebacks, as well as the total number of Chargebacks that are Open, Closed, and Reversed.

#### Retrievals

While there are many reasons an issuing bank may send a retrieval request, the notification process can be very simple. The Retrievals selection will help you facilitate the process of retrieving and fulfilling sales draft requests. In some instances, unanswered retrieval requests can result in a chargeback being initiated by the issuing bank.

#### Sites

Referential information with identifiers associated with the sites – physical and virtual. The site identifiers will be present within the transactions and this cross reference will provide additional information like city, state, hierarchy details etc.

#### Bins

Additional information associated with the card that provides general rules on how a card can be routed through the various networks, information about the card class Consumer, Corporate, Hybrid etc. Relevant transactions are tagged with the bin identifier for cross reference against Bins.

#### Disbursements

Fiserv’s Digital Disbursement product allows a business to create a payment to a consumer (B2C) or another business (B2B) electronically. Likewise, the product allows the recipient to select the method to be used to disburse the payment.

The basic steps used to complete a Digital Disbursement are as follows:

 * Merchant Identifies the Recipient(s)
 * Merchant Initiates the Payment(s)
 * Merchant Approves the Payment(s) via Workflow Management
 * Merchant Notifies the Recipient(s)
 * Recipient accepts the Payment (Acceptance Process)
 * Recipient selects a Disbursement Method
 * Fiserv disburses Funds to the recipient via the chosen method.

#### Prepaid Transactions

For customers using our closed loop ValueLink product, the following information is available. Prepaid card processing involves many transaction types – like activation, redemption, reload, balance look up etc. The transaction provides details associated with these transaction types. Depending on the merchant integration, i.e., direct to ValueLink or through the Authorization switch, the transactions may also appear within the Authorization stream.

#### Prepaid Unclaimed Property

For customers using our closed loop ValueLink product, the following information is available. Prepaid account balances are snapshotted on a rolling 30-day basis. Information (age of the card, time since last activity) associated with accounts with non-zero balances is available through this interface.
