import unittest
import os


class TestImports(unittest.TestCase):

    def test_tree_imports(self):
        base_path = os.path.dirname(os.path.abspath(__file__))
        for base, dirs, files in os.walk(os.path.join(base_path, "k8s_datamodels")):
            for file in files:
                if file != "__init__.py" and file.endswith(".py"):
                    module_name = base.replace(base_path, "").replace("\\", "/").replace(
                        "/__pycache__", "").replace("/", ".")
                    if module_name.startswith("."):
                        module_name = module_name[1:]  # avoid relative import
                    exec(f"from {module_name} import {file.replace('.py', '')}")


if __name__ == '__main__':
    unittest.main()
