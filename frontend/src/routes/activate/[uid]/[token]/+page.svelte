<script lang="ts">
	export let data: any
</script>

<section>
	<div class="container">
		<p>
			An error occured while activating your account.<br />
			Reason: {data.error.detail}({data.status})
		</p>
	</div>
</section>
