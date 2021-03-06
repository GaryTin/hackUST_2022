![Banner](https://github.com/GaryTin/hackUST_2022/blob/main/title_banner.png)
# ๐#Bargain

> #Bargain is a Decentralized Supply Chain Management Web Application, aiming to promote a Smart Shopping Experience by minimizing overspending and overproduction in the consumption cycle. It also features many of the Web3.0 users engagement by the introduction of reliable review system. 
[๐ฝWatch our Presentation Video](https://youtu.be/iCX0bOnjBM0)
> 

# ๐จBuilt With

๐ธ๏ธ This website is developed with [**Python Django Framework**](https://www.djangoproject.com/), [**Web3.py**](https://web3py.readthedocs.io/en/stable/), [**Web3.js**](https://web3js.readthedocs.io/en/v1.7.1/), [**jQuery**](https://jquery.com/) and [**Chart.js**](https://www.chartjs.org/), integrated with [**MetaMask**](https://metamask.io/) and [**Infura**](https://infura.io/), hosted on [**PythonAnywhere**](https://www.pythonanywhere.com/). It does not contain any web templates online. 

๐ The smart contract is developed with [**Solidity**](https://docs.soliditylang.org/en/v0.8.13/). (Details: [Smart Contract Deployed](https://github.com/GaryTin/hackUST_2022#smart-contract-deployed))

๐ For development purpose, the smart contact used in this project is now deployed on the public blockchain, **Ropsten Ethereum Test Network**. The speed of reading and writing data may be slow, while writing data may even take longer time. The speed is solely depending on the blockchain traffic. We apologize for any inconvenience caused. 

In a real implementation, the smart contract will deploy on a self-developed blockchain instead of a public blockchain, which can greatly improve the read-write speed.

# ๐Link to Our Web Prototype - You Can Try!
Click here: [**Sharp Bargain**](http://tinkwaiki.pythonanywhere.com/SharpBargain/index/) <br>
โ๏ธ This website is currently designed for `๐ป Desktop View` only. <br>
โ๏ธ The mobile version will be developed in Phase two (See below: [Future Development](https://github.com/GaryTin/hackUST_2022/edit/main/README.md#future-development)).

[๐ฝ Watch our Demonstration Video](https://youtu.be/Ayr0fSBbhik)

# ๐จ UI/UX Design and Appendix
Please refer to the [PDF file](Appendix_UIUX.pdf).

# ๐ญRoles (Test account addresses)

- ๐ญManufacturer (0xDE37A3dce5249C31b12e45F46988fc30b50e19FD)
- ๐ฌRetailer (0xEfA8901C15007db0b19B17cEF667120397143239)
- ๐ง๐ปConsumer (0x6c4d9360e36B1a59daCF7FB9d71AaFB68b9657b8)

โ๏ธ All addresses are defaulted as Consumer accounts. If you would like to test functions on the Manufacturer or Retailer pages, please feel free to use our designated Test Accounts. (See below: [MetaMask Test Accounts Set Up](https://github.com/GaryTin/hackUST_2022#metamask-test-accounts-set-up))
<br>
<br>
โ๏ธ If you would like to try our website with your own public addresses, please feel free to contact us. We are more than happy to help you signing up as `Manufacturer` or `Retailer` accounts. (See more: [Why can't I register as Manufacturer or Retailer by myself?](https://github.com/GaryTin/hackUST_2022#can-i-register-as-manufacturer-or-retailer-myself) ) 


# ๐ฐPrerequisites

## ๐ฟCompatible Browsers

- Firefox
- Google Chrome
- Safari
- Opera

## ๐ฆMetaMask Test Accounts Set Up

This website can only login in with a **MetaMask** account. Please install MetaMask Extension if you want to try this website. 

1. Install MetaMask on your browser at [https://metamask.io/download/](https://metamask.io/download/).
2. Press the buttons `Get Started` > `Import Wallet` > `I Agree`. <br>
    
    <p align="center">
    <img src="https://github.com/GaryTin/hackUST_2022/blob/main/screenshots/metamask_step2.1.png?raw=true" alt="MetaMask Setup Step2.1 Instruction" width="200"/>
    <img src="https://github.com/GaryTin/hackUST_2022/blob/main/screenshots/metamask_step2.2.png?raw=true" alt="MetaMask Setup Step2.2 Instruction" width="300"/>
    <img src="https://github.com/GaryTin/hackUST_2022/blob/main/screenshots/metamask_step2.3.png?raw=true" alt="MetaMask Setup Step2.3 Instruction" width="300"/>
    </p>

    
3. Enter the following 12-word Seed Phrase:
    
    > churn drift kind explain jeans weird give pipe draw style speak vivid
    > 
    
    โ?๏ธ This account is created for demonstration purposes only, for your own safety, please **DO NOT** use it for other purposes.
    <p align="center">
    <img src="https://github.com/GaryTin/hackUST_2022/blob/main/screenshots/metamask_step3.png?raw=true" alt="MetaMask Setup Step3 Instruction" width="600"/>
    </p>
    
4. Create your own password.
5. Click on the circle located at the top right hand corner, then choose `โSettings` > `Advanced`.
    <p align="center">
    <img src="https://github.com/GaryTin/hackUST_2022/blob/main/screenshots/metamask_step5.1.png?raw=true" alt="MetaMask Setup Step5.1 Instruction" width="400"/>
    <img src="https://github.com/GaryTin/hackUST_2022/blob/main/screenshots/metamask_step5.2.png?raw=true" alt="MetaMask Setup Step5.2 Instruction" width="400"/>
    </p>
6. Turn ON `Show Test Networks`.
    <p align="center">
    <img src="https://github.com/GaryTin/hackUST_2022/blob/main/screenshots/metamask_step6.png?raw=true" alt="MetaMask Setup Step6 Instruction" width="600"/>
    </p>
7. Click on the dropdown list named `๐ขEthereum Mainnet` next to the circle you have just clicked, and switch to `๐ดRopsten Test Network`.
    <p align="center">
    <img src="https://github.com/GaryTin/hackUST_2022/blob/main/screenshots/metamask_step7.1.png?raw=true" alt="MetaMask Setup Step7.1 Instruction" width="600"/>
    <img src="https://github.com/GaryTin/hackUST_2022/blob/main/screenshots/metamask_step7.2.png?raw=true" alt="MetaMask Setup Step7.2 Instruction" width="200"/>
    </p>
    
8. Click on the Circle again and choose `โCreate Account`, name it as โRetailerโ, then click `Create`.
    <p align="center">
    <img src="https://github.com/GaryTin/hackUST_2022/blob/main/screenshots/metamask_step8.1.png?raw=true" alt="MetaMask Setup Step8.1 Instruction" width="200"/>
    <img src="https://github.com/GaryTin/hackUST_2022/blob/main/screenshots/metamask_step8.2.png?raw=true" alt="MetaMask Setup Step8.2 Instruction" width="400"/>
    </p>
    
9. Repeat Step 8 and name it as โManufacturerโ.
    <p align="center">
    <img src="https://github.com/GaryTin/hackUST_2022/blob/main/screenshots/metamask_step9.png?raw=true" alt="MetaMask Setup Step9 Instruction" width="400"/>
    </p>

Three test accounts has been set up. You can now use these accounts to log in to the web. (**Account 1** is the Consumer account, **Retailer** is the retailer account and **Manufacturer** is the manufacturer account.)
<p align="center">
<img src="https://github.com/GaryTin/hackUST_2022/blob/main/screenshots/metamask_finish.png?raw=true" alt="MetaMask Setup Finished" width="400"/>
</p>

# ๐ธAbout Our Prototype
## ๐ญAssumptions

- We assume that Retailerโs POS system will only scan(input) their own procured products (which are bought from the Manufacturer). Random data input may lead to undefined behaviors as scanning products that do not exist in the store will not happen in real-life operations.
    - List of product IDs that can be inputted into the POS system for the demonstration account: [65,67,68,69,85,86,89].
    - If more products are supplied by manufacturers. Please refer to the .txt file for those product IDs. This file is auto-generated after the manufacturer's wholesale sale process.

## ๐Disconnecting MetaMask Account

โ?๏ธ For security reasons, MetaMask does not allow disconnecting by the website. Please  disconnect your account after logging out and log in with a different role.


1. Click the MetaMask Web Extension (Fox Icon: ๐ฆ) and click on the button `๐ข Connected`  at the top left hand corner.
    - If you cannot see the MetaMask Web Extension button, please pin it via Extension Tool Dropdown list. (See image)
    <p align="center">
    <img src="https://github.com/GaryTin/hackUST_2022/blob/main/screenshots/metamask_disconnect_step1.png?raw=true" alt="MetaMask Disconnect Account Step1 Instruction"/>
    <img src="https://github.com/GaryTin/hackUST_2022/blob/main/screenshots/metamask_extension.png?raw=true" alt="MetaMask Extension Instruction"/>
    </p>
    
2. Click the button with 3 dots placed vertically, and click `Disconnect this account` .
    <p align="center">
    <img src="https://github.com/GaryTin/hackUST_2022/blob/main/screenshots/metamask_disconnect_step2.1.png?raw=true" alt="MetaMask Disconnect Account Step2.1 Instruction"/>
    <img src="https://github.com/GaryTin/hackUST_2022/blob/main/screenshots/metamask_disconnect_step2.2.png?raw=true" alt="MetaMask Disconnect Account Step2.2 Instruction"/>
    </p>
3. Now you disconnected the account, and can log in with a different role.

## ๐Smart Contract Deployed
[View Smart Contract Source Code](https://github.com/GaryTin/hackUST_2022/blob/main/hackUST_2022_B_Sharp/sc.sol) <br>
[View Smart Contract on Etherscan](https://ropsten.etherscan.io/address/0x8dCEDE30c2a8bD175654b67e010F898061fF0072)

# โFAQ

## Can I register as Manufacturer or Retailer myself?

No, you cannot. For security reason, only the smart contract owner can modify the list of manufacturers and retailers. We are sorry that it is impossible for any other users to register their own addresses as a manufacturer or a retailer.

# ๐ฎFuture Development
- [ ] ๐ Extra Features:
    - [ ]  Inventory Loss Record (Normal Loss/Abnormal Loss)
    - [ ]  Inventory Recall of Defective Products from Retailer
    - [ ]  Goods Return from Consumer
- [ ] ๐ซ Token Generation
- [ ] ๐ Online Shop Integration
- [ ] ๐ฑ Mobile App and Mobile Friendly Website
