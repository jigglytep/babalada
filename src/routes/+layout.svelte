<script lang="ts">
	let currentYear: number = new Date().getFullYear();
</script>

<style lang="scss"></style>

<header id="page-header">
	<nav>
		<ul>
			<li><a href="/">Home</a></li>
			<li><a href="/f">Forum</a></li>
			<li><a href="/p">Profiles</a></li>
			<li><a href="/u">Users</a></li>
		</ul>
	</nav>
</header>

<div id="page-container">
	<slot />
</div>

<footer id="page-footer">
	<p>Copyright © {currentYear} Babalada | All rights reserved.</p>
</footer>