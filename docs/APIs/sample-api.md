# Sample APIs

### Authorizations
```java
    /**
     * Provides the meta data for the byDate api. The meta data will be utilized for building custom queries for the dataset.  For instance the field results 'id' attribute will be input into the byDate API to return the aforementioned fields.
     *
     * @method /v1/authorization/details/metaData
     * @param none
     * @return AuthorizationSearchMetaData
     */
```

##### Example Response
```json
{
    "fields": [
        {
            "id": "a_approvalCode",
            "name": "Approval Status",
            "type": "Map",
            "description": "Identifies if the authorization was approved or declined.",
            "mapping": {
                "0": "Unknown",
                "1": "Approved",
                "2": "Declined"
            }
        },
        {
            "id": "a_type",
            "name": "Type",
            "type": "Map",
            "description": "Transaction type code e.g. sale, refund etc.",
            "mapping": {
                "0": "Unknown",
                "1": "Totals",
                "2": "Purchase",
                "3": "Pre Auth Request",
                "4": "Pre Auth Complete",
                "5": "Reversal",
                "6": "Return",
                "7": "Cancellation",
                "8": "Mail Auth",
                "9": "Activate",
                "10": "Reload",
                "11": "Verification",
                "12": "TeleCheck",
                "13": "Start Fueling",
                "14": "Unknown",
                "15": "Fee",
                "16": "Withdrawal",
                "17": "Deposit",
                "18": "Transfer",
                "19": "Balance Inquiry",
                "20": "Score Fraud",
                "21": "Generate Token",
                "22": "Adjustment",
                "23": "Report Lost/Stolen",
                "24": "Close Account",
                "25": "Freeze Account",
                "26": "Unfreeze Account",
                "27": "Transaction History",
                "28": "Timeout Reversal",
                "29": "Setup Auto-reload",
                "30": "Return Reversal",
                "31": "Cash Back"
            }
        },
        {
            "id": "a_transactionDateTime",
            "name": "Txn Date & Time",
            "type": "Time",
            "description": "Date & Time of the authorization transaction."
        },
        {
            "id": "a_accountNumber",
            "name": "Account #",
            "type": "String",
            "description": "Card number used for authorization transaction."
        }
    ],
    "filters": [
        {
            "field": "a_accountNumber",
            "type": "Text"
        }
    ]
}
```

