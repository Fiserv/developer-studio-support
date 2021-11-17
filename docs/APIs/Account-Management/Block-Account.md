# Block-Unblock Account

This service is used to update the Account Block Code.

This service can be called with an account number. When either *blockCode 1* or *blockCode2* has a value other than spaces, the new Block code can be applied to the unused entry on the account. 
> *If there is an entry in the Block Code, the system is using the block code priorities established on the Logo record. The message then will check if the new block code has a higher priority than the block code it is replacing. If so new block code will be applied else the old will remain.* 


# Endpoint
`PATCH /v1/accounts/blockUnblock`


## Payload Example


### Request Payload

```json
{
  "businessUnit": "100",
  "accountNumber": "0001000010000510481",
  "blockCode1": "X"
}
```

### Minimum Requirements
The below table contains the mandatory fields required for a successful request. The full request schemas are available in our [API Explorer](../api/?type=patch&path=/v1/accounts/blockUnblock).

The below table identifies the required parameters in the request payload.

| Variable | Type | Length | Description/Values |
| -------- | :--: | :------------: | ------------------ |
| `businessUnit` | *number* | 3 | Identification number of the organization associated with the account. |
| `accountNumber` | *string* | 19 | Account Number of the cardholder. | 
| `blockCode1` | *string* | 1 | Block Code to assign to the account. |



### Successful Response Payload


```json
{
    "businessUnit": "100",
    "accountNumber": "0001000010000510481",
    "product": "1",
    "billingAcctInd": "0",
    "blockCode1": "X",
    "blockCodeDate1": "08/18/2021",
    "blockCode2": " ",
    "blockCodeDate2": "00/00/0000"
}
```

### Error Response Payload

```json
{
  "errorCode": "V5BS0125SV",
  "errorMessage": "AMBS - Invalid Block Code 1"  
}
```
Below table provides the list of application's error code and its description. 

| ErrorCode |  Description/Values |
| --------  | ------------------ |
| `V5BS0011SF` |	Update Request - Record Add Pending|
| `V5BS4001EA` |	Invalid Business Unit|                                      
| `V5BS4001SC` |	Business Unit is in Purged Status|     
| `V5BS4002SA` |	Invalid Account Number|  
| `V5BS0125SV` | AMBS - Invalid Block Code 1 |
| `V5BS0127SV` | AMBS - Invalid Block Code 2 |
| `V5BS0125SC` | Block Code 1 cannot be replaced with one of the lower priority |  
| `V5BS0127SC` | Block Code 2 cannot be replaced with one of the lower priority |
