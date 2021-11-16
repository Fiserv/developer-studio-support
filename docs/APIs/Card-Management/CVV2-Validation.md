# CVV2 Validation

The Card Secure Code Validation service is used to validate the CVV2  and optionally the expiry date of a given card. 

This service is typically called before the card activation or PIN reset service to validate the cardholder.

# Endpoint
`POST /v1/cards/secureCode`


## Payload Example

### Request Payload

```json
{
    "businessUnit": "100",
    "cardNumber": "0009846801010065787",
    "cVV2": "855",
    "expiryDateMMYY": "1123"
}
```

### Minimum Requirements
The below table contains the mandatory fields required for a successful request. The full request schemas are available in our [API Explorer](../api/?type=post&path=/v1/cards/secureCode).

The below table identifies the required parameters in the request payload.

| Variable | Type | Length | Description |
| -------- | :--: | :------------: | ------------------ |
| `businessUnit` | *number* | 3 | Identification number of the organization associated with the account. |
| `cardNumber` | *string* | 19 | Token Number associated with the clear PAN. | 
| `cVV2` | *string* | 3 | CVV2 value of the card |



### Successful Response Payload

```json
{
    "cardNumber": "0009846801010065787"
}
```

### Error Response Payload

```json
{
  "errorCode": "V5VC4003AE",
  "errorMessage": "Invalid CVV2"  
}
```
Below table provides the list of application's error code and its description. 

| ErrorCode |  Description |
| --------  | ------------------ |
|`V5VC4001EA` |	Invalid Business Unit|
|`V5VC0287EA` |	Business Unit not found or in add-pending status|
|`V5VC4002EA` |	Invalid Card number|
|`V5VC4002EA` |	Card number not found |
|`V5VC4004AE` |	Invalid expiry date|
|`V5VC4003AE` |	Invalid CVV2 |
