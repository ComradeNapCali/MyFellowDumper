import uncompyle6
import glob
import io

class ModuleDecompiler:
    def __init__(self, folder_name):
        self.folder_name = folder_name
        self.files = glob.glob(f"{self.folder_name}/**/*.pyc", recursive=True)
        self.files_numb = len(self.files)

    def decompile_modules(self):
        for module_count, module in enumerate(self.files, 1):
            with open(module[:-1], 'w') as writable_decompiler:
                decompiled_result = io.StringIO()
                try:
                    uncompyle6.decompile_file(module, outstream=decompiled_result)
                except:
                    writable_decompiler.write("# MyFellowDumper\n# Failed to decompile file")
                    print(f"Failed to decompile: {writable_decompiler.name}", f"({module_count}/{self.files_numb})")
                    continue
                writable_decompiler.write(decompiled_result.getvalue())
            print(f"Decompiled module: {writable_decompiler.name}", f"({module_count}/{self.files_numb})")