<script lang="ts">
	import '../app.css'
	import Header from '../lib/Header.svelte'
	// import Header from '$lib/Header.svelte'

	// export const prerender = true

	const routes = ['dashboard', 'accountabilty', 'uninstall', 'subscription', 'account']
</script>

<Header />

<aside>
	<nav>
		<ul>
			{#each routes as route}
				<li>
					<a href={route} sveltekit:prefetch>{route}</a>
				</li>
			{/each}
		</ul>
	</nav>
</aside>

<main>
	<!-- <div class="crumbs">
		<ol>
			<li>
				<a href="/console">Console</a>
			</li>
		</ol>
	</div> -->

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
</style>
