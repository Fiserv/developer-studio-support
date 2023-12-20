# Fiserv Single Sing On (SSO)

DevStudio application works with Ping to authenticate Fiserv internal users.

## Pairing your device with PingID

Set up your device for secure authentication with PingID by pairing it with your account. When you have selected the device and method you want, pair it to your account, so you can use it to authenticate with PingID.

### What is pairing and why do I need to do it?

PingID lets you register, or 'set up' a device or authentication method by pairing it with your account, so you can sign on to your company services and applications with the added security of multi-factor authentication (MFA). 
Pairing creates a trust between the authentication method you want to use and your account, so you can use that authentication method to authenticate during the sign on process.

### Using PingID mobile app authentication

To get started, you'll need to download the app to your mobile device, and pair (connect) your device with your account. After you've paired your device, each time you sign on to your account, you will receive a push notification to your mobile device asking you to authenticate.

## DevStudion authirization flow useing PingID

By clicking on **Fiserv email log in** button the user is redirected to the IAM (Identity Access Management) owned login page.
The user provides necessary credentials.
The PingID mobile app receives the notification.
and completes the authentication flow.
After authentication, the user is redirected back to DevStudio, that authorizes the user.

