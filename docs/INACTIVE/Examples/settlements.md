# Settlements

TBD

---
#### List settled Transactions [TBD]
<!-- theme: success -->
>**POST** `/v1/settlement/search`

##### Payload

<!--
type: tab
title: Request
-->

```json
curl -X 'POST' \
  'http://localhost:5005/v1/settlement/search' \
  -H 'accept: application/json' \
  -H 'apiKey: YOUR KEY' \
  -H 'Content-Type: application/json' \
  -d '{
        "fromDate": "20210801",
        "toDate": "20210807",
        "limit": 1
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
    "ECIIndicator": "Unknown",
    "ECIIndicatorKey": "0",
    "accountNumber": "XXXXXXXXXXXX0000",
    "acquirerFeeAmount": 0,
    "acquirerFeePerTranAmount": 0,
    "acquirerFeePerTranRate": 0,
    "acquirerRefNo": null,
    "adminFeeAmount": 0,
    "adminFeePerTranAmount": 0,
    "adminFeePerTranRate": 0,
    "afdCompletionCode": null,
    "airLineTicketNumber": null,
    "authCode": "W9J2J6",
    "authCurrency": "USD",
    "authCurrencyKey": "1",
    "authSource": null,
    "authorizationAmount": 4.989999771118164,
    "authorizationDate": null,
    "authorizationResponseCode": null,
    "authorizationType": null,
    "avsFlag": "0",
    "bankReferenceNumber": null,
    "batchDate": "08/03/2021",
    "batchDescription": "5",
    "batchNo": "65796",
    "batchSequenceID": null,
    "batchSlipNumber": null,
    "batchUID": null,
    "billBackReason": null,
    "binID": "350508",
    "captureMethod": null,
    "cardExpirationDate": "1025",
    "cardPresenceIndicator": null,
    "cardScheme": null,
    "cardSchemeDescription": null,
    "cardUsage": null,
    "cardholderIDMethod": null,
    "cardholderNumber": null,
    "cashBackAmount": 0,
    "catLevel": null,
    "cbaFeeAmount": 0,
    "cbaFeePerTranAmount": 0,
    "cbaFeePerTranRate": 0,
    "chipConditionCode": null,
    "clientNumber": null,
    "convinienceFee": 0,
    "currency": "USD",
    "currencyKey": "1",
    "customTracking": null,
    "cvc2Result": null,
    "cvv2Result": null,
    "dbaName": "AWESOME STORE 2",
    "debitTerminalDate": null,
    "debitTerminalTime": null,
    "discountAmount": 0,
    "driverID": null,
    "entryModeSource": "Unknown",
    "entryModeSourceKey": null,
    "externalMID": "0004455667",
    "first6": "",
    "flatRate": 0,
    "foreignCurrAmount": 4.989999771118164,
    "foreignCurrRate": 0,
    "fundedDate": "08/04/2021",
    "iCFeePerTranRate": 0,
    "icFeeAmount": 0.2225,
    "icFeePerTranAmount": 0.2199999988079071,
    "ifFeeAmount": 0,
    "infrastructureFeePerTranAmount": 0,
    "infrastructureFeePerTranRate": 0,
    "integrityClass": null,
    "invalidTxnInd": 1,
    "invoiceNo": "HE7SU1GH",
    "isaFeeAmount": 0,
    "isaFeePerTranAmount": 0,
    "isaFeePerTranRate": 0,
    "last4": "0000",
    "markerID": null,
    "marketSpecificIndicator": null,
    "mcCardholderAuthentication": null,
    "mcPrdtId": null,
    "mcSecurityProtocol": null,
    "merchantCategory": "Eating Places & Restaurants (5812)",
    "merchantCategoryKey": "5812",
    "merchantReferenceNumber": null,
    "mobileIndicator": null,
    "mobileWallet": null,
    "mobileWalletKey": null,
    "netSalesCount": 1,
    "network": "Visa",
    "networkKey": "2",
    "networkSecurityFeeAmount": 0,
    "networkSecurityFeePerTranAmount": 0,
    "networkSecurityFeePerTranRate": 0,
    "newAuthFee": 0,
    "odometerReading": null,
    "orderNumber": null,
    "origPlanCodeDesc": "VN09 : VI-US REGULATED NON-CPS (DB)",
    "originalPlanCode": "VN09",
    "paymentMethod": "EMV",
    "paymentMethodKey": "4",
    "pcTaxAmount": 0,
    "pcTerminalCapability": null,
    "planCode": "VN09",
    "planCodeDesc": "VN09 : VI-US REGULATED NON-CPS (DB)",
    "platformID": "1",
    "posEntryMode": "10",
    "postedIndicator": null,
    "processedNetAmount": 4.989999771118164,
    "processedRefundAmount": 0,
    "processedRejectAmount": 0,
    "processedTransactionAmount": 4.989999771118164,
    "processor": "North",
    "processorKey": "1",
    "productCode": "Amex",
    "productCodeKey": "5",
    "purchaseIdentifier": null,
    "receiptNumber": null,
    "reclassCd": "Regular",
    "reclassCdKey": "0",
    "recordDate": "08/03/2021",
    "refundCount": 0,
    "rejectCount": 0,
    "rejectReason": "0",
    "rejectReasonCD": "0",
    "salesCount": 1,
    "salesTaxAmount": 0,
    "serviceCode": null,
    "settleSpendQualifiedIndicator": null,
    "siteID": "222222222222",
    "siteIDKey": "222222222222",
    "storeNumber": null,
    "subMerchantID": null,
    "subMerchantName": null,
    "submittedNetAmount": 4.989999771118164,
    "submittedRefundAmount": 0,
    "submittedRejectAmount": 0,
    "submittedTransactionAmount": 4.989999771118164,
    "surChargeAmount": 0,
    "surChargeInd": null,
    "switchFeeAmount": 0,
    "switchFeePerTranAmount": 0,
    "switchFeePerTranRate": 0,
    "terminalID": "0",
    "tipAmount": 0,
    "tokenRequesterId": null,
    "tokenType": null,
    "totalAuthAmount": 4.989999771118164,
    "tranId": null,
    "tranUID": null,
    "transactionDate": "08/02/2021",
    "transactionMode": "Manual",
    "transactionModeKey": "1",
    "transactionSource": null,
    "transactionStatus": "Processed",
    "transactionStatusKey": "1",
    "transactionTime": "1627955396",
    "trckrNbr": null,
    "type": "Purchase",
    "typeKey": "2",
    "userData": null,
    "vehicleNumber": null,
    "visaPrdtId": null,
    "visaServiceDevelop": null,
    "visaTranId": null
  }
]
```
---

