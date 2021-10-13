# Spend Limit Updates

This service is used to update the spending limits to control the card usage.  These limits are set at individual card level.


# Endpoint
`PATCH /v1/cardS/spendLimits`


## Payload Example

### ***Request Payload***

```json
{
  "businessUnit":"100",
  "cardNumber":"000984680NNNNNN3605",
  "cardSequence": "0001",
  "maximumAuthorizationsFrequency": "1",
  "maximumAmountSingleATMTransactionAllowed": "10000",
  "maximumAmountATMCashAuthorizationsAllowed": "10000",
  "maximumNumberATMCashAuthorizationsAllowed": "1",  
  "singleOTCCashAuthorizationAllowed": "10000",
  "maximumNumberOTCAuthorizationsAllowed": "1",
  "maximumAmountOTCCashAuthorizationsAllowed": "20000",  
  "singleRetailAuthorizationAllowed": "00000",
  "maximumNumberRetailAuthorizationsAllowed": "1",  
  "maximumAmountRetailAuthorizationsAllowed": "10000"  
}
```

### Minimum Requirements
The below table contains the mandatory fields required for a successful request. The full request schemas are available in our [API Explorer](../api/?type=patch&path=/v1/card/spendLimits).

The below table identifies the required parameters in the request payload.

| Variable | Type | Length | Description |
| -------- | :--: | :------------: | ------------------ |
| `businessUnit` | *number* | 3 | Identification number of the organization associated with the account. |
| `cardNumber` | *string* | 19 | Token Number associated with the clear PAN. | 
| `cardSequence` | *number* | 04 | A sequence number of the card in case of card scheme 2 else pass the default value of 0001. | 
| `maximumAuthorizationsFrequency` | *number* | 1 | Limit frequency to update. Valid values are a) "1"  Daily limits b) "2" Cycle to Date limits c) "3" Year to Date limits  | 
| `maximumAmountSingle***TransactionAllowed` | *number* | 09 | Maximum amount of the Single ***(ATM / OTC / Retail) transaction allowed. | 
| `maximumNumber***AuthorizationsAllowed` | *number* | 09 | Maximum number of the cumulatative ***(ATM / OTC / Retail) transaction allowed for a given frequency (daily / CTD/ YTD). | 
| `maximumAmount***AuthorizationsAllowed` | *number* | 17 | Maximum amount of the cumulatative ***(ATM / OTC / Retail) transaction allowed for a given frequency (daily / CTD/ YTD). | 


### ***Successful Response Payload***

```json
{
    "businessUnit": "100",
    "cardNumber": "000984680NNNNNN3605",
    "cardSequence": "1",
    "maximumNumberRetailAuthorizationsAllowed": "1",
    "maximumAmountSingleATMTransactionAllowed": "$100.00",
    "singleOTCCashAuthorizationAllowed": "$100.00",
    "maximumAmountATMCashAuthorizationsAllowed": "$100.00",
    "postToAccountNumber": "000100001NNNNNN0760",
    "maximumNumberOTCAuthorizationsAllowed": "1",
    "maximumNumberATMCashAuthorizationsAllowed": "1",
    "singleRetailAuthorizationAllowed": "$0.00",
    "maximumAmountRetailAuthorizationsAllowed": "$100.00",
    "maximumAuthorizationsFrequnecy": "1",
    "maximumAmountOTCCashAuthorizationsAllowed": "$200.00"    
}

```

### ***Error Response Payload***

```json
{
  "errorCode": "V5ED0405SF",
  "errorMessage": "Entered amount is exceeding the spend limit threshold"  
}
```
Below table provides the list of application's error code and its description. 

| ErrorCode |  Description |
| --------  | ------------------ |
| `V5ED4001SN` | Business Unit is not numeric |
| `V5ED0407SB` | Business Unit not found in the system |
| `V5ED0405SF` | Entered amount is exceeding the spend limit threshold |  