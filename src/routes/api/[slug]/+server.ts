import type { ServerLoad } from "@sveltejs/kit";

export const GET: ServerLoad = async ({ params, request }) => {
	console.log(request);
	return await fetch(`http://127.0.0.1:5000/api/${params.slug}`, request);
}

export const POST: ServerLoad = async ({ params, request }) => {
	let url = `http://127.0.0.1:5000/api/${params.slug}`;
	let newRequest = {
		method: request.method,
		body: request.body,
		redirect: request.redirect,
		// @ts-ignore
		duplex: 'half',
	}
	let response = await fetch(url, newRequest);
	console.log('REQUEST:')
	console.log(newRequest);
	console.log('RESPONSE:')
	console.log(response)
	console.log('URL:')
	console.log(url);
	return response;
}

export const PATCH: ServerLoad = async ({ params, request }) => {
	console.log(request);
	return await fetch(`http://127.0.0.1:5000/api/${params.slug}`, request);
}

export const PUT: ServerLoad = async ({ params, request }) => {
	console.log(request);
	return await fetch(`http://127.0.0.1:5000/api/${params.slug}`, request);
}

export const DELETE: ServerLoad = async ({ params, request }) => {
	console.log(request);
	return await fetch(`http://127.0.0.1:5000/api/${params.slug}`, request);
}