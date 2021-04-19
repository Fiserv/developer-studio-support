# Security

## API Keys
An API key is a string value passed by a client application to the provisioned API proxies. The key uniquely identifies the client application. The application developer embeds the consumer key in the client application header. The client application must present the consumer key for each request. API Services verifies the consumer key before permitting the applications's request.

## Authentication
Fiserv Reporting API authentication is based on the API keys concept. Each consumer will be assigned their own set of API keys that allow message passing to and from the exposed RESTful interface. Your API keys restrict data to only the owners of that data set. 

Your assigned API keys perform an [HTTP Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication) by passing the assigned key via the request header. 

### Authenticated Request
```javascript
curl -X GET "https://cat.api.firstdata.com/reporting/fraud/search/getMetaData" -H "accept: application/json" -H "apikey: YOURAPIKEY"
```

For more information on creating and using API keys for your organization, please click [here](https://www.google.com). 

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