import ConfigParser
config = ConfigParser.RawConfigParser()
config.read('config.ini')
section_a_Value = config.get('MYSERVER', 'HOST')
print("myhost: "+str(section_a_Value))