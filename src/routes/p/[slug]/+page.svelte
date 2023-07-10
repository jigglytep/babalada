<script lang="ts">
  import type { PageData } from "./$types";
  export let pageData: PageData;
  let stocks = [
    {ticker: "FSC", name:"FakeStock.com", price: "$1.00", quanity: "1"},
    {ticker: "S12", name: "Stock123.com", price: "$2.50", quanity: "3"}
  ]
  function sell() {
    console.log("Sell");
  }
  function buy() {
    console.log("Buy")
  }
  let name : string = "John Smtih";

  let chartData:Array<Number> = []
  let chartLabels:Array<String> = []
  let count: any = 0;  
  let chart: any;
  let temp: string;

  function addData() {
    while(count <= 100) {
      temp = "L" + count;
      chartLabels.push(temp);
      temp = "";
      chartData.push(count);
      count++;
      chartData = chartData;
      chart.update();
      console.table(count);
    }
  }

  // chart js
  import {
    Chart,
  } from 'svelte-chartjs';
  import {
    Chart as ChartJS,
    Tooltip,
    Legend,
    BarElement,
    PointElement,
    LineElement,
    CategoryScale,
    LinearScale,
    LineController,
    BarController,
  } from 'chart.js';

  ChartJS.register(
    LinearScale,
    CategoryScale,
    BarElement,
    PointElement,
    LineElement,
    Legend,
    Tooltip,
    LineController,
    BarController
  );

  let linedata = {
  labels: chartLabels,
  datasets: [
    {
      type: 'bar',
      label: 'Test Chart 1',
      data: chartData
    }
  ]
  }
</script>

<div id="main-container">
  <h1>{name}'s Porfolio </h1>
  <hr />
  <br />
  <div id="secondary-container">
    <h2>Metrics</h2>
    <div id="chart">
      <Chart data={linedata} options={{responsive: true}} bind:chart/> 
    </div>
    <button on:click={addData}>Add Data</button>
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
            <td><button on:click={sell}>Sell Shares</button><button on:click={buy}>Buy Shares</button></td>
          </tr>
          {/each}
      </tbody>
    </table>
    {/if}
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

  #chart {
    height: auto;
    width: auto;
  }
</style>
