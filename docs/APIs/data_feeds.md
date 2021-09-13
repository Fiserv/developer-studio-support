# Data Feeds

If traditional restful APIs do not satisfy your requirements and you would rather get data feeds, we have multiple ways to get your data to you easily and in a timely manner. Choose from one of the following options to consume your data across the value chain.
 
#### Snowflake
 
Snowflake (hyper link to https://www.snowflake.com) is a cloud-based data warehousing solution. We have partnered with Snowflake to make Secure data shares (hyper link to https://www.snowflake.com/workloads/data-sharing) available. Data is available in your share on a near real-time basis. Authorizations, Gateway, and Value-added services transactions are available within a few seconds. Batch processed objects are available as soon as the processing is complete. No messy ETL, file exchanges etc. to worry about. Spin up your Warehouses (hyper link to https://www.snowflake.com/workloads/data-warehouse-modernization) and join/mingle it with your data in Snowflake. Use traditional SQL to query and analyze your data.
 
If you are interested in this option, please contact your account rep to enable a secure share.
 
#### AWS S3 Integration
 
If AWS is your choice of cloud, we can make your data (as files) available in a secure manner in S3 (hyper link to https://aws.amazon.com/s3). You can use your favorite lambdas or ETL suite to process the files into your system.
 
Files are available at the logical business end of day. We support multiple file formats including CSV, JSON and Parquet.
 
Use the feed status APIs to lookup the status of your feeds.
If you are interested in this option, please contact your account rep to get a secure S3 integration setup.
 
#### Azure Blob Integration
 
If Azure is your choice of cloud, we can make your data (as files) available in a secure manner within your Blobs (hyper link to https://azure.microsoft.com/en-us/services/storage/blobs). You can use your favorite Automations or ETL suite to process the files into your system.
 
Files are available at the logical business end of day. We support multiple file formats including CSV, JSON and Parquet.
 
Use the feed status APIs to lookup the status of your feeds.
If you are interested in this option, please contact your account rep to get a secure Azure Blob Storage integration setup.
 
#### Inbox Pull
 
Schedule on demand requests or periodic requests for delivery to your Reporting Inbox. Files are available at the logical business end of day. We support multiple file formats including CSV, JSON and Parquet. Use the feed status APIs to lookup the status of your feeds.
 
 
Feed status API
 
To be filled in…..


# TBD

# Domain Models

#### What are Domain Models?
Domain models represent the type of data that you may be interested in.  IE authorization transactions, chargebacks, etc. Reporting supports the following domain models. 

#### Authorizations 
>Authorizations refers to the transactions as soon as they are received by the receiving end point. An authorization can either be Approved or Declined. There are many details associated with the transaction that will determine where the authorization is ultimately routed to. The transaction details are captured in this report.

#### Chargebacks
>The Disputes Overview provides an overview of Outstanding, Reversed, and Closed Chargebacks. Merchants can quickly see the total number of Open, Fulfilled, and Expired Retrievals, as well as the total number of Chargebacks that are Open, Closed, and Reversed.

#### Disbursements
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

#### Fraud Detect
>Fraudsters are continually becoming more sophisticated and discovering new ways to steal sensitive customer data. As businesses and financial institutions strive to find fraud mitigation strategies, First Data provides an integrated and powerful solution that can address total loss prevention needs for payment and non-payment fraud.
>
>Fraud Detect is an ecommerce solution that enables merchants to reduce chargebacks while driving profits and providing a frictionless customer experience.  Based on machine learning that uses complex rules and algorithms, it provides real time, risk-based scoring decisions.  Fraud Detect’s machine learning solution utilizes decisions made by artificial intelligence and human analysis to improve accuracy and effectiveness.  

#### Funding
>Funding activity denotes what was transferred into the merchant account, broken down by deposit and various fees. Funding reports are used in the reconciliation process to the merchant bank account. Any adjustments will be shown as deductions made from the merchant's total sales (chargebacks, fees, interchange charges, etc. 

#### Retrievals
>While there are many reasons an issuing bank may send a retrieval request, the notification process can be very simple. The Retrievals selection will help you facilitate the process of retrieving and fulfilling sales draft requests. In some instances, unanswered retrieval requests can result in a chargeback being initiated by the issuing bank.

#### Settlements
>The Search option allows you to perform searches on specific card numbers over time. This report option provides a list of transactions associated with a specific cardholder account number for up to 13 months.
