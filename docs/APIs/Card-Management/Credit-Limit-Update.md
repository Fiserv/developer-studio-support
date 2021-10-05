# Credit Limit Update

This service is used to update the credit limit of the cardholder’s account. The service can also be used to update the available credit for relationship when the Credit limit is changed to any of the accounts tied to that relationship. The input request can have either card number or FirstVision account number but the credit limit update will be applied on the account level.

In the response message, system returns the resulting account open-to-buy amount based on the updated credit limit, account number, updated credit limit.


Fields that are not provided in the Request object will be initialised to their default values. All numeric fields are initialised to zero and alphanumeric fields initialised to spaces