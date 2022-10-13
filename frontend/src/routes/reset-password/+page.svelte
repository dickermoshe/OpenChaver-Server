<script lang="ts">
	import { api } from '$lib/api'

	let email: string, errs: any

	const requestPswd = async () => {
		const res = await api('POST', 'auth/users/reset_password/', {
			email
		})
		errs = {}

		if(res.status === 204) {
			alert('Email sent to reset your password.')
		} else if(res.status === 400) {
			errs = await res.json()
			console.log(errs)
		}
	}
</script>

<svelte:head>
	<title>Reset password | OpenChaver</title>
	<meta
		name="description"
		content="Reset your password to access your account."
	/>
</svelte:head>

<section>
	<div class="container">
		<div class="signupContainer form">
			<h3>Reset password</h3>
			<form action="https://api.openchaver.com/auth/users/reset_password/" method="POST">
				<div class="inputContainer">
					<label for="email">Email</label>
					<input bind:value={email} type="email" name="email" id="email" autocomplete="email" />
					<div class="error smallBody">{errs?.email?.[0] ?? ''}</div>
				</div>
				<div class="buttonContainer">
					<a href="/login" class="button">Login</a>
					<input type="submit" value="Signup" on:click|preventDefault={requestPswd} />
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
