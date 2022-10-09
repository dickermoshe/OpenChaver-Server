<svelte:head>
	<title>Dashboard | OpenChaver</title>
	<meta name="description" content="Control and modify your OpenChaver account." />
</svelte:head>

<section>
	<div class="category" style="grid-column: 1/3;">
		<div class="header">
			<!-- <img src="https://compass-ssl.microsoft.com/assets/f4/dc/f4dcc07f-010b-4bbb-9ef2-f51f02fe0b7e.svg?n=Devices_Icon_2.svg" alt=""> -->
			<img src="data:image/svg+xml,%0A%3Csvg xmlns='http://www.w3.org/2000/svg' height='24' viewBox='0 0 24 24' width='24'%3E%3Cpath d='M0 0h24v24H0V0z' fill='none'/%3E%3Cpath d='M21 2H3c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h7v2H8v2h8v-2h-2v-2h7c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm0 14H3V4h18v12z'/%3E%3C/svg%3E" alt="">
			<div class="title">Devices</div>
		</div>
		<div class="body">
			No devices associated to your account.
			<a href="/dashboard">Add a device</a>
		</div>
	</div>

	<div class="category">
		<div class="header">
			<img src="data:image/svg+xml,%0A%3Csvg xmlns='http://www.w3.org/2000/svg' height='24' viewBox='0 0 24 24' width='24'%3E%3Cpath d='M0 0h24v24H0V0z' fill='none'/%3E%3Cpath d='M15.73 3H8.27L3 8.27v7.46L8.27 21h7.46L21 15.73V8.27L15.73 3zM19 14.9L14.9 19H9.1L5 14.9V9.1L9.1 5h5.8L19 9.1v5.8z'/%3E%3Ccircle cx='12' cy='16' r='1'/%3E%3Cpath d='M11 7h2v7h-2z'/%3E%3C/svg%3E" alt="">
			<div class="title">Activity</div>
		</div>
		<div class="body">
			No questionable activity detected.
		</div>
	</div>
</section>

<!-- 
- Devices (active/total) [quick link to add a new device]<br />
- Did the system trip<br />
-->

<style>
	section {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: var(--general-spacing);
	}

	.category {
		border: 2px solid var(--default-border-color);
		border-radius: 8px;
		overflow: hidden;
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
		padding-inline-start: calc(var(--general-spacing) / 3);
		font-size: .875rem;
		font-weight: 700;
	}
	.body {
		padding: calc(var(--general-spacing) / 2) calc(var(--general-spacing) / 2);
	}
	.body a {
		padding: calc(var(--general-spacing) / 1.5) 0;
		display: block;
		width: 100%;
		text-align: center;
	}
</style>