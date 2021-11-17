# PIN Block Change

The PIN Block Change Service is used to update the PIN Block with the prerequisite that the existing PIN block must be supplied and validated.

# Endpoint
`PATCH /v1/cards/pinBlock`


## Payload Example

### Request Payload

```json
{
    "businessUnit": "200",    
    "cardNumber": "0009543491000080172",
    "currentPinBlock": "A8EFRS432RTODS2R",
    "requestedPinBlock": "6BA8F5DFB742A878",
    "pinChannel": "W",    
    "pinOffset": ""
}
```

### Minimum Requirements
The below table contains the mandatory fields required for a successful request. The full request schemas are available in our [API Explorer](../api/?type=patch&path=/v1/cards/pinBlock).

The below table identifies the required parameters in the request payload.

| Variable | Type | Length | Description |
| -------- | :--: | :------------: | ------------------ |
| `businessUnit` | *number* | 3 | Identification number of the organization associated with the account. |
| `cardNumber` | *string* | 19 | Token Number associated with the clear PAN. | 
| `currentPinBlock` | *string* | 16 | Current PIN block |
| `requestedPinBlock` | *string* | 16 | PIN block to be updated |

### Successful Response Payload

```json
{
    "cardNumber": "0009543491000080172",
    "userFiller": "",
    "filler": "",
}
```

### Error Response Payload

```json
{
  "errorCode": "V5CP4005SZ",
  "errorMessage": "Update Access not granted for Requested Pin Block"  
}
```
Below table provides the list of application's error code and its description. 

| ErrorCode |  Description |
| --------  | ------------------ |
|`V5CP4001SV`| Invalid Business Unit|  
|`V5CP4006SN`| Pin Offset is not numeric |                                      
|`V5CP4005SZ`| Update Access not granted for Requested Pin Block|          
|`V5CP4006SZ`| Update Access not granted for Pin Offset |                       
|`V5CP4007SZ`| Update Access not granted for Pin Channel |                      
|`V5CP4007SV`| Invalid Pin Channel|                                             
|`V5CP0001SF`| Invalid User|                                                  
|`V5CP0021SF`| Not Allowed. System in After hours mode|                         
|`V5CP0022SF`| Not Allowed. System in After hours Update mode |
