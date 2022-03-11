# Test 

<!--
type: tab
titles: additionalDataCommon, JSON Example, example 3, example 4
-->


The below table identifies the parameters in the `additionalDataCommon` object.


| Variable | Type  | Description |
|--------|---|------------------|
| `additionalData` | *object*  | Used to identify specific data based on transaction requirements. |
| `installments` | *object*| Used in installment bill payments |
| `recurring` | *object*  | Used in recurring bill payments |
| `deferredPayments` | *object* |  Used in defferred bill payments |
| `directedRouting` | *object* |  Required in Directed Routing transactions. |
| `privateLabel` | *object* |  Used to process Private Label payment cards. |
| `customFields` | *array* |  Used to submit merchant custom fields used in terminal processing such as Key Value Pair. |


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
