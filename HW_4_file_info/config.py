import ConfigParser

parser = ConfigParser.ConfigParser()

DICT_CONFIG = {'c': ['.c','.h'],
               'py':['.py','.pyc'],
               'pl':['.pl','.pm']}
CONFIG_PATH = 'config.ini'

def __create_config_file():
    parser.add_section('Extensions')
    for key in DICT_CONFIG.keys():
        parser.set('Extensions', key, DICT_CONFIG[key])

    with open(CONFIG_PATH, 'w') as f:
        parser.write(f)

def get_dict_config(property_key = '',config_path = CONFIG_PATH):

    parser.read(config_path)
    confdict = {section: dict(parser.items(section)) for section in parser.sections()}
    if property_key:
        try:
            return confdict[property_key]
        except KeyError:
            print 'No {prop} property in file'.format(prop = property_key)
    else:
        return confdict

if __name__ == '__main__':
    __create_config_file()
    # print get_dict_config('Extensions')