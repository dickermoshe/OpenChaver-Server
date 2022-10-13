<script lang="ts">
	import { page } from '$app/stores'
</script>

<svelte:head>
	<title>Error | OpenChaver</title>
</svelte:head>

<section>
	<div class="container">
		{#if $page.status === 404}
			<h1>Page missing</h1>
			This is our fault, we will try to fix this soon.<br />
			Go to the <a href="../">Homepage</a>.
		{:else}
			<h1>{$page.status}</h1>
			<div>{$page.error?.message}</div>
		{/if}
	</div>
</section>
