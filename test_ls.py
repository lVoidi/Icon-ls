import unittest
import os
import tempfile
from pathlib import Path
from ls import Extensions, Ls

class TestExtensions(unittest.TestCase):
    def setUp(self):
        # Crear un directorio temporal para las pruebas
        self.test_dir = tempfile.mkdtemp()
        self.old_dir = os.getcwd()
        os.chdir(self.test_dir)
        
        # Crear algunos archivos de prueba
        open('.hidden_file', 'w').close()
        open('normal_file.txt', 'w').close()
        open('test.py', 'w').close()
        os.mkdir('test_dir')
        os.mkdir('.hidden_dir')
        
        self.extensions = Extensions()

    def tearDown(self):
        # Limpiar después de las pruebas
        os.chdir(self.old_dir)
        for root, dirs, files in os.walk(self.test_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(self.test_dir)

    def test_is_hidden(self):
        ls = Ls([])
        self.assertTrue(ls.is_hidden('.hidden_file'))
        self.assertFalse(ls.is_hidden('normal_file.txt'))

    def test_is_config_file(self):
        ls = Ls([])
        open('.config', 'w').close()
        open('test.conf', 'w').close()
        self.assertTrue(ls.is_config_file('.config'))
        self.assertTrue(ls.is_config_file('test.conf'))
        self.assertFalse(ls.is_config_file('normal_file.txt'))

    def test_file_icon(self):
        ls = Ls([])
        self.assertEqual(ls.file_icon('test_dir'), ls.extensions['folder'])
        self.assertEqual(ls.file_icon('test.py'), ls.extensions['py'])
        self.assertEqual(ls.file_icon('unknown.xyz'), ls.extensions['default'])

    def test_show_hidden_flag(self):
        ls = Ls(['-sh'])
        ls.show_files()
        self.assertTrue('.hidden_file' in ls.files)
        self.assertTrue('normal_file.txt' in ls.files)

    def test_only_hidden_flag(self):
        ls = Ls(['-oh'])
        ls.show_files()
        self.assertTrue('.hidden_file' in ls.files)
        self.assertFalse('normal_file.txt' in ls.files)

    def test_only_dirs_flag(self):
        ls = Ls(['-od'])
        ls.show_files()
        self.assertTrue('test_dir' in ls.files)
        self.assertFalse('normal_file.txt' in ls.files)

    def test_exclude_flag(self):
        ls = Ls(['-ex', 'py'])
        ls.show_files()
        self.assertFalse('test.py' in ls.files)
        self.assertTrue('normal_file.txt' in ls.files)

if __name__ == '__main__':
    unittest.main() 