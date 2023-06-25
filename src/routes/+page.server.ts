import type { PageServerLoad } from './$types.js';

export const load: PageServerLoad = async ({ params }) => {
	const response = await fetch('http://localhost:5000/api/');
	return {
		response
	};
}