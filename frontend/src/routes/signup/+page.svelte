<script lang="ts">
	import { api } from '$lib/api'

	let email: string, password: string, errs: any

	const register = async () => {
		const res = await api('POST', 'auth/users/', {
			email,
			password
		})
		errs = {}

		if (res.status === 201) {
			alert('confirm email')
		} else if (res.status === 400) {
			errs = await res.json()
			console.log(errs)
		}
	}
</script>

<svelte:head>
	<title>Signup | OpenChaver</title>
	<meta name="description" content="Setup an account to access our content filtering services." />
</svelte:head>

<section>
	<div class="container">
		<div class="signupContainer form">
			<h3>Signup for OpenChaver</h3>
			<form action="https://api.openchaver.com/auth/users/" method="POST">
				<div class="inputContainer">
					<label for="email">Email</label>
					<input bind:value={email} type="email" name="email" id="email" autocomplete="email" />
					<div class="error smallBody">{errs?.email?.[0] ?? ''}</div>
				</div>
				<div class="inputContainer">
					<label for="password">Password</label>
					<input
						bind:value={password}
						type="password"
						name="password"
						id="password"
						autocomplete="new-password"
					/>
					<div class="error smallBody">{errs?.password?.[0] ?? ''}&nbsp;</div>
				</div>
				<!-- <p class="smallBody">Forgot your password and cannot login?<br /><a href="reset-password">Reset password</a></p> -->
				<div class="buttonContainer">
					<a href="/login" class="button" data-sveltekit-prefetch>Login</a>
					<input type="submit" value="Signup" on:click|preventDefault={register} />
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
	.inputContainer .error {
		margin-top: calc(var(--general-spacing) / 3);
		color: var(--red);
	}
	.smallBody {
		font-size: 0.875rem;
	}
	.buttonContainer {
		display: flex;
		justify-content: space-between;
		margin-top: var(--general-spacing);
	}
	button,
	input[type='submit'] {
		padding: 0.5rem 1rem;
		border: none;
		background: var(--secondary-bg-color);
		font-size: 0.875rem;
		letter-spacing: 0.05rem;
		cursor: pointer;
	}
</style>
