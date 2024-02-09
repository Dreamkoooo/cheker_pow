### SOLANA POW ADDRESS CHEKER ###

Script find 'pow' file in the select directory

https://twitter.com/pow_mint

https://pow.cafe/

### Install Solana-cli ###

## MacOS ##

brew install solana

solana --version

OR

sh -c "$(curl -sSfL https://release.solana.com/v1.18.1/install)"

solana --version

## Windows ##

cmd /c "curl https://release.solana.com/v1.18.1/solana-install-init-x86_64-pc-windows-msvc.exe --output C:\solana-install-tmp\solana-install-init.exe --create-dirs"

C:\solana-install-tmp\solana-install-init.exe v1.18.1

solana --version

### Start grinding address ###

solana-keygen grind --starts-with pow:100000 --num-threads 20 (CHANGE NUM THREADS If your processor has fewer cores or threads reduce!)

### Check files ###

1. Navigate to the directory with the pow.py file

cd YOUR DIRECTORY

2. Start script, it find and print console

python3 pow.py

### FOLOW ME PLEASE ###

https://t.me/planetamoney