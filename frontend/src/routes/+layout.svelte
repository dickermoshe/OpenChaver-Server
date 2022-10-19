<script lang="ts">
	import { page } from '$app/stores'
	import { authToken } from '$lib/authToken'
	import Header from '$lib/Header.svelte'
	import '../app.css'

	$: if($page.routeId === 'signup' || $page.routeId === 'login') authToken.set('')
</script>

<Header />
<slot />
