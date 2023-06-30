<script lang="ts">
	let doSignUp = false;
</script>

<div class="form-slider">
	<input type="radio" name="slider" id="login" checked>
	<input type="radio" name="slider" id="signup">
	<!-- svelte-ignore a11y-click-events-have-key-events -->
	<label for="login" class="login" on:click={() => doSignUp=false}>Login</label>
	<!-- svelte-ignore a11y-click-events-have-key-events -->
	<label for="signup" class="signup" on:click={() => doSignUp=true}>Signup</label>
	<div class="slider-tab"></div>
</div>

{#if !doSignUp}
	<form method="dialog" class="login">
		<input type="text" name="email" placeholder="Email Address" required>
		<input type="text" name="password" placeholder="Password" required>
		<input type="submit" value="Login">
	</form>
{:else}
	<form method="dialog" class="signup">
		<input type="text" name="email" placeholder="Email Address" required>
		<input type="text" name="password" placeholder="Password" required>
		<input type="text" name="password-confirm" placeholder="Confirm Password" required>
		<input type="submit" value="Signup">
	</form>
{/if}

<style lang="scss">
	.form-slider {
		input[type="radio"]{
			display:none;
		}
		label {
			z-index: 1;
			&.login {
				color: white;
			}
			&.signup {
				color: black;
			}
		}
		// .slider-tab {
		// 	position: absolute;
		// 	background-color: red;
		// }
		#signup:checked {
			& ~ label {
				&.login {
					color: black;
				}
				&.signup {
					color: white;
				}
			}
			// & ~ .slider-tab {
			// 	left: 50%;
			// }
		}
	}
</style>