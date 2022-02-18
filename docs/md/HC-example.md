---
tags: [carat, commerce-hub, enterprise, master-data, additional-transaction-data]
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
| `additionalData` | *object* | N/A | Used to identify specific data based on transaction requirements. |
| `directedRouting` | *object* | N/A | Required in Directed Routing transactions. |
| `customFields` | *array* | N/A | Used to submit merchant custom fields used in terminal processing such as Key Value Pair. |


---

<!--
type: tab
title: JSON Example
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

---

#### Bill Payment Indicator

<!-- theme: warning -->
> Bill Payment Indicator is required for Charges, Cancel and Capture transactions where a bill payment is being processed.

The below table identifies the valid values of the `billPaymentIndicator`.

| Value | Description |
| ----- | ----- |
| *SINGLE* | Single charge not for recurring services or installment plan. |
| *DEFERRED* | A charge for an order with a delayed payment for a specified amount of time. |
| *INSTALLMENT* | Single purchase where the cardholder is billed (charged) in installments. |
| *RECURRING* | Agreement where charges will occur on a periodic basis (e.g. subscriptions). |

---

## Additional Data

Additional Data identifies various elments based on the specific transaction type.

<!--
type: tab
titles: additionalDataCommon, JSON Example
title: additionalDataCommon
-->

| Variable | Type | Maximum Length | Description/Values |
| ----- | ----- | ----- | ----- |
| `ecomURL` | *string* | 512 | Contains the URL of the site performing the Ecommerce transaction. |
| `requestedTestResponseCode` | *string* | 28 | Value used to test/replicate a transaction Error. **Valid Values:** NO_CONNECTION_AVAILABLE, IOEXCEPTION_RECEIVED.|

<!---
| `baiFlag` | *string* | 31 | Visa required [Business Application Identifier](#business-application-identifier) (BAI) used to identify the intended use of a [disbursement](?path=docs/Resources/Guides/Disbursement.md). |
| `emvParameterDownloadIndicator` | *boolean* |  N/A  | Indicator if EMV Parameter has to be downloaded, sent as part of Auth/Sale Response.|
-->

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

<!---
#### Business Application Identifier
The BAI determines the data carried in the message, the limits and economics that may apply to the transaction, and may be used by the sending and/or receiving issuer to make an authorization decision. Below table identifies the valid values of `baiFlag`.

| Value | Description |
| ----- | ----- |
| *PERSON_TO_PERSON* | Person to person initiated. |
| *PERSON_TO_PERSON_BANK_INITIATED* | Person to person bank initiated. |
| *BUSINESS_TO_BUSINESS* | Business to business initiated. |
| *DIGITAL_WALLET* | Digital Wallet transfer. |
| *ACCOUNT_TO_ACCOUNT* | Account to account transfer. |
| *TOP_OFF* | Account top off or reload. |
| *ACCOUNT_VERIFICATION* | [Account verification](?path=docs/Resources/API-Documents/Payments_VAS/Verification.md) or $0.00 auth. |
| *FUNDS_TRANSFER* | Funds Transfer. |
| *DISBURSEMENT* | Funds disbursement or payout. |
| *GAMBLING_PAYOUT* | Gambling payout non-online. |
| *GAMBLING_PAYOUT_ONLINE* | Online gambling payout. |
-->

---

<!--
## See Also

- [API Explorer](../api/?type=post&path=/payments/v1/charges)
- [Charge Request](?path=docs/Resources/API-Documents/Payments/Charges.md)
- [Capture Request](?path=docs/Resources/API-Documents/Payments/Capture.md)
- [Cancel Request](?path=docs/Resources/API-Documents/Payments/Cancel.md)
- [Refund Request](?path=docs/Resources/API-Documents/Payments/Refund.md)
-->
<!---
- [Credit Request](?path=docs/Resources/API-Documents/Payments/Credit.md)
- [Forced Post](?path=docs/Resources/API-Documents/Payments/Forced.md)
-->
<!-- Example of the comment... -->
