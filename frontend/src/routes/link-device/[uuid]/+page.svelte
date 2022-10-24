<script lang="ts">
	import { page } from '$app/stores'
	export const prerender = false

	let status = false

	const linkDevice = async () => {
		const attmept = await fetch('http://localhost:61195/configure', {
			method: 'POST',
			headers: new Headers({ 'content-type': 'application/json' }),
			body: JSON.stringify({
				device_id: $page.params.uuid
			})
		})

		const res = await attmept.clone().json()
		if (res.error === 'Device already registered' || res.success === true) status = true
		else setTimeout(() => linkDevice(), 10000)

		console.log(
			res.error === 'Device already registered',
			res.success === true,
			res.error === 'Device already registered' || res.success === true
		)
	}

	linkDevice()
</script>

<section>
	<p>
		{status}<br />
		{#if !status}
			We are attempting to link your device to your account.
		{:else}
			Your device was successfully linked to your account.
		{/if}
	</p>
</section>
