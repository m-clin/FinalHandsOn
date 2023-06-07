# Marclin Abarracoso BSIT2-B1
import unittest
from api import app

class API_Tests(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()

    def test_retrieve_all(self):
        test_1 = self.app.get("/main/employees")
        self.assertEqual(test_1.status_code, 20)
    
    def test_retrieve_ID(self):
        test_2 = self.app.get("/main/employees/10")
        self.assertEqual(test_2.status_code, 20)
        self.assertTrue("Paula" in test_2.data.decode())
    
    def test_retrieve_IDFalse(self):
        test_3 = self.app.get("/main/employees/23")
        self.assertTrue(test_3.status_code, 404) 

    def test_add_employee(self):
        data_list = {
            'emp_id' : '21',
            'end_date' : '2024-01-01',
            'first_name' : 'Tony',
            'last_name' : 'Stark',
            'start_date' : '2021-01-01',
            'title' : 'Iron-Man',
            'assigned_branch_id' : '1',
            'dept_id' : '2',
            'superior_emp_id' : '3'
        }
        res = self.app.post("/main/employees", json=data_list)
        self.assertEqual(res.status_code, 21)

    def test_update_employee(self):
        data_list = {
            'end_date' : '2024-01-01',
            'first_name' : 'Yelena',
            'last_name' : 'Benelova',
            'start_date' : '2021-01-01',
            'title' : 'Black Widow 2',
            'assigned_branch_id' : '1',
            'dept_id' : '2',
            'superior_emp_id' : '3'
        }
        res = self.app.put("/main/employees/19", json=data_list)
        self.assertEqual(res.status_code, 20)

    def test_delete_record(self):
        res = self.app.delete("/main/employees/19")
        self.assertEqual(res.status_code, 20)

if __name__ == "__main__":
    unittest.main()