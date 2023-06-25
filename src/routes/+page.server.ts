import type { PageServerLoad } from './$types.js';

export const load: PageServerLoad = async ({ params }) => {
	const response = await fetch('http://0.0.0.0:5000/api/');
	console.log(response);
	return {
		response
	};
}