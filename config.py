if __name__=='__main__':
    import os
    import json

    # create instance folder
    instance_dir = 'instance/'
    if not os.path.exists(instance_dir):
        print("Creating direcory: " + instance_dir)
        os.makedirs(instance_dir)

    config = {}

    # read configuration from the instance_config
    instance_config_path = os.path.join(instance_dir, 'config.json')


    try:
        with open(instance_config_path) as f:
            print("Reading " + instance_config_path)
            instance_json = json.load(f)

            # add instance configurations
            for key, value in instance_json.items():
                if key not in config:
                    config[key] = value
    except:
        print('Could not find ' + instance_config_path + '. Will create.')

    # read configuration from the default_config
    default_config_path = 'config/default_config.json'

    try:
        with open(default_config_path) as f:
            print("Reading " + default_config_path)
            default_json = json.load(f) 
            
            # add all default configurations that aren't in the instance file
            for key, value in default_json.items():
                if key not in config:
                    config[key] = value
        
            # add all app configurations separately
            for key, value in default_json['app'].items():
                if key not in config['app']:
                    config['app']['key'] = value
    except:
        print('Could not find ' + default_config_path)

    # write configuration to file
    try:
        with open(instance_config_path, 'w') as f:
            print("Writing " + instance_config_path)
            json.dump(config, f, indent=4, sort_keys=True)
    except:
        print("Failed to write " + instance_config_path)