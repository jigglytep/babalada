<script lang="ts">
  import type { PageData } from "./$types";
  export let data: PageData;
  import { GET } from '../../api/[slug]/+server'

  // for chartjs
  import { Chart } from 'chart.js/auto'
  import { onMount } from "svelte";

  // fake content vars
  let stocks = [
    {ticker: "FSC", name:"FakeStock.com", price: 1.00, quanity: 7},
    {ticker: "S12", name: "Stock123.com", price: 2.50, quanity: 10}
  ]
  let count1 = 0;
  let count2 = 0;
  let funds: number = 50.00;

  // chart js varibles
  let chartCanvas: any;
  let chartData: Array<Number> = Array.from({length: 50}, () => Math.floor(Math.random() * 101));
  let chartLabels: Array<String> = Array.from({length: 50}, () => "L" + ++count1);
  let ctx:any;
  let linechart: any;
  let stockChartCanvas: any;
  let stockChartData: Array<Number> = Array.from({length: 50}, () => Math.floor(Math.random() * 101));
  let stockChartLabels: Array<String> =  Array.from({length: 50}, () => "L" + ++count2);
  let stockCtx: any;
  let stockLineChart: any;

  // modal varibles
  let stockName: String;
  let stockModal: any;
  let stockTicker: String;
  let stockPrice: Number;
  let stockOwned: number;

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
    });
  }
  
onMount(createGraph);

function createStockGraph() {
  stockCtx = stockChartCanvas.getContext('2d');
  stockLineChart = new Chart(stockCtx, {
    type: "line",
    data: {
      labels: stockChartLabels,
      datasets: [{
        label: stockName + " Metrics",
        data: stockChartData
      }]
    }
  })
};

function sell(name: String) {
  let s = stocks.find(s => s.name == name);
  if (s != null) {
    if (s.quanity > 0) {
      s.quanity = s.quanity - 1;
      stockOwned = s.quanity;
      funds += s.price;

    }
    if (s.quanity == 0) {
      stocks.splice(stocks.indexOf(s), 1);
    }
  }
  stocks = stocks;
}
function buy(name: String) {
  let s = stocks.find(s => s.name == name);
  if (s != null) {
    if(funds - s.price >= 0) {
      s.quanity = s.quanity + 1;
      stockOwned = s.quanity;
      funds -= s.price;
    }
    else {
      alert("Not Enough Funds");
    }
  }
  stocks = stocks;
}

function inspect(stock: any) {
  stockModal = document.getElementById('modal');
  stockModal.showModal();
  stockModal.style.display = "grid";
  stockName = stock.name;
  stockTicker = stock.ticker;
  stockPrice = stock.price;
  stockOwned = stock.quanity;
  createStockGraph();
}

function closeInspect() {
  stockModal.style.display = "none";
  stockModal.close();
  stockLineChart.destroy();
}

async function getStockInfo() {
  let params: String = "stock_info/aapl";
  let reqHeaders: Headers = new Headers();
  let request: RequestInit = {
    method: "GET",
    headers: reqHeaders
  }
  const fetchres = await fetch("http://127.0.0.1:5000/api/stock_info/aapl", request);
  const res = await fetchres.json();
  console.log(res);
}


</script>

<div id="main-container">
  <h1>Porfolio: {[data.slug]}</h1>
  <hr />
  <br />
  <div id="secondary-container">
    <h2>Metrics</h2>
    <div id="charts">
      <canvas bind:this={chartCanvas} id="chartCanvas"></canvas>
    </div>
    <h2>Stocks Owned</h2>
    <h3>Current Amount of Money in Portfolio: ${funds}</h3>
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
        {#if stock.quanity != 0} 
          <tr>
            <td>{stock.ticker}</td>
            <td>{stock.name}</td> 
            <td>${stock.price}</td> 
            <td>{stock.quanity}</td> 
            <td><button on:click={() => {sell(stock.name)}}>Sell Shares</button><button on:click={() => {buy(stock.name)}}>Buy Shares</button>
            <button on:click={() => {inspect(stock)}}>Inspect</button></td>
          </tr>
          {/if}
          {/each}
      </tbody>
    </table>
    {/if}
    <dialog id="modal">
      <div id="dialogHeader">
        <h1>{stockName}</h1>
        <hr />
      </div>
      <button on:click={closeInspect} id="closeInspect">X</button>
      <div id="dialogChart">
        <canvas bind:this={stockChartCanvas} id="stockCanvas"></canvas>
      </div>
      <div id="dialogLeft">
        <h3>Ticker: {stockTicker}</h3>
        <h3>Price: ${stockPrice}</h3>
        <h3>Currernt Funds: ${funds}</h3>
        <button on:click={() => {buy(stockName)}}>Buy Shares</button>
      </div>
      <div id="dialogRight">
        <h3>Shares Owned: {stockOwned}</h3>
        <h3>Out of Price Range: No</h3>
        <button on:click={() => {sell(stockName)}}>Sell Shares</button>
        <button on:click={getStockInfo}>TEST GET</button>
      </div>
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
    display: none;
    grid-template-columns: 1fr 1fr 1fr;
    grid-template-rows: 10% 1fr 1fr;
  }

  #dialogHeader {
    grid-column: 1 / 4;
    grid-row: 1 / 2;
  }

  #closeInspect {
    grid-column: 3/ 4;
    grid-row: 1 / 2;
    height: 3em;
    width: 3em;
    position: absolute;
    top: 0;
    right: 0;
    background-color: red;
  }

  #dialogChart {
    grid-column: 1 / 4;
    grid-row: 2 / 3;
    margin-bottom: 1em;
    width: 95%;
    margin:auto;
  }

  #dialogLeft{
    grid-column: 1 / 2;
    grid-row: 3 / 4;
  }

  #dialogRight{
    grid-column: 3 / 4;
    grid-row: 3 / 4;
  }
</style>
