<script lang="ts">
    export let number: Number;
    export let name: String;
    export let created: String;
    export let funds: Number;

    function inspect(pname: String) {
        window.location.href = `/p/${pname}`;
    }
</script>

<div>
    <h3>{number}) {name}</h3>
    <small>Created: {created}</small>
    <br />
    <small>Current Funds: ${funds}</small>
    <br />
    <button on:click={() => inspect(name)}>Inspect</button>
</div> 

<style lang="scss">
  div {
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
  }
</style>
