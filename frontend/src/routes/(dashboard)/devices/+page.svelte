<script lang='ts'>
	import { api } from "$lib/api"

	api('GET', 'devices/')
	.then(res => res.json())
	.then(json => console.log(json))
</script>

This page will show all the devices connected to a given user.
