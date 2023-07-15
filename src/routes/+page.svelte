<script lang="ts">
  import type { PageServerData } from "./$types";
  // export let data: PageData;

  // import { onMount } from "svelte";
  // import { apiData, drinkNames } from "./store.js";

  export let data: PageServerData;
  console.log(data);
</script>

<div id="first-container">
  <h1>"INSERT INFO HERE"</h1>
</div>
<p>TEST</p>

<style>
  #first-container {
    min-height: 88vh;
    display: grid;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }


</style>