#### List settled Transactions with specific fields
<!-- theme: success -->
>**POST** `/v1/settlement/search`

##### Payload

<!--
type: tab
title: Request
-->

```json
curl -X 'POST' \
  'http://localhost:5005/v1/settlement/search' \
  -H 'accept: application/json' \
  -H 'apiKey: YOUR KEY' \
  -H 'Content-Type: application/json' \
  -d '{
        "fromDate": "20210801",
        "toDate": "20210807",
        "limit": 3,
        "fields": [
          "AccountNumber",
          "ProcessedNetAmount",
          "Currency",
          "PaymentMethod",
          "Network"
        ]
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
    "accountNumber": "XXXXXXXXXXXX0000",
    "currency": "USD",
    "network": "Visa",
    "paymentMethod": "EMV",
    "processedNetAmount": 4.989999771118164
  },
  {
    "accountNumber": "XXXXXXXXXXXX0000",
    "currency": "USD",
    "network": "Visa",
    "paymentMethod": "EMV",
    "processedNetAmount": 4.090000152587891
  },
  {
    "accountNumber": "XXXXXXXXXXXX0000",
    "currency": "USD",
    "network": "Master",
    "paymentMethod": "EMV",
    "processedNetAmount": 4.550000190734863
  }
]
```
---

#### Search settled transactions Auth Code, Last 4
<!-- theme: success -->
>**POST** `/v1/settlement/search`

##### Payload

<!--
type: tab
title: Request
-->

