<script lang="ts">
  import PortfolioThumbnail from "$components/PortfolioThumbnail.svelte";
  let ports = [
    {name: "Main", created: "7/6/2023", funds: 1345},
    {name: "Backup", created: "7/6/2023", funds: 1245},
    {name: "Startegy 3", created: "7/1/2023", funds: 1320.85},
    {name: "Portfolio4", created: "7/5/2023", funds: 0.01}
  ]

  function remove(port: any) {
    let p = ports.find(p => p.name == port.name);
    if (p != null) {
      ports.splice(ports.indexOf(p), 1);
    }
    ports = ports;
  }
</script>

<div id="main-container">
    <h1>Active Portfolios</h1>
    {#if ports.length == 0}
    <p>You have no created portfolios</p>
    {:else}
      {#each ports as p, i}
      <PortfolioThumbnail number = {i + 1} name = {p.name} created = {p.created} funds = {p.funds} />
      {/each}
  {/if}
</div>

<style>
  #main-container {
    width: 90%;
    margin: auto;
    padding-top: 1em;
  }
</style>