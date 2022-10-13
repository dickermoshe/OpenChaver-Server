<script lang="ts">
	import { api } from '$lib/api'

	let email: string, password: string, errs: any

	const login = async () => {
		const res = await api('POST', 'auth/token/login/', {
			email,
			password
		})
		errs = {}

		if(res.status === 200) {
			alert('user logged in [need to save user_token]')
		} else if(res.status === 400) {
			errs = await res.json()
			console.log(errs)
		}
	}
</script>

<svelte:head>
	<title>Login | OpenChaver</title>
	<meta
		name="description"
		content="Login to your account to configure your content filtering setup."
	/>
</svelte:head>

<section>
	<div class="container">
		<div class="signupContainer form">
			<h3>Login to OpenChaver</h3>
			<form action="https://api.openchaver.com/auth/token/login/" method="POST">
				<div class="inputContainer">
					<label for="email">Email</label>
					<input bind:value={email} type="email" name="email" id="email" />
				</div>
				<div class="inputContainer">
					<label for="password">Password</label>
					<input bind:value={password} type="password" name="password" id="password" />
				</div>
				<p class="smallBody">Forgot your password and cannot login?<br /><a href="reset-password">Reset password</a></p>
				<p class="error">{errs?.non_field_errors?.[0] ?? ''}</p>
				<div class="buttonContainer">
					<a href="/signup" class="button">Signup</a>
					<input type="submit" value="Login" on:click|preventDefault={login} />
				</div>
			</form>
		</div>
	</div>
</section>

<style>
	section > .container {
		display: grid;
		justify-content: center;
		padding-top: var(--general-spacing);
	}
	.form {
		width: 350px;
		padding: var(--general-spacing);
		border: 2px solid var(--secondary-bg-color);
		border-radius: 8px;
	}
	.form h3 {
		text-align: center;
	}
	.inputContainer {
		margin-top: 1rem;
	}
	.inputContainer label {
		display: block;
		width: 100%;
	}
	.inputContainer input {
		display: block;
		margin-top: calc(var(--general-spacing) / 3);
	}
	.error {
		margin-top: calc(var(--general-spacing) / 3);
		color: var(--red);
	}
	.smallBody {
		font-size: .875rem;
	}
	.buttonContainer {
		display: flex;
		justify-content: space-between;
		margin-top: var(--general-spacing);
	}
	button, input[type=submit] {
		padding: .5rem 1rem;
		border: none;
		background: var(--secondary-bg-color);
		font-size: .875rem;
		letter-spacing: .05rem;
		cursor: pointer;
	}
</style>
