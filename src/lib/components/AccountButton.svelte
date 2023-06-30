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

<style lang="scss"></style>