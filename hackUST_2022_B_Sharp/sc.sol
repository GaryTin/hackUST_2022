// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;
pragma abicoder v2;
import "@openzeppelin/contracts/utils/Strings.sol";

//Strings.toString(myUINT)
contract SharpBargain
{
    uint256 product_count;
    uint256 batch_count;

    address[] manufacturers;
    address[] retailers;
    address owner;

    Product[] products;
    Retailer_Purchase_Record[] retailer_purchase_records;
    Buyer_Purchase_Record[] buyer_purchase_records;
    Buyer_Comment[] buyer_comments;



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



    struct Product
    {
        uint256 batch_id;               //find which make with this tgt
        string prod_type;               //what is that

        address manu_address;           //who make
        uint256 prod_production_date;   //when this is made

        string prod_wholesale_price;
        string prod_retail_price;
        uint256 start_index;
        uint256 end_index;
        uint256 remaining;
    }

    struct Retailer_Purchase_Record
    {
        address retailer_address;
        string prod_indexs;
        uint256 retailer_purchase_date;
    }

    struct Buyer_Purchase_Record
    {
        address buyer_address;
        uint[] prod_ids;
        uint256 buyer_purchase_date;
    }

    struct Buyer_Comment
    {
        uint prod_id;
        string comment;
        uint8 rate;
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

        for (uint i; i < manufacturers.length; i++)
        {
            if(input_address == manufacturers[i])
            {
                return "manufacturer";
            }
        }

        for (uint i; i < retailers.length; i++)
        {
            if(input_address == retailers[i])
            {
                return "retailer";
            }
        }

        return "customer";
    }

    function increasement_product_count(uint n) internal
    {
        product_count = product_count +n;
    }

    function increasement_batch_count() internal
    {
        batch_count ++;
    }

    function add_product(string memory prod_type,address m_address,uint256 prod_production_date,string memory prod_wholesale_price,string memory prod_retail_price,uint256 quantity) public addressMatch(m_address)
    {
        uint256 start = product_count;
        increasement_product_count(quantity);
        products.push(Product(batch_count,prod_type,m_address,prod_production_date,prod_wholesale_price,prod_retail_price,start,product_count,quantity));
        increasement_batch_count();
    }

    function get_remaining(address m_address,string memory prod_type) internal view returns(uint)
    {
        uint count = 0;
        for (uint i = 0; i < products.length;i++)
        {
            if(products[i].manu_address == m_address && compareStrings(products[i].prod_type,prod_type))
            {
                count = count + products[i].remaining;
            }
        }
        return count;
    }

    function retailer_purchase_from_manu(address m_address,address r_address,string memory prod_type,uint256 purchase_date,uint256 quantity) public returns (string memory)
    {

        uint remaining = get_remaining(m_address,prod_type);
        string memory result;
        if(remaining < quantity)
        {
            return "Out of Supply";
        }
        for (uint i = 0; i < products.length;i++)
        {
            if (quantity ==0)
            {
                break;
            }
            if(products[i].manu_address == m_address && compareStrings(products[i].prod_type,prod_type) && products[i].remaining>0)
            {
                uint end_i = products[i].start_index + products[i].remaining;
                if(products[i].remaining>=quantity)
                {
                    products[i].remaining = products[i].remaining - quantity;
                    result = (string)(abi.encodePacked(result,"[",uint2string(products[i].start_index + products[i].remaining),"/",uint2string(end_i),"]"));
                    break;
                }
                else
                {
                    quantity = quantity-products[i].remaining;
                    products[i].remaining = 0;
                    result = (string)(abi.encodePacked(result,"[",uint2string(products[i].start_index + products[i].remaining),"/",uint2string(end_i),"],"));

                }
            }
        }
        retailer_purchase_records.push(Retailer_Purchase_Record(r_address,result,purchase_date));
        return result;
    }

    function buyer_purchase_from_retailer(uint[] memory prod_id_list,address b_address,uint256 purchase_date) public
    {
        buyer_purchase_records.push(Buyer_Purchase_Record( b_address,prod_id_list,purchase_date));
    }

    function get_comment_and_rate(uint prod_id) internal view returns(string memory,uint8)
    {
        for(uint i = 0; i<buyer_comments.length;i++)
        {
            if(buyer_comments[i].prod_id == prod_id)
                return (buyer_comments[i].comment,buyer_comments[i].rate);
        }
        return ("",6);
    }

    function get_all_pid(address b_address) internal view returns(uint[] memory)
    {
        uint count = 0;
        for(uint i =0; i<buyer_purchase_records.length;i++)
        {
            if (buyer_purchase_records[i].buyer_address == b_address)
            {
                count = count + buyer_purchase_records[i].prod_ids.length;
            }
        }
        uint[] memory pid_list = new uint[](count);
        count = 0;
        for(uint i =0; i<buyer_purchase_records.length;i++)
        {
            if (buyer_purchase_records[i].buyer_address == b_address)
            {
                uint[] memory pid_list_record = buyer_purchase_records[i].prod_ids;
                for (uint j = 0;j<pid_list_record.length;j++)
                {
                    pid_list[count] = pid_list_record[j];
                    count ++;
                }

            }
        }
        return pid_list;

    }
    function get_prod_type_price(uint256 prod_id) internal view returns (string memory,string memory)
    {
        for(uint i = 0; i< products.length;i++)
        {
            if (prod_id>=products[i].start_index && prod_id<products[i].end_index)
            {
                return (products[i].prod_type,products[i].prod_retail_price);
            }
        }
        return ("","");
    }

    function get_buyer_purchase_date(address b_address,uint pid) internal view returns (uint256)
    {
        for (uint i=0;i<buyer_purchase_records.length;i++)
        {
            if(buyer_purchase_records[i].buyer_address == b_address)
            {
                uint[] memory temp =  buyer_purchase_records[i].prod_ids;
                for (uint j=0;j<temp.length;j++)
                {
                    if (pid == temp[j])
                    {
                        return buyer_purchase_records[i].buyer_purchase_date;
                    }
                }
            }
        }
        return 0;
    }
    function get_user_history(address b_address) public view returns (string memory)
    {
       uint[] memory pid_list = get_all_pid(b_address);
       string memory result;
       for(uint i=0; i<pid_list.length;i++)
       {
           string memory prod_type;
           string memory prod_retail_price;
           (prod_type,prod_retail_price) = get_prod_type_price(pid_list[i]);
           uint256 purchase_date = get_buyer_purchase_date(b_address,pid_list[i]);
           string memory comment;
           uint8 rate;
           (comment,rate) = get_comment_and_rate(pid_list[i]);
           result = (string)(abi.encodePacked(result,"[",prod_type,"/",uint2string(pid_list[i]),"/",uint2string(purchase_date),"/",prod_retail_price,"/",comment,"/",uint2string(rate),"],"));
       }
       return result;
    }

    function get_buyer_address(uint256 pid) internal view returns(address)
    {
        for (uint i=0;i<buyer_purchase_records.length;i++)
        {
            uint[] memory temp =  buyer_purchase_records[i].prod_ids;
            for (uint j=0;j<temp.length;j++)
            {
                if (pid == temp[j])
                {
                    return buyer_purchase_records[i].buyer_address;
                }
            }

        }
        revert("No one have yet buy this product.");
    }

    function set_comment(uint256 pid,string memory comment,uint8 rate) public
    {
        buyer_comments.push(Buyer_Comment(pid,comment,rate));
    }

    function get_uncomment_prod_by_id (address b_address,uint256 prod_id) public view returns(string memory)
    {
        uint[] memory pid_list = get_all_pid(b_address);
        string memory result;
        for(uint i=0; i<pid_list.length;i++)
        {
            if(pid_list[i] ==prod_id)
            {
                string memory comment;
                uint8 rate;
                (comment,rate) = get_comment_and_rate(pid_list[i]);
                if(!compareStrings(comment,""))
                {
                    string memory prod_type;
                    string memory prod_retail_price;
                    (prod_type,prod_retail_price) = get_prod_type_price(pid_list[i]);
                    uint256 purchase_date = get_buyer_purchase_date(b_address,pid_list[i]);

                    result = (string)(abi.encodePacked(result,"[",prod_type,"/",uint2string(pid_list[i]),"/",uint2string(purchase_date),"/",prod_retail_price,"/",comment,"/",uint2string(rate),"]"));
                    return result;
                }
                else
                {
                    return "Already comment!";
                }
            }

        }
        return "You did not buy this product!";

    }

    function get_all_uncomment_prod (address b_address) public view returns(string memory)
    {
        uint[] memory pid_list = get_all_pid(b_address);
        string memory result;
        for(uint i=0; i<pid_list.length;i++)
        {
            string memory comment;
            uint8 rate;
            (comment,rate) = get_comment_and_rate(pid_list[i]);
            if(!compareStrings(comment,""))
            {
                string memory prod_type;
                string memory prod_retail_price;
                (prod_type,prod_retail_price) = get_prod_type_price(pid_list[i]);
                uint256 purchase_date = get_buyer_purchase_date(b_address,pid_list[i]);

                result = (string)(abi.encodePacked(result,"[",prod_type,"/",uint2string(pid_list[i]),"/",uint2string(purchase_date),"/",prod_retail_price,"/",comment,"/",uint2string(rate),"],"));
            }
        }
        return result;

    }




}

