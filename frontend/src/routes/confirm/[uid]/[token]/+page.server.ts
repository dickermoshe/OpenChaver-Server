import { api } from '$lib/api'
import { redirect } from '@sveltejs/kit'
import type { PageServerLoad } from './$types'

export const load: PageServerLoad = ({ params }) => {
	const { token, uid } = params

	api('POST', 'auth/users/activation/', {
		token,
		uid
	})

	throw redirect(307, '/dashboard')

	// on:fail | display fail cause
	return {
		some: 'Account confirmed'
	}
}

export const prerender = false
