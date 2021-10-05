# Account Transfer

## Intro

This service is used to transfer the account across the products as part product upgrade/downgrade, copy, or fraud transfer. The same service can be used to transfer the primary account with the multi-schemes card products, from one product to another. This service can be executed in a validate mode or update mode based on the mode indicator received in the request message. The request must also contain account number, new account logo and new card logo for this service.

As part of the account transfer the details of old account gets copied to the new account, the active cards get transferred to the new account or if applicable new cards are created in the case of a product upgrade.


Fields that are not provided in the Request object will be initialised to their default values. All numeric fields are initialised to zero and alphanumeric fields initialised to spaces