```json
curl -X 'POST' \
  'http://localhost:5005/v1/settlement/search' \
  -H 'accept: application/json' \
  -H 'apiKey: YOUR KEY' \
  -H 'Content-Type: application/json' \
  -d '{
  "fromDate": "20210801",
  "toDate": "20210807",
  "limit": 3,
  "fields": [
    "ProcessedNetAmount",
    "PaymentMethod",
    "Currency",
    "AccountNumber",
    "Network",
    "AuthCode",
    "First6",
    "Last4"
  ],
  "filters": {
    "authCode": "I7B1Q1",
    "last4": "0000"
  }
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
    "accountNumber": "XXXXXXXXXXXX0000",
    "authCode": "I7B1Q1",
    "currency": "USD",
    "first6": "",
    "last4": "0000",
    "network": "Master",
    "paymentMethod": "EMV",
    "processedNetAmount": 4.550000190734863
  }
]
```
---

#### List settled transactions for a specific store
<!-- theme: success -->
>**POST** `/v1/settlement/search`

##### Payload

<!--
type: tab
title: Request
-->

```json
curl -X 'POST' \
  'http://localhost:5005/v1/settlement/search' \
  -H 'accept: application/json' \
  -H 'apiKey: YOUR KEY' \
  -H 'Content-Type: application/json' \
  -d '{
  "fromDate": "20210801",
  "toDate": "20210807",
  "limit": 3,
  "fields": [
    "AccountNumber",
    "ProcessedNetAmount",
    "Currency",
    "PaymentMethod",
    "Network"
  ],
  "filters": {
    "siteIDs": [
      "222222222222"
    ]
  }
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
    "accountNumber": "XXXXXXXXXXXX0000",
    "currency": "USD",
    "network": "Amex",
    "paymentMethod": "EMV",
    "processedNetAmount": 14.829999923706055
  },
  {
    "accountNumber": "XXXXXXXXXXXX0000",
    "currency": "USD",
    "network": "Visa",
    "paymentMethod": "EMV",
    "processedNetAmount": 0.6800000071525574
  },
  {
    "accountNumber": "XXXXXXXXXXXX0000",
    "currency": "USD",
    "network": "Master",
    "paymentMethod": "EMV",
    "processedNetAmount": 0.25999999046325684
  }
]
```

---

#### Settled Transactions Summary
<!-- theme: success -->
>**POST** `/v1/settlement/summary`

##### Payload

<!--
type: tab
title: Request
-->

```json
curl -X 'POST' \
  'http://localhost:5005/v1/settlement/summary' \
  -H 'accept: application/json' \
  -H 'apiKey: YOUR KEY' \
  -H 'Content-Type: application/json' \
  -d '{
        "fromDate": "20210801",
        "toDate": "20210807"
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
    "acquirerAmount": 0,
    "adminAmount": 0,
    "cbaAmount": 0,
    "currency": "USD",
    "ifAmount": 0,
    "interchangeAmount": 125.87749,
    "isaAmount": 0,
    "netAmount": 3941.25,
    "networkSecurityAmount": 0,
    "refundAmount": 0,
    "refundCount": 0,
    "rejectAmount": 0,
    "rejectCount": 0,
    "salesAmount": 3941.25,
    "salesCount": 555,
    "switchAmount": 0
  }
]
```
---

#### Settled Transactions Summary by Network
<!-- theme: success -->
>**POST** `/v1/settlement/summary`

##### Payload

<!--
type: tab
title: Request
-->

