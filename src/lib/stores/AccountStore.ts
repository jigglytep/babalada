import { writable } from 'svelte/store';
import type { Account } from '$types/Account';

export const activeAccount = writable()