<script lang="ts">
	import AccountButton from "$components/AccountButton.svelte";
</script>

<nav>
	<a class="icon-home" href="/">Babalada</a>
	<ul>
		<li><a href="/f">Forum</a></li>
		<li><a href="/p">Profiles</a></li>
		<li><a href="/u">Users</a></li>
		<li><AccountButton /></li>
	</ul>
</nav>

<style lang="scss">
	nav {
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin: 6px 0 6px 0;
	}
	.icon-home {
		text-decoration: none;
	}
	ul {
		display: flex;
		align-items: center;
		list-style-type: none;
		li a {
			display: block;
			padding: 6px 10px;
			border: 2px solid black;
			border-radius: 8px;
			text-decoration: none;
			&:visited {
				text-decoration: none;
			}
			&:hover {
				background-color: lightgray;
			}
			&:active {
				background-color: gray;
			}
		}
	}
</style>