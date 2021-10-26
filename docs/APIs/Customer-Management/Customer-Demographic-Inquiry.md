# Inquire Customer Demographic Information

This service will be used to enquire the customer demographic details such as Name / Address / Phone Number / Email ID/ Date of Birth of the given customer.  The customer ID will be passed in the input request to retrieve the demographic information. 



# Endpoint
`GET /v1/customers/nameAddress?businessunit=100&accountNumber=0001000000000150191`


## Payload Example


### Request Payload

```json
Empty. The Business Unit and AccountNumber should be send in the query parameters
```

### Minimum Requirements
The below table contains the mandatory fields required for a successful request. The full request schemas are available in our [API Explorer](../api/?type=patch&path=/v1/customers/nameAddress).

The below table identifies the required query parameters in the request message.

| Variable | Type | Length | Description/Values |
| -------- | :--: | :------------: | ------------------ |
| `businessUnit` | *number* | 3 | Identification number of the organization associated with the Card. |
| `accountNumber` | *string* | 19 | Customer Number of the cardholder. | 


### Successful Response Payload

```json
{
    "postalCode1": "2011",
    "city1": "SYDNEY",
    "nameLine21": "CHRISTIAN",
    "firstName1": "KIARA",
    "emailAddress1": "SAM@GMAIL.COM",
    "homePhoneFlag1": "0",
    "userDefinedField41": "Y",
    "stateProvince1": "NSW",
    "middleName1": "CHRISTIAN",
    "faxNumber1": "",
    "addressLine21": "",
    "addressLine41": "",
    "lastName1": "HARBER",
    "faxPhoneFlag1": "0",
    "nameLine31": "HARBER",
    "nameLine11": "KIARA",
    "mobileNumber1": "12345678901",
    "countryCode1": "AU",
    "accountNumber": "0001000000000150191",
    "businessunit": "100",
    "languageIndicator1": "AUS",
    "addressLine31": "",
    "sMSFlag1": "0",
    "homePhoneNumber1": "123456788999999",
    "addressLine11": "77 30 HARVEY ISLAND",
    "houseNumber1": "",
    "mobilePhoneFlag1": "0",
    "dateOfBirth1": "04/02/1975"
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
