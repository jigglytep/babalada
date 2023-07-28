<script lang="ts">
  import type { PageData } from "./$types";
	export let data: PageData;
  import PortfolioThumbnail from "$components/PortfolioThumbnail.svelte";
  import userIcon from '$pictures/userIcon.png'
  import { accountStore } from "$stores/AccountStore";
	const { account } = accountStore;
	// TODO: if $account.id equals data.slug, show full user profile
	// TODO: otherwise, show user profile from data from endpoint /api/user/{data.slug}

  let bio = "We the People of the United States, in Order to form a more perfect Union, establish Justice, insure domestic Tranquility, provide for the common defence, promote the general Welfare, and secure the Blessings of Liberty to ourselves and our Posterity, do ordain and establish this Constitution for the United States of America.";
  let currentYear: number = new Date().getFullYear();
  let stocks = [
    {ticker: "FSC", name:"FakeStock.com", price: "$1.00", quanity: "1"},
    {ticker: "S12", name: "Stock123.com", price: "$2.50", quanity: "3"}
  ]
  let portfolios = [
    {name: "Main", created: "7/6/2023", funds: 1345},
    {name: "Backup", created: "7/6/2023", funds: 1245},
    {name: "Startegy 3", created: "7/1/2023", funds: 1320.85},
    {name: "Portfolio4", created: "7/5/2023", funds: 0.01}
  ]
</script>

<div id="main-container">
  <img src={userIcon} alt="User's profile picture">
  <div id="userInfo">
    <h1>{data.slug}</h1>
    <p>Username: @Babalada1</p>
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
    {#if portfolios.length == 0}
    <p>{data.slug} has no created portfolios</p>
    {:else}
      {#each portfolios as p, i}
      <PortfolioThumbnail number = {i + 1} name = {p.name} created = {p.created} funds = {p.funds} />
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
  
  img {
    width: 15em;
    height: 15em;
    margin-right: 1em;
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


</style>