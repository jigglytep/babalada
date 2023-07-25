import { derived, writable } from 'svelte/store';
import type { Account } from '$types/Account';
import { getAccountData } from '$api/AccountRequests';

class AccountStore {
	constructor(
		public jwt = writable<string>(''),
		private _account = writable<Account | null>(null),
	) {
		// TODO: make store reactive, the following results in errors
		//	jwt.subscribe(newJWT => {
		//		getAccountData(newJWT);
		//		// TODO: update _account
		//	});
	}
	public get account() {
		return derived(this._account, ($_account) => {
			return $_account;
		});
	}
}

export const accountStore = new AccountStore();
