<script lang="ts">
	import Modal from '$components/Modal.svelte';
	import LoginForm from '$components/LoginForm.svelte';
  import { accountStore } from '$stores/AccountStore';
  import userIcon from '$pictures/userIcon.png'
	const { account } = accountStore;
	let doShowModal = false;
	accountStore.account.subscribe(newAccount => {
		if (newAccount !== null) {
			console.log(newAccount);
			doShowModal = false;
		}
	});
</script>

{#if $account === null}
	<button on:click={() => doShowModal=true}>
		Login
	</button>
{:else}
	<a href='/u/{$account.id}'><img src={userIcon} alt="Profile Picture"></a>
{/if}
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
	a {
		img	{
			display: block;
			height: calc(1rem + 24px);
		}
		&:hover {
			background-color: lightgray;
		}
		&:active {
			background-color: gray;
		}
	}
</style>