Usage:
1. Set file config.properties:
    Set property "yfolder" with your hybris installations folder
    For example, you have 5.4.0.0 and 5.7.0.0 in /Users/me/Hybris/installations, then:

        yfolder=/Users/me/Hybris/installations

    During runHybris.py execution the folders 5.4.0.0 and 5.7.0.0 will be listed

2. On *nix platforms where python is installed, run:
    python runHybris.py

3. Running in hybris in debug mode:
    python runHybris.py debug

4. cowsay installation is optional but it's cool