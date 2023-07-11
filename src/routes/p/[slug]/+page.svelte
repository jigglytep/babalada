<script lang="ts">
  import type { PageData } from "./$types";
  export let data: PageData;
  import { GET } from '../../api/[slug]/+server'

  // for chartjs
  import { Chart } from 'chart.js/auto'
  import { onMount } from "svelte";

  // fake content vars
  let stocks = [
    {ticker: "FSC", name:"FakeStock.com", price: "$1.00", quanity: 1},
    {ticker: "S12", name: "Stock123.com", price: "$2.50", quanity: 3}
  ]
  let name: String = "John Smtih";
  // chart js varibles
  let chartCanvas: any;
  let chartData: Array<Number> = [1, 2, 3, 4, 5];
  let chartLabels: Array<String> = ["L1", "L2", "L3", "L4", "L5"];
  let ctx:any;
  let linechart: any;

  // modal varibles
  let stockName: String;
  let stockModal: any;

  function createGraph() {    
      ctx = chartCanvas.getContext('2d');
      linechart = new Chart(ctx, {
        type: "line",
        data: {
          labels: chartLabels,
          datasets: [{
            label: 'Metrics',
            data: chartData
          }]
        }
      })
    };
  
onMount(createGraph);

function sell(stock: any) {
  if (stock.quanity > 0) {
    stock.quanity -= 1;
  }
}
function buy(stock: any) {
  stock.quanity += 1;
}

function inspect(name: String) {
  stockModal = document.getElementById('modal');
  stockModal.showModal();
  stockName = name;
}

function closeInspect() {
  stockModal.close();
}

function testGet() {
  
}


</script>

<div id="main-container">
  <h1>{name}'s Porfolio </h1>
  <hr />
  <br />
  <div id="secondary-container">
    <h2>Metrics</h2>
    <div id="charts">
      <canvas bind:this={chartCanvas} id="chartCanvas"></canvas>
    </div>
    <h2>Stocks Owned</h2>
    <br />
    {#if stocks.length === 0}
      <p>You currently have 0 stocks to display</p>
    {:else}
    <table border={1} width="100%" cellspacing="3">
      <thead>
        <tr>
          <th>Ticker</th>
          <th>Stock Name</th>
          <th>Indiviaul Price</th>
          <th>Quanity</th>
          <th>Sell</th>
          </tr>
      </thead>
      <tbody>
        {#each stocks as stock}
          <tr>
            <td>{stock.ticker}</td>
            <td>{stock.name}</td> 
            <td>{stock.price}</td> 
            <td>{stock.quanity}</td> 
            <td><button on:click={() => {sell(stock)}}>Sell Shares</button><button on:click={() => {buy(stock)}}>Buy Shares</button>
            <button on:click={() => {inspect(stock.name)}}>Inspect</button></td>
          </tr>
          {/each}
      </tbody>
    </table>
    {/if}
    <dialog id="modal">
      <h2>{stockName}</h2>
      <button on:click={closeInspect}>Toggle Inspect</button>
      <button on:click={testGet}>Test GET</button>
    </dialog>
    <br />
    <h2>Aviable Stocks</h2>
    <br />
  </div>
</div>

<style lang="scss">
  #main-container {
    width: 90%;
    margin: auto;
    padding-top: 1em;
  }
  #secondary-container {
    width: 95%;
    margin: auto;
  }
  
  button {
    display: block;
    padding: .5em;
  }

  #modal::backdrop {
    background-color: grey; 
    opacity: .65;
  }

  #modal {
    width: 55em;
    height: 45em;
    margin: auto;
    padding: 1em;
    border-radius: 15px;
    box-shadow: 7px 5px 5px black;
  }

</style>
