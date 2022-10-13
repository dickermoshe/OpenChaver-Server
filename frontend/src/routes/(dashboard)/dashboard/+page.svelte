<script lang="ts">
	// import Devices from "./Devices.svelte"

	const widgetData = [
		{
			title: 'Devices',
			img: "data:image/svg+xml,%0A%3Csvg xmlns='http://www.w3.org/2000/svg' height='24' viewBox='0 0 24 24' width='24'%3E%3Cpath d='M0 0h24v24H0V0z' fill='none'/%3E%3Cpath d='M21 2H3c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h7v2H8v2h8v-2h-2v-2h7c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm0 14H3V4h18v12z'/%3E%3C/svg%3E",
			prompt: 'View devices',
			size: 'large',
			href: 'devices'
		},
		{
			title: 'Accountabilty',
			img: "data:image/svg+xml,%0A%3Csvg xmlns='http://www.w3.org/2000/svg' height='24' viewBox='0 0 24 24' width='24'%3E%3Cpath d='M0 0h24v24H0V0z' fill='none'/%3E%3Cpath d='M15.73 3H8.27L3 8.27v7.46L8.27 21h7.46L21 15.73V8.27L15.73 3zM19 14.9L14.9 19H9.1L5 14.9V9.1L9.1 5h5.8L19 9.1v5.8z'/%3E%3Ccircle cx='12' cy='16' r='1'/%3E%3Cpath d='M11 7h2v7h-2z'/%3E%3C/svg%3E",
			prompt: 'Review incidents',
			href: 'accountabilty'
		},
		{
			title: 'Subscription',
			img: "data:image/svg+xml,%0A%3Csvg xmlns='http://www.w3.org/2000/svg' enable-background='new 0 0 24 24' height='24' viewBox='0 0 24 24' width='24'%3E%3Cg%3E%3Crect fill='none' height='24' width='24'/%3E%3Cpath d='M19,14V6c0-1.1-0.9-2-2-2H3C1.9,4,1,4.9,1,6v8c0,1.1,0.9,2,2,2h14C18.1,16,19,15.1,19,14z M17,14H3V6h14V14z M10,7 c-1.66,0-3,1.34-3,3s1.34,3,3,3s3-1.34,3-3S11.66,7,10,7z M23,7v11c0,1.1-0.9,2-2,2H4c0-1,0-0.9,0-2h17V7C22.1,7,22,7,23,7z'/%3E%3C/g%3E%3C/svg%3E",
			prompt: 'Manage subscription',
			href: 'subscription'
		}
	]
</script>

<svelte:head>
	<title>Dashboard | OpenChaver</title>
	<meta name="description" content="Control and modify your OpenChaver account." />
</svelte:head>

<section>
	{#each widgetData as data}
		<div class="category" class:large={data.size === 'large'}>
			<div class="header">
				<!-- <img src="https://compass-ssl.microsoft.com/assets/f4/dc/f4dcc07f-010b-4bbb-9ef2-f51f02fe0b7e.svg?n=Devices_Icon_2.svg" alt=""> -->
				<img src={data.img} alt="" />
				<div class="title">{data.title}</div>
			</div>
			<div class="body">
				<a href={data.href} data-sveltekit-prefetch>{data.prompt}</a>
				<!-- {#if data.title === 'Devices'}
					<Devices />
				{:else}
					<a href={data.href} data-sveltekit-prefetch>{data.prompt}</a>
				{/if} -->
			</div>
		</div>
	{/each}
</section>

<style>
	section {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: var(--general-spacing);
	}

	.category {
		border: 1px solid var(--default-border-color);
		border-radius: 8px;
		overflow: hidden;
	}
	.category.large {
		grid-column: 1/3;
	}
	.header {
		display: flex;
		flex-direction: row;
		align-items: center;
		padding: calc(var(--general-spacing) / 3) calc(var(--general-spacing) / 2);
		border-bottom: 1px solid var(--default-border-color);
		background: var(--secondary-bg-color);
	}
	.header img {
		display: block;
		height: 1.375rem;
	}
	.header .title {
		padding-inline-start: calc(var(--general-spacing) / 2);
		font-size: 0.875rem;
		font-weight: 700;
	}
	.body {
		padding: calc(var(--general-spacing) / 2) calc(var(--general-spacing) / 2);
		background-color: var(--default-bg-color);
	}
	.body a {
		padding: calc(var(--general-spacing) / 1.5) 0;
		display: block;
		width: 100%;
		text-align: center;
	}
</style>
