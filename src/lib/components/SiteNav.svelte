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
		margin: 0 2rem 0 2rem;
		.icon-home {
			font-size: 2rem;
			text-decoration: none;
			color: black;
			&:hover {
				background-color: lightgray;
			}
			&:active {
				background-color: gray;
			}
		}
		ul {
			padding: 0;
			display: flex;
			justify-content: space-between;
			gap: 0.4rem;
			align-items: center;
			list-style-type: none;
			li a {
				display: block;
				padding: 6px 10px;
				border: 2px solid black;
				border-radius: 8px;
				color: black;
				background-color: inherit;
				text-decoration: none;
				&:hover {
					background-color: lightgray;
				}
				&:active {
					background-color: gray;
				}
			}
		}
	}
</style>