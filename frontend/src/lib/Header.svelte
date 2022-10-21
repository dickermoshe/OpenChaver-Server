<script lang="ts">
	import { page } from "$app/stores"
	import { authToken } from "./authToken"

	let isDashboard: boolean
	$: isDashboard = ($page.routeId?.search(/\(dashboard\)\//) ?? -1) > -1

	const logout = async () => {
		$authToken = ''
		await fetch('https://api.openchaver.com/auth/token/logout/', {
			method: 'POST'
		})
		window.location.href = '../'
	}
</script>

<header class:dark={!$page.routeId}>
	<a href={isDashboard && $page.routeId !== '(dashboard)/dashboard'? "/dashboard": "../"} id="logo">
		<!-- <img src="/favicon.png" alt="logo"> -->
		<h1>OpenChaver</h1>
	</a>
	<div class="buttons">
		{#if isDashboard}
			<a href="../" on:click|preventDefault={logout} data-sveltekit-prefetch>Logout</a>
		{:else if $authToken}
			<a href="/dashboard" data-sveltekit-prefetch>Dashboard</a>
		{:else}
			<a href="/login" data-sveltekit-prefetch>Login</a>
		{/if}
	</div>
</header>

<style>
	header {
		display: flex;
		align-items: center;
		justify-content: space-between;
		height: var(--header-height);
		width: 100%;
		padding: 0 var(--general-spacing);
		box-sizing: border-box;
		background-color: var(--default-bg-color);
		border-bottom: 2px solid var(--default-border-color);
		z-index: 100;
	}
	header.dark {
		background-color: var(--default-txt-color);
		border-bottom-color: #222a36;
	}
	a {
		color: var(--default-txt-color);
		text-decoration: none;
	}
	.dark a {
		color: var(--secondary-bg-color);
	}
	#logo {
		display: flex;
		flex-direction: row;
		align-items: center;
	}
	/* #logo img {
		height: 26px;
		padding-right: calc(var(--general-spacing) / 3);
	} */
	h1 {
		font-size: 1.375rem;
	}
</style>
