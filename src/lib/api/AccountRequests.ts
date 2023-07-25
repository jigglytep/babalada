import { accountStore } from "$stores/AccountStore";
import type { Account } from "$types/Account";

export const login = async (formData: FormData) => {
	const request: RequestInit = {
		method: 'POST',
		body: formData,
		redirect: 'follow',
	};
	const response = await fetch('/api/login', request);
	const responseJSON = await response.json();
	if (responseJSON.token) {
		accountStore.jwt.set(responseJSON.token);
	}
	return responseJSON;
}

export const logout = async () => {
	const request: RequestInit = {
		method: 'POST',
		redirect: 'follow',
	};
	const response = await fetch('/api/logout', request);
	const responseJSON = await response.json();
	return responseJSON;
}

export const getAccountData = async (jwt: string | undefined) => {
	// TODO: request by id instead of by jwt
	const request: RequestInit = {
		headers: (jwt === undefined) ? undefined : new Headers({'x-access-token': jwt}),
		method: 'GET',
		redirect: 'follow',
	};
	const response = await fetch('/api/account', request);
	const responseJSON = await response.json();
	// TODO: return Account datatype
	console.log(responseJSON);
	return responseJSON;
}
