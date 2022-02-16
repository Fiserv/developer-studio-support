#Image centering

<!-- align: center -->
![Logo centered](../assets/images/Fiserv_Logo.jpg)
![Logo NOT centered](../assets/images/Fiserv_Logo.jpg)

#Tabs

<!--
type: tab
titles: First Tab, Second Tab
-->

tab content

<!--
type: tab
-->

second tab content:

<!-- type: row -->

<!-- type: card
title: Card One
description: About...
link: ?path=docs/about-developer-studio.md
-->

<!-- type: card
title: Second Card
description: About...
link: ?path=docs/about-developer-studio.md
-->

<!-- type: row-end -->

<!-- type: tab-end -->

---
tags: [carat, commerce-hub, enterprise, master-data, additional-transaction-data]
---

# Additional Data Common

Additional data common is used for specific business requirements.

<!--
type: tab
titles: additionalDataCommon, JSON Example
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

<!-- type: tab-end -->

---

## Blockquotes Themes

> Blockquotes in default color.
<!-- theme: success -->
> Blockquotes in success theme: <!-- theme: success -->
<!-- theme: warning -->
> Blockquotes in warning theme.
<!-- theme: danger -->
> Blockquotes in danger theme.

---

## Additional Data

Additional Data identifies various elments based on the specific transaction type.

<!--
type: tab
titles: additionalData, JSON Example
-->


The below table identifies the valid values of the `billPaymentIndicator`.

| Value | Description |
| ----- | ----- |
| *SINGLE* | Single charge not for recurring services or installment plan. |
| *DEFERRED* | A charge for an order with a delayed payment for a specified amount of time. |
| *INSTALLMENT* | Single purchase where the cardholder is billed (charged) in installments. |
| *RECURRING* | Agreement where charges will occur on a periodic basis (e.g. subscriptions). |


---

<!-- type: tab -->

JSON string format for `additionalData`:

```json
{
   "additionalData":{
      "baiFlag": "PERSON_TO_PERSON", // Future Release
      "billPayment": false, // Future Release
      "ecomURL": "https://www.somedomain.com",
      "goodsSoldCode": "GIFT_CARD", // Future Release
      "requestedTestResponseCode": "705", // Future Release
      "emvParameterDownloadIndicator": true // Future Release
   }
}
```

<!-- type: tab-end -->

---
