<link rel="stylesheet" href="/css/form_styles.css">
<script>
    function show(shown, hidden) {
        document.getElementById(shown).style.display = 'block';
        document.getElementById(hidden).style.display = 'none';
        return false;
    }
</script>
<div id="ticket_form">
    <div class="title">Ticket viewer</div>

    <body>
        <div id="Page1">
            <pre>
            {{feedback}}
            </pre>
            <a href="#" onclick="return show('Page2','Page1');">Show previous page</a>
            </br>
            <a href="#" onclick="return show('Page2','Page1');">Show next page</a>
        </div>

        <div id="Page2" style="display:none">
            <pre>
            {{feedback}}
            </pre>
            <a href="#" onclick="return show('Page2','Page1');">Show previous page</a>
            </br>
            <a href="#" onclick="return show('Page2','Page1');">Show next page</a>
        </div>

    </body>



    </form>
</div>