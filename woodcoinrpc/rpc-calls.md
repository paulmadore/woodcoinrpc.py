**addmultisigaddress &lt;nrequired&gt; &lt;'["key","key"]'&gt; [account]**

*Add a nrequired-to-sign multisignature address to the wallet. Each key is a Litecoin address or hex-encoded public key. If [account] is specified, assign address to [account].*
    
**addnode	&lt;node&gt; &lt;add/remove/onetry&gt;**
    
*Attempts add or remove &lt;node&gt; from the addnode list or try a connection to &lt;node&gt; once.*

**backupwallet &lt;destination&gt;**
    
*Safely copies wallet.dat to destination, which can be a directory or a path with filename.*

**bannode &lt;node&gt; &lt;expiration&gt;**
    
*OMG2 only Bans &lt;node&gt; until unix timestamp &lt;expiration&gt;. Set &lt;expiration&gt; to -1 to unban a node.*
    
**createmultisig &lt;nrequired&gt; &lt;'["key,"key"]'&gt;**
    
*Creates a multi-signature address and returns a json object.*

**createrawtransaction [{"txid":txid,"vout":n},...] {address:amount,...}**
    
*Creates a raw transaction spending given inputs.*

**decoderawtransaction 	&lt;hex string&gt;**
    
*Produces a human-readable JSON object for a raw transaction.*

**dumpprivkey 	&lt;woodcoinaddress&gt;**
    
*Reveals the private key corresponding to &lt;woodcoinaddress&gt;.*
    
**encryptwallet 	&lt;passphrase&gt;**
    
*Encrypts the wallet with &lt;passphrase&gt;.*

**getaccount 	&lt;woodcoinaddress&gt;**
*Returns the account associated with the given address.*

**getaccountaddress 	&lt;account&gt;**
    
*Returns the current Litecoin address for receiving payments to this account.*

**getaddednodeinfo 	&lt;dns&gt; [node]**
    
*Returns information about the given added node, or all added nodes (note that onetry addnodes are not listed here) If dns is false, only a list of added nodes will be provided, otherwise connected information will also be available.*
    
**getaddressesbyaccount 	&lt;account&gt;**
    
*Returns the list of addresses for the given account.*
    
**getbalance 	[account] [minconf=1]**
    
*If [account] is not specified, returns the server's total available balance.
    If [account] is specified, returns the balance in the account.*

**getbestblockhash**
    
*Returns the hash of the newest block in the longest block chain.*

**getblock &lt;hash&gt;**
    
*Returns information about the block with the given hash.*


**getblockcount**

*Returns the number of blocks in the longest block chain.*


**getblockhash &lt;index&gt;**

*Returns hash of block in best-block-chain at &lt;index&gt;; index 0 is the genesis block.*


**getblocktemplate [params]**

*Returns data needed to construct a block to work on.*

**getconnectioncount**

*Returns the number of connections to other nodes.*


**getdifficulty**

*Returns the proof-of-work difficulty as a multiple of the minimum difficulty.*

**getinfo**

*Returns an object containing various state info.*

**getmininginfo**

*Returns an object containing mining-related information: blocks, currentblocksize, currentblocktx, difficulty, errors, generate, genproclimit, hashespersec, networkhashps, pooledtx, testnet.*

**getnetworkhashps 	[blocks] [height]**

*Returns the estimated network hashes per second based on the last 120 blocks. Pass in [blocks] to override # of blocks, -1 specifies since last difficulty change. Pass in [height] to estimate the network speed at the time when a certain block was found. Optional [height] parameter.*

**getnewaddress 	[account]**

*Returns a new Litecoin address for receiving payments. If [account] is specified (recommended), it is added to the address book so payments received with the address will be credited to [account].*

**getpeerinfo**

*Returns data about each connected node.*

**getrawmempool**

*Returns all transaction ids in memory pool.*

**getrawtransaction 	&lt;txid&gt; [verbose=0]**

*Returns raw transaction representation for given transaction id.
getreceivedbyaccount 	[account] [minconf=1] 	Returns the total amount received by addresses with [account] in transactions with at least [minconf] confirmations. If [account] not provided return will include all transactions to all accounts.*

**getreceivedbyaddress 	&lt;woodcoinaddress&gt; [minconf=1]**

*Returns the total amount received by    &lt;woodcoinaddress&gt; in transactions with at least [minconf] confirmations. While some might consider this obvious, value reported by this only considers __receiving__ transactions. It does not check payments that have been made __from__ this address. In other words, this is not "getaddressbalance". Works only for addresses in the local wallet, external addresses will always show 0.*

**gettransaction 	&lt;txid&gt;**

*Returns an object about the given transaction containing: amount, confirmations, txid, time[1], details (an array of objects containing: account, address, category, amount, fee).*

**gettxout 	&lt;txid&gt; &lt;n&gt; [includemempool=true]**

*Returns details about an unspent transaction output (UTXO).*

