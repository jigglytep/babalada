import type { ServerLoad } from "@sveltejs/kit";

export const GET: ServerLoad = async ({ params, request }) => {
	let internalURL = `http://127.0.0.1:5000/api/${params.slug}`;
	let internalRequest: RequestInit = {
		method: request.method,
		headers: request.headers,
		body: request.body,
		redirect: request.redirect,
		// @ts-ignore
		duplex: 'half',
	}
	let response = await fetch(internalURL, internalRequest);
	return response;
}

export const POST: ServerLoad = async ({ params, request }) => {
	let internalURL = `http://127.0.0.1:5000/api/${params.slug}`;
	let internalRequest: RequestInit = {
		method: request.method,
		headers: request.headers,
		body: request.body,
		redirect: request.redirect,
		// @ts-ignore
		duplex: 'half',
	}
	let response = await fetch(internalURL, internalRequest);
	return response;
}

export const PATCH: ServerLoad = async ({ params, request }) => {
	let internalURL = `http://127.0.0.1:5000/api/${params.slug}`;
	let internalRequest: RequestInit = {
		method: request.method,
		headers: request.headers,
		body: request.body,
		redirect: request.redirect,
		// @ts-ignore
		duplex: 'half',
	}
	let response = await fetch(internalURL, internalRequest);
	return response;
}

export const PUT: ServerLoad = async ({ params, request }) => {
	let internalURL = `http://127.0.0.1:5000/api/${params.slug}`;
	let internalRequest: RequestInit = {
		method: request.method,
		headers: request.headers,
		body: request.body,
		redirect: request.redirect,
		// @ts-ignore
		duplex: 'half',
	}
	let response = await fetch(internalURL, internalRequest);
	return response;
}

export const DELETE: ServerLoad = async ({ params, request }) => {
	let internalURL = `http://127.0.0.1:5000/api/${params.slug}`;
	let internalRequest: RequestInit = {
		method: request.method,
		headers: request.headers,
		body: request.body,
		redirect: request.redirect,
		// @ts-ignore
		duplex: 'half',
	}
	let response = await fetch(internalURL, internalRequest);
	return response;
}