<script lang="ts">
	import { page } from '$app/stores'
	import '../app.css'
	import Header from '../lib/Header.svelte'

	const routes = ['dashboard', 'filtering', 'accountabilty', 'account', 'subscription', 'uninstall']
</script>

<Header />

{#if $page.routeId !== ''}
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
{/if}

<main class:fullWidth={$page.routeId === ''}>
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
		color: var(--secondary-txt-color);
		transition: all ease-in-out 75ms;
	}
	nav li:hover,
	nav li:active {
		background-color: var(--hover-color);
		color: var(--default-txt-color);
	}
	nav li.active {
		background-color: var(--active-color);
		color: var(--default-bg-color);
	}
	nav li a {
		display: block;
		padding: calc(var(--general-spacing) / 3) 0 calc(var(--general-spacing) / 3)
			var(--general-spacing);
		color: inherit;
		text-decoration: none;
	}
	:global(main > h1) {
		margin-top: 0;
	}
	main h1::first-letter {
		text-transform: capitalize;
	}
</style>
