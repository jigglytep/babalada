<script lang="ts">
	let doSignUp = false;

	let loginFormHTML: HTMLFormElement;
	let signupFormHTML: HTMLFormElement;
	let loginEmail: string = '';
	let loginPassword: string = '';
	let signupEmail: string = '';
	let signupPassword: string = '';
	let signupPasswordConfirm: string = '';

	const submitLogin = async (e: SubmitEvent) => {
		e.preventDefault();
		const response = await fetch(
			loginFormHTML.action,
			{
				method: loginFormHTML.method,
				body: new FormData(loginFormHTML),
				redirect: 'follow',
			}
		);
		const responseJSON = await response.json();
		console.log(JSON.stringify(responseJSON));
		// TODO: implement update of AccountStore from response
	}
	const submitSignup = async (e: SubmitEvent) => {}
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
		<form method="POST" action="/api/login" class="login" autocomplete="on" on:submit={submitLogin} bind:this={loginFormHTML}>
			<input type="text" name="email" placeholder="Email Address" required bind:value={loginEmail}/>
			<input type="password" name="password" placeholder="Password" required bind:value={loginPassword}/>
			<a href="#">Forgot password?</a>
			<input type="submit" value="Login"/>
		</form>
	{:else}
		<form method="POST" action="/api/signup" class="signup" autocomplete="off" on:submit={submitSignup} bind:this={signupFormHTML}>
			<input type="text" name="email" placeholder="Email Address" required bind:value={signupEmail}/>
			<input type="password" name="password" placeholder="Password" required bind:value={signupPassword}/>
			<input type="password" name="password-confirm" placeholder="Confirm Password" required bind:value={signupPasswordConfirm}/>
			<input type="submit" value="Signup"/>
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