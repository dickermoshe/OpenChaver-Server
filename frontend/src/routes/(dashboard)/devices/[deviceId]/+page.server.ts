import { redirect } from '@sveltejs/kit'
import type { PageServerLoad } from './$types'

export const prerender = false

export const load: PageServerLoad = async ({ params }) => {
	const { deviceId } = params

	// pass params to page as `data`
	throw redirect(307, '/devices')
	return {
		deviceId
	}
}