```json
curl -X 'POST' \
  'http://localhost:5005/v1/settlement/summary' \
  -H 'accept: application/json' \
  -H 'apiKey: YOUR KEY' \
  -H 'Content-Type: application/json' \
  -d '{
        "fromDate": "20210801",
        "toDate": "20210807",
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
    "acquirerAmount": 0,
    "adminAmount": 0,
    "cbaAmount": 0,
    "currency": "USD",
    "ifAmount": 0,
    "interchangeAmount": 9.56572,
    "isaAmount": 0,
    "netAmount": 280.26,
    "networkSecurityAmount": 0,
    "refundAmount": 0,
    "refundCount": 0,
    "rejectAmount": 0,
    "rejectCount": 0,
    "salesAmount": 280.26,
    "salesCount": 34,
    "switchAmount": 0,
    "value": "American Express"
  },
  {
    "acquirerAmount": 0,
    "adminAmount": 0,
    "cbaAmount": 0,
    "currency": "USD",
    "ifAmount": 0,
    "interchangeAmount": 89.8177,
    "isaAmount": 0,
    "netAmount": 2753.55,
    "networkSecurityAmount": 0,
    "refundAmount": 0,
    "refundCount": 0,
    "rejectAmount": 0,
    "rejectCount": 0,
    "salesAmount": 2753.55,
    "salesCount": 402,
    "switchAmount": 0,
    "value": "Visa"
  },
  {
    "acquirerAmount": 0,
    "adminAmount": 0,
    "cbaAmount": 0,
    "currency": "USD",
    "ifAmount": 0,
    "interchangeAmount": 24.23086,
    "isaAmount": 0,
    "netAmount": 827.72,
    "networkSecurityAmount": 0,
    "refundAmount": 0,
    "refundCount": 0,
    "rejectAmount": 0,
    "rejectCount": 0,
    "salesAmount": 827.72,
    "salesCount": 110,
    "switchAmount": 0,
    "value": "Mastercard"
  },
  {
    "acquirerAmount": 0,
    "adminAmount": 0,
    "cbaAmount": 0,
    "currency": "USD",
    "ifAmount": 0,
    "interchangeAmount": 2.26321,
    "isaAmount": 0,
    "netAmount": 79.72,
    "networkSecurityAmount": 0,
    "refundAmount": 0,
    "refundCount": 0,
    "rejectAmount": 0,
    "rejectCount": 0,
    "salesAmount": 79.72,
    "salesCount": 9,
    "switchAmount": 0,
    "value": "Discover"
  }
]
```
---

#### Settled transactions summary for a store by Payment Method
<!-- theme: success -->
>**POST** `/v1/settlement/summary`

##### Payload

<!--
type: tab
title: Request
-->

```json
curl -X 'POST' \
  'http://localhost:5005/v1/settlement/summary' \
  -H 'accept: application/json' \
  -H 'apiKey: YOUR KEY' \
  -H 'Content-Type: application/json' \
  -d '{
        "fromDate": "20210801",
        "toDate": "20210807",
        "summaryBy": "PaymentMethod",
        "filters": {
          "siteIDs": [
            "222222222222"
          ]
        }
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
    "acquirerAmount": 0,
    "adminAmount": 0,
    "cbaAmount": 0,
    "currency": "USD",
    "ifAmount": 0,
    "interchangeAmount": 1.55606,
    "isaAmount": 0,
    "netAmount": 60.51,
    "networkSecurityAmount": 0,
    "refundAmount": 0,
    "refundCount": 0,
    "rejectAmount": 0,
    "rejectCount": 0,
    "salesAmount": 60.51,
    "salesCount": 6,
    "switchAmount": 0,
    "value": "Contactless Magnetic Stripe"
  },
  {
    "acquirerAmount": 0,
    "adminAmount": 0,
    "cbaAmount": 0,
    "currency": "USD",
    "ifAmount": 0,
    "interchangeAmount": 0.22148,
    "isaAmount": 0,
    "netAmount": 2.96,
    "networkSecurityAmount": 0,
    "refundAmount": 0,
    "refundCount": 0,
    "rejectAmount": 0,
    "rejectCount": 0,
    "salesAmount": 2.96,
    "salesCount": 1,
    "switchAmount": 0,
    "value": "Magnetic Stripe"
  },
  {
    "acquirerAmount": 0,
    "adminAmount": 0,
    "cbaAmount": 0,
    "currency": "USD",
    "ifAmount": 0,
    "interchangeAmount": 45.89766,
    "isaAmount": 0,
    "netAmount": 1327.5,
    "networkSecurityAmount": 0,
    "refundAmount": 0,
    "refundCount": 0,
    "rejectAmount": 0,
    "rejectCount": 0,
    "salesAmount": 1327.5,
    "salesCount": 200,
    "switchAmount": 0,
    "value": "EMV"
  },
  {
    "acquirerAmount": 0,
    "adminAmount": 0,
    "cbaAmount": 0,
    "currency": "USD",
    "ifAmount": 0,
    "interchangeAmount": 16.53151,
    "isaAmount": 0,
    "netAmount": 585.4,
    "networkSecurityAmount": 0,
    "refundAmount": 0,
    "refundCount": 0,
    "rejectAmount": 0,
    "rejectCount": 0,
    "salesAmount": 585.4,
    "salesCount": 70,
    "switchAmount": 0,
    "value": "Contactless Chip"
  }
]
```
---

