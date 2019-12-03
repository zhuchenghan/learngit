from django.test import TestCase

# Create your tests here.
import os
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(base_dir, 'polls',"views.py")
print(base_dir)
print(file_path)
