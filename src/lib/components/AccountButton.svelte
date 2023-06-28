<script lang="ts">
	import Modal from '$components/Modal.svelte';
	let doShowModal = false;
</script>

<button on:click={() => doShowModal=true}>
	Login
</button>

<Modal bind:doShowModal>
	<p>TDOO: login form</p>
</Modal>

<style lang="scss">
	
</style>