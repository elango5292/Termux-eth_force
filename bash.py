import os
os.system("apt update && apt full-upgrade\npkg install git\napt update && apt full-upgrade\npip install wheel\npkg update\npkg install build-essential\npkg install binutils\npip install coincurve --no-binary all\npip install bit\nMATHLIB=\"m\" pip3 install numpy\npip install bitcoinlib --no-binary all\npip install eth_hash")
