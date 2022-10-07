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
		border-bottom: 2px solid #d7e4f4;
		background-color: var(--default-bg-color);
		z-index: 100;
	}
	a {
		color: var(--default-color);
		text-decoration: none;
	}
	h1 {
		font-size: 1.375rem;
	}
</style>
