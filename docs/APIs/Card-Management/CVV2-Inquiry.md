# CVV2 Inquiry

This service is used to retrieve the CVV2 block for the supplied Card number and optional elements which will be validated if present as input. On successful validation of the input an encrypted CVV2 Block is returned. All the following values if not left ‘blank’ on the input will be validated against the Card data at the relevant level.

CARD level: Expiry Date, Embosser Name 1

ACCOUNT level: Bank Sort Code (routing number), Bank Account Number

CUSTOMER level: Date of Birth, Postal Code, Memorable Word, Social Security Number, Mobile Phone Number, Home Phone Number, Unique ID

The service will return a ‘pass’ or ‘fail’ for the overall request and a specific response (RC) depending on the CVV2 check: RC value 0 - CVV VALID. All other values means an error has occurred

Fields that are not provided in the Request object will be initialised to their default values. All numeric fields are initialised to zero and alphanumeric fields initialised to spaces