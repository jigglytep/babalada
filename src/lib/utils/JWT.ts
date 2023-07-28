export const decodeJWT = (token: string) => {
	// https://stackoverflow.com/questions/38552003/how-to-decode-jwt-token-in-javascript-without-using-a-library
	if (!token) {
		throw new Error('token is undefined');
	}
	const parts = token.split('.');
	if (parts.length !== 3) {
		throw new Error('invalid token format');
	}
	return {
		header: JSON.parse(atob(parts[0])),
		payload: JSON.parse(atob(parts[1])),
		// signature: JSON.parse(atob(parts[2])),
	}
}
