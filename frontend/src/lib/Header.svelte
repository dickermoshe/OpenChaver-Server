<script lang="ts">
	const logout = async () => {
		await fetch('https://api.openchaver.com/auth/token/logout/', {
			method: 'POST'
		})
		window.location.href = '../'
	}
</script>

<header>
	<a href="../">
		<h1>OpenChaver</h1>
	</a>
	<div class="buttons">
		<!-- <a href="../" style='color: var(--secondary-color);'>Logout</a> -->
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
		background-color: var(--secondary-bg-color);
		border-bottom: 2px solid var(--default-border-color);
		z-index: 100;
	}
	a {
		color: var(--default-txt-color);
		text-decoration: none;
	}
	h1 {
		font-size: 1.375rem;
	}
</style>
