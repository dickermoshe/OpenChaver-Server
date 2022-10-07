<script lang="ts">
	import { page } from '$app/stores'
	import '../app.css'
	import Header from '../lib/Header.svelte'

	const routes = ['dashboard', 'accountabilty', 'account', 'subscription', 'uninstall']
</script>

<Header />

<aside>
	<nav>
		<ul>
			{#each routes as route}
				<li>
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
		padding: 0;
	}
	nav li {
		margin-right: var(--general-spacing);
		margin-bottom: 2px;
		border-radius: 0px 50px 50px 0px;
		transition: background-color ease-in-out 75ms;
	}
	nav li:hover {
		background-color: rgba(0, 84, 59, 0.12);
	}
	nav li a {
		display: block;
		padding: calc(var(--general-spacing) / 5) 0 calc(var(--general-spacing) / 5)
			var(--general-spacing);
		color: var(--default-color);
		text-decoration: none;
	}
	main h1::first-letter {
		text-transform: capitalize;
	}
</style>
