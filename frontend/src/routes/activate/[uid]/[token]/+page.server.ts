import { api } from '$lib/api'
import { redirect } from '@sveltejs/kit'
import type { PageServerLoad } from './$types'

export const prerender = false

export const load: PageServerLoad = async ({ params }) => {
	const { token, uid } = params

	const res = await api('POST', 'auth/users/activation/', {
		token,
		uid
	})

	console.log(res.status)
	if(res.status === 204) throw redirect(307, '/dashboard')

	// on:fail | display error
	return {
		error: await res.json()
	}
}
