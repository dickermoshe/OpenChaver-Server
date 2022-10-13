<script lang="ts">
	import { api } from '$lib/api'

	let devices = [
		{
			id: 0,
			name: 'DESKTOP-QDI5S9G',
			model: 'Surface book',
			form_factor: 'laptop',
			os: 'Windows 10 Pro 21H2',
			last_location: 'West Jerusalem, Israel',
			last_timestamp: 1234567890,
			chaver: {
				name: 'John Doe',
				email: 'johndoe@example.com'
			}
		},
		{
			id: 0,
			name: 'DESKTOP-8SJ4SQJ',
			model: 'OptiPlex 3070',
			form_factor: 'desktop',
			os: 'Windows 11 2203',
			last_location: 'Borough Park, NY',
			last_timestamp: 1234567890,
			chaver: {
				name: 'John Doe',
				email: 'johndoe@example.com'
			}
		}
	]

	const loadDevices = () => {
		api('GET', 'devices/')
			.then((res) => res.json())
			.then((json) => (devices = json))
	}
</script>

<p>View the devices linked to your account and/or register new ones.</p>

<section>
	{#each devices as device}
		<div class="category row">
			<img src="{device.form_factor}.png" alt="" />
			<div class="stats">
				<div class="largeText">{device.name}</div>
				<div class="subText">{device.model}</div>
				<div class="subText">{device.os}</div>
				<div class="subText">Chaver: {device.chaver.name}</div>
				<a href="">Edit details</a>
			</div>
		</div>
	{/each}
</section>

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
	.category img {
		padding: 1rem calc(var(--general-spacing) * 1.5);
		box-sizing: border-box;
		max-height: 160px;
		max-width: 200px;
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
		padding-bottom: calc(var(--general-spacing) / 3);
		font-size: 0.875rem;
		color: var(--secondary-txt-color);
	}
	.category a {
		display: inline-block;
		margin-top: 0.5rem;
	}
</style>
