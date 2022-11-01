<script lang="ts">
	import { browser } from '$app/environment'
	import { goto } from '$app/navigation'
	import { page } from '$app/stores'
	import { authToken } from '$lib/authToken'

	// Send user to /login page if not authenticated
	if (!$authToken && browser) goto('/login')

	const routes = ['dashboard', 'devices', 'accountabilty', 'account', 'subscription'],
		logout = async () => {
			$authToken = ''
			await fetch('https://api.openchaver.com/auth/token/logout/', {
				method: 'POST'
			})
			window.location.href = '../'
		}
</script>

<aside>
	<nav>
		<ul>
			{#each routes as route}
				<li class:active={route === $page.url.toString().split('/').pop() ?? $page.routeId}>
					<a href={route} data-sveltekit-prefetch>{route}</a>
				</li>
			{/each}
			<li>
				<a href="../" on:click|preventDefault={logout} data-sveltekit-prefetch>Logout</a>
			</li>
		</ul>
	</nav>
</aside>

<main>
	<h1>{$page.routeId?.replaceAll('(dashboard)/', '')}</h1>
	<slot />
</main>

<style>
	aside,
	nav,
	ul {
		position: relative;
		height: 100%;
	}
	aside a {
		text-transform: capitalize;
	}
	nav ul {
		list-style: none;
		margin: 0;
		padding: 0;
	}
	nav li {
		margin-bottom: 4px;
		border-radius: 8px;
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
			calc(var(--general-spacing) / 2);
		color: inherit;
		/* font-size: .875rem; */
		text-decoration: none;
	}
	nav li:last-of-type {
		position: absolute;
		bottom: 0;
		width: 100%;
		display: block;
		margin-bottom: var(--general-spacing);
	}
	:global(main > h1) {
		margin-top: 0;
	}
	main h1::first-letter {
		text-transform: capitalize;
	}
</style>
