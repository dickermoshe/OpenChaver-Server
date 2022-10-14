<svelte:head>
	<title>Home | OpenChaver</title>
	<meta
		name="description"
		content="Early tester access | An OSS content filtering service to block mature content."
	/>
</svelte:head>

<section id='hero'>
	<div class="container">
		<h1>Stay accountable for what is on your screen&nbsp;<div class="tag">Early access</div></h1>
		<h3>Software that shares screenshots of your computer screen with a partner to monitor what you are viewing.</h3>
		<a href="/signup" class="button" data-sveltekit-prefetch>Filter my device</a>
	</div>
</section>

<section>
	<div class="container">
		<h1>Links</h1>
		Desktop client [still in development]: <a href="https://github.com/dickermoshe/openchaver/releases">Releases</a><br />
		View the code: <a href="https://github.com/dickermoshe/openchaver">Github repo</a>
	</div>
</section>

<style>
	#hero {
		padding: calc(var(--general-spacing) * 3) 0 calc(var(--general-spacing) * 4);
		background: var(--default-txt-color);
		color: var(--default-bg-color);
	}
	#hero h1 {
		display: inline-block;
		max-width: 700px;
		margin: 0 0 1rem;
		font-size: 3rem;
	}
	.tag {
		display: inline-block;
		padding: calc(var(--general-spacing) / 5) calc(var(--general-spacing) / 2);
		border-radius: 4px;
		font-size: .75rem;
		font-weight: 700;
		text-transform: uppercase;
		vertical-align: super;
		color: #fff;
		background-color: var(--active-color);
	}
	#hero h3 {
		font-weight: 500;
		max-width: 650px;
		margin-bottom: var(--general-spacing);
		color: var(--default-border-color);
	}
	a.button {
		display: inline-block;
		margin-top: 1rem;
		padding: .5rem 1rem;
		border-radius: 4px;
		font-size: .875rem;
		font-weight: 700;
		color: #fff;
		background-color: var(--active-color);
		text-decoration: none;
		transition: all ease-in-out 100ms;
	}
	a.button:hover {
		background-color: var(--hover-color);
		color: var(--default-txt-color);
	}
</style>
