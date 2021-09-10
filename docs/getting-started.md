# Getting Started 

## Welcome to Reporting

The Fiserv Reporting APIs are built on the foundation of REST. The APIs accept standard JSON requests and return JSON encoded responses while leveraging industry standard [HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) for a seamless integration. Interaction through our Reporting APIs provides the developer community the ability to retrieve transaction, chargeback, funding and settlement information in a simple and intuitive manner. You will find that access to itemized or summary data can be quickly initiated programmatically for statistical analysis purposes. 

- Reporting through our APIs allows access to all of your transactional data within a well defined restful interface and clearly defined models. 
- Schedule your custom reports to be delivered at regular intervals. 
- Export data through csv, json or even have delivered on the cloud.

---

### Overview
Reporting information is available across the value chain. The following diagram depicts typical flow of information through the settlement process. Our APIs provide you with the ability to pull information across these various stages.

![reportingoverview](../../assets/images/reportingoverview.jpeg)

#### Authorizations

Authorizations refers to the transactions as soon as they are received by the receiving end point. An authorization can either be Approved or Declined. There are many details associated with the transaction that will determine where the authorization is ultimately routed to. The transaction details are captured in this report.

#### Chargebacks

The Disputes Overview provides an overview of Outstanding, Reversed, and Closed Chargebacks. Merchants can quickly see the total number of Open, Fulfilled, and Expired Retrievals, as well as the total number of Chargebacks that are Open, Closed, and Reversed.

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

#### Fraud Detect

Fraudsters are continually becoming more sophisticated and discovering new ways to steal sensitive customer data. As businesses and financial institutions strive to find fraud mitigation strategies, First Data provides an integrated and powerful solution that can address total loss prevention needs for payment and non-payment fraud.

Fraud Detect is an ecommerce solution that enables merchants to reduce chargebacks while driving profits and providing a frictionless customer experience. Based on machine learning that uses complex rules and algorithms, it provides real time, risk-based scoring decisions. Fraud Detect’s machine learning solution utilizes decisions made by artificial intelligence and human analysis to improve accuracy and effectiveness.

#### Funding

Funding activity denotes what was transferred into the merchant account, broken down by deposit and various fees. Funding reports are used in the reconciliation process to the merchant bank account. Any adjustments will be shown as deductions made from the merchant's total sales (chargebacks, fees, interchange charges, etc.

#### Retrievals

While there are many reasons an issuing bank may send a retrieval request, the notification process can be very simple. The Retrievals selection will help you facilitate the process of retrieving and fulfilling sales draft requests. In some instances, unanswered retrieval requests can result in a chargeback being initiated by the issuing bank.

#### Settlements

The Search option allows you to perform searches on specific card numbers over time. This report option provides a list of transactions associated with a specific cardholder account number for up to 13 months.
 

## Data Retrieval
>Data can be accessed in two ways. Each domain model supports both itemized transaction download as well as summarized data. In order to utilize the API for the data that you are interested, the developer will need to retrieve the meta data associated with that domain model. 
