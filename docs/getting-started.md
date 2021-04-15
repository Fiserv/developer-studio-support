# Getting Started 

## Welcome to Reporting

The Fiserv Reporting APIs are built on the foundation of REST. The APIs accept standard JSON requests and return JSON encoded responses while leveraging industry standard [HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) for a seamless integration. Interaction through our Reporting APIs provides the developer community the ability to retrieve transaction, chargeback, funding and settlement information in a simple and intuitive manner. You will find that access to itemized or summary data can be quickly initiated programmatically for statistical analysis purposes. 

---

## Access Reporting APIs

Get up and running with access to our development portal to use our Reporting APis.

### 1. Get Access to our Developer Platform

Request and create a developer account in the Developer Portal.

> After registration the developer will have an instant access to Reporting APIs.

### 2. Generate an API key

Go to the Reporting page and create a Sandbox app to obtain your client APIKey and APISecret.

> These are required in the Authentication Header.

### 3. Constructing the API call

Construct an [API request](?path=docs/APIs/api-model.md) to use the Reporting APIs.

---

## Authentication
Fiserv Reporting API authentication is based on the API keys concept. Each consumer will be assigned their own set of API keys that allow message passing to and from the exposed RESTful interface. Your API keys restrict data to only the owners of that data set. 

Your assigned API keys perform an [HTTP Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication) by passing the assigned key via the request header. 

### Authenticated Request
```javascript
curl -X GET "https://cat.api.firstdata.com/reporting/v1/fraud/search/getMetaData" -H "accept: application/json" -H "apikey: YOURAPIKEY"
```

For more information on creating and using API keys for your organization, please click [here](https://www.google.com). 

---

## API Structure

## Data Retrieval
>Data can be accessed in two ways. Each domain model supports both itemized transaction download as well as summarized data. In order to utilize the API for the data that you are interested, the developer will need to retrieve the meta data associated with that domain model. 
