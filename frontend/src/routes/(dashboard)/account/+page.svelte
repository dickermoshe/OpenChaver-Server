<script lang="ts">
	// load the users data
</script>

<p>Control everything important at your fingertips.</p>

<section>
	<div class="category large">
		<div class="header">
			<img alt="" />
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
		font-size: .875rem;
	}
</style>
