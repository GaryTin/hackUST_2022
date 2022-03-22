// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;
pragma abicoder v2;
import "@openzeppelin/contracts/utils/Strings.sol";

//Strings.toString(myUINT)
contract SharpBargain
{
    uint256 product_count;
    uint256 batch_count;
    mapping(uint => Chain_Product) products; //prod_id => Chain_Product

    address[] manufacturers;
    address[] retailers;
    address owner;
    uint256[] prod_id_array;
    Chain_Product[] temp_prod_array;
    string[] temp_string_array;

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

    modifier addressMatch(address target)
    {
        require(msg.sender == target, "Not Match");
        _;
    }


    //TO-DO
    //design 2 method

    /*
        both method, manu need to input retailer address


        1 is for demp purpose, so manu input prod_type and quantity n, then program check it quantity vaild, if vaild, search from begining to get first n prod
        with that prod_type and manu address

        2 of real application, manu need to use RFID scanner to get all selling product_id, the input the array of prod_id to function,
        program will set all inform in those products ID

    */


    struct Chain_Product                //pk = batch_id + manu_address + prod_type
    {
        uint256 prod_id;                //unique ID
        uint256 batch_id;               //find which make with this tgt
        string prod_type;               //what is that

        address manu_address;           //who make
        address retailer_address;       //who sell
        address buyer_address;          //who buy

        uint256 prod_production_date;   //when this is made
        uint256 procure_date;           //when retailer buy
        uint256 purchase_date;          //when buyer buy

        string prod_wholesale_price;    //retailer buy price
        //string purchase_retail_price;   //buyer buy price

        string comment;                 //buyer how see
        uint8 rate;                     //0-5 start

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

    function compareStrings(string memory a, string memory b) public pure returns (bool)
    {
        return (keccak256(abi.encodePacked((a))) == keccak256(abi.encodePacked((b))));
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

    function remove_manufacturer(address m_address) public onlyOwner returns (bool)
    {
        for(uint i = 0; i<manufacturers.length;i++)
        {
            if (manufacturers[i] == m_address)
            {
                delete manufacturers[i];
                return true;
            }
        }
        return false;
    }

    function add_retailer(address new_retailers) public onlyOwner
    {
        retailers.push(new_retailers);
    }

    function remove_retailer(address r_address) public onlyOwner returns (bool)
    {
        for(uint i = 0; i<retailers.length;i++)
        {
            if (retailers[i] == r_address)
            {
                delete retailers[i];
                return true;
            }
        }
        return false;
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

    function add_product(address m_address,string memory prod_type,string memory prod_wholesale_price, uint256 prod_production_date,uint quantity) public addressMatch(m_address) returns (uint256[] memory)
    {
        delete prod_id_array ;
        for (uint i =0; i<quantity;i++)
        {
            products[product_count] = Chain_Product(product_count,batch_count,prod_type,m_address,m_address,m_address,prod_production_date,0,0,prod_wholesale_price,"",6);
            prod_id_array.push(product_count);
            increasement_product_count();
        }
        increasement_batch_count();
        return prod_id_array;

    }

    function retailer_purchase_from_manu_demo(address m_address,address r_address,string memory prod_type,uint256 quantity) public addressMatch(m_address) returns (bool)
    {

        uint256 count = quantity;
        for (uint i =0;i<product_count;i++)
        {
            if(products[i].manu_address==m_address && compareStrings(products[i].prod_type, prod_type))
            {
                products[i].retailer_address = r_address;
                count--;
            }
            if (count == 0)
            {
                return true;
            }
        }

        if(count>0)
        {
            return false;
        }
        else
        {
            return true;
        }
    }

    function retailer_purchase_from_manu_final(address m_address,address r_address,uint256[] memory pid_array) public addressMatch(m_address)
    {
        for (uint i; i<pid_array.length;i++)
        {
            products[pid_array[i]].retailer_address = r_address;
        }
    }

    function buyer_purchase_from_retailer(address buyer_address, uint256 prod_id,uint256 purchase_date) public
    {
        products[prod_id].buyer_address = buyer_address;
        products[prod_id].purchase_date = purchase_date;

    }

    function get_user_history(bool pull_all,address b_address) public returns (Chain_Product[] memory)
    {
        delete temp_prod_array;
        for (uint i =0;i<product_count;i++)
        {
            if(products[i].buyer_address == b_address)
            {
                if (pull_all||(!pull_all && !compareStrings(products[i].comment,"")))
                {
                    temp_prod_array.push(products[i]);
                }

            }
        }
        return temp_prod_array;
    }

    function set_comment(string memory input_comment,uint8 input_rate,uint256 product_id) public
    {
        products[product_id].comment = input_comment;
        products[product_id].rate = input_rate;

    }


    function buyer_view_comment(uint256 product_id) public returns (Chain_Product[] memory)
    {
        delete temp_prod_array;
        string memory p_type = products[product_id].prod_type;
        address r_address = products[product_id].retailer_address;
        for (uint i =0;i<product_count;i++)
        {
           if(compareStrings(products[i].prod_type,p_type) && r_address==products[i].retailer_address && !compareStrings(products[i].comment,"") && products[i].rate <6)
           {
               temp_prod_array.push(products[i]);
           }
        }
        return temp_prod_array;
    }

    function get_remaining(address m_address,string memory p_type) public view returns(uint)
    {
        uint256 count = 0;
        for (uint i =0;i<product_count;i++)
        {
            if(products[i].manu_address==m_address && compareStrings(products[i].prod_type, p_type) && products[i].manu_address==products[i].retailer_address)
            {
                count++;
            }
        }
        return count;
    }

    function retailer_get_all_prod_type(address r_address) public addressMatch(r_address) returns (string[] memory)
    {
        delete temp_string_array;
        for (uint i =0;i<product_count;i++)
        {
            if(products[i].retailer_address == r_address)
            {
                temp_string_array.push(string(abi.encodePacked("{",products[i].prod_type,"}",products[i].manu_address)));
            }
        }
        return temp_string_array;

    }

    function retailer_view_comment(address r_address,string memory p_type) public addressMatch(r_address) returns (Chain_Product[] memory)
    {
        delete temp_prod_array;
        for (uint i =0;i<product_count;i++)
        {
            if(products[i].retailer_address == r_address && compareStrings(products[i].prod_type,p_type) && !compareStrings(products[i].comment,"") && products[i].rate <6)
            {
                temp_prod_array.push(products[i]);
            }
        }
        return temp_prod_array;
    }

    function manu_get_all_data(address m_address) public addressMatch(m_address) returns (Chain_Product[] memory)
    {
        delete temp_prod_array;
        for (uint i =0;i<product_count;i++)
        {
            if(products[i].manu_address == m_address)
            {
                temp_prod_array.push(products[i]);
            }
        }
        return temp_prod_array;
    }

}