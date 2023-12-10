import os
import importlib.util

def LazyLoadModule(module_name, **kwargs):
    """
    Lazy load a module and create an instance of the class within that module.

    Parameters:
    - module_name (str): The name of the module to load. It should be the same as the file name without the extension.
    - kwargs (dict): Keyword arguments to be passed to the class constructor.
    """
    current_directory = os.path.dirname(os.path.abspath(__file__))
    module_path = os.path.join(current_directory, f"{module_name}.py")

    if not os.path.exists(module_path):
        raise ValueError(f"The module '{module_name}' does not exist in the current directory.")

    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(module)

        if hasattr(module, module_name):
            module_class = getattr(module, module_name)
            instance = module_class(**kwargs)
            print(f"Instance of class '{module_name}' created successfully.")
            return instance
        else:
            raise AttributeError(f"The module '{module_name}' does not contain a class with the same name.")

    except Exception as e:
        print(f"Failed to load module '{module_name}': {str(e)}")
        return None
    
def main():
    test_module = "PythonFileWriter"
    test_kwargs = '{"file_name": "test.py", "body": "print(test)"}'
    test = LazyLoadModule(test_module, **eval(test_kwargs))

if __name__ == "__main__":
        main()