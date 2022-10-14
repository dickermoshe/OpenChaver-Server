import storage from './store'

export const authToken = storage<string>('authToken', '')
