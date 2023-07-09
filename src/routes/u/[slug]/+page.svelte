<script lang="ts">
  import type { PageData } from "./$types";
	export let data: PageData;

  let name = "John Smtih";
  let bio = "We the People of the United States, in Order to form a more perfect Union, establish Justice, insure domestic Tranquility, provide for the common defence, promote the general Welfare, and secure the Blessings of Liberty to ourselves and our Posterity, do ordain and establish this Constitution for the United States of America.";
  let currentYear: number = new Date().getFullYear();
  let stocks = [
    {ticker: "FSC", name:"FakeStock.com", price: "$1.00", quanity: "1"},
    {ticker: "S12", name: "Stock123.com", price: "$2.50", quanity: "3"}
  ]
  let ports = [
    {name: "Main", created: "7/6/2023", funds: "$1,345"},
    {name: "Backup", created: "7/6/2023", funds: "$1,245"},
    {name: "Startegy 3", created: "7/1/2023", funds: "1,320.85"},
    {name: "Portfolio4", created: "7/5/2023", funds: "$0.01"}
  ]
</script>

<div id="main-container">
  <div id="picturePlaceholder"></div>
  <div id="userInfo">
    <h1>{name}</h1>
    <p>Username: @JohnSmtih1</p>
    <br />
    <h4>Bio: "{bio}""</h4>
    <br />
    <p>Babalada User since {currentYear}</p>
  </div>
  <aside id="recent">
    <h3>Recently Purchased</h3>
      {#if stocks.length == 0}
        <p>No recently bought stocks</p>
      {:else}
        <ul>
          {#each stocks as stock, i}
          <li>{stock.quanity} shares of {stock.name}</li>
          {/each}
        </ul>
      {/if}
  </aside>
  <main id="mainUserInfo">
    <h2>Active Portfolios</h2>
    {#if ports.length == 0}
    <p>{name} has no created portfolios</p>
    {:else}
      {#each ports as p, i}
      <div class="port">
        <h3>{i + 1}) {p.name}</h3>
        <small>Created: {p.created}</small>
        <br />
        <small>Current Funds: {p.funds}</small>
      </div>
      {/each}
  {/if}
  </main>
</div>

<style>
    #main-container {
    width: 90%;
    margin: auto;
    padding-top: 1em;
    display: grid;
    grid-template-columns: 20em, auto;
    grid-template-rows: 17em auto;
  }
  
  #picturePlaceholder {
    width: 15em;
    height: 15em;
    background-color: grey;
    margin-right: 1em;
    grid-column: 1/ 2;
    grid-row: 1 / 2;
    border-radius: 15px;
  }
  
  #userInfo {
    grid-column: 2 / 3;
    grid-row: 1 / 2;
  }

  #recent {
    grid-column: 1 / 2;
    grid-row: 2 / 3;
  }

  #mainUserInfo {
    grid-column: 2 / 3;
    grid-row: 2 / 3;
  }

  .port {
    width: auto;
    height: auto;
    background-color: grey;
    border-radius: 15px;
    margin-bottom: 1em;
    color: white;
    padding: 1em;
  }
</style>