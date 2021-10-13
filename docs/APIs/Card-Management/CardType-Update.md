# CardType Update

This service is used to update the type of cardholder between primary and supplementary (Joint Cardholder). 

# Endpoint
`PATCH /v1/cards/profile`


## Payload Example

### ***Request Payload***

```json
{
    "businessUnit":"100",
    "cardNumber":"000984680NNNNNN3613",
    "cardSequence": "0001",
    "cardholderType": "1",
}
```

### Minimum Requirements
The below table contains the mandatory fields required for a successful request. The full request schemas are available in our [API Explorer](../api/?type=patch&path=/v1/card/profile).

The below table identifies the required parameters in the request payload.

| Variable | Type | Length | Description |
| -------- | :--: | :------------: | ------------------ |
| `businessUnit` | *number* | 3 | Identification number of the organization associated with the account. |
| `cardNumber` | *string* | 19 | Token Number associated with the clear PAN. | 
| `cardSequence` | *number* | 04 | A sequence number of the card in case of card scheme 2 else pass the default value of 0001. | 
| `cardholderType` | *numeric* | 1 | Pass value 1 for Single primary cardholder. Pass value 0 for Joint cardholder |



### ***Successful Response Payload***

```json
{
    "businessUnit": "100",
    "cardNumber": "000984680NNNNNN3613",
    "cardSequence": "1",
    "postToAccountNumber": "000100001NNNNNN0760",    
    "cardholderType": "1",
}
```

### ***Error Response Payload***

```json
{
  "errorCode": "V5ED0237SV",
  "errorMessage": "Invalid Cardholder-type"  
}
```
Below table provides the list of application's error code and its description. 

| ErrorCode |  Description |
| --------  | ------------------ |
| `V5ED4001SN` | Business Unit is not numeric |
| `V5ED0407SB` | Business Unit not found in the system |
| `V5ED0407SE` | Post to Account record not in file |
| `V5ED9981SF` | Record Not Found |  
| `V5ED0237SV` | Invalid Cardholder-type |  