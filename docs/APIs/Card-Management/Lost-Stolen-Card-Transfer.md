# Lost Stolen Card Transfer

This Lost or Stolen service is used to block the lost card and request for the replacement card.


# Endpoint
`PUT /v1/cards/transfer`


## Payload Example

### ***Request Payload***

```json
{
    "businessUnit": "100",
    "cardNumber": "000984680NNNNNN1264",
    "cardSequenceNumber": "0001",
    "accountNumber": "000100001NNNNNN3777",
    "action": "T",
    "effectiveDate": "",
    "cardReplacementIndicator": "1",
    "blockCode": "L"    
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
| `accountNumber` | *string* | 19 | Account Number. |
| `action` | *string* | 19 | Pass value as "T" for transfer. |
| `cardReplacementIndicator` | *number* | 1 |  Pass "1" for replacement of card or "0" to avoid initiation of Card Replacement . |
| `blockCode` | *string* | 1 | Pass value as "L" to block the old card. |



### ***Successful Response Payload***

```json
{
  "serviceReturnCode": "P",
  "numberOfErrors": "0",
  "maskCardnumber": "000404940XXXXXX4481",
  "cardNumber": "000984680NNNNNN0089",
  "effectiveDate": "10/01/2021",
  "transferFromAccount": "000100001NNNNNN3777",
  "transferToAccount": "000100001NNNNNN3777",
  "transferToCustomer": "984100001NNNNNN3777",
  "blockCode": "L"
}
```

### ***Error Response Payload***

```json
{
  "errorCode": "V5E10004EA",
  "errorMessage": "Invalid Card Number"  
}
```
Below table provides the list of application's error code and its description. 

| ErrorCode |  Description |
| --------  | ------------------ |
| `V5E10004EA` | Invalid Card Number |
| `V5E11020EA` | Only reversal or trasnfer function can be performed |
| `V5E11022SA` | Invalid Transfer-to account number |
| `V5E11024EA` | Invalid Block-code provided |  
| `V5E11026EA` | Invalid effective Date |  
| `V5E11066EA` | Invalid Customer Record Status |  
| `V5E14014SF` | Invalid Card Replacement Indicator |  
