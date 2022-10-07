<script lang="ts">
	import { page } from '$app/stores'
	import '../app.css'
	import Header from '../lib/Header.svelte'

	const routes = ['dashboard', 'filtering', 'accountabilty', 'account', 'subscription', 'uninstall']
</script>

<Header />

<aside>
	<nav>
		<ul>
			{#each routes as route}
				<li class:active={route === $page.url.toString().split('/').pop() ?? $page.routeId}>
					<a href={route} data-sveltekit-prefetch>{route}</a>
				</li>
			{/each}
		</ul>
	</nav>
</aside>

<main>
	{#if $page.routeId}
		<h1>{$page.routeId}</h1>
	{/if}

	<slot />
</main>

<style>
	aside a {
		text-transform: capitalize;
	}
	nav ul {
		list-style: none;
		margin: 0;
		padding: 0;
	}
	nav li {
		margin-right: var(--general-spacing);
		margin-bottom: 2px;
		border-radius: 0px 50px 50px 0px;
		transition: background-color ease-in-out 75ms;
	}
	nav li:hover {
		background-color: #059669;
	}
	nav li.active {
		background-color: #10b981;
	}
	nav li a {
		display: block;
		padding: calc(var(--general-spacing) / 3) 0 calc(var(--general-spacing) / 3)
		var(--general-spacing);
		color: var(--default-color);
		text-decoration: none;
	}
	nav li:hover a, nav li.active a {
		color: #fff;
	}
	:global(main > h1) {
		margin-top: 0;
	}
	main h1::first-letter {
		text-transform: capitalize;
	}
</style>
