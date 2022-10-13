import { api } from '$lib/api'
import { redirect } from '@sveltejs/kit'
import type { PageServerLoad } from './$types'

export const prerender = false

export const load: PageServerLoad = ({ params }) => {
	const { token, uid } = params

	api('POST', 'auth/users/reset_password/', {
		token,
		uid
	})

	throw redirect(307, '/dashboard')

	// on:fail | display error
	return {
		some: 'Reset password confirmed'
	}
}
