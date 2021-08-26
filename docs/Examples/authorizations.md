# Authorization

***[TBD]***
---

### Endpoint
<!-- theme: success -->
>**POST** `/v1/authorization/search`

---

### Payload Example

<!--
type: tab
title: Request
-->

##### Example of search of authorizations by Network only payload request.

```json
{
  "fromDate": "20210217",
  "toDate": "20210218",
  "limit": 2,
  "fields": [
    "PumpRegisterNumber","TimeTaken","SendMode","TransactionTime","SubType"
  ],
  "paymentMethods": [
    "Unknown", "Manual"
    ],
  "networks": [
    "Master", "Discover"
  ]
}
```
[![Try it out](../../../../DeveloperPortalCode/ClientLineX/assets/images/button.png)](../api/?type=post&path=/v1/authorization/search)

<!--
type: tab
title: Response
-->

##### Example of authorizations by Network (200: Created) response.

```json
[
    {
        "pumpRegisterNumber": "6",
        "timeTaken": 574,
        "subType": "Signature",
        "sendMode": "Normal",
        "transactionTime": 1613576686
    },
    {
        "pumpRegisterNumber": "5",
        "timeTaken": 2087,
        "subType": "Signature",
        "sendMode": "Normal",
        "transactionTime": 1613631743
    }
```
---

### Endpoint
<!-- theme: success -->
>**POST** `/v1/authorization/search`

---

### Payload Example

<!--
type: tab
title: Request
-->

##### Example of search of authorizations matching an auth code, first6 and last4: payload request.

```json
{
  "fromDate": "20210117",
  "toDate": "20210218",
  "limit": 200,
  "fields": [
    "PumpRegisterNumber","TimeTaken","SendMode","TransactionTime","SubType"
  ],
  "authCode": "149912",
  "first6": "123456",
  "last4": "7890"
}
```
[![Try it out](../../../../DeveloperPortalCode/ClientLineX/assets/images/button.png)](../api/?type=post&path=/v1/authorization/search)

<!--
type: tab
title: Response
-->

##### Example of authorizations matching an auth code, first6 and last4 (200: Created) response.

```json
[
    {
        "pumpRegisterNumber": "1",
        "timeTaken": 326,
        "subType": "Signature",
        "sendMode": "Normal",
        "transactionTime": 1611233371
    },
    {
        "pumpRegisterNumber": "4",
        "timeTaken": 628,
        "subType": "Unknown",
        "sendMode": "Normal",
        "transactionTime": 1613555350
    },
    {
        "pumpRegisterNumber": "5",
        "timeTaken": 662,
        "subType": "Signature",
        "sendMode": "Normal",
        "transactionTime": 1613341192
    }
]
```
---

### Endpoint
<!-- theme: success -->
>**POST** `/v1/authorization/summary`

---

### Payload Example

<!--
type: tab
title: Request
-->

##### Example of summary of all authorizations: payload request.

```json
{
  "fromDate": "20210117",
  "toDate": "20210218",
  "summaryBy": "TxnMonth"
  
}
```
[![Try it out](../../../../DeveloperPortalCode/ClientLineX/assets/images/button.png)](../api/?type=post&path=/v1/authorization/summary)

<!--
type: tab
title: Response
-->

##### Example of a getting all authorizations by TransactionMonth (200: Created) response.

```json
[
    {
        "currency": "N/A",
        "value": "Y2021M01",
        "countTotal": 248035,
        "amountTotal": 1.480132768E8,
        "approvedCount": 234200
    },
    {
        "currency": "N/A",
        "value": "Y2021M02",
        "countTotal": 284857,
        "amountTotal": 1.6728192718E8,
        "approvedCount": 269079
    },
    {
        "currency": "USD",
        "value": "Y2021M01",
        "countTotal": 33570264,
        "amountTotal": 2.7700459764E8,
        "approvedCount": 32967163
    },
    {
        "currency": "USD",
        "value": "Y2021M02",
        "countTotal": 39530263,
        "amountTotal": 3.2859115801E8,
        "approvedCount": 38776504
    }
]
```
