
<!--
type: tab
titles: additionalDataCommon, JSON Example, example 3, example 4
-->


The below table identifies the parameters in the `additionalDataCommon` object.


| Variable | Type | Maximum Length | Description |
| -------- | -- | ------------ | ------------------ |
| `additionalData` | *object* | N/A | Used to identify specific data based on transaction requirements. |
| `installments` | *object* | N/A | Used in [installment bill payments](?path=docs/Resources/Guides/Bill-Payments/Installment-Payment.md) |
| `recurring` | *object* | N/A | Used in [recurring bill payments](?path=docs/Resources/Guides/Bill-Payments/Recurring-Payment.md) |
| `amountComponents` | *object* | N/A | Used in transactions where additional [amount](?path=docs/Resources/Master-Data/Amount-Components.md) fields such as tax, surcharge, fees are required as part of the request. |
| `billPaymentType` | *string* | 12 | Indicates the type of [bill payment](#bill-payment-indicator). Required for Charges, Cancel and Capture transactions where a bill payment is being processed. | 
| `deferredPayments` | *object* | N/A | Used in [defferred bill payments](?path=docs/Resources/Guides/Bill-Payments/Deferred-Payment.md) |
| `directedRouting` | *object* | N/A | Required in Directed Routing transactions. |
| `subMerchant` | *object* | N/A | Required in transaction initiated by a [Payment Facilitator](?path=docs/Resources/Guides/Industry-Verticals/Payment-Faciliator.md) to identify the sub-merchant information. |
| `privateLabel` | *object* | N/A | Used to process [Private Label](?path=docs/Resources/Guides/Payment-Sources/Private-Label.md) payment cards. |
| `customFields` | *array* | N/A | Used to submit merchant custom fields used in terminal processing such as Key Value Pair. |


---

<!-- type: tab -->

JSON string format for `additionalDataCommon`:

```json
{
   "additionalDataCommon":{
      "additionalData":{
         "baiFlag": "PERSON_TO_PERSON",
         "ecomURL":"https://www.somedomain.com",
         "requestedTestResponseCode":"NO_CONNECTION_AVAILABLE",
         "emvParameterDownloadIndicator":true
      }
   }
}
```

<!-- type: tab -->

JSON string format for `additionalDataCommon`:

```json
{
   "additionalDataCommon":{
      "additionalData":{
         "baiFlag": "PERSON_TO_PERSON",
         "ecomURL":"https://www.somedomain.com",
         "requestedTestResponseCode":"NO_CONNECTION_AVAILABLE",
         "emvParameterDownloadIndicator":true
      }
   }
}
```

<!-- type: tab -->

JSON string format for `additionalDataCommon`:

```json
{
   "additionalDataCommon":{"name": "rekha"}
}
```

<!-- type: tab-end -->
---
