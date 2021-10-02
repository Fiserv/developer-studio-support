## Chargeback Transaction Details
```java
    /**
     * Provides a list of chargeback transactions.
     *
     * @method /v1/chargeback/details/byDate
     * @param ChargebackSearchRequest
     * @return ChargebackSearchResponse
     */
```

##### Example Request
><strong>Curl</strong>
>```javascript
>curl -X POST "https://cat.api.firstdata.com/reporting/v1/chargeback/details/byDate" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"date\": 20210217, \"fields\": [ \"cb_backendMID\", \"cb_authNetwork\", \"cb_receivedDate\", \"cb_statusDate\", \"cb_transactionDate\", \"cb_status\", \"cb_category\", \"cb_workType\", \"cb_winLoss\", \"cb_Reason\", \"cb_reasonCode\", \"cb_currency\", \"cb_chargebackAmount\", \"cb_dueDate\", \"cb_transactionType\", \"cb_dispositionDate\", \"cb_Disposition\", \"cb_ECIndicator\", \"cb_transactionAmount\", \"cb_accountNumber\", \"cb_first6\", \"cb_last4\", \"cb_invoiceNumber\", \"cb_terminalId\", \"cb_disputeID\", \"cb_referenceNumber\", \"cb_authCode\", \"cb_trackingNumber\", \"cb_svcCd\", \"cb_merchantCategory\", \"cb_orderNumber\", \"cb_responseReceived\", \"cb_respondedDate\", \"cb_externalMid\", \"cb_paymentMethod\", \"cb_sendMode\", \"cb_recurring\", \"cb_mobileWallet\", \"cb_tokenResponseInd\", \"cb_adjDate\", \"cb_captureMethod\" ], \"filters\": [ { \"field\": \"o_chargebackDateType\", \"values\": [ \"1\" ] } ]}"
>```
```json
{
  "date": 20210217,
  "fields": [
    "cb_backendMID",
    "cb_authNetwork",
    "cb_receivedDate",
    "cb_statusDate",
    "cb_transactionDate",
    "cb_status",
    "cb_category",
    "cb_workType",
    "cb_winLoss",
    "cb_Reason",
    "cb_reasonCode",
    "cb_currency",
    "cb_chargebackAmount",
    "cb_dueDate",
    "cb_transactionType",
    "cb_dispositionDate",
    "cb_Disposition",
    "cb_ECIndicator",
    "cb_transactionAmount",
    "cb_accountNumber",
    "cb_first6",
    "cb_last4",
    "cb_invoiceNumber",
    "cb_terminalId",
    "cb_disputeID",
    "cb_referenceNumber",
    "cb_authCode",
    "cb_trackingNumber",
    "cb_svcCd",
    "cb_merchantCategory",
    "cb_orderNumber",
    "cb_responseReceived",
    "cb_respondedDate",
    "cb_externalMid",
    "cb_paymentMethod",
    "cb_sendMode",
    "cb_recurring",
    "cb_mobileWallet",
    "cb_tokenResponseInd",
    "cb_adjDate",
    "cb_captureMethod"
  ],
  "filters": [
    {
      "field": "o_chargebackDateType",
      "values": [
        "1"
      ]
    }
  ]
}
```

##### Example Response
```json
{
  "response": [
    {
      "cb_Reason": 6,
      "cb_recurring": 0,
      "cb_tokenResponseInd": 1,
      "cb_transactionType": 3,
      "cb_transactionAmount": 24.45,
      "cb_externalMid": "3721234880",
      "cb_first6": "411234",
      "cb_ECIndicator": 6,
      "cb_workType": 1,
      "cb_dueDate": "03/07/2021",
      "cb_last4": "5643",
      "cb_responseReceived": "N",
      "cb_currency": 1,
      "cb_backendMID": "372123480",
      "cb_chargebackAmount": 24.45,
      "cb_paymentMethod": 10,
      "cb_adjDate": "02/23/2021",
      "cb_accountNumber": "414712XXXXXX1243",
      "cb_receivedDate": "02/19/2021",
      "cb_transactionDate": "02/14/2021",
      "cb_authCode": "06127D",
      "cb_sendMode": 1,
      "cb_merchantCategory": 5814,
      "cb_reasonCode": "1261",
      "cb_referenceNumber": "2494312345678465601",
      "cb_category": 1,
      "cb_statusDate": "03/08/2021",
      "cb_authNetwork": 2,
      "cb_winLoss": 2,
      "cb_mobileWallet": 0,
      "cb_status": 2,
      "cb_invoiceNumber": "DWXXXX4ZWCS",
      "cb_disputeID": "8112345678001",
      "cb_dispositionDate": "02/20/2021",
      "cb_Disposition": 71
    },
    {
      "cb_Reason": 1,
      "cb_recurring": 0,
      "cb_tokenResponseInd": 1,
      "cb_transactionType": 3,
      "cb_transactionAmount": 10,
      "cb_externalMid": "371234567884",
      "cb_first6": "441234",
      "cb_ECIndicator": 6,
      "cb_workType": 1,
      "cb_dueDate": "03/07/2021",
      "cb_last4": "4124",
      "cb_responseReceived": "N",
      "cb_currency": 1,
      "cb_backendMID": "3721234567884",
      "cb_chargebackAmount": 10,
      "cb_paymentMethod": 10,
      "cb_adjDate": "02/23/2021",
      "cb_accountNumber": "440012XXXXXX1234",
      "cb_receivedDate": "02/18/2021",
      "cb_transactionDate": "01/27/2021",
      "cb_authCode": "03102D",
      "cb_sendMode": 1,
      "cb_merchantCategory": 5814,
      "cb_reasonCode": "1040",
      "cb_referenceNumber": "24431123456786649",
      "cb_category": 1,
      "cb_statusDate": "03/08/2021",
      "cb_authNetwork": 2,
      "cb_winLoss": 2,
      "cb_mobileWallet": 0,
      "cb_status": 2,
      "cb_invoiceNumber": "DW9XXXXK5MZ",
      "cb_disputeID": "810412343501",
      "cb_dispositionDate": "02/20/2021",
      "cb_Disposition": 71
    }
  ]
}
```

