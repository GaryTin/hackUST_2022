

const userWallet = document.getElementById('userWallet')
const name = document.getElementById('name')

async function getAccount() {
    const accounts = await ethereum.request({ method: 'eth_requestAccounts' });
    const account = accounts[0];
    userWallet.innerText = account;
}

window.addEventListener('DOMContentLoaded', () => {
    getAccount()
});


function run_function(param1, param2){
    window.CSRF_TOKEN = "{{ csrf_token }}";
    console.log("running");
    $.ajax({
        url : "random_url/", // the endpoint
        type : "POST", // http method
        data : { param_first : param1,
                param_second : param2 ,
                csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
                },
                // data sent with the get request

        // handle a successful response
        success : function(json) {
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};

function read_name(){
    console.log("running");
    $.ajax({
        url : "read_name/", // the endpoint
        type : "GET", // http method
        data : { }, // data sent with the get request

        // handle a successful response
        success : function(data) {
            console.log("success"); // another sanity check
            name.innerText = data
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};

function change_name(){
    console.log("running");
    $.ajax({
        url : "change_name/", // the endpoint
        type : "GET", // http method
        data : { }, // data sent with the get request

        // handle a successful response
        success : function(data) {
            console.log("success"); // another sanity check
            name.innerText = data
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};