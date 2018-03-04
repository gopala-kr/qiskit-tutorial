APItoken = '9a273b55fb6c782ed1a321b51e2849503a9f4d583ca2bf23dfff9f82618c532af439095ea55f8f9458e6b0ec64d09651dd61b24b924edd44f31d210b7013e1b0'
config = {'url': 'https://quantumexperience.ng.bluemix.net/api'}

if 'APItoken' not in locals():
    raise Exception('Please set up your access token. See Qconfig.py.')
