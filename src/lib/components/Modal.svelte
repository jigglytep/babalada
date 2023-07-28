<script lang="ts">
	import 'iconify-icon';
	export let doShowModal: boolean;
	let dialogHTML: HTMLDialogElement;
	$: {
		if (dialogHTML) {
			if (doShowModal) dialogHTML.showModal();
			else dialogHTML.close();
		}
	}
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<dialog
	bind:this={dialogHTML}
	on:close={() => doShowModal=false}
	on:click|self={() => dialogHTML.close()}
>
	<div class="modal-container" on:click|stopPropagation>
		<!-- svelte-ignore a11y-autofocus -->
		<button autofocus on:click={() => dialogHTML.close()}>
			<iconify-icon icon="ph:x-circle-thin"/>
		</button>
		<slot />
	</div>
</dialog>

<style lang="scss">
	dialog {
		margin: auto;
		margin-top: 6rem;
		border-radius: 0.4em;
		border: none;
		button {
			float: right;
			display: flex;
			margin: 0.2rem;
			border: none;
			font-size: 2rem;
			background-color: inherit;
		}
	}
	dialog::backdrop {
		background: rgba(0, 0, 0, 0.4);
	}
	dialog[open] {
		animation: zoom 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
	}
	@keyframes zoom {
		from {
			transform: scale(0.95);
		}
		to {
			transform: scale(1);
		}
	}
	dialog[open]::backdrop {
		animation: fade 0.2s ease-out;
	}
	@keyframes fade {
		from {
			opacity: 0;
		}
		to {
			opacity: 1;
		}
	}
</style>