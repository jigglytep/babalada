<script lang="ts">
  import type { PageServerData } from "./$types";
  // export let data: PageData;

  // import { onMount } from "svelte";
  // import { apiData, drinkNames } from "./store.js";

  export let data: PageServerData;
  console.log(data);
</script>

<div id="main-container">
  <h1>Welcome to Babalada!</h1>
  <div id="secondary-container">
  </div>
</div>

<style>
  #main-container {
    width: 90%;
    margin: auto;
    padding-top: 1em;
  }

  #secondary-container {
    width: 95%;
    margin: auto;
  }

</style>