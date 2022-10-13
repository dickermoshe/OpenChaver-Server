<script lang="ts">
	export let data: any
	$: console.log(data)
</script>

An error occured while activating your account.<br />
Reason: {data.error.detail}({data.status})
