<script lang="ts">
  import type { PageData } from "./$types";
  export let data: PageData;

  // for chartjs
  import { Chart } from 'chart.js/auto'
  import { onMount } from "svelte";

  // fake content vars
  let stocks = [
    {ticker: "AAPL", name:"Apple", price: 0, quanity: 7},
    {ticker: "AMZN", name: "Amazon", price: 0, quanity: 10},
    {ticker: "TSLA", name: "Tesla", price: 0, quanity: 3}
  ]
  let funds: number = 1000.00;

  // chart js varibles
  let chartCanvas: any;
  let chartData: Array<Number> = [];
  let chartLabels: Array<String> = [];
  let ctx:any;
  let linechart: any;
  let stockChartCanvas: any;
  let stockChartData: Array<Number> = [];
  let stockChartLabels: Array<String> = [];
  let stockCtx: any;
  let stockLineChart: any;

  // modal varibles
  let stockName: String;
  let stockModal: any;
  let stockTicker: String;
  let stockPrice: Number;
  let stockOwned: number;

  async function getCurrentPriceForOwnedStocks() {
    let request: RequestInit = {
      method: "GET"
    }
    let url: any;
    for(let i = 0; i < stocks.length; i++) {
      url = "http://127.0.0.1:5000/api/stock_info/" + (stocks[i]["ticker"]).toLowerCase();
      let fetchResponce = await fetch(url, request);
      let responce = await fetchResponce.json();
      stocks[i]["price"] = responce[0]["ask"];
      stocks = stocks;
    }
  }

  function updateMetrics() {
    let date = new Date();
    let label = `${date.getMonth() + 1}/${date.getDay()}/${date.getFullYear()}`;
    chartLabels.push(label);
    chartData.push(funds);
    linechart.update();
  }

  async function getStockChartInfo(ticker: String) {
    let request: RequestInit = {
      method: "GET"
    }
    let url = "http://127.0.0.1:5000/api/stock_info/" + ticker.toLowerCase();
    for(let i = 0; i < 15; i++) {
      setTimeout(async () => {
        let fetchResponce = await fetch(url, request);
        let responce = await fetchResponce.json();
        stockChartData.push(responce[0]["ask"]);
        let date = new Date();
        let label = `${date.getHours()}:${date.getMinutes()}:${date.getMilliseconds()}`;
        stockChartLabels.push(label);
        stockLineChart.update();  
      }, 3000)
    }
  }

  function createGraph() {    
    ctx = chartCanvas.getContext('2d');
    linechart = new Chart(ctx, {
      type: "line",
      data: {
        labels: chartLabels,
        datasets: [{
          label: 'Funds Over Time',
          data: chartData
        }]
      }
    })
  }
  
  function createStockGraph() {
    stockCtx = stockChartCanvas.getContext('2d');
    stockLineChart = new Chart(stockCtx, {
      type: "line",
      data: {
        labels: stockChartLabels,
        datasets: [{
          label: "Price (labels are time)",
          data: stockChartData
        }]
      }
    })
  }

onMount(() => {
  createGraph();
  getCurrentPriceForOwnedStocks();
  updateMetrics();
});

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
      closeInspect();
    }
    updateMetrics();
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
      updateMetrics();
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
  getStockChartInfo(stockTicker);
}

function closeInspect() {
  stockModal.style.display = "none";
  stockModal.close();
  stockLineChart.destroy();
  stockChartData.splice(0, stockChartData.length);
  stockChartLabels.splice(0, stockChartLabels.length);
}

async function test() {
  let request: RequestInit = {
      method: "GET"
    }
  let url = "http://127.0.0.1:5000/api/algos/" + stockTicker.toLocaleLowerCase();
  let fetchResponce = await fetch(url, request);
  let responce = await fetchResponce.json();
  console.log(responce)
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
        <button on:click={test}>Test</button>
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

  #stockCanvas {
    margin-bottom: .5em;
  }
</style>
