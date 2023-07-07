<script>
    let forums = [
        {title: "FakeStocks123 is the Future", created: "7/6/2023", author: "RealUser2", content: "All legislative Powers herein granted shall be vested in a Congress of the United States, which shall consist of a Senate and House of Representatives. The House of Representatives shall be composed of Members chosen every second Year by the People of the several States, and the Electors in each State shall have the Qualifications requisite for Electors of the most numerous Branch of the State Legislature."},
        {title: "Why You Should Buy 30 Shares of CoolStock", created: "7/4/2023", author: "John Smtih", content: "The Senate of the United States shall be composed of two Senators from each State, chosen by the Legislature thereof, for six Years; and each Senator shall have one Vote.Immediately after they shall be assembled in Consequence of the first Election, they shall be divided as equally as may be into three Classes. The Seats of the Senators of the first Class shall be vacated at the Expiration of the second Year, of the second Class at the Expiration of the fourth Year, and of the third Class at the Expiration of the sixth Year, so that one third may be chosen every second Year;"}, 
        {title: "Just Bought 3 Shares of Stock12", created: "7/2/2023", author: "Geogre Washington", content: "The Times, Places and Manner of holding Elections for Senators and Representatives, shall be prescribed in each State by the Legislature thereof; but the Congress may at any time by Law make or alter such Regulations, except as to the Places of chusing Senators. The Congress shall assemble at least once in every Year, and such Meeting shall be on the first Monday in December, unless they shall by Law appoint a different Day."}
    ]

    let trending = [
        {title: "Stock3's Shares Are Down", author: "User25"},
        {title: "The Best Stocks of 2023", author: "StockExpert"},
        {title: "$3 a Share??!", author: "StockMan12"}
    ]

    let users = [
        {name: "StockExpert"},
        {name: "John Smtih"},
        {name: "User25"},
        {name: "RealUser2"}
    ]
</script>

<div id="main-container">
    <header>
        <h1>Babalada Forums</h1>
        <hr />
        <br />
    </header>
    <aside id="userForms">
        <h3>Trending Users</h3>
        <ol>
            {#each users as user}
                <li>{user.name}</li>
            {/each}
        </ol>  
    </aside>
    <main>
        {#each forums as f}
        <div class="forums">
            <h2>{f.title}</h2>
            <h3>By {f.author}</h3>
            <p>{f.created}</p>
            <br />
            <p><small>{f.content}</small></p>
        </div>
        {/each}
    </main>
    <aside id="trending">
        <h3>Trending</h3>
        <ol>
            {#each trending as t}
                <li>"{t.title}" by {t.author}</li>
            {/each}
        </ol>  
    </aside>
</div>
  
  <style>
    #main-container {
      width: 90%;
      margin: auto;
      padding-top: 1em;
      display: grid;
      grid-template-columns: 33%, 33%, 33%;
      grid-template-rows: 10em, auto;
    }

    header {
        grid-column: 1 / 4;
        grid-row: 1 / 2;
    }

    #userForms {
        grid-column: 1 / 2;
        grid-row: 2 / 3;
    }

    main {
        grid-column: 2 / 3;
        grid-row: 2 / 3;
    }

    #trending{
        grid-column: 3 / 4;
        grid-row: 2 / 3;
    }

    .forums {
        width: 35em;
        height: auto;
        background-color: grey;
        border-radius: 15px;
        color: white;
        padding: 1em;
        margin-bottom: 1em;
    }
  </style>