<script lang="ts">
    import userIcon from '../pictures/userIcon.png'
    export let name: String;
    export let username: String;
    export let numOfPorts: Number;
    export let numOfStocks: Number;
    
    function inspect(uname: String) {
        window.location.href = `/u/${uname}`;
    }

</script>

<div id="container">
    <img src={userIcon} alt="">
    <div id="name">{name} / @{username}</div>
    <p>{numOfPorts}</p>
    <p>{numOfStocks}</p>
    <button on:click={() => inspect(name)}>Inspect</button>
</div>

<style lang="scss">
    #container {
        height: 6em;
        border: .15em solid black;
        display: grid;
        grid-template-columns: 5em 30% 20% 20% 20%;
    }

    img {
        width: 5em;
        height: 5em;
        margin: .5em;
    }

    p, #name {
        margin: auto;
    }

    button {
        margin: auto;
        height: fit-content;
        width: fit-content;
        padding: 1em;
    }

</style>