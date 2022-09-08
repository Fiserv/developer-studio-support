# Requirements

To execute the sample Go program, you will need to download and install Go in your environment.

The Go language [install page](https://go.dev/doc/install) includes detailed download and installation 
instructions for most popular environments.

# Description
The Go program included here issues a Charge request to Commerce Hub. If the request succeeds 
a transaction Id is returned. The program then uses the transaction Id to Cancel the charge.

# Execution

Edit app.go and replace the placeholders with the API Key and Secret that you obtained from Developer Studio.

```bash
$ go run app
```