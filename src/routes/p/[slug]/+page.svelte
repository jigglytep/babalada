<script lang="ts">
  import type { PageData } from "./$types";
  export let data: PageData;

  import { onMount } from "svelte";
  import { apiData, drinkNames } from "./store.js";

  onMount(async () => {
    fetch("localhost:5000/api/")
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        apiData.set(data);
      })
      .catch((error) => {
        console.log(error);
        return [];
      });
  });
</script>

<h1>Porfolio [{data.home}]</h1>
<p>Aa about [{data.status}].</p>
