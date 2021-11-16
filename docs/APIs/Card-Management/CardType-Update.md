# CardType Update

This service is used to update the type of cardholder between primary and supplementary (Joint Cardholder). 

# Endpoint
`PATCH /v1/cards/profile`


## Payload Example

### Request Payload

```json
{
    "businessUnit":"100",
    "cardNumber":"0009846801010273613",
    "cardSequence": "0001",
    "cardholderType": "1"
}
```

### Minimum Requirements
The below table contains the mandatory fields required for a successful request. The full request schemas are available in our [API Explorer](../api/?type=patch&path=/v1/cards/profile).

The below table identifies the required parameters in the request payload.

| Variable | Type | Length | Description |
| -------- | :--: | :------------: | ------------------ |
| `businessUnit` | *number* | 3 | Identification number of the organization associated with the account. |
| `cardNumber` | *string* | 19 | Token Number associated with the clear PAN. | 
| `cardSequence` | *number* | 04 | A sequence number of the card in case of card scheme 2 else pass the default value of 0001. | 
| `cardholderType` | *numeric* | 1 | Pass value 1 for Single primary cardholder. Pass value 0 for Joint cardholder |



### Successful Response Payload

```json
{
    "businessUnit": "100",
    "cardNumber": "0009846801010273613",
    "cardSequence": "1",
    "postToAccountNumber": "0001000010000510760",    
    "cardholderType": "1",
}
```

### Error Response Payload

```json
{
  "errorCode": "V5ED0237SV",
  "errorMessage": "Invalid Cardholder-type"  
}
```
Below table provides the list of application's error code and its description. 

| ErrorCode |  Description |
| --------  | ------------------ |
|`V5ED4001SA` |	Business Unit not found |
|`V5ED4001SB` |	Business Unit is in Add Pending Status|
|`V5ED4001SC` |	Business Unit in Purged Status|
|`V5ED4001SE` |	Invalid Business Unit|
|`V5ED0010SF` |	Update Request - Record not found|
|`V5ED0011SF` |  Update Request - Record Add Pending|
|`V5ED4003ED` |  Card Sequence must be greater than zeroes|   
|`V5ED4004SF` |  Invalid Card Sequence| 
|`V5ED0237SV` |	Invalid  Cardholder-type|
|`V5ED0237EA` |	User not allowed to change cardholder type from 1 to 0 |
|`V5ED0237EB` |	Cannot have more than one primary card|