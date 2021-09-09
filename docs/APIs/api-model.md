# Merchant Portal Reporting

[TBD] pls find attached Reporting image for better understanding 

![searchsummary](../../assets/images/searchsummary.png)


#### (1) Number of Transactions,Total Sales,Approval Rate

<!-- theme: success -->
>**POST** `/v1/authorization/summary`

##### Payload

<!--
type: tab
title: Request
-->

```json
curl -X 'POST' \
  'http://localhost:5005/v1/authorization/summary' \
  -H 'accept: application/json' \
  -H 'apiKey: YOUR KEY' \
  -H 'Content-Type: application/json' \
  -d '{
  "fromDate": "20210801",
  "toDate": "20210906"
}'
```

<!--
type: tab
title: Response
-->

##### Successful response (200)

```json
[
  {
    "currency": "CAD",
    "countTotal": 5678,
    "amountTotal": 24665.82,
    "approvedCount": 5000
  },
  {
    "currency": "N/A",
    "countTotal": 5457,
    "amountTotal": 369636.79000000004,
    "approvedCount": 3000
  },
  {
    "currency": "USD",
    "countTotal": 4000,
    "amountTotal": 745544.89,
    "approvedCount": 3675
  }
]
```

#### (2) Sales Details

<!-- theme: success -->
>**POST** `/v1/authorization/search`

##### Payload

<!--
type: tab
title: Request
-->

```json
curl -X 'POST' \
  'http://localhost:5005/v1/authorization/search' \
  -H 'accept: application/json' \
  -H 'apiKey: YOUR KEY' \
  -H 'Content-Type: application/json' \
  -d '{
  "fromDate": "20210801",
  "toDate": "20210906",
  "limit":2,
  "fields":["ApprovalCode","TransactionDateTime","Type","AccountNumber","Currency","Network","AuthCode","Amount"]
}'
```

<!--
type: tab
title: Response
-->

##### Successful response (200)

```json
[
  {
        "approvalCode": "Declined",
        "amount": 12.0,
        "authCode": 289932,
        "transactionDateTime": "08/13/2021 08:26:10 AM",
        "currency": "USD",
        "type": "PreAuthRequest",
        "accountNumber": "XXXXXXXXXXXX6660",
        "network": "Discover"
    },
    {
        "approvalCode": "Approved",
        "amount": 10.0,
        "authCode": "607279",
        "transactionDateTime": "08/13/2021 08:25:50 AM",
        "currency": "USD",
        "type": "Purchase",
        "accountNumber": "XXXXXXXXXXXX0018",
        "network": "Visa"
    }
]
```

#### (3) Total Funded

<!-- theme: success -->
>**POST** `/v1/funding/summary`

##### Payload

<!--
type: tab
title: Request
-->

```json
curl -X 'POST' \
  'http://localhost:5005/v1/funding/summary' \
  -H 'accept: application/json' \
  -H 'apiKey: YOUR KEY' \
  -H 'Content-Type: application/json' \
  -d '{
  "fromDate": "20210801",
  "toDate": "20210906",
  "summaryBy": "ProductCode"
}'
```

<!--
type: tab
title: Response
-->

##### Successful response (200)

```json
[
  {
    "currency": "USD",
    "value": "MASTERCARD",
    "processedNetSales": 11267048.91,
    "processedPaidByOthers": 0,
    "processedAdjustments": 0,
    "processedICCharges": -410.19,
    "processedServiceCharges": -21.84,
    "processedFees": -67.18,
    "processedChargebacksReversals": -531.82,
    "processedDeposit": 11266017.88,
    "processedAmountPaid": 11266017.88
  },
  {
    "currency": "USD",
    "value": "VISA",
    "processedNetSales": 29368092.33,
    "processedPaidByOthers": 0,
    "processedAdjustments": 0,
    "processedICCharges": -470.5,
    "processedServiceCharges": -18.11,
    "processedFees": -49.1,
    "processedChargebacksReversals": -1456.12,
    "processedDeposit": 29366098.5,
    "processedAmountPaid": 29366098.5
  }
]
```

#### (4) Chargebacks Received

<!-- theme: success -->
>**POST** `/v1/chargeback/summary`

##### Payload

<!--
type: tab
title: Request
-->

```json
curl -X 'POST' \
  'http://localhost:5005/v1/chargeback/summary' \
  -H 'accept: application/json' \
  -H 'apiKey: YOUR KEY' \
  -H 'Content-Type: application/json' \
  -d '{
  "fromDate": "20210801",
  "toDate": "20210906",
  "summaryBy": "Category"
}'
```

<!--
type: tab
title: Response
-->

##### Successful response (200)

```json
[
  {
    "currency": "USD",
    "value": "Debited",
    "countTotal": 125,
    "chargebackAmountTotal": 2311.7,
    "adjustmentAmountTotal": -1530.25
  }
]
```

#### (5) Sales Trend [TBD]

#### (6) Associations

<!-- theme: success -->
>**POST** `/v1/authorization/summary`

##### Payload

<!--
type: tab
title: Request
-->

```json
curl -X 'POST' \
  'http://localhost:5005/v1/authorization/summary' \
  -H 'accept: application/json' \
  -H 'apiKey: YOUR KEY' \
  -H 'Content-Type: application/json' \
  -d '{
  "fromDate": "20210801",
  "toDate": "20210906",
  "summaryBy": "Network"
}'
```

<!--
type: tab
title: Response
-->

##### Successful response (200)

```json
[
  {
    "currency": "USD",
    "value": "American Express",
    "countTotal": 124,
    "amountTotal": 350289.66,
    "approvedCount": 119
  },
  {
    "currency": "USD",
    "value": "Visa",
    "countTotal": 887,
    "amountTotal": 45384.76,
    "approvedCount": 851
  },
  {
    "currency": "USD",
    "value": "Mastercard",
    "countTotal": 218,
    "amountTotal": 5288.55,
    "approvedCount": 217
  }
]
```














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

