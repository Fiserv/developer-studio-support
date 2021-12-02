# Update Customer Demographic Information

This service will be used to update the customer demographic details such as Name / Address / Phone Number / Email ID/ Date of Birth of the given customer.  The customer ID will be passed in the input request to retrieve the demographic information. 



# Endpoint
`PUT /v1/customers/nameAddress?businessunit=100&accountNumber=0001000000000150191`


## Payload Example

### Request Payload

```json
{  
  "firstName1" : "JOHN",
  "middleName1" : "SMITH"  
}
```

### Minimum Requirements
The below table contains the mandatory fields required for a successful request. The full request schemas are available in our [API Explorer](../api/?type=patch&path=/v1/customers/nameAddress).

The below table identifies the required parameters in the request payload.

| Variable | Type | Length | Description/Values |
| -------- | :--: | :------------: | ------------------ |
| `businessUnit` | *number* | 3 | Identification number of the organization associated with the Card. |
| `accountNumber` | *string* | 19 | Customer Number of the cardholder. | 

Along with above key fields any of the Name / address / Phone number / email ID information that is required to be updated.


### Successful Response Payload

```json
{
    "postalCode1": "2011",
    "city1": "SYDNEY",
    "nameLine21": "CHRISTIAN",
    "firstName1": "JOHN",
    "emailAddress1": "SAM@GMAIL.COM",
    "homePhoneFlag1": "0",
    "userDefinedField41": "Y",
    "stateProvince1": "NSW",
    "middleName1": "SMITH",
    "faxNumber1": " ",
    "addressLine21": " ",
    "addressLine41": " ",
    "lastName1": "HARBER",
    "faxPhoneFlag1": "0",
    "nameLine31": "HARBER",
    "nameLine11": "Smith",
    "mobileNumber1": "11110976444",
    "accountNumber": "0001000000000150191",
    "countryCode1": "AU",
    "businessunit": "100",
    "languageIndicator1": "AUS",
    "addressLine31": " ",
    "sMSFlag1": "0",
    "homePhoneNumber1": "123456788999999",
    "addressLine11": "77 30 HARVEY ISLAND",
    "houseNumber1": " ",
    "mobilePhoneFlag1": "0",
    "dateOfBirth1": "04/02/1975"
} 
```

### Error Response Payload

```json
{
  "errorCode": "V5NA4001SN",
  "errorMessage": "Business unit is not numeric"  
}
```
Below table provides the list of application's error code and its description. 

| ErrorCode |  Description/Values |
| --------  | ------------------ |
|`V5NA4001SN` |	Business unit is not numeric|
|`V5NA0010SF` |	Update Request - Record not found|
|`V5NA0011SF` |	Update Request - Record Add Pending|
|`V5NA4002SC` |	Customer account is in purged|
|`V5NA4001SV` |	Invalid Business Unit|  
|`V5NA0318EA` |	Invalid  country  code|
|`V5NA0713EA` |	Postal Code Format invalid|
|`V5NA0320EA` |	Invalid  ISO language code|
|`V5NA0328SV` |	Invalid Home Phone flag|
|`V5NA0334SV` |	Invalid  Mobile Phone Flag|                              
|`V5NA0202EA` |	Either of first/middle/last name is required for maker|
|`V5NA0202EB` |	Either of first/middle/last name is required for maker and comaker|
|`V5NA0312SZ` |	Update Access not granted for Address Line 1|
|`V5NA0313SZ` |	Update Access not granted for Address Line 2|
|`V5NA0242SZ` |	Update Access not granted for Address Line 3|
|`V5NA0243SZ` |	Update Access not granted for Address Line 4|
|`V5NA0314SZ` |	Update Access not granted for City|
|`V5NA0315SZ` |	Update Access not granted for State/Province|
|`V5NA0202SZ` |	Update Access not granted for First Name|
|`V5NA0327SZ` |	Update Access not granted for Home Phone Number|
|`V5NA0330SZ` |	Update Access not granted for Fax Number|
|`V5NA0333SZ` |	Update Access not granted for Mobile Number|
|`V5NA0504SZ` |	Update Access not granted for User Defined Field 4|
|`V5NA0419SZ` |	Update Access not granted for Email Address|

