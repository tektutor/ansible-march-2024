#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule

def sayHello(msg):
  return "Hello " + msg + " !" 

def main():
    module = AnsibleModule(
        argument_spec=dict(
            message=dict(type='str'),
        ),
        supports_check_mode=True
    )

    msg = module.params['message']
    response = sayHello( msg )

    result = dict(
        output=response,
    )

    module.exit_json(**result)

if __name__ == '__main__':
    main()
