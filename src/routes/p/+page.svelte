<script>
let ports = [
    {name: "Main", created: "7/6/2023", funds: "$1,345"},
    {name: "Backup", created: "7/6/2023", funds: "$1,245"},
    {name: "Startegy 3", created: "7/1/2023", funds: "1,320.85"},
    {name: "Portfolio4", created: "7/5/2023", funds: "$0.01"}
  ]

  function remove() {
    console.log("delete");
  }
</script>

<div id="main-container">
    <h1>Active Portfolios</h1>
    {#if ports.length == 0}
    <p>You have no created portfolios</p>
    {:else}
      {#each ports as p, i}
      <div class="port">
        <h3>{i + 1}) {p.name}</h3>
        <small>Created: {p.created}</small>
        <br />
        <small>Current Funds: {p.funds}</small>
        <br />
        <button on:click={remove}>Delete</button>
      </div>
      {/each}
  {/if}
</div>

<style>
  #main-container {
    width: 90%;
    margin: auto;
    padding-top: 1em;
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
  
  button {
    padding: 1em;
    background-color: gainsboro;
  }
</style>