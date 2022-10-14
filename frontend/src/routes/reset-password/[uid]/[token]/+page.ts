import type { PageLoad } from './$types'

export const prerender = false

export const load: PageLoad = async ({ params }) => {
	const { token, uid } = params

	// pass params to page as `data`
	return {
		token,
		uid
	}
}
