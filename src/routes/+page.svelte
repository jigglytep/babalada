<script lang="ts">
  import type { PageServerData } from "./$types";

	export let data: PageServerData;
</script>

<h1>Babalada</h1>
<p>Aa Home</p>
<p>{data.response.json().toString()}</p>
