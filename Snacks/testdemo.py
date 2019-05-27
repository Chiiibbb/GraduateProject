class LoginTest:
    def test_login(self):
        rep=self.client.get('/login')
        self.assertEqual(rep.status_code,200)