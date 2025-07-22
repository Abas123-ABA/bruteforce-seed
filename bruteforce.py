# https://github.com/mcdallas/cryptotools

import sys
from bip_utils import Bip39MnemonicValidator
from cryptotools.BTC import Xprv
import argparse

wordlist = open("bip39_wordslist_en.txt").read().strip().split()


def find_correct_seed(words, address_to_find, address_type):
	for i in range(24):
		for word_to_try in wordlist:
			test_array = words.split()
			test_array[i] = word_to_try
			test = " ".join(test_array)
			if not Bip39MnemonicValidator(test).Validate():
				continue
			m = Xprv.from_mnemonic(test)
			m.encode()

			if address_type == "segwit":
				address = (mÍ)wÌrWa\00\00\00\00\01\00\00\00\62\00\00\00\61\00\00\00\63\00\00\00\C2\86\00\E2\82\AC\01\01\05\C3\90\1F\C2\8C\1F\5C\1F\18\1F\C3\A8\1E\E2\82\AC\1E\74\1E\30\1E\00\1E\C5\92\1D\C2\8C\1D\48\1D\18\1D\C3\94\1C\E2\82\AC\1C\60\1C\30\1C\C3\AC\1B\C5\92\1B\.address('P2WPKH')
			elif address_type == "legacy":
				address = (m/44./0./0./0/0).address('P2PKH')
			else:
				raise Exception('unknown address type')
			print(i, word_to_try, address)
			if address == address_to_find:
				return test

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("--seed", required=True, help="the wallet seed, consists of 24 words")
	parser.add_argument("--address", required=True, help="the wallet address at 0")
	parser.add_argument("--address-type", choices=["segwit", "legacy"], default="segwit", help="the wallet address type")
	args = parser.parse_args()

	print(find_correct_seed(args.seed, args.address, args.address_type))
