<script lang="ts">
	import { api } from '$lib/api'

	let devices: any = [],
		newDeviceName: string,
		newDevice: any

	const loadDevices = () => {
		api('GET', 'devices/')
			.then((res) => {
				console.assert(!(res.status === 401), 'Logout and re-login in to continue.')
				return res.json()
			})
			.then((json) => (devices = json))
	}
	const createDevice = () => {
		api('POST', 'devices/', {
			name: newDeviceName
		})
			.then((res) => {
				if (res.status === 201) return res.json()
			})
			.then((json) => {
				newDeviceName = ''
				newDevice = json
				devices = [...devices, newDevice]
			})
	}
	$: loadDevices()
</script>

<svelte:head>
	<title>Devices | OpenChaver</title>
	<meta name="description" content="View the devices on your account." />
</svelte:head>

<p>View the devices linked to your account and/or register new ones.</p>

<section>
	{#each devices as device}
		<div class="category row">
			<img src="desktop.png" alt={device.form_factor} />
			<div class="stats">
				<div class="largeText">{device.name}</div>
				<div class="subText">Id: {device.id}</div>
				{#if device.registered}
					<div class="subText">Chaver: {device.chaver?.name ?? 'Not set'}</div>
				{:else}
					<a href="/link-device/{device.id}" class="subText err">Device is not linked</a>
				{/if}
				<a href="/devices/{device.id}">Edit details</a>
			</div>
		</div>
		<!-- {:else}
		<div class="category">You don't have any devices on your account</div> -->
	{/each}
	<div class="category row" style="justify-content: center;">
		<a href="/devices" on:click={() => false}>Register device</a>
	</div>
</section>

<form
	action="https://api.openchaver.com/devices/"
	method="POST"
	on:submit|preventDefault={createDevice}
>
	<h2>Add device</h2>
	<label for="new_name">Name device</label>
	<input type="text" id="new_name" bind:value={newDeviceName} />
	<br />
	<input type="submit" value="Create device" />
</form>

{#if newDevice}
	<br />
	The new device id is: {newDevice.id}
{/if}

<style>
	section {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: var(--general-spacing);
		padding-top: var(--general-spacing);
	}
	.row {
		display: flex;
		flex-flow: row nowrap;
		align-items: center;
	}
	.category {
		padding: calc(var(--general-spacing) / 2);
		border: 1px solid var(--default-border-color);
		border-radius: 8px;
		overflow: hidden;
	}
	/* .category.large {
		grid-column: 1/3;
	} */
	.category img {
		max-height: 160px;
		max-width: 160px;
		margin: 0.75rem calc(var(--general-spacing) * 1.5);
		box-sizing: border-box;
	}
	.category .stats {
		max-width: 60%;
		padding-left: var(--general-spacing);
	}
	.category .largeText {
		margin-bottom: 1rem;
		color: var(--default-txt-color);
		font-size: 1.125rem;
		font-weight: 700;
	}
	.category .subText {
		display: block;
		padding-bottom: calc(var(--general-spacing) / 3);
		font-size: 0.875rem;
		color: var(--secondary-txt-color);
		text-decoration: none;
	}
	.category a {
		display: inline-block;
		margin-top: 0.5rem;
	}
	.category .err {
		color: var(--yellow);
		font-weight: 700;
	}
</style>
