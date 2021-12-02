# List Accounts' Transactions

 The service provides list of transactions along with detail information for transactions posted in the last statement cycle. 

# Endpoint
`GET /v1/accounts/{accountNumber}/transactions/lastStatement/?businessUnit=xxx&product=n&statementDate=DD/MM/YYYY`


## Payload Example


### Request Payload
> Empty.  

### Minimum Requirements
The below table contains the mandatory fields required for a successful request. The full request schemas are available in our [API Explorer](../api/?type=get&path=/v1/accounts/listAccountTransactions).

The below table identifies the required parameters in the request payload.

| Variable | Type | Length | Description/Values |
| -------- | :--: | :------------: | ------------------ |
| `accountNumber` | *string* | 19 | Account Number of the cardholder. | 
| `businessUnit` | *number* | 3 | Identification number of the organization associated with the account. |
| `product` | *number* | 3 | Product associated with the Account. |
| `statementDate` | *Date* | DD/MM/YYYY | Date the statement is produced for the account holder |



### Successful Response Payload


```json
{
    "transactionList": [
        {
            "recordNumber": "52",
            "amount": "$30.83",
            "businessUnit": "200",
            "authorizationCode": " ",
            "description": "DEBIT CARD OFFSET CREDIT",
            "postingDate": "03/26/2021",
            "transactionCode": "7016",
            "aMSLKey": " ",
            "reference": "19999999980326199980140",
            "transactionType": "C",
            "creditPlan": "10002",
            "logo": "1",
            "logicModule": "4",
            "effectiveDate": "03/26/2021"
        },
        {
            "recordNumber": "52",
            "amount": "$30.83",
            "businessUnit": "200",
            "authorizationCode": " ",
            "description": "DEBIT CARD OFFSET CREDIT",
            "postingDate": "03/26/2021",
            "transactionCode": "7016",
            "aMSLKey": " ",
            "reference": "19999999980326199980140",
            "transactionType": "C",
            "creditPlan": "10002",
            "logo": "1",
            "logicModule": "4",
            "effectiveDate": "03/26/2021"
        }
    ],
    "accountRelationship": "0002000010000001211",
    "statementDate": "04/09/2021",
    "tranPrevToken": "2000002000010000001211202109y50003",
    "tranNextToken": "2000002000010000001211202109y50052",
    "planNextTokenlast": "",
    "tableIND": "",
    "cPLastFunc": "",
    "hiddenKey": "",
    "planPREVTokenlast": "",
    "fileType": "SL"
}
```

### Error Response Payload

```json
{
  "errorCode": "V5S34003SA",
  "errorMessage": "No Statement History information found on file"  
}
```
Below table provides the list of application's error code and its description. 

| ErrorCode |  Description/Values |
| --------  | ------------------ |
| `V5BS0011SF` |	Update Request - Record Add Pending|
| `V5BS4001EA` |	Invalid Business Unit|                                      
| `V5BS4001SC` |	Business Unit is in Purged Status|     
| `V5BS4002SA` |	Invalid Account Number|  
| `V5S34003SA` |	No Statement History information found on file|