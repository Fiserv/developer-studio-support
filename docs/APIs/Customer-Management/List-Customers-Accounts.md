# List Customers Accounts

 The service provides list of accounts associated with the customer. 

# Endpoint
`GET https://stg34.visionplus.io/apidev/v1/customers/{customerNumber}/accountList/`


## Payload Example


### Request Payload
> Empty.  

### Minimum Requirements
The below table contains the mandatory fields required for a successful request. The full request schemas are available in our [API Explorer](../api/?type=get&path=/v1/customer/accountList).

The below table identifies the required parameters in the request payload.

| Variable | Type | Length | Description/Values |
| -------- | :--: | :------------: | ------------------ |
| `customerNumber` | *string* | 19 | An identifier of the customer. | 



### Successful Response Payload


```json
{
    "accountList": [
        {
            "product": "1",
            "businessUnit": "100",
            "amountMemoCredit": "$0.00",
            "ddaAccountNumber": "890005226",
            "mailingIndicator": " ",
            "blockCode2Date": "00/00/0000",
            "accountNumber": "0001000011000052268",
            "sUPPRESSTOKEN": "0",
            "internalStatus": "D",
            "amountMemoDebit": "$0.00",
            "nbrOfTokenizedCards": "0",
            "blockCode1": " ",
            "rEISSCONTOLMETHOD": "0",
            "blockCode2": " ",
            "blockCode1Date": "00/00/0000"
        }
    ],
    "totalAvailable": "$0.00",
    "dateofBirth": "11/14/1940",
    "businessUnit": "0",
    "homePhoneNumber": "++61430010348",
    "gender": "0",
    "mobileNumber": "++61430010348",
    "nameLine1": "UATMFNCU448 TWOPPPUATMLNCUST448",
    "emailAddress": "UATMFNCU448@GMAIL.COM",
    "sSNID": "113902",
    "workPhoneNumber": "++61430010348",
    "cREDITlimit": "$0.00",
    "addressLine1": "62 CHARTERIS DR",
    "addressLine2": "",
    "addressLine3": "",
    "addressLine4": "",
    "relationshipnbr": "",
    "billingLvl": "0",
    "userDefinedField4": "",
    "numberofCards": "1",
    "numberofAccounts": "1",
    "customerNumber": "0001000000000113902",
    "customerName": "UATMFNCU448",
    "homeDistricName": "",    
    "rELNAME": "",
    "status": ""
}

```

### Error Response Payload

```json
{
  "errorCode": "V5DB4001AS",
  "errorMessage": "Customer Number not found"  
}
```
Below table provides the list of application's error code and its description. 

| ErrorCode |  Description/Values |
| --------  | ------------------ |
| `V5DB4001AS` |	Customer Number not found|
