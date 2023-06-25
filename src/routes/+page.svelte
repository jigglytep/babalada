<script lang="ts">
  import type { PageServerData } from "./$types";
  // export let data: PageData;

  // import { onMount } from "svelte";
  // import { apiData, drinkNames } from "./store.js";

  export let data: PageServerData;
  console.log(data);
</script>

<h1>Babalada</h1>
<p>Aa Home</p>
<p>data.s.home: {data.s.home}</p>
<p>data.s.status: {data.s.status}</p>
