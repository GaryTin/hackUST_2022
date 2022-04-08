# README

# 🛒#Bargain

> #Bargain is a Decentralized Supply Chain Management Web Application, aiming to promote a Smart Shopping Experience by minimizing overspending and overproduction in the consumption cycle. It also features many of the Web3.0 users engagement by the introduction of reliable review system. 
[📽Watch our Presentation Video]()
> 

# 🔨Built With

This website is developed with **Python Django Framework**, **Web3.py**, **Web3.js**, j**Query** and **Chart.js**. It does not contain any web templates online.

For development purpose, the smart contact used in this project is now deployed on the public blockchain, **Ropsten Ethereum Test Network**. The speed of reading and writing data may be slow, while writing data may even take longer time. The speed is solely depending on the blockchain traffic. We apologize for any inconvenience caused. 

In a real implementation, the smart contract will deploy on a self-developed blockchain instead of a public blockchain, which can greatly improve the read-write speed.

📽 Demonstration Video:

# 🎭Roles

- 🏭Manufacturer
- 🏬Retailer
- 🧑🏻Consumer

❄️ All addresses are defaulted as Consumer accounts. If you would like to test functions on the Manufacturer or Retailer pages, please feel free to use our designated Test Accounts. (See below: [MetaMask Test Accounts Set Up](https://github.com/GaryTin/hackUST_2022#metamask-test-accounts-set-up))


# 🔰Prerequisites

## 💿Compatible Browsers

- Firefox
- Google Chrome
- Safari
- Opera

## 🦊MetaMask Test Accounts Set Up

This website can only login in with a **MetaMask** account. Please install MetaMask Extension if you want to try this website. 

1. Install MetaMask on your browser at [https://metamask.io/download/](https://metamask.io/download/).
2. Press the buttons `Get Started` > `Import Wallet` > `I Agree`.
3. Enter the following 12-word Seed Phrase:
    
    > churn drift kind explain jeans weird give pipe draw style speak vivid
    > 
    
    ⚠️ This account is created for demonstration purposes only, for your own safety, please **DO NOT** use it for other purposes.
    
    
4. Create your own password.
5. Click on the circle located at the top right hand corner, then choose `⚙Settings` > `Advanced`.
6. Turn ON `Show Test Networks`.
7. Click on the dropdown list named `🟢Ethereum Mainnet` next to the circle you have just clicked, and switch to `🔴Ropsten Test Network`.
8. Click on the Circle again and choose `➕Create Account`, name it as “Retailer”, then click `Create`.
9. Repeat Step 8 and name it as “Manufacturer”.

Three test accounts has been set up. You can now use these accounts to log in to the web. (**Account 1** is the Consumer account, **Retailer** is the retailer account and **Manufacturer** is the manufacturer account.)

# 🕸Try Our Web!

🔗Link to our Website:  [Sharp Bargain](http://tinkwaiki.pythonanywhere.com/SharpBargain/index/)


❄️ This website is currently designed for `💻 Desktop View` only. The mobile version will be developed in Phase two.

## 💭Assumptions

- We assume that Retailer’s POS system will only scan(input) their own procured products (which are bought from the Manufacturer). Random data input may lead to undefined behaviors as scanning products that do not exist in the store will not happen in real-life operations.
    - List of product IDs that can be inputted into the POS system for the demonstration account: [65,67,68,69,85,86,89].
    - If more products are supplied by manufacturers. Please refer to the .txt file for those product IDs. This file is auto-generated after the manufacturer's wholesale sale process.


## 🔌Disconnecting MetaMask Account

⚠️ For security reasons, MetaMask does not allow disconnecting by the website. Please  disconnect your account after logging out and log in with a different role.


1. Click the MetaMask Web Extension (Fox Icon: 🦊) 
2. Click on the button `🟢 Connected`  at the top left hand corner below the Fox (🦊).
3. Click the button with 3 dots placed vertically, and click `Disconnect this account` .
4. Now you disconnected the account, and can log in with a different role.

## 📄Smart Contract Deployed
[View Smart Contract Source Code](https://github.com/GaryTin/hackUST_2022/blob/main/hackUST_2022_B_Sharp/sc.sol) <br>
[View Smart Contract on Etherscan](https://ropsten.etherscan.io/address/0x8dCEDE30c2a8bD175654b67e010F898061fF0072)

# ❓FAQ

## Can I register as Manufacturer or Retailer myself?

No, you cannot. For security reason, only the smart contract owner can modify the list of manufacturers and retailers. We are sorry that it is impossible for any other users to register their own addresses as a manufacturer or a retailer.

# 🔮Future Development

- 🎫Token Generation
- 🛍Online Shop Integration
- 📱 Mobile App
- Mobile Friendly Website

# 🙌🏻Credentials

abcdefg
