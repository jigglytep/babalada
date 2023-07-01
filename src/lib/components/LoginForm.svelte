<script lang="ts">
	let doSignUp = false;
</script>

<div class="login-form-container">
	<div class="form-slider">
		<input type="radio" name="slider" id="login-radio" on:click={() => doSignUp=false} checked>
		<!-- svelte-ignore a11y-click-events-have-key-events -->
		<label for="login-radio" class="login" on:click={() => doSignUp=false}>Login</label>
		<input type="radio" name="slider" id="signup-radio" on:click={() => doSignUp=true}>
		<!-- svelte-ignore a11y-click-events-have-key-events -->
		<label for="signup-radio" class="signup" on:click={() => doSignUp=true}>Signup</label>
		<div class="slider-tab"></div>
	</div>
	
	{#if !doSignUp}
		<form method="dialog" class="login" autocomplete="on">
			<input type="text" name="email" placeholder="Email Address" required>
			<input type="password" name="password" placeholder="Password" required>
			<a href="#">Forgot password?</a>
			<input type="submit" value="Login">
		</form>
	{:else}
		<form method="dialog" class="signup" autocomplete="off">
			<input type="text" name="email" placeholder="Email Address" required>
			<input type="password" name="password" placeholder="Password" required>
			<input type="password" name="password-confirm" placeholder="Confirm Password" required>
			<input type="submit" value="Signup">
		</form>
	{/if}
</div>

<style lang="scss">
	.login-form-container {
		padding: 0.4rem;
	}
	.form-slider {
		position: relative;
		display: flex;
		justify-content: space-between;
		clear: both;
		border: solid 1px;
		input[type="radio"]{
			display:none;
		}
		label {
			z-index: 1;
			width: 50%;
			padding: 0.3rem;
			text-align: center;
			font-size: 1.4rem;
			font-weight: 600;
			&.login {
				color: white;
			}
			&.signup {
				color: black;
			}
		}
		.slider-tab {
			position: absolute;
			z-index: 0;
			width: 50%;
			height: 100%;
			left: 0;
			background-color: lightgrey;
		}
		#login-radio:not(:checked) {
			& ~ label {
				&.login {
					color: black;
				}
				&.signup {
					color: white;
				}
			}
			& ~ .slider-tab {
				left: 50%;
			}
		}
	}
	form {
		max-width: 20rem;
		width: 60vw;
		input {
			width: 100%;
			height: 2rem;
			margin-top: 0.6rem;
			outline: none;
			border-top: 0;
			border-right: 0;
			border-left: 0;
		}
		a {
			font-size: 0.8rem;
		}
		input[type="submit"] {
			height: 1.6rem;
			border: none;
		}
	}
</style>