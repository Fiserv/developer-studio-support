# Block-Unblock Card

This service is used to update the block codes and the reason codes for the block codes for cards and accounts. Same service can be used to unblock the card by passing spaces in the block-code field of the request body.

# Endpoint
`PUT /v1/cards/blockUnblock`


## Payload Example


### Request Payload

```json
{
  "businessUnit": "100",
  "cardNumber": "0009846801010273605",
  "cardSequence": "0001",
  "blockCode": "X" 
}
```

### Minimum Requirements
The below table contains the mandatory fields required for a successful request. The full request schemas are available in our [API Explorer](../api/?type=patch&path=/v1/cards/blockUnblock).

The below table identifies the required parameters in the request payload.

| Variable | Type | Length | Description/Values |
| -------- | :--: | :------------: | ------------------ |
| `businessUnit` | *number* | 3 | Identification number of the organization associated with the Card. |
| `CardNumber` | *string* | 19 | Card Number of the cardholder. | 
| `cardSequence` | *number* | 04 | A sequence number of the card in case of card scheme 2 else pass the default value of 0001. | 
| `blockCode1` | *string* | 1 | Block Code to assign to the Card. |



### Successful Response Payload


```json
{
    "businessUnit": "100",
    "cardNumber": "0009846801010273605",
    "cardSequence": "1",
    "postToAccountNumber": "0001000010000510760",    
    "blockCode": "X",
    "blockDate": "01/10/2021", 
    "warningCode1": "1",
    "cardholderType": "1"
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
| `V5ED4001SA` | Business Unit not found |
| `V5ED4001SB` | Business Unit is in Add Pending Status |
| `V5ED4001SC` | Business Unit is in Purge Status |
| `V5ED0010SF` | Update Request - Record not found | 
| `V5ED0011SF` | Update Request - Record Add Pending |
| `V5ED4002ED` | Card Number must be provided | 
| `V5ED4003ED` | CARD Sequence number must be greater than zero |   
| `V5ED4004SF` | Invalid Card Sequence |   
| `V5ED0301EA` | Priority of new block code cannnot be lower than the existing block code |            
| `V5ED0301EB` | Block Code not maintainable for card scheme 0 |
| `V5ED4005ED` | Can't update Block Code when card status is F |  




