## Chargeback MetaData
```java
    /**
     * Provides the meta data for the byDate api. The meta data will be utilized for building custom queries for the dataset.  For instance the field results 'id' attribute will be input into the byDate API to return the aforementioned fields.
     *
     * @method /v1/chargeback/details/metaData
     * @param none
     * @return ChargebackSearchMetaData
     */
```

##### Example Request
><strong>Curl</strong>
>```javascript
>curl -X GET "https://cat.api.firstdata.com/reporting/v1/chargeback/details/metaData" -H "accept: application/json"
>```

##### Example Response
```json
{
    "fields": [
        {
            "id": "cb_backendMID",
            "name": "Site (BE)",
            "type": "String",
            "description": "Site (BE) - merchant number associated with each the business location. "
        },
        {
            "id": "cb_authNetwork",
            "name": "Auth Network",
            "type": "Map",
            "description": "Authorization network of the credit card utilized for the transaction.",
            "mapping": {
                "0": "Unknown",
                "1": "American Express",
                "2": "Visa",
                "3": "Mastercard",
                "4": "Discover",
                "5": "Pulse",
                "6": "Accel",
                "7": "Interlink",
                "8": "Jeanie",
                "9": "Maestro",
                "10": "NYCE",
                "11": "CU Alliance",
                "12": "Shazam",
                "13": "EBT",
                "14": "AFFN",
                "15": "Telecheck",
                "16": "Diners Club",
                "17": "PayPal",
                "18": "ValueLink",
                "19": "Private Label",
                "20": "Debit/Other",
                "21": "Voyager",
                "22": "ATH",
                "23": "JCB",
                "24": "Star",
                "25": "Star SE",
                "26": "Star W",
                "27": "Star Access",
                "28": "Fleet",
                "29": "Stored Value Systems (SVS)",
                "30": "Wright Express (WEX)",
                "31": "Incomm",
                "32": "Canadian Debit (Interac)",
                "33": "Not Applicable",
                "34": "Moneris",
                "35": "Vaulted Card",
                "36": "Pin-Authenticated Visa Debit (PAVD)",
                "37": "Mastercard MoneySend",
                "38": "Union Pay",
                "39": "Fraud FlexDetect",
                "40": "Certegy",
                "41": "MCI"
            }
        },
        {
            "id": "cb_receivedDate",
            "name": "Received Date",
            "type": "String",
            "description": "Date when the Chargeback was initiated."
        },
        {
            "id": "cb_statusDate",
            "name": "Status Date",
            "type": "String",
            "description": "Date for an expected response to the client."
        }
    ],
    "filters": [
        {
            "field": "o_chargebackDateType",
            "type": "Choice",
            "mapping": {
                "0": "Authorization Date",
                "1": "Chargeback Date",
                "2": "Status Date",
                "3": "Adjustment Date",
                "4": "Due Date"
            }
        },
        {
            "field": "s_st_abbr_nm",
            "type": "Text"
        },
        {
            "field": "s_altid",
            "type": "Text"
        },
        {
            "field": "s_city",
            "type": "Text"
        },
        {
            "field": "s_zip",
            "type": "Text"
        },
        {
            "field": "cb_accountNumber",
            "type": "Text"
        },
        {
            "field": "cb_first6",
            "type": "Text"
        },
        {
            "field": "cb_last4",
            "type": "Text"
        },
        {
            "field": "cb_invoiceNumber",
            "type": "Text"
        },
        {
            "field": "cb_disputeID",
            "type": "Text"
        },
        {
            "field": "cb_referenceNumber",
            "type": "Text"
        },
        {
            "field": "amountmin",
            "type": "DecimalMin"
        },
        {
            "field": "amountmax",
            "type": "DecimalMax"
        },
        {
            "field": "cb_orderNumber",
            "type": "Text"
        },
        {
            "field": "cb_authNetwork",
            "type": "Choice",
            "mapping": {
                "0": "Unknown",
                "1": "American Express",
                "2": "Visa",
                "3": "Mastercard",
                "4": "Discover",
                "5": "Pulse",
                "6": "Accel",
                "7": "Interlink",
                "8": "Jeanie",
                "9": "Maestro",
                "10": "NYCE",
                "11": "CU Alliance",
                "12": "Shazam",
                "13": "EBT",
                "14": "AFFN",
                "15": "Telecheck",
                "16": "Diners Club",
                "17": "PayPal",
                "18": "ValueLink",
                "19": "Private Label",
                "20": "Debit/Other",
                "21": "Voyager",
                "22": "ATH",
                "23": "JCB",
                "24": "Star",
                "25": "Star SE",
                "26": "Star W",
                "27": "Star Access",
                "28": "Fleet",
                "29": "Stored Value Systems (SVS)",
                "30": "Wright Express (WEX)",
                "31": "Incomm",
                "32": "Canadian Debit (Interac)",
                "33": "Not Applicable",
                "34": "Moneris",
                "35": "Vaulted Card",
                "36": "Pin-Authenticated Visa Debit (PAVD)",
                "37": "Mastercard MoneySend",
                "38": "Union Pay",
                "39": "Fraud FlexDetect",
                "40": "Certegy",
                "41": "MCI"
            }
        }
    ]
}
```