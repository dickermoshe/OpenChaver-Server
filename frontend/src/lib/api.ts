const base = 'https://api.openchaver.com'

export const api = (method: string, resource: string, data?: Record<string, unknown>) => {
	return fetch(`${base}/${resource}`, {
		method,
		headers: {
			'content-type': 'application/json',
			// Authorization: `Token 3d1214170dd3cd1dbf1828736e94c4c0407b556c`
			// 'Authorization': `Token {localStorage.authToken}`
		},
		body: data && JSON.stringify(data)
	})
}
