from secp256k1 import *

def single_leaf_script():
  print("Running Taproot test")
  internal_key = "a34b99f22c790c4e36b2b3c2c35a36db06226e41c692fc82b8b56ac1c540c5bd"
  internal_key_bytes = bytes.fromhex(internal_key)
  leaf_version = "cc"

  leaf_script = "41069228de6902abb4f541791f6d7f925b10e2078ccb1298856e5ea5cc5fd667f930eac37a00cc07f9a91ef3c2d17bf7a17db04552ff90ac312a5b8b4caca6c97aa4ac"
  leaf_hash = TaggedHash("TapLeaf", bytes.fromhex(leaf_version + f'{len(leaf_script)//2:0x}' + leaf_script))
  tap_tweak = TaggedHash("TapTweak", internal_key_bytes + leaf_hash)
  tweaked_key = ECPubKey().set(internal_key_bytes).tweak_add(tap_tweak)
  p2tr_spk = "5120" + tweaked_key.get_bytes(True).hex()

  print("P2TR scriptPubKey: " + p2tr_spk)
