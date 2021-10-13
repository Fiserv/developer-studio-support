# Activate Card

This service is used to activate the card after successful verification of the cardholder. 


>Cardholder verification is the separate API that must be called in the card activation workflow.  Please [click here](../docs/?path=docs/APIs/Card-Management/card-secure-code-validation.md) to explore the cardholder verfication APIs.


# Endpoint
`PUT /v1/card/activate`


## Payload Example

### ***Request Payload***

```json
{
    "businessUnit":"100",
    "cardNumber":"000984NNNNNNNNN3613",
    "cardSequence": "0001",
    "currentCardRequireActivation": "N",
    "postToAccountNumber": "",    
    "lastCardActivation": "N"    
}
```

### Minimum Requirements
The below table contains the mandatory fields required for a successful request. The full request schemas are available in our [API Explorer](../api/?type=patch&path=/v1/card/activate).

The below table identifies the required parameters in the request payload.

| Variable | Type | Length | Description |
| -------- | :--: | :------------: | ------------------ |
| `businessUnit` | *number* | 3 | Identification number of the organization associated with the account. |
| `cardNumber` | *string* | 19 | Token Number associated with the clear PAN. | 
| `cardSequence` | *number* | 04 | A sequence number of the card in case of card scheme 2 else pass the default value of 0001. | 
| `currentCardRequireActivation` | *string* | 1 | Value ‘N’ To be passed to activate the card. |



### ***Successful Response Payload***

```json
{
    "businessUnit": "100",
    "cardNumber": "000984NNNNNNNNN3613",
    "cardSequence": "1",
    "lastCardActivation": "N",
    "currentCardRequireActivation": "N",
    "cardActivatedDate": "01/10/2021",
    "postToAccountNumber": "000100NNNNNNNNN0760"    
}
```

### ***Error Response Payload***

```json
{
  "errorCode": "V5ED0407SB",
  "errorMessage": "Business Unit not found in the system"  
}
```
Below table provides the list of application's error code and its description. 

| ErrorCode |  Description |
| --------  | ------------------ |
| `V5ED4001SN` | Business Unit is not numeric |
| `V5ED0407SB` | Business Unit not found in the system |
| `V5ED0407SE` | Post to Account record not in file |
| `V5ED9981SF` | Record Not Found |  