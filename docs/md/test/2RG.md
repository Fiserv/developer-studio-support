---
tags: [carat, commerce-hub, enterprise, master-data, additional-transaction-data]
<!-- Comments -->
---

# Additional Data Common

Additional data common is used for specific business requirements.

<!--
type: tab
titles: additionalDataCommon, JSON Example
title: additionalDataCommon
-->

The below table identifies the parameters in the `additionalDataCommon` object.

| Variable | Type | Maximum Length | Description |
| -------- | -- | ------------ | ------------------ |
| `additionalData`  <!-- Comment 2 --> | *object* | N/A | Used to identify specific data based on transaction requirements. |
| [NetworkToken]<!--(?path=docs/Resources/Guides/Payment-Sources/Network-Token.md)--> | *object* | N/A | Required in Directed Routing transactions. |
| `customFields` | *array* | N/A | Used to submit merchant custom fields used in terminal processing such as Key Value Pair. |


---

<!--
type: tab
title: JSON Example
<!-- Comment 2 --> 
-->

JSON string format for `additionalDataCommon`:

```json
{
   "additionalDataCommon":{
      "additionalData":{
         "baiFlag": "PERSON_TO_PERSON",
         "ecomURL":"https://www.somedomain.com",
         "requestedTestResponseCode":"NO_CONNECTION_AVAILABLE",
         "emvParameterDownloadIndicator":true
      },
      "directedRouting":{ // Future Release
         "network": "VISA", // Future Release
         "cardFunction": "CREDIT", // Future Release
         "processor": "fiserv" // Future Release
      },
      "deferredPayments":{ // Future Release
         "numberOfPayments": "5", // Future Release
         "paymentPlan": "PAY_LATER", // Future Release
         "timePeriod": "12" // Future Release
      },
      "recurringPayments":{
        "frequency": "MONTHLY",
        "expiry": "05-05-2025"
      },
      "privateLabel":{ // Future Release
         "paymentSource": "SHELL", // Future Release
         "paymentType": "REFUND", // Future Release
         "specialFinanceIndicator": "24/0" // Future Release
      },
      "customFields":{ // Future Release
         "keyValuePair":{ // Future Release
            "key": "", // Future Release
            "value": "" // Future Release
         }
      }
   }
}
```

<!-- type: tab-end -->
