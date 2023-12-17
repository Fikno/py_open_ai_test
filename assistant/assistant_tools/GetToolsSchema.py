import os
import importlib.util

from pydantic import Field
from instructor import OpenAISchema

class GetToolsSchema(OpenAISchema):
    """Makes a list of JSON schemas associated with the tools available"""

    current_directory: str = Field(default=os.path.dirname(os.path.abspath(__file__)),
        description="directory containing tools available, defaults to the directory containing the file this module is stored on.")

    def get_python_files(self, directory_path):
        python_files = []
    
        # Iterate through all files in the directory
        for filename in os.listdir(directory_path):
            # Check if the file has a .py extension
            if filename.endswith(".py") and filename != '__init__.py':
                # Remove the file extension and add to the list
                file_name_without_extension = os.path.splitext(filename)[0]
                python_files.append(file_name_without_extension)
    
        return python_files
    
    def ModuleSchema(self, module_name, current_directory):
    
        #current_directory = os.path.dirname(os.path.abspath(__file__))
        module_path = os.path.join(current_directory, f"{module_name}.py")

        if not os.path.exists(module_path):
            raise ValueError(f"The module '{module_name}' does not exist in the current directory.")

        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)

        try:
            spec.loader.exec_module(module)

            if hasattr(module, module_name):
                module_class = getattr(module, module_name)
                result = module_class.openai_schema
                print(f"openai_schema called on class '{module_name}' successfully.")
                return result
            else:
                raise AttributeError(f"The module '{module_name}' does not contain a class with the same name.")

        except Exception as e:
            print(f"Failed to load module '{module_name}': {str(e)}")
            return None
        
    def run(self):
        list_of_modules = []
        test_list = self.get_python_files(self.current_directory)

        for i in test_list:
            print(i)
            schema = self.ModuleSchema(i, self.current_directory)

            if schema != None:
                list_of_modules.append(schema)

        return list_of_modules
    
    def is_safe(self) -> bool:
        return True
        

#current_directory = os.path.dirname(os.path.abspath(__file__))
def main():
    _test = GetToolsSchema()

    test = _test.run()

    print(test)


if __name__ == "__main__":
    main()
