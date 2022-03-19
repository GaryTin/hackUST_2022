// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;
import "@openzeppelin/contracts/utils/Strings.sol";

//Strings.toString(myUINT)
contract SharpBargain
{
    uint256 product_count;
    uint256 batch_count;
    mapping(uint =>Purchase) pid_purchases; //prod_id => Purchase
    mapping(address =>Purchase) bid_purchases; //user_id => Purchase
    mapping(address =>Purchase) mid_purchases; //manu_id => Purchase
    Procurement[] procurements;
    mapping(uint => Chain_Product) products; //prod_id => Chain_Product

    address[] manufacturers;
    address[] retailers;
    address owner;

    constructor()
    {
        owner = msg.sender;
        product_count = 0;
        batch_count = 0;
    }


    modifier onlyOwner()
	{
		require(msg.sender == owner, "Not owner");
		_;
	}

    struct Purchase
    {
        address user_address;
        address retailer_address;
        uint256 prod_id;
        uint256 purchase_date;
        string purchase_comment;
        string purchase_retail_price;
    }

    struct Procurement
    {
        address retailer_address;
        address manu_address;
        string procure_prod_category;
        uint256 procure_quantity;
        uint256 produre_date;
    }

    struct Chain_Product
    {
        address manu_address;
        uint256 prod_id;
        string procure_prod_category;
        string prod_wholesale_price;
        uint256 prod_production_date;

    }


    function str2uint(string memory numString) internal pure returns(uint)
    {
        uint val=0;
        bytes memory stringBytes = bytes(numString);
        for (uint  i =  0; i<stringBytes.length; i++)
        {
            uint exp = stringBytes.length - i;
            bytes1 ival = stringBytes[i];
            uint8 uval = uint8(ival);
            uint jval = uval - uint(0x30);

            val +=  (uint(jval) * (10**(exp-1)));
        }
        return val;
    }

    function uint2string(uint _i) internal pure returns (string memory)
    {
        return Strings.toString(_i);
    }

    function increasement_product_count() internal
    {
        product_count ++;
    }
    function increasement_batch_count() internal
    {
        batch_count ++;
    }

    function add_manufacturer(address new_manufacturer) public onlyOwner
    {
        manufacturers.push(new_manufacturer);
    }

    function add_retailer(address new_retailers) public onlyOwner
    {
        retailers.push(new_retailers);
    }

    function get_role(address input_address) public view returns (string memory)
    {

        for (uint i; i < manufacturers.length; i++) {
            if(input_address == manufacturers[i])
            {
                return "manufacturer";
            }
        }

        for (uint i; i < retailers.length; i++) {
            if(input_address == retailers[i])
            {
                return "retailer";
            }
        }

        return "customer";
    }

    function add_product(address m_address,string memory prod_type,string memory prod_wholesale_price, uint256 prod_production_date,uint quantity) public
    {
        string memory new_procure_prod_category = string(abi.encodePacked(prod_type,  "-", uint2string(batch_count))) ;
        for (uint i =0; i<quantity;i++)
        {
            products[product_count] = Chain_Product(m_address,product_count,new_procure_prod_category,prod_wholesale_price,prod_production_date);
            increasement_product_count();
        }
        increasement_batch_count();

    }

    function get_product_from_pid(uint256 prod_id) internal view returns (Chain_Product memory)
    {
        return products[prod_id];
    }

    function add_purchase(address buyer_address,address retailer_address, uint256 prod_id,uint256 purchase_date,string memory purchase_retail_price) public
    {
        Purchase memory this_Purchase = Purchase(buyer_address,retailer_address,prod_id,purchase_date,"",purchase_retail_price);
        pid_purchases[prod_id] = this_Purchase;
        bid_purchases[buyer_address] = this_Purchase;
        mid_purchases[products[prod_id].manu_address] = this_Purchase;

    }

    function set_comment(string memory input_comment,uint256 product_id) public
    {
        pid_purchases[product_id].purchase_comment = input_comment;
    }

    function view_comment(uint256 product_id) public view returns (string memory)
    {
        return pid_purchases[product_id].purchase_comment;
    }
}