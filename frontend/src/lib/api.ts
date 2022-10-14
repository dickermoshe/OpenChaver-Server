import { authToken } from "./authToken"

let token: any
authToken.subscribe(val => token = val)

const base = 'https://api.openchaver.com'

export const api = (method: string, resource: string, data?: Record<string, unknown>) => {
	return fetch(`${base}/${resource}`, {
		method,
		headers: {
			'content-type': 'application/json',
			Authorization: token? `Token ${token}`: ''
		},
		body: data && JSON.stringify(data)
	})
}
