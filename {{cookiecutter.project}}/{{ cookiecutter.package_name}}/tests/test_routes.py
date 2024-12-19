from django.test import TestCase
from ninja.testing import TestAsyncClient
from kitchenai_cookbook.kitchenai import app  # Adjust this import to match your router location
from django.core.files.uploadedfile import SimpleUploadedFile
import pytest



class TestKitchenAIRoutes(TestCase):

    def setUp(self):
        self.client = TestAsyncClient(app._router)

    # setting up the client with headers and cookies
    # def setUp(self):
    #     self.client = TestClient(
    #         router,
    #         headers={"Default-Header": "value"},
    #         COOKIES={"session": "test-session"}
    #     )
    @pytest.mark.asyncio
    async def test_query_endpoint(self):
        query_data = {"query": "test query"}
        

        print(self.client)
        response = await self.client.post(
            "/query/simple",
            json=query_data
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("msg", response.json())

    @pytest.mark.asyncio
    async def test_storage_endpoint(self):
        # Create a dummy file for testing
        file_content = b"Test content for file"
        test_file = SimpleUploadedFile(
            "test.txt",
            file_content,
            content_type="text/plain"
        )

        # Django Ninja's TestAsyncClient might require files to be in a specific tuple format
        files = {
            "file": ("test.txt", file_content, "text/plain")
        }

        # Use files parameter for file upload
        response = await self.client.post(
            "/storage/chromadb-storage-ephemeral",
            files=files  # Ensuring file is structured for multipart/form-data
        )
        
        # Verify response
        print(response.status_code)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"msg": "ok"})

    # # Example of testing with headers
    # def test_query_with_auth_header(self):
    #     query_data = {"query": "test query"}
        
    #     response = self.client.post(
    #         "/query/simple",
    #         json=query_data,
    #         headers={"Authorization": "Bearer test-token"}
    #     )
        
    #     self.assertEqual(response.status_code, 200)