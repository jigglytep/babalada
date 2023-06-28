<script lang="ts">
	import SiteNav from '$components/SiteNav.svelte';

	let currentYear: number = new Date().getFullYear();

	import './+layout.scss'
</script>

<header id="page-header">
	<SiteNav />
</header>

<div id="page-container">
	<slot />
</div>

<footer id="page-footer">
	<p>Copyright © {currentYear} Babalada</p>
</footer>

<style lang="scss">
	#page-header {
		flex-shrink: 0;
		box-shadow: 0px -2px 6px black;
	}
	#page-container {
		flex: 1 0 auto;
	}
	#page-footer {
		flex-shrink: 0;
		box-shadow: 0px 2px 6px black;
		p {
			margin: 6px 0 6px 0;
			text-align: center;
		}
	}
	</style>