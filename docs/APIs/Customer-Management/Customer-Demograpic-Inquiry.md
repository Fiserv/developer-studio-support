# Inquire Customer Demographic Information

This service will be used to enquire the customer demographic details such as Name / Address / Phone Number / Email ID/ Date of Birth of the given customer.  The customer ID will be passed in the input request to retrieve the demographic information. 



# Endpoint
`GET /v1/customers/nameAddress`


## Payload Example


### Request Payload

```json
{ 
  "businessunit" : "100",
  "accountNumber" : "0001000000000150191
}
```

### Minimum Requirements
The below table contains the mandatory fields required for a successful request. The full request schemas are available in our [API Explorer](../api/?type=patch&path=/v1/customers/nameAddress).

The below table identifies the required parameters in the request payload.

| Variable | Type | Length | Description/Values |
| -------- | :--: | :------------: | ------------------ |
| `businessUnit` | *number* | 3 | Identification number of the organization associated with the Card. |
| `accountNumber` | *string* | 19 | Customer Number of the cardholder. | 


### Successful Response Payload

```json
{
  "businessunit": "100",
  "accountNumber": "0001000000000150191",	
  "nameLine11" : "KIARA",
  "nameLine21" : "CHRISTIAN",
  "nameLine31" : "HARBER",
  "addressLine11": "80.ANGLES",
  "addressLine21": "",	
  "addressLine31": "",
  "addressLine41": "",
  "city1": "US",
  "state/Province1": "USA",  
  "countryCode1": "USA",
  "postalCode1": "27899",
  "emailAddress1": "SAM@GMAIL.COM",
  "homePhoneFlag1": "0",
  "mobileNumber1": "11110976444",
  "homePhoneNumber1": "123456788999999",
  "faxNumber1": "",
  "sMSFlag1": "0",
  "faxPhoneFlag1": "0",		
  "mobilePhoneFlag1": "0",
  "languageIndicator1": "AUS"
}  
```

### Error Response Payload

```json
{
  "errorCode": "V5ED0301EA",
  "errorMessage": "Priority of new block code cannnot be lower than the existing block code"  
}
```
Below table provides the list of application's error code and its description. 

| ErrorCode |  Description/Values |
| --------  | ------------------ |
|`V5NA4001SV` |	Invalid Business Unit|  
|`V5NA4002SA` |	Customer Account not found|
|`V5NA4002SB` |	Customer Account is in add pending|
|`V5NA4002SC` |	Customer Account is purged|
|`V5NA0004SF` |	Get  Request - Record not found|
|`V5NA0005SF` |	Get Request - Record Add Pending|