**gettxoutsetinfo**

*Returns statistics about the unspent transaction output (UTXO) set.*

**getwork	[data]**

*If [data] is not specified, returns formatted hash data to work on: midstate, data, hash1, target. If [data] is specified, tries to solve the block and returns true if it was successful.*

**help [command]**

*List commands, or get help for a command.*

**importprivkey &lt;woodcoinprivkey&gt; [label] [rescan=true]**

*Adds a private key (as returned by dumpprivkey) to your wallet. This may take a while, as a rescan is done, looking for existing transactions. Optional [rescan] parameter added in 0.8.0.*

**keypoolrefill**

*Fills the keypool, requires wallet passphrase to be set.*

**listaccounts 	[minconf=1]**

*Returns Object that has account names as keys, account balances as values.*

**listaddressgroupings**

*Returns all addresses in the wallet and info used for coincontrol.*

**listbannednodes**

*OMG2 only Returns a list of currently banned nodes along with the ban expiration timestamps.*
    
**listlockunspent**

*Returns list of temporarily unspendable outputs.*

**listreceivedbyaccount [minconf=1] [includeempty=false]**

*Returns an array of objects containing: account, amount, confirmations.*

**listreceivedbyaddress [minconf=1] [includeempty=false]**

*Returns an array of objects containing: address, account, amount, confirmations. To get a list of accounts on the system, execute litecoind*

**listreceivedbyaddress 0 true**

**listsinceblock 	[blockhash] [target-confirmations]**

*Get all transactions in blocks since block [blockhash], or all transactions if omitted.*

**listtransactions [account] [count=10] [from=0]**

*Returns up to [count] most recent transactions skipping the first [from] transactions for account [account]. If [account] not provided will return recent transaction from all accounts.*

**listunspent [minconf=1] [maxconf=9999999] ["address",...]**

*Returns array of unspent transaction inputs in the wallet.*

**lockunspent &lt;unlock?&gt; [array-of-Objects]**

*Updates list of temporarily unspendable outputs.*

**move &lt;fromaccount&gt; &lt;toaccount&gt; &lt;amount&gt; [minconf=1] [comment]**

*Move from one account in your wallet to another.*

**sendfrom &lt;fromaccount&gt; &lt;towooodcoinaddress&gt; &lt;amount&gt; [minconf=1] [comment] [comment-to]**

*&lt;amount&gt; is a real and is rounded to 8 decimal places. Will send the given amount to the given address, ensuring the account has a valid balance using [minconf] confirmations. Returns the transaction ID if successful (not in JSON object).*

**sendmany &lt;fromaccount&gt; {address:amount,...} [minconf=1] [comment]**

*Amounts are double-precision floating point numbers.*

**sendrawtransaction 	&lt;hexstring&gt;**

*Submits raw transaction (serialized, hex-encoded) to local node and network.*

**sendtoaddress &lt;woodcoinaddress&gt; &lt;amount&gt; [comment] [comment-to]**

*&lt;amount&gt; is a real and is rounded to 8 decimal places. Returns the transaction ID &lt;txid&gt; if successful.*

**setaccount &lt;woodcoinaddress&gt; &lt;account&gt;**

*Sets the account associated with the given address. Assigning address that is already assigned to the same account will create a new address associated with that account.*

**setmininput &lt;amount&gt;**

*&lt;amount&gt; is a real and is rounded to the nearest 0.00000001.*

**settxfee &lt;amount&gt;**

*&lt;amount&gt; is a real and is rounded to the nearest 0.00000001.*

**signmessage &lt;woodcoinaddress&gt; &lt;message&gt;**

*Sign a message with the private key of an address.*

**signrawtransaction 	&lt;hexstring&gt; [{"txid":txid,"vout":n,"scriptPubKey":hex},...]**

*[&lt;privatekey1&gt;,...] 	Adds signatures to a raw transaction and returns the resulting raw transaction.*

**stop**

*Stop Litecoin server.*

**submitblock &lt;hex data&gt; [optional-params-obj]**

*Attempts to submit new block to network.*

**validateaddress &lt;woodcoinaddress&gt;**

*Return information about &lt;woodcoinaddress&gt;.*

**verifychain**

*Verifies chain database at runtime.*

**verifymessage &lt;woodcoinaddress&gt; &lt;signature&gt; &lt;message&gt;**

*Verifies a signed message.*

**walletlock**

*Removes the wallet encryption key from memory, locking the wallet. After calling this method, you will need to call walletpassphrase again before being able to call any methods which require the wallet to be unlocked.*

**walletpassphrase &lt;passphrase&gt; &lt;timeout&gt;**

*Stores the wallet decryption key in memory for &lt;timeout&gt; seconds.*

**walletpassphrasechange 	&lt;oldpassphrase&gt; &lt;newpassphrase&gt;**

*Changes the wallet passphrase from &lt;oldpassphrase&gt; to &lt;newpassphrase&gt;.*