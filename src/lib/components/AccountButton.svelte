<script lang="ts">
	import Modal from '$components/Modal.svelte';
	import LoginForm from '$components/LoginForm.svelte';
	let doShowModal = false;
</script>

<!--TODO: if signed in, show account button instead-->
<button on:click={() => doShowModal=true}>
	Login
</button>

<Modal bind:doShowModal>
	<LoginForm />
</Modal>

<style lang="scss">
	button {
		display: block;
		padding: 6px 10px;
		border: 2px solid black;
		border-radius: 8px;
		font-size: 1rem;
		color: black;
		background-color: inherit;
		&:hover {
			background-color: lightgray;
		}
		&:active {
			background-color: gray;
		}
	}
</style>