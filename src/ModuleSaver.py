import os

class ModuleSaver:
    def __init__(self, module_contents):
        self.module_contents = module_contents
        self.magic = b"\x03\xF3\x0D\x0A" + b"\x00" * 4

    def save_modules(self):
        for module in self.module_contents:
            module_name = module['module_string']
            module_size = module['module_size']
            module_code = self.magic + module['module_code']

            if module_size < 0:
                module_name += '.__init__'

            saveable_module = module_name.replace(".", "/") + '.pyc'
            if saveable_module.count('/') > 0:
                module_dir, module_filename = saveable_module.rsplit("/", 1)
                if not os.path.isdir(f"gamedump/{module_dir}"):
                    os.makedirs(f"gamedump/{module_dir}")
            else:
                module_dir = ''
                module_filename = saveable_module

            with open(f"gamedump/{module_dir}/{module_filename}", 'wb') as writable_module:
                writable_module.write(module_code)

            print(f"Successfully dumped: {writable_module.name[9:]}!")