<script lang='ts'>
	import { api } from '$lib/api'

	export let data: any

	const { token, uid } = data
	let new_password: string, errs: any

	const resetPswd = async () => {
		const res = await api('POST', 'auth/users/reset_password_confirm/', {
			token,
			uid,
			new_password
		})
		errs = {}

		if(res.status === 204) {
			window.location.href = '/login'
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
			<form action="https://api.openchaver.com/auth/users/reset_password_confirm/" method="POST">
				<div class="inputContainer">
					<label for="passsword">New password</label>
					<input bind:value={new_password} type="password" name="passsword" id="passsword" autocomplete="new-password" />
					<div class="error smallBody">{errs?.new_password?.[0] ?? ''}</div>
				</div>
				<div class="buttonContainer">
					<a href="/login" class="button">Login</a>
					<input type="submit" value="Set Password" on:click|preventDefault={resetPswd} />
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
