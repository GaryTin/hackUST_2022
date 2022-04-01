<script >
    var ac;
    async function get_accounts()
    {
        const accounts = await ethereum.request({ method: 'eth_accounts' });
        return accounts;
    }
    get_accounts().then(
        function (value)
            {
                var new_href = "{% url "cusDashboard" 1234 %}".replace(/1234/,value[0].toString());
                document.getElementById("home").href=new_href;
                new_href = "{% url "cusHistory" 1234 %}".replace(/1234/,value[0].toString());
                document.getElementById("History").href=new_href;
                new_href = "{% url "cusView" 1234 %}".replace(/1234/,value[0].toString());
                document.getElementById("View").href=new_href;
                new_href = "{% url "cusComment" 1234 %}".replace(/1234/,value[0].toString());
                document.getElementById("Comment").href=new_href;
            }
    );
</script>