APItoken = ' '
config = {'url': 'https://quantumexperience.ng.bluemix.net/api'}

if 'APItoken' not in locals():
    raise Exception('Please set up your access token. See Qconfig.py.')
