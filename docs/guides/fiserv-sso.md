# Fiserv Single Sing On (SSO)

DevStudio application works with Ping to authenticate Fiserv internal users.

## Pairing your device with PingID

Set up your device for secure authentication with PingID by pairing it with your account. When you have selected the device and method you want, pair it to your account, so you can use it to authenticate with PingID.

### What is pairing and why do I need to do it?

PingID lets you register, or 'set up' a device or authentication method by pairing it with your account, so you can sign on to your company services and applications with the added security of multi-factor authentication (MFA). 
Pairing creates a trust between the authentication method you want to use and your account, so you can use that authentication method to authenticate during the sign on process.

### Using PingID mobile app authentication

To get started, you'll need to download the app to your mobile device, and pair (connect) your device with your account. After you've paired your device, each time you sign on to your account, you will receive a push notification to your mobile device asking you to authenticate.

### Diferent Environments (DEV, QA, STAGE, PROD)

DevStudio has a number of environments with each own unique purpose and its own resources. PingID has correspinding to DevStudio environments. In order to sign in with PingID for a particular environment, a user must pair (connect) a device with user account for that particular environment. Similarely a user would create an account for each environment separately.

### Device pairing flow by Environment

Download and install the PingID app on your mobile device.<br><br>

Device pairing link for [DEV Environment](https://desktop.pingone.com/fiservdev)<br><br>

The link redirectes to PingID for authentication with **Fiserv email credentials**.<br><br>
![PingID SignOn page](../assets/images/sso/ping-signon.png)

After authentication, click on the profile icon in the top right corner and choose **Devices** menu item.<br><br>
![PingID Account page](../assets/images/sso/ping-profile.png)

On **My Devices** page, click **+ Add** button to register your mobile device.<br><br>
![PingID My Devices page](../assets/images/sso/ping-add-devices.png)

Open your **PingID mobile app** to view the list of registrations under **My Organizations** section.<br><br>
![PingID Mobile app](../assets/images/sso/ping-mobile.png)


## DevStudion authirization flow useing PingID

By clicking on **Fiserv email log in** button a user is redirected to the PingID IAM (Identity Access Management) owned login page.<br>
A user provides necessary credentials.<br>
The PingID mobile app receives the notification to complete the authentication flow.<br>
After authentication, a user is redirected back to DevStudio to complete account authorization.

