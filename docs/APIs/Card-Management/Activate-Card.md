# Activate Card

This service is used to activate the card after successful verification of the cardholder. 


>Cardholder verification is the separate API that must be called in the card activation workflow.  Please [click here](../docs/?path=docs/APIs/Card-Management/card-secure-code-validation.md) to explore the cardholder verfication APIs.


# Endpoint
`PUT /v1/card/activate`


## Payload Example

### Request Payload

```json
{
    "businessUnit":"100",
    "cardNumber":"0009846801010273613",
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



### Successful Response Payload

```json
{
    "businessUnit": "100",
    "cardNumber": "0009846801010273613",
    "cardSequence": "1",
    "lastCardActivation": "N",
    "currentCardRequireActivation": "N",
    "cardActivatedDate": "01/10/2021",
    "postToAccountNumber": "0001000010000510760"    
}
```

### Error Response Payload

```json
{
  "errorCode": "V5ED4001SA",
  "errorMessage": "Business Unit not found in the system"  
}
```
Below table provides the list of application's error code and its description. 

| ErrorCode |  Description |
| --------  | ------------------ |
| `V5ED0010SF` | Update Request - Record not found |  
| `V5ED0011SF` | Update Request - Record Add Pending |
| `V5ED4002ED` | Card Number must be provided |
| `V5ED4001SA` | Business Unit not found in the system |
| `V5ED4001SB` | Business Unit is in Add Pending Status |
| `V5ED4001SC` | Business Unit is in Purge Status |
| `V5ED0309SV` | Invalid Current Card Activation | 
| `V5ED0310SV` | Invalid Last Card Activation |  