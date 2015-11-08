from rest_framework.test import APITestCase

class UploadMedia(APITestCase):

    def testUpload(self):
        with open('app/test_assets/image.jpg', 'rb') as fp:
            response = self.client.post('/media/', {'name': 'foo', 'file': fp}, format='multipart')
        self.assertEqual(response.status_code, 200)