#### Settled transactions trend for a store
<!-- theme: success -->
>**POST** `/v1/settlement/summary`

##### Payload

<!--
type: tab
title: Request
-->

```json
curl -X 'POST' \
  'http://localhost:5005/v1/settlement/summary' \
  -H 'accept: application/json' \
  -H 'apiKey: YOUR KEY' \
  -H 'Content-Type: application/json' \
  -d '{
        "fromDate": "20210801",
        "toDate": "20210807",
        "summaryBy": "TxnDay",
        "filters": {
          "siteIDs": [
            "222222222222"
          ]
        }
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
    "acquirerAmount": 0,
    "adminAmount": 0,
    "cbaAmount": 0,
    "currency": "USD",
    "ifAmount": 0,
    "interchangeAmount": 11.23418,
    "isaAmount": 0,
    "netAmount": 382.03,
    "networkSecurityAmount": 0,
    "refundAmount": 0,
    "refundCount": 0,
    "rejectAmount": 0,
    "rejectCount": 0,
    "salesAmount": 382.03,
    "salesCount": 49,
    "switchAmount": 0,
    "value": "20210802"
  },
  {
    "acquirerAmount": 0,
    "adminAmount": 0,
    "cbaAmount": 0,
    "currency": "USD",
    "ifAmount": 0,
    "interchangeAmount": 7.68776,
    "isaAmount": 0,
    "netAmount": 184.16,
    "networkSecurityAmount": 0,
    "refundAmount": 0,
    "refundCount": 0,
    "rejectAmount": 0,
    "rejectCount": 0,
    "salesAmount": 184.16,
    "salesCount": 36,
    "switchAmount": 0,
    "value": "20210804"
  },
  {
    "acquirerAmount": 0,
    "adminAmount": 0,
    "cbaAmount": 0,
    "currency": "USD",
    "ifAmount": 0,
    "interchangeAmount": 10.92098,
    "isaAmount": 0,
    "netAmount": 293.68,
    "networkSecurityAmount": 0,
    "refundAmount": 0,
    "refundCount": 0,
    "rejectAmount": 0,
    "rejectCount": 0,
    "salesAmount": 293.68,
    "salesCount": 48,
    "switchAmount": 0,
    "value": "20210803"
  },
  {
    "acquirerAmount": 0,
    "adminAmount": 0,
    "cbaAmount": 0,
    "currency": "USD",
    "ifAmount": 0,
    "interchangeAmount": 11.31923,
    "isaAmount": 0,
    "netAmount": 399.13,
    "networkSecurityAmount": 0,
    "refundAmount": 0,
    "refundCount": 0,
    "rejectAmount": 0,
    "rejectCount": 0,
    "salesAmount": 399.13,
    "salesCount": 48,
    "switchAmount": 0,
    "value": "20210806"
  },
  {
    "acquirerAmount": 0,
    "adminAmount": 0,
    "cbaAmount": 0,
    "currency": "USD",
    "ifAmount": 0,
    "interchangeAmount": 11.45948,
    "isaAmount": 0,
    "netAmount": 328.68,
    "networkSecurityAmount": 0,
    "refundAmount": 0,
    "refundCount": 0,
    "rejectAmount": 0,
    "rejectCount": 0,
    "salesAmount": 328.68,
    "salesCount": 47,
    "switchAmount": 0,
    "value": "20210805"
  },
  {
    "acquirerAmount": 0,
    "adminAmount": 0,
    "cbaAmount": 0,
    "currency": "USD",
    "ifAmount": 0,
    "interchangeAmount": 11.58508,
    "isaAmount": 0,
    "netAmount": 388.69,
    "networkSecurityAmount": 0,
    "refundAmount": 0,
    "refundCount": 0,
    "rejectAmount": 0,
    "rejectCount": 0,
    "salesAmount": 388.69,
    "salesCount": 49,
    "switchAmount": 0,
    "value": "20210807"
  }
]
```

---

