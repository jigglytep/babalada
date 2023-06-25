import type { PageServerLoad } from './$types.js';

export const load: PageServerLoad = async ({ params }) => {
	let s = fetch("http://0.0.0.0:5000/api/")
    .then((response) => response.json())
    .catch((error) => {
      console.log(error);
      return [];
    });
	return {s};
}