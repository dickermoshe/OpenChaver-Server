<script lang='ts'>
	import { api } from "$lib/api"

	let screenshots: any = [],
	devices: any = []

	const loadScreenshots = async () => {
		const res = await api('GET', 'devices/')
		if(res.status === 200)
			devices = [...devices, ...await res.json()]


		const tempres = await api('GET', 'screenshots/')
		if(res.status === 200)
			screenshots = [...screenshots, ...await tempres.json()]
	}

	$: loadScreenshots()
</script>

<p>
	Review captured screenshots and mark false positives
</p>

{#each devices as device}
	<section>
		{#each device.screenshots as event}
			<div class="card row">
				<img src={event.image} alt="Screenshot from device">
				<div class="info">
					<div class="largeText">{device.name}</div>
					<div class="subtext">{event.created}</div>
					<div class="subtext">{event.nsfw? 'Inappropriate content': 'Random screen review'}</div>
					{#if event.false_positive}
						<a href="">Mark as false positive</a>
					{/if}
				</div>
			</div>
		{:else}
			<div class="card">
				{device.name} doesn't have screenshots captures.
			</div>
		{/each}
	</section>
{:else}
	<section>
		<div class="card">
			You must first <a href="/devices">add devices</a> to your account.
		</div>
	</section>
{/each}
	
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
	.card {
		padding: calc(var(--general-spacing) / 2);
		border: 1px solid var(--default-border-color);
		border-radius: 8px;
		overflow: hidden;
	}
	/* .card.large {
		grid-column: 1/3;
	} */
	.card img {
		max-height: 160px;
		max-width: 160px;
		margin: .75rem calc(var(--general-spacing) * 1.5);
		box-sizing: border-box;
	}
	.card .info {
		max-width: 60%;
		padding-left: var(--general-spacing);
	}
	.card .largeText {
		margin-bottom: 1rem;
		color: var(--default-txt-color);
		font-size: 1.125rem;
		font-weight: 700;
	}
	.card .subtext {
		padding-bottom: calc(var(--general-spacing) / 3);
		font-size: 0.875rem;
		color: var(--secondary-txt-color);
	}
	.card a {
		display: inline-block;
		margin-top: 0.5rem;
	}
</style>
