# Vendor Management System

# Introduction

Vendor Management System using Django and Django REST Framework. This
system will handle vendor profiles, track purchase orders, and calculate vendor performance
metrics.

### Main features

* Vendor Profile Management
* Purchase Order Tracking
* Vendor Performance Evaluation

# Getting Started

1. **Prerequisites:**

   - Python (>=3.6)
2. **Setting Up Virtual Environment:**

   - Create a new virtual environment:
     ```bash
      python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
        venv\Scripts\activate
       ```
     - On macOS and Linux:
       ```bash
        source venv/bin/activate
       ```
3. **Installation:**

   - First clone the repository from Github and switch to the new directory:
     ```bash
      git clone https://github.com/shashank-1995/Vendor-Management-System.git
     ```
   - Install project dependencies:
     ```bash
      cd Vendor-Management-System/
     ```
   - change branch to master:
     ```bash
      git checkout master
     ```     
   - Install project dependencies:
     ```bash
      pip install -r requirements.txt
     ```
   - Then simply apply the migrations:
     ```bash
      python manage.py migrate
     ```
   - Create a superuser for API access
     ```bash
      python manage.py createsuperuser
     ```
   - You can now run the development server:
     ```bash
      python manage.py runserver
     ```
4. **API Documentaion:**

   - API postman collection is shared in this repository with name ""vendor-management-system-api-documentation.postman_collection""

   ## 1. GET API Token

   ### Detail:

    This API endpoint is used to fetch access tokens to access other API's.

   ### Request:


   - Method: POST
   - URL: [http://127.0.0.1:8000/api/token/](http://127.0.0.1:8000/api/token/)
   - Body: `{ "username": "dev", "password": "dev" }`

   ### Response:

   - Status: OK (200)
   - Body: `{ "refresh": "<refresh_token>", "access": "<access_token>" }`

   ## 2. Refresh Access Token

   ### Detail:

    This API endpoint is used to refresh access tokens.

   ### Request:

   - Method: POST
   - URL: [http://127.0.0.1:8000/api/token/refresh/](http://127.0.0.1:8000/api/token/refresh/)
   - Body: `{ "refresh": "<refresh_token>" }`

   ### Response:

   - Status: OK (200)
   - Body: `{ "access": "<access_token>" }`

   ## 3. LIST VENDORS

   ### Detail:

    This API endpoint is used to list vendor details.

   ### Request:

   - Method: GET
   - URL: [http://127.0.0.1:8000/api/vendors/?page=1](http://127.0.0.1:8000/api/vendors/?page=1)
   - Authentication:
   - Type: Bearer Token
   - Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0ODA2NzUzLCJpYXQiOjE3MTQ4MDU4NTMsImp0aSI6IjMwYzdkNWExMjBjMjRlZmQ4OGRkYzZkMjc1ZTIwYjg5IiwidXNlcl9pZCI6Mn0.Qdd0MvV4b1M1M1OmRb7UqdB0PWWfdQevKLWUA0FgACI

   ### Response:

   - Status: OK (200)
   - Body:

   ```json
   {
       "count": 900,
       "next": "http://127.0.0.1:8000/api/vendors/?page=2",
       "previous": null,
       "results": [
           {
               "id": 1,
               "created": "2024-05-04T06:30:48.533271Z",
               "updated": "2024-05-04T06:30:48.533363Z",
               "name": "Example Vendor",
               "contact_details": "contact@example.com",
               "address": "123 Example St, City, Country",
               "vendor_code": "VENDOR123",
               "on_time_delivery_rate": 0.95,
               "quality_rating_avg": 4.5,
               "average_response_time": 2.5,
               "fulfillment_rate": 0.98
           },

       ]
   }
   ```
   ## 4. CREATE VENDOR

   ### Detail:

    This API endpoint is used to create a vendor.

   ### Request:

   - Method: POST
   - URL: [http://127.0.0.1:8000/api/vendors/](http://127.0.0.1:8000/api/vendors/)
   - Authentication:
   - Type: Bearer Token
   - Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0ODA0OTI0LCJpYXQiOjE3MTQ4MDQwMjQsImp0aSI6IjRmMTVlYmUzMDUxNDQwZjE4M2NjMjFhYWI4Y2E1YzY4IiwidXNlcl9pZCI6Mn0.41HRSVjnhewD42yap1FZtBsn_bDLTpgi4E7J6IMp-YA
   - Body:

   ```json
   {
       "name": "Example Vendor",
       "contact_details": "contact@example.com",
       "address": "123 Example St, City, Country",
       "vendor_code": "VENDOR123",
       "on_time_delivery_rate": 0.95,
       "quality_rating_avg": 4.5,
       "average_response_time": 2.5,
       "fulfillment_rate": 0.98
   }
   ```
   ### Response:

   ```json
   {
       "id": 1,
       "created": "2024-05-04T06:30:48.533271Z",
       "updated": "2024-05-04T06:30:48.533363Z",
       "name": "Example Vendor",
       "contact_details": "contact@example.com",
       "address": "123 Example St, City, Country",
       "vendor_code": "VENDOR123",
       "on_time_delivery_rate": 0.95,
       "quality_rating_avg": 4.5,
       "average_response_time": 2.5,
       "fulfillment_rate": 0.98
   }
   ```
   ## 5. RETRIEVE VENDOR

   ### Detail:

    This API endpoint is used to retrieve vendor details uding vendor_id.

   ### Request:

   - Method: GET
   - URL: [http://127.0.0.1:8000/api/vendors/10](http://127.0.0.1:8000/api/vendors/10)
   - Authentication:
   - Type: Bearer Token
   - Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0ODA2NzUzLCJpYXQiOjE3MTQ4MDU4NTMsImp0aSI6IjMwYzdkNWExMjBjMjRlZmQ4OGRkYzZkMjc1ZTIwYjg5IiwidXNlcl9pZCI6Mn0.Qdd0MvV4b1M1M1OmRb7UqdB0PWWfdQevKLWUA0FgACI

   ### Response:

   - Status: OK (200)
   - Body:

   ```json
   {
       "id": 10,
       "created": "2024-05-04T06:41:19.490047Z",
       "updated": "2024-05-04T06:41:19.490053Z",
       "name": "SNccNpGuExCCdycbRkgF",
       "contact_details": "JtLpyXTjlPUNHRyRYcVu@example.com",
       "address": "QqNuIGjXtqkNRYgLWNpKDXXrSvfrgc, City, Country",
       "vendor_code": "VENDOR752",
       "on_time_delivery_rate": 0.8820169429019925,
       "quality_rating_avg": 4.751234131031381,
       "average_response_time": 2.060527682237158,
       "fulfillment_rate": 0.9957698817835712
   }
   ```
   ## 6. UPDATE VENDOR

   ### Detail:

    This API endpoint is used to update vendor details using vendor_id.

   ### Request:

   - Method: PUT
   - URL: [http://127.0.0.1:8000/api/vendors/10/](http://127.0.0.1:8000/api/vendors/10/)
   - Authentication:
   - Type: Bearer Token
   - Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0ODA2NzUzLCJpYXQiOjE3MTQ4MDU4NTMsImp0aSI6IjMwYzdkNWExMjBjMjRlZmQ4OGRkYzZkMjc1ZTIwYjg5IiwidXNlcl9pZCI6Mn0.Qdd0MvV4b1M1M1OmRb7UqdB0PWWfdQevKLWUA0FgACI
   - Body:

   ```json
   {
       "name": "Updated Vendor Name",
       "contact_details": "Updated Contact Details",
       "address": "Updated Address",
       "on_time_delivery_rate": 0.95,
       "quality_rating_avg": 4.5,
       "average_response_time": 5.2,
       "fulfillment_rate": 0.92,
       "vendor_code": "VENDR634"
   }
   ```
   ### Response:

   - Status: OK (200)
   - Body:

   ## 7. DELETE VENDOR

   ### Detail:

   This API endpoint is used to delete a vendor using vendor_id.

   ### Request:

   - Method: DELETE
   - URL: [http://127.0.0.1:8000/api/vendors/11/](http://127.0.0.1:8000/api/vendors/11/)
   - Authentication:
   - Type: Bearer Token
   - Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0ODA4NDMyLCJpYXQiOjE3MTQ4MDc1MzIsImp0aSI6ImQzNjJmMmVjZjZiYjRmODVhZGQ1ZGM1ZjZiZjZjMjhkIiwidXNlcl9pZCI6Mn0.5Ri6Q8eK0_85IzZRskgYnFv3Sj2Pv2f-reP6IE2mxwk

   ### Response:

   - Status: No Content (204)

   ## 8. CREATE PURCHASE ORDERS

   ### Detail:

   This API endpoint is used to create a new purchase order.

   ### Request:

   - Method: POST
   - URL: [http://localhost:8000/api/purchase_orders/](http://localhost:8000/api/purchase_orders/)
   - Authentication:
   - Type: Bearer Token
   - Token: Your Bearer Token
   - Headers:
   - Authorization: Bearer <your_access_token>
   - Content-Type: application/json
   - Body (raw JSON):

   ```json
   {
       "po_number": "PO-12345",
       "vendor": 1,
       "order_date": "2024-05-05T10:00:00Z",
       "delivery_date": "2024-05-10T10:00:00Z",
       "items": [
           {
               "name": "Item 1",
               "price": 10
           },
           {
               "name": "Item 2",
               "price": 20
           }
       ],
       "quantity": 50,
       "status": "Pending",
       "issue_date": "2024-05-04T10:00:00Z"
   }
   ```
   ### Response:

   - Status: OK (200)

   ```json
   {
       "id": 1352,
       "created": "2024-05-04T07:25:50.179827Z",
       "updated": "2024-05-04T07:25:50.179865Z",
       "po_number": "PO-12345",
       "order_date": "2024-05-05T10:00:00Z",
       "delivery_date": "2024-05-10T10:00:00Z",
       "items": [
           {
               "name": "Item 1",
               "price": 10
           },
           {
               "name": "Item 2",
               "price": 20
           }
       ],
       "quantity": 50,
       "status": "Pending",
       "quality_rating": null,
       "issue_date": "2024-05-04T10:00:00Z",
       "acknowledgment_date": null,
       "vendor": 1
   }
   ```
   ## 9. LIST PURCHASE ORDERS

   ### Detail:

   This API endpoint is used to list purchase orders.

    ### Request:
    - Method: GET
    - URL: [http://localhost:8000/api/purchase_orders/?page=2](http://localhost:8000/api/purchase_orders/?page=2)
    - Authentication:
    - Type: Bearer Token
    - Token: Your Bearer Token
    - Headers:
    - Authorization: Bearer <your_access_token>

    ### Response:
    - Status: OK (200)
    - Body (raw JSON):
    ```json
    {
        "count": 999,
        "next": "http://localhost:8000/api/purchase_orders/list/?page=3",
        "previous": "http://localhost:8000/api/purchase_orders/list/",
        "results": [
            {
                "id": 362,
                "created": "2024-05-04T07:21:46.963854Z",
                "updated": "2024-05-04T07:21:46.963860Z",
                "po_number": "PO-5639",
                "order_date": "2023-10-16T07:21:46.963795Z",
                "delivery_date": "2023-11-02T07:21:46.963795Z",
                "items": [
                    {
                        "name": "Item 0",
                        "price": 36
                    },
                    {
                        "name": "Item 1",
                        "price": 13
                    },
                    {
                        "name": "Item 2",
                        "price": 55
                    },
                    {
                        "name": "Item 3",
                        "price": 44
                    },
                    {
                        "name": "Item 4",
                        "price": 27
                    }
                ],
                "quantity": 32,
                "status": "In Progress",
                "quality_rating": null,
                "issue_date": "2023-10-13T07:21:46.963795Z",
                "acknowledgment_date": null,
                "vendor": 578
            },
        ]
    }
    ```
    ## 10. PURCHASE ORDERS BY VENDOR

    ### Detail:

    This API endpoint is used to list purchase order for any vendor.

    ### Request:
    - Method: GET
    - URL: [http://localhost:8000/api/purchase_orders/?vendor=818](http://localhost:8000/api/purchase_orders/?vendor=818)
    - Authentication:
    - Type: Bearer Token
    - Token: Your Bearer Token

    ### Response:
    - Status: OK (200)
    - Body (raw JSON):
    ```json
    {
        "count": 2,
        "next": null,
        "previous": null,
        "results": [
            {
            "id": 367,
            "created": "2024-05-04T07:21:46.970443Z",
            "updated": "2024-05-04T07:21:46.970450Z",
            "po_number": "PO-7368",
            "order_date": "2023-07-04T07:21:46.970384Z",
            "delivery_date": "2023-07-23T07:21:46.970384Z",
            "items": [
            {
            "name": "Item 0",
            "price": 3
            },
            {
            "name": "Item 1",
            "price": 23
            }
            ],
            "quantity": 80,
            "status": "Completed",
            "quality_rating": 2.325527326670778,
            "issue_date": "2023-07-02T07:21:46.970384Z",
            "acknowledgment_date": "2023-07-23T07:21:46.970384Z",
            "vendor": 818
        },
    ]
    }
    ```

    ## 11. RETRIEVE-PURCHASE-ORDER

    ### Detail:

    This API endpoint is used to list purchase order by po_id.

    ### Request:
    - Method: GET
    - URL: [http://localhost:8000/api/purchase_orders/367](http://localhost:8000/api/purchase_orders/367)
    - Authentication:
    - Type: Bearer Token
    - Token: Your Bearer Token

    ### Response:
    - Status: OK (200)
    ```json
    {
        "id": 367,
        "created": "2024-05-04T07:21:46.970443Z",
        "updated": "2024-05-04T07:21:46.970450Z",
        "po_number": "PO-7368",
        "order_date": "2023-07-04T07:21:46.970384Z",
        "delivery_date": "2023-07-23T07:21:46.970384Z",
        "items": [
            {
                "name": "Item 0",
                "price": 3
            },
            {
                "name": "Item 1",
                "price": 23
            }
        ],
        "quantity": 80,
        "status": "Completed",
        "quality_rating": 2.325527326670778,
        "issue_date": "2023-07-02T07:21:46.970384Z",
        "acknowledgment_date": "2023-07-23T07:21:46.970384Z",
        "vendor": 818
    }
    ```

    ## 12. DELETE-PURCHASE-ORDER

    ### Detail:

    This API endpoint is used to delete purchase order by po_id.

    ### Request:
    - Method: DELETE
    - URL: [http://localhost:8000/api/purchase_orders/368/](http://localhost:8000/api/purchase_orders/368/)
    - Authentication:
    - Type: Bearer Token
    - Token: Your Bearer Token

    ### Response:
    - Status: No Content (204)

    ## 13. UPDATE-PURCHASE-ORDER

    ### Detail:

    This API endpoint is used to update purchase order by po_id.

    ### Request:
    - Method: PUT
    - URL: [http://localhost:8000/api/purchase_orders/361/](http://localhost:8000/api/purchase_orders/361/)
    - Authentication:
    - Type: Bearer Token
    - Token: Your Bearer Token
    - Headers: None
    - Body:
    ```json
    {
        "po_number": "PO-912345",
        "vendor": 1,
        "order_date": "2024-05-05T10:00:00Z",
        "delivery_date": "2024-05-10T10:00:00Z",
        "items": [
            {
                "name": "Item 1",
                "price": 10
            },
            {
                "name": "Item 2",
                "price": 20
            }
        ],
        "quantity": 50,
        "status": "Completed",
        "issue_date": "2024-05-04T10:00:00Z",
        "acknowledgment_date": "2024-05-11T10:00:00Z"
    }
    ```
    ### Response:
    - Status: OK (200)
    ```json
    {
        "id": 361,
        "created": "2024-05-04T07:21:46.963129Z",
        "updated": "2024-05-04T07:58:59.072873Z",
        "po_number": "PO-912345",
        "order_date": "2024-05-05T10:00:00Z",
        "delivery_date": "2024-05-10T10:00:00Z",
        "items": [
            {
                "name": "Item 1",
                "price": 10
            },
            {
                "name": "Item 2",
                "price": 20
            }
        ],
        "quantity": 50,
        "status": "Completed",
        "quality_rating": null,
        "issue_date": "2024-05-04T10:00:00Z",
        "acknowledgment_date": "2024-05-11T10:00:00Z",
        "vendor": 1
    }

    ```
    ## 14. VENDOR-PERFORMANCE

    ### Detail:

    This API endpoint is used to get performance of any vendor using vendor_id.

    ### Request:
    - Method: GET
    - URL: [http://127.0.0.1:8000/api/vendors/110/performance/](http://127.0.0.1:8000/api/vendors/110/performance/)
    - Authentication:
    - Type: Bearer Token
    - Token: Your Bearer Token
    - Headers:
    - Authorization: Bearer your_access_token

    ### Response:
    - Status: OK (200)
    ```json
    {
        "on_time_delivery_rate": 0.9421962202723356,
        "quality_rating_avg": 3.4343122952481613,
        "average_response_time": 7.177848631442217,
        "fulfillment_rate": 0.8308475777962241
    }
    ```
    ## 15. ACKNOWLEDGE-PO

    ### Detail:

    This API endpoint is used to acknowledge vendor.

    ### Request:
    - Method: POST
    - URL: [http://127.0.0.1:8000/api/purchase_orders/810/acknowledge/](http://127.0.0.1:8000/api/purchase_orders/810/acknowledge/)
    - Authentication:
    - Type: Bearer Token
    - Token: Your Bearer Token
    - Headers:
    - Authorization: Bearer your_access_token

    ### Response:
    - Status: OK (200)
    - Body:
    ```json
    {
        "message": "Purchase order acknowledged successfully"
    }
    ```

    ## 16. VENDOR-PERFORMANCE-TRENDS
    ### Detail:

    This API endpoint is used to get vendor performance trends.

    ### Request:
    - Method: GET
    - URL: [http://127.0.0.1:8000/api/vendors/21/trend/](http://127.0.0.1:8000/api/vendors/21/trend/)
    - Authentication:
    - Type: Bearer Token
    - Token: Your Bearer Token
    - Headers: None

    ### Response:
    - Status: OK (200)
    - Body:
    ```json
    {
        "vendor_id": 21,
        "day_performance": {
            "on_time_delivery_rate": 0.48228493939226824,
            "quality_rating_avg": 3.3733123621387535,
            "average_response_time": 9,
            "fulfillment_rate": 0.15840634055974379
        },
        "week_performance": {
            "on_time_delivery_rate": null,
            "quality_rating_avg": null,
            "average_response_time": null,
            "fulfillment_rate": null
        },
        "month_performance": {
            "on_time_delivery_rate": null,
            "quality_rating_avg": null,
            "average_response_time": null,
            "fulfillment_rate": null
        }
    }
    ```

    ## Implemented Features

    ### a. BaseModel

    - **Description:**
    - Implemented a base model `BaseModel` serving as the foundation for other models.
    - Includes `created` and `updated` timestamps.
    - Utilizes a custom manager `BaseModelManager` for common operations.

    ### b. DEFAULT_AUTHENTICATION_CLASSES

    - **Description:**
    - Configured default authentication classes for the project's API views.

    ### c. Pagination of API Custom

    - **Description:**
    - Custom pagination for API views to manage large datasets efficiently.

    ### d. Signals for Calculating Metrics for Real-time Updates

    - **Description:**
    - Implemented signals to trigger calculations of metrics for real-time updates.

    ### e. Implementing Threading for Efficient Calculation

    - **Description:**
    - Utilized threading for efficient calculation of resource-intensive tasks.

    ### f. Backend Filter

    - **Description:**
    - Backend filters implemented for efficient data querying and filtering.

    ### g. Data Integrity: Division by Zero Handling

    - **Description:**
    - Error handling for division by zero scenarios to ensure data integrity.

    ### h. RESTful Principles in API Design

    - **Description:**
    - Followed RESTful principles in designing API endpoints for consistency and predictability.

    ### i. Django ORM for Database Interactions

    - **Description:**
    - Leveraged Django's ORM for standardized and efficient database interactions.

    ### j. PEP 8 Style Guidelines Adherence

    - **Description:**
    - Adherence to PEP 8 style guidelines for code consistency and readability.

    ### k. Proper Documentation

    - **Description:**
    - Comprehensive documentation provided for clarity and ease of use.

    ## Test Suite

    ### a. `./manage.py insert_dummy_vendor_data`

    - **Description:**
    - Command to insert dummy vendor data into the database for testing purposes.

    ### b. `./manage.py insert_dummy_purchase_order`

    - **Description:**
    - Command to insert dummy purchase orders into the database for testing scenarios.

    ### c. Utilization of API Documentation

    - **Description:**
    - Utilize the API documentation provided with this repository for testing API endpoints.
