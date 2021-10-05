# Account Block Code Update

This service is used to update the Account Block Code.

This service can be called with an account number. When either Block Code 1 or Block Code 2 has a value of space, the new Block code can be applied to the unused entry. If there is an entry in the Block Code, the system is using the block code priorities established on the Logo record. The message then will check if the new block code has a higher priority than the block code it is replacing. If so new block code will be applied else the old will remain. Additional to this function a restructure flag has been added.


Fields that are not provided in the Request object will be initialised to their default values. All numeric fields are initialised to zero and alphanumeric fields initialised to spaces