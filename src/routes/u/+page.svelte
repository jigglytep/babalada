<script>
    let users = [
        {name: "John Smtih", username: "JohnSmtih1"},
        {name: "Jane Don", username: "StockExpert"},
        {name: "James Smith Jr", username: "RealUser2"},
        {name: "Bill Bob", username: "StockHaver"},
        {name: "Thomas LastName", username: "InvestKnower"},
        {name: "Douglas Thomas", username: "CaptinStocks"},
        {name: "Geogre Washington", username: "PresidentofStocks"},
        {name: "Kate Mitchel", username: "StocksRCool"}
    ]

    function goToProfile() {
        console.log("goToProfile");
    }
</script>

<div id="main-container">
    <h1>Users</h1>
    <hr />
    <br />
    <div id="secondary-container">
        {#if users.length == 0}
            <p>You have no created portfolios</p>
        {:else}
        {#each users as u}
            <div class="user">
                <div class="picture"></div>
                <h3>{u.name}</h3>
                <p>@{u.username}</p>
                <br />
                <button on:click={goToProfile}>Go To Profile</button>
            </div>
        {/each}
        {/if}
    </div>
</div>

<style>
  #main-container {
    width: 90%;
    margin: auto;
    padding-top: 1em;
  }

  #secondary-container {
    width: 95%;
    margin: auto;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
  }

  .picture {
    width: 10em;
    height: 10em;
    background-color: black;
    padding: 1em;
  }

  .user {
    width: 12em;
    height: 20em;
    background-color: grey;
    border-radius: 15px;
    color: white;
    padding: 1em;
    margin:1em;
  }
</style>