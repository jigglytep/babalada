export type Account = {
	id: string;
	nameFirst: string;
	nameLast?: string;
	email?: string;
	bio?: string;
	pfpURL?: string;
}

export const mockAccount: Account = {
	id: 'mock_account',
	nameFirst: 'Mock',
	nameLast: 'User',
	email: 'mock@example.com',
	bio: 'This bio records the autobiographical epic of Mock User, the most skilled stock trader from The Emerald City.',
	pfpURL: '/img/default_user_picture.png',
}
