import { accountStore } from "$stores/AccountStore";
import type { Account } from "$types/Account";
import { redirect } from "@sveltejs/kit";

export const login = async (formData: FormData) => {
	const request: RequestInit = {
		method: 'POST',
		body: formData,
		redirect: 'follow',
	};
	const response = await fetch('/api/login', request);
	const responseJSON = await response.json();
	if (responseJSON.token) {
		accountStore.accessToken.set(responseJSON.token)
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

export const getAccountByToken = async (accessToken: string) => {
	const request: RequestInit = {
		method: 'GET',
		headers: new Headers({
			'x-access-token': accessToken,
		}),
		redirect: 'follow'
	}
	const response = await fetch('/api/account', request)
	const responseJSON = await response.json();
	return responseJSON;
}

export const getAccountById = async () => {
	
}
