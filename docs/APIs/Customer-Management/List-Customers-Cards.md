# List Customers Cards

 The service provides list of cards associated with the customer. 

# Endpoint
`GET https://stg34.visionplus.io/apidev/v1/customers/{customerNumber}/cardList/`


## Payload Example


### Request Payload
> Empty.  

### Minimum Requirements
The below table contains the mandatory fields required for a successful request. The full request schemas are available in our [API Explorer](../api/?type=get&path=/v1/customer/cardList).

The below table identifies the required parameters in the request payload.

| Variable | Type | Length | Description/Values |
| -------- | :--: | :------------: | ------------------ |
| `customerNumber` | *string* | 19 | An identifier of the customer. | 



### Successful Response Payload


```json
{
    "cardList": [
        {
            "cardholderType": "1",
            "businessUnit": "100",
            "iNTATMPOSFlag": "Y",
            "lastCardExpirationDate": "00/00/0000",
            "cardIssueDate": "09/28/2020",
            "lastCardAction": "1",
            "dateOpened": "09/17/2020",
            "lastCardNeedActivation": "Y",
            "pinoffset": "329861",
            "productDescription": "VISA PLATINUM DEBIT",
            "posttoAccount": "0001000011000052268",
            "blockDate": "00/00/0000",
            "cardTechnology": "3",
            "mCCLIMIT10": "$0.00",
            "pLASTICSUPPRESSSTATUS": "N",
            "cHEQUEACCOUNTNBR": " ",
            "currCardAction": "0",
            "dATELASTWALLETUSED": "0",
            "mOTOFlag": " ",
            "embosserRecordStatus": "0",
            "cardNumber": "0009846801010009405",
            "timeLastPlasticIssue": "13815",
            "numberofcards": "0",
            "sAVINGSACCOUNTNBR": " ",
            "eMBRNAME2": " ",
            "digitalid": " ",
            "maskCardnumber": "000      XXXXXX",
            "aTMFlag": "Y",
            "currentCardNeedActivation": "Y",
            "nameOnCard": "U T UATMLNCUST448",
            "pOSFlag": "Y",
            "cardActivatedDate": "00/00/0000",
            "pAYwaveFlag": "Y",
            "dATELASTPLASTICUSED": "0",
            "blockCode": " ",
            "product": "1",
            "mCCLIMIT6": "$0.00",
            "cardSequence": "1",
            "warningCode": "0",
            "mCCLIMIT7": "$0.00",
            "mCCLIMIT8": "$0.00",
            "mCCLIMIT9": "$0.00",
            "mCCLIMIT2": "$0.00",
            "mCCLIMIT3": "$0.00",
            "mCCLIMIT4": "$0.00",
            "mCCLIMIT5": "$0.00",
            "cashBackTranFlag": "Y",
            "mCCLIMIT1": "$0.01",
            "dATELASTPLASTICSUPRESED": "0",
            "eCOMACTFlag": "1",
            "cardExpirationDate": "09/16/2023"
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
