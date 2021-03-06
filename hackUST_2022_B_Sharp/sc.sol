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
		require(msg.sender == owner, "Not owner!");
		_;
	}

    modifier addressMatch(address target)
    {
        require(msg.sender == target, "Sender Address not match! You can view or modify this!");
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

    function get_remaining(address m_address,string memory prod_type) public view returns(uint)
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

    event retailer_receipt (string prod_index);

    function retailer_purchase_from_manu(address m_address,address r_address,string memory prod_type,uint256 purchase_date,uint256 quantity) public addressMatch(m_address)
    {

        uint remaining = get_remaining(m_address,prod_type);
        string memory result;
        if(remaining < quantity)
        {
            result = "Out of Supply";
            emit retailer_receipt(result);
            return;
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
        emit retailer_receipt(result);
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
    function toAsciiString(address x) internal pure returns (string memory) {
        bytes memory s = new bytes(40);
        for (uint i = 0; i < 20; i++) {
            bytes1 b = bytes1(uint8(uint(uint160(x)) / (2**(8*(19 - i)))));
            bytes1 hi = bytes1(uint8(b) / 16);
            bytes1 lo = bytes1(uint8(b) - 16 * uint8(hi));
            s[2*i] = char(hi);
            s[2*i+1] = char(lo);
        }
        return string(s);
    }

    function char(bytes1 b) internal pure returns (bytes1 c) {
        if (uint8(b) < 10) return bytes1(uint8(b) + 0x30);
        else return bytes1(uint8(b) + 0x57);
    }

    function get_user_history(address b_address) public addressMatch(b_address) view returns (string memory)
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

    function get_uncomment_prod_by_id (address b_address,uint256 prod_id) public addressMatch(b_address) view returns(string memory)
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
                if(compareStrings(comment,""))
                {
                    string memory prod_type;
                    string memory prod_retail_price;
                    (prod_type,prod_retail_price) = get_prod_type_price(pid_list[i]);
                    uint256 purchase_date = get_buyer_purchase_date(b_address,pid_list[i]);
                    result = (string)(abi.encodePacked(result,"[",prod_type,"/",uint2string(pid_list[i]),"/",uint2string(purchase_date),"/",prod_retail_price,"/",comment,"/",uint2string(rate),"],"));
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

    function get_all_uncomment_prod (address b_address) public addressMatch(b_address) view returns(string memory)
    {
        uint[] memory pid_list = get_all_pid(b_address);
        string memory result;
        for(uint i=0; i<pid_list.length;i++)
        {
            string memory comment;
            uint8 rate;
            (comment,rate) = get_comment_and_rate(pid_list[i]);
            if(compareStrings(comment,""))
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

    function get_manu_address(uint256 pid) internal view returns (address)
    {
        for (uint i=0;i<products.length;i++)
        {
            if(pid>=products[i].start_index && pid < products[i].end_index )
            {
                return  products[i].manu_address;
            }
        }
        revert("Cant find Manufacturer for this Product ID.");

    }

    function get_purchase_date(uint pid) internal view returns (uint256)
    {
        for (uint i=0;i<buyer_purchase_records.length;i++)
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
        return 0;
    }

    function buyer_view_comment(uint256 pid) public view returns (string memory)
    {
        string memory result;
        string memory prod_type;
        string memory retailer_price;
        (prod_type,retailer_price) = get_prod_type_price(pid);
        address m_address = get_manu_address(pid);
        for(uint i =0; i<products.length;i++)
        {
            if (products[i].manu_address == m_address && compareStrings(products[i].prod_type,prod_type))
            {
                for (uint j = products[i].start_index;j<products[i].end_index;j++)
                {
                    string memory comment;
                    uint8 rate;
                    (comment,rate) = get_comment_and_rate(j);
                    if(!compareStrings(comment,""))
                    {
                        uint256 purchase_data = get_purchase_date(j);
                        result = (string)(abi.encodePacked(result,"[",uint2string(purchase_data),"/",prod_type,"/",comment,"/", uint2string(rate) ,"],"));
                    }

                }

            }
        }
        return result;

    }


    function substring(string memory str, uint startIndex, uint endIndex) internal pure returns (string memory )
    {
        bytes memory strBytes = bytes(str);
        bytes memory result = new bytes(endIndex-startIndex);
        for(uint i = startIndex; i < endIndex; i++)
        {
            result[i-startIndex] = strBytes[i];
        }
        return string(result);
    }

    function utfStringLength(string memory str) internal pure returns (uint length)
    {
        uint i=0;
        bytes memory string_rep = bytes(str);

        while (i<string_rep.length)
        {
            if (string_rep[i]>>7==0)
                i+=1;
            else if (string_rep[i]>>5==bytes1(uint8(0x6)))
                i+=2;
            else if (string_rep[i]>>4==bytes1(uint8(0xE)))
                i+=3;
            else if (string_rep[i]>>3==bytes1(uint8(0x1E)))
                i+=4;
            else
                i+=1;

            length++;
        }
    }



    function get_position(string memory str,string memory target ) internal pure returns(uint256)
    {
        uint length = utfStringLength(str);
        for (uint i =0; i<length;i++)
        {
            if(compareStrings(substring(str,i,i+1),target))
            {
                return i;
            }
        }
        revert("Cant find this char in this string.");
    }


    function retailer_get_all_prod_type(address r_address) public addressMatch(r_address) view returns (string memory)
    {
        string memory result;
        for(uint i =0; i<retailer_purchase_records.length;i++)
        {
            if(retailer_purchase_records[i].retailer_address == r_address)
            {
                uint256 pid = str2uint(substring(retailer_purchase_records[i].prod_indexs,1,get_position(retailer_purchase_records[i].prod_indexs,"/"))) ;
                string memory prod_type;
                string memory prod_retail_price;
                (prod_type,prod_retail_price) = get_prod_type_price(pid);
                result = (string)(abi.encodePacked(result,prod_type,","));
            }
        }
        return result;

    }

    function get_index_pair(string memory str) internal pure returns(uint,uint,uint)
    {
        uint256 slash_pos = get_position(str,"/");
        uint256 open_bracket_pos = get_position(str,"[");
        uint256 close_bracket_pos = get_position(str,"]");
        string memory start_index_str = substring(str,open_bracket_pos+1,slash_pos);
        string memory end_index_str = substring(str,slash_pos+1,close_bracket_pos);
        return (str2uint(start_index_str),str2uint(end_index_str),close_bracket_pos+2);

    }

    function retailer_view_comment(address r_address,string memory _prod_type) public addressMatch(r_address) view returns (string memory)
    {
        string memory result;
        uint256 start_index;
        uint256 end_index;
        uint256 next=0;
        uint256 str_length =1;
        for(uint i = 0; i<retailer_purchase_records.length;i++)
        {
            if(retailer_purchase_records[i].retailer_address == r_address)
            {

                do{
                    str_length = utfStringLength(retailer_purchase_records[i].prod_indexs);
                    (start_index,end_index,next) = get_index_pair(retailer_purchase_records[i].prod_indexs);
                    for(uint j = start_index;j<end_index;j++)
                    {
                        string memory prod_type;
                        string memory prod_retail_price;
                        (prod_type,prod_retail_price) = get_prod_type_price(j);
                        if(compareStrings(prod_type,_prod_type))
                        {
                            string memory comment;
                            uint8 rate;
                            (comment,rate) = get_comment_and_rate(j);
                            if (!compareStrings(comment,""))
                            {
                                uint256 purchase_data = get_purchase_date(j);
                                result = (string)(abi.encodePacked(result,"[",uint2string(purchase_data) ,"/",comment,"/",uint2string(rate),"],"));
                            }
                        }

                    }
                }while (str_length>=next);

            }
        }
        return result;
    }


    function is_sold_to_retailer(uint256 pid) internal view returns(bool)
    {
        uint256 start_index;
        uint256 end_index;
        uint256 next=0;
        uint256 str_length =1;

        for(uint i = 0;i< retailer_purchase_records.length;i++)
        {
            do{
                str_length = utfStringLength(retailer_purchase_records[i].prod_indexs);
                (start_index,end_index,next) = get_index_pair(retailer_purchase_records[i].prod_indexs);
                if(pid>=start_index && pid<end_index)
                {
                    return true;
                }
            }while (str_length>=next);

        }
        return false;
    }

    function is_sold_to_buyer(uint256 pid) internal view returns(bool)
    {
        for(uint i = 0; i<buyer_purchase_records.length;i++)
        {
            uint[] memory temp =  buyer_purchase_records[i].prod_ids;
            for (uint j=0;j<temp.length;j++)
            {
                if (pid == temp[j])
                {
                    return true;
                }
            }
        }
        return false;
    }

    function get_retailer_data(uint pid) internal view returns (string memory,string memory)
    {
        uint256 start_index;
        uint256 end_index;
        uint256 next=0;
        uint256 str_length =1;

        for(uint i = 0;i< retailer_purchase_records.length;i++)
        {
            do{
                str_length = utfStringLength(retailer_purchase_records[i].prod_indexs);
                (start_index,end_index,next) = get_index_pair(retailer_purchase_records[i].prod_indexs);
                if(pid>=start_index && pid<end_index)
                {
                    return (toAsciiString(retailer_purchase_records[i].retailer_address),uint2string(retailer_purchase_records[i].retailer_purchase_date));
                }
            }while (str_length>=next);

        }
        return ("","");

    }

    function manu_get_all_data(address m_address) public addressMatch(m_address) view returns (string memory)
    {
        string memory result;
        for(uint i = 0; i<products.length;i++)
        {
            if(products[i].manu_address==m_address)
            {
                uint256 start_index = products[i].start_index;
                uint256 end_index = products[i].end_index;
                for(uint j = start_index;j<end_index;j++)
                {
                    string memory r_status;
                    if(is_sold_to_retailer(j))
                    {
                        if(is_sold_to_buyer(j))
                        {
                            r_status = "Sold to Buyer";
                        }
                        else
                        {
                            r_status = "In retailer stock";
                        }
                    }
                    else
                    {
                        r_status = "In manufacturer stock";
                    }

                    string memory r_address;
                    string memory retailer_purchase_date;
                    (r_address,retailer_purchase_date) = get_retailer_data(j);
                    result = (string)(abi.encodePacked(result,"[",products[i].prod_type,"/",r_address,"/",retailer_purchase_date,"/",uint2string(products[i].prod_production_date),"/",r_status,"],"));

                }
            }
        }
        return result;
    }

    function retailer_get_prod_info_by_pid(uint pid) public view returns (string memory)
    {
        string memory result;
        for(uint i = 0; i<products.length;i++)
        {
            if(pid>=products[i].start_index && pid<products[i].end_index)
            {
                result = (string)(abi.encodePacked(result,"[",uint2string(pid) ,"/",products[i].prod_type,"/",products[i].prod_retail_price,"],"));
            }
        }

        return result;
    }

    function get_lastest_retailer_record(address r_address) public view returns(string memory)
    {
        for (uint i = retailer_purchase_records.length-1;i>=0;i--)
        {
            if(retailer_purchase_records[i].retailer_address == r_address)
            {
                return retailer_purchase_records[i].prod_indexs;
            }
        }
        return "No record for this retailer!";
    }


}

    