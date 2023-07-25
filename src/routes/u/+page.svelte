<script lang="ts">
  import UserThumbnails from "$components/UserThumbnails.svelte";
  let users = [
    {name: "John Smith", username: "JohnSmith1", ports: 10, stocks: 15},
    {name: "Jane Doe", username: "StockExpert", ports: 5, stocks: 20}, 
    {name: "James Smith Jr", username: "RealUser2", ports: 3, stocks: 10},
    {name: "Bill Bob", username: "StockHaver", ports: 2, stocks: 31},
    {name: "Thomas LastName", username: "InvestKnower", ports: 1, stocks: 42},
    {name: "Douglas Thomas", username: "CaptinStocks", ports: 5, stocks: 2},
    {name: "Geogre Washington", username: "PresidentStocks", ports: 3, stocks: 1}
  ]
</script>

<div id="main-container">
  <h1>Search Users</h1>
  <div id="users-container">
    {#if users.length == 0}
    <p>No Users Found</p>
    {:else}
    <div id="headers">
      <p id="placeholder">img</p>
      <p>Name</p>
      <p>Number of Active Portfolios</p>
      <p>Number of Owned Stocks</p>
      <p>Go To Profile</p>
    </div>
    {#each users as u}
    <UserThumbnails name = {u.name} username = {u.username} numOfPorts = {u.ports} numOfStocks = {u.stocks}/>
    {/each}
    {/if}
  </div>
</div>

<style lang="scss">
  #main-container, #users-container{
    width: 95%;
    margin: auto;
  }

  #main-container h1 {
    padding: .5em;
  }

  #headers {
    border: .15em solid black;
    display: grid;
    grid-template-columns: 5em 30% 20% 20% 20%;
    text-align: center;
  }

  #placeholder {
    visibility: hidden;
  }
</style>