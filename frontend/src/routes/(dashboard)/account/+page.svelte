<script lang="ts">
	// load the users data
</script>

<p>Control everything important at your fingertips.</p>

<section>
	<div class="category large">
		<div class="header">
			<img
				src="data:image/svg+xml,%0A%3Csvg xmlns='http://www.w3.org/2000/svg' height='24' viewBox='0 0 24 24' width='24'%3E%3Cpath d='M0 0h24v24H0V0z' fill='none'/%3E%3Cpath d='M19 3h-4.18C14.4 1.84 13.3 1 12 1s-2.4.84-2.82 2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7-.25c.22 0 .41.1.55.25.12.13.2.31.2.5 0 .41-.34.75-.75.75s-.75-.34-.75-.75c0-.19.08-.37.2-.5.14-.15.33-.25.55-.25zM19 19H5V5h14v14zM12 6c-1.65 0-3 1.35-3 3s1.35 3 3 3 3-1.35 3-3-1.35-3-3-3zm0 4c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1zm-6 6.47V18h12v-1.53c0-2.5-3.97-3.58-6-3.58s-6 1.07-6 3.58zM8.31 16c.69-.56 2.38-1.12 3.69-1.12s3.01.56 3.69 1.12H8.31z'/%3E%3C/svg%3E"
				alt="ID card"
			/>
			<div class="title">Contact info</div>
			<a href="/help#topic" class="right">Learn more</a>
		</div>
		<div class="body">fields to update</div>
	</div>
	<div class="category large">
		<div class="header">
			<img alt="" />
			<div class="title">{'{Individual setting}'}</div>
			<!-- button to learn more -->
		</div>
		<div class="body">fields to update</div>
	</div>
</section>

<style>
	section {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: var(--general-spacing);
		padding-top: var(--general-spacing);
	}
	.category {
		border: 1px solid var(--default-border-color);
		border-radius: 8px;
		overflow: hidden;
	}
	.category.large {
		grid-column: 1/3;
	}
	.category .header {
		position: relative;
		display: flex;
		flex-direction: row;
		align-items: center;
		padding: calc(var(--general-spacing) / 3) calc(var(--general-spacing) / 2);
		border-bottom: 1px solid var(--default-border-color);
		background: var(--secondary-bg-color);
	}
	.category .header img {
		display: block;
		height: 1.375rem;

		width: 1.375rem;
		background-color: var(--secondary-bg-color);
		border-radius: 8px;
	}
	.category .header .title {
		padding-inline-start: calc(var(--general-spacing) / 2);
		font-size: 0.875rem;
		font-weight: 700;
	}
	.category .body {
		padding: calc(var(--general-spacing) / 2) calc(var(--general-spacing) / 2);
		background-color: var(--default-bg-color);
	}
	.category .body a {
		padding: calc(var(--general-spacing) / 1.5) 0;
		display: block;
		width: 100%;
		text-align: center;
	}
	.category .header a.right {
		position: absolute;
		right: calc(var(--general-spacing) / 3);
		font-size: 0.875rem;
	}
</style>
