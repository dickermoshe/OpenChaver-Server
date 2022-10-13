<script lang="ts">
	import { api } from '$lib/api'

	let email: string, password: string

	const login = async () => {
		const attempt = await api('POST', 'auth/token/login/', {
			email,
			password
		})
		const res = attempt.json()

		// save credentials
		// save credentials
		// save credentials
	}
</script>

<section>
	<div class="container">
		Login to your OpenChaver account
		<form action="https://api.openchaver.com/auth/token/login/" method="post">
			<label for="email">Email</label>
			<input bind:value={email} type="email" name="email" id="email" /><br />
			<label for="password">Password</label>
			<input bind:value={password} type="password" name="password" id="password" />
			<input type="submit" value="Login" on:submit|preventDefault={login} />
		</form>
	</div>
</section>
