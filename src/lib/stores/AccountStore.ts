import { derived, writable } from 'svelte/store';
import type { Account } from '$types/Account';
import { getAccountByToken } from '$api/AccountRequests';

class AccountStore {
	constructor(
		public accessToken = writable<string | null>(null),
		private _account = writable<Account | null>(null),
	) {
		accessToken.subscribe(newAccessToken => {
			if (!newAccessToken) {
				_account.set(null);
				return;
			}
			getAccountByToken(newAccessToken).then((responseJSON) => {
				if (!responseJSON.id || !responseJSON.name) {
					console.error('invalid account properties, cancelling login:', responseJSON)
					accessToken.set(null);
					_account.set(null);
					return;
				}
				let account: Account = {
					id: responseJSON.id,
					nameFirst: responseJSON.name,
					nameLast: responseJSON.lastname,
					email: responseJSON.email,
					bio: responseJSON.bio,
					pfpURL: responseJSON.photoUrl,
				};
				console.log(account);
				_account.set(account);
			})
		});
	}
	public get account() {
		return derived(this._account, ($_account) => {
			return $_account;
		});
	}
}

export const accountStore = new AccountStore();
