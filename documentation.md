
# API Documentation

This section contains the documentation for all available endpoints in the Django Inventory Store backend server.

## Suppliers Management

### 1. Get All Suppliers
- **Endpoint**: `GET /suppliers/`
- **Description**: Fetch all suppliers. Optionally accepts a `page` query parameter to paginate results.
- **URL Parameters**:
    - `page` (optional): The page number for pagination.
- **Example Request**:
    ```sh
    GET http://localhost:8000/suppliers/
    ```
- **Example Response**:
    ```json
    {
        "count": 2,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": "6ac7a550-b82b-424f-a93e-9a86fc86db84",
                "mobile_number": "08084950385",
                "address": "",
                "other_contact_info": "",
                "items": [
                    {
                        "id": "e21a240d-ff0e-4cac-bfcc-ae4d50e36c16",
                        "name": "item 1",
                        "description": "description for item 1",
                        "price": "1000.00",
                        "created": "2024-06-12T16:31:29.277631Z"
                    },
                    {
                        "id": "8c743c13-7eb3-4688-99ef-a1c1e88a84cf",
                        "name": "item 2",
                        "description": "description for item 2",
                        "price": "5000.00",
                        "created": "2024-06-12T16:38:41.754062Z"
                    }
                ],
                "name": "Housing Supplies",
                "email": "house.supplies@example.com",
                "date_joined": "2024-06-12T16:23:57.371965Z"
            },
            {
                "id": "59cf51c8-23e8-41f0-bc97-60874ecb9ad9",
                "mobile_number": "+2348084950384",
                "address": "",
                "other_contact_info": "",
                "items": [
                    {
                        "id": "8c743c13-7eb3-4688-99ef-a1c1e88a84cf",
                        "name": "item 2",
                        "description": "description for item 2",
                        "price": "5000.00",
                        "created": "2024-06-12T16:38:41.754062Z"
                    }
                ],
                "name": "Micheal Supplies",
                "email": "michealsupplies@example.com",
                "date_joined": "2024-06-12T16:18:07.627485Z"
            }
        ]
    }
    ```

### 2. Create Supplier
- **Endpoint**: `POST /suppliers/`
- **Description**: Add a new supplier.
- **Request Body**:
    ```json
    {
        "name": "Base Supplies",
        "email": "basesupplies@example.com",
        "mobile_number": "+2348084050385",
        "address": "",
        "other_contact_info": ""
    }
    ```
- **Example Request**:
    ```sh
    POST http://localhost:8000/suppliers/
    ```
- **Example Response**:
    ```json
    {
        "id": "59cf51c8-23e8-41f0-bc97-60874ecb9ad9",
        "mobile_number": "+2348084950384",
        "address": "",
        "other_contact_info": "",
        "items": [],
        "name": "Micheal Supplies",
        "email": "michealsupplies@example.com",
        "date_joined": "2024-06-12T16:18:07.627485Z"
    }
    ```

### 3. Get Supplier by UUID
- **Endpoint**: `GET /suppliers/{uuid}/`
- **Description**: Get details of a specific supplier by their UUID.
- **URL Parameters**:
    - `uuid` (required): The UUID of the supplier.
- **Example Request**:
    ```sh
    GET http://localhost:8000/suppliers/6ac7a550-b82b-424f-a93e-9a86fc86db84/
    ```
- **Example Response**:
    ```json
    {
        "id": "6ac7a550-b82b-424f-a93e-9a86fc86db84",
        "mobile_number": "08084950385",
        "address": "",
        "other_contact_info": "",
        "items": [
            {
                "id": "e21a240d-ff0e-4cac-bfcc-ae4d50e36c16",
                "name": "item 1",
                "description": "description for item 1",
                "price": "1000.00",
                "created": "2024-06-12T16:31:29.277631Z"
            },
            {
                "id": "8c743c13-7eb3-4688-99ef-a1c1e88a84cf",
                "name": "item 2",
                "description": "description for item 2",
                "price": "5000.00",
                "created": "2024-06-12T16:38:41.754062Z"
            }
        ],
        "name": "Housing Supplies",
        "email": "house.supplies@example.com",
        "date_joined": "2024-06-12T16:23:57.371965Z"
    }
    ```

### 4. Update Supplier
- **Endpoint**: `PUT /suppliers/{uuid}/`
- **Description**: Update all details of a supplier by their UUID. All fields must be provided.
- **URL Parameters**:
    - `uuid` (required): The UUID of the supplier.
- **Request Body**:
    ```json
    {
        "name": "Housing Supplies",
        "email": "house.supplies@example.com",
        "mobile_number": "08084950385",
        "address": "Direction to my super address.",
        "other_contact_info": ""
    }
    ```
- **Example Request**:
    ```sh
    PUT http://localhost:8000/suppliers/6ac7a550-b82b-424f-a93e-9a86fc86db84/
    ```
- **Example Response**:
    ```json
    {
        "id": "6ac7a550-b82b-424f-a93e-9a86fc86db84",
        "mobile_number": "08084950385",
        "address": "Direction to my super address.",
        "other_contact_info": "",
        "items": [
            {
                "id": "e21a240d-ff0e-4cac-bfcc-ae4d50e36c16",
                "name": "item 1",
                "description": "description for item 1",
                "price": "1000.00",
                "created": "2024-06-12T16:31:29.277631Z"
            },
            {
                "id": "8c743c13-7eb3-4688-99ef-a1c1e88a84cf",
                "name": "item 2",
                "description": "description for item 2",
                "price": "5000.00",
                "created": "2024-06-12T16:38:41.754062Z"
            }
        ],
        "name": "Housing Supplies",
        "email": "house.supplies@example.com",
        "date_joined": "2024-06-12T16:23:57.371965Z"
    }
    ```

### 5. Update Supplier Partially
- **Endpoint**: `PATCH /suppliers/{uuid}/`
- **Description**: Partially update details of a supplier by their UUID. Only the provided fields will be updated.
- **URL Parameters**:
    - `uuid` (required): The UUID of the supplier.
- **Request Body**:
    ```json
    {
        "address": "Direction to my super patch address."
    }
    ```
- **Example Request**:
    ```sh
    PATCH http://localhost:8000/suppliers/6ac7a550-b82b-424f-a93e-9a86fc86db84/
    ```
- **Example Response**:
    ```json
    {
        "id": "6ac7a550-b82b-424f-a93e-9a86fc86db84",
        "mobile_number": "08084950385",
        "address": "Direction to my super patch address.",
        "other_contact_info": "",
        "items": [
            {
                "id": "e21a240d-ff0e-4cac-bfcc-ae4d50e36c16",
                "name": "item 1",
                "description": "description for item 1",
                "price": "1000"

.00",
                "created": "2024-06-12T16:31:29.277631Z"
            },
            {
                "id": "8c743c13-7eb3-4688-99ef-a1c1e88a84cf",
                "name": "item 2",
                "description": "description for item 2",
                "price": "5000.00",
                "created": "2024-06-12T16:38:41.754062Z"
            }
        ],
        "name": "Housing Supplies",
        "email": "house.supplies@example.com",
        "date_joined": "2024-06-12T16:23:57.371965Z"
    }
    ```

### 6. Delete Supplier
- **Endpoint**: `DELETE /suppliers/{uuid}/`
- **Description**: Remove a supplier by their UUID.
- **URL Parameters**:
    - `uuid` (required): The UUID of the supplier.
- **Example Request**:
    ```sh
    DELETE http://localhost:8000/suppliers/6ac7a550-b82b-424f-a93e-9a86fc86db84/
    ```
- **Example Response**: No content (204 status code).

---

## Inventory Management

### 1. Get All Inventory Items
- **Endpoint**: `GET /inventory/`
- **Description**: Fetch all inventory items. Optionally accepts a `page` query parameter to paginate results.
- **URL Parameters**:
    - `page` (optional): The page number for pagination.
- **Example Request**:
    ```sh
    GET http://localhost:8000/inventory/
    ```
- **Example Response**:
    ```json
    {
        "count": 2,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": "8c743c13-7eb3-4688-99ef-a1c1e88a84cf",
                "suppliers": [
                    {
                        "id": "59cf51c8-23e8-41f0-bc97-60874ecb9ad9",
                        "name": "Micheal Supplies",
                        "email": "michealsupplies@example.com",
                        "mobile_number": "+2348084950384",
                        "address": "",
                        "other_contact_info": "",
                        "date_joined": "2024-06-12T16:18:07.627485Z"
                    },
                    {
                        "id": "6ac7a550-b82b-424f-a93e-9a86fc86db84",
                        "name": "Housing Supplies",
                        "email": "house.supplies@example.com",
                        "mobile_number": "08084950385",
                        "address": "",
                        "other_contact_info": "",
                        "date_joined": "2024-06-12T16:23:57.371965Z"
                    }
                ],
                "price": "5000.00",
                "name": "item 2",
                "description": "description for item 2",
                "created": "2024-06-12T16:38:41.754062Z"
            },
            {
                "id": "e21a240d-ff0e-4cac-bfcc-ae4d50e36c16",
                "suppliers": [
                    {
                        "id": "6ac7a550-b82b-424f-a93e-9a86fc86db84",
                        "name": "Housing Supplies",
                        "email": "house.supplies@example.com",
                        "mobile_number": "08084950385",
                        "address": "",
                        "other_contact_info": "",
                        "date_joined": "2024-06-12T16:23:57.371965Z"
                    }
                ],
                "price": "1000.00",
                "name": "item 1",
                "description": "description for item 1",
                "created": "2024-06-12T16:31:29.277631Z"
            }
        ]
    }
    ```

### 2. Create Inventory Item
- **Endpoint**: `POST /inventory/`
- **Description**: Add a new item to the inventory.
- **Request Body**:
    ```json
    {
        "name": "item 2",
        "description": "description for item 2",
        "price": "5000",
        "supplier_ids": [
            "6ac7a550-b82b-424f-a93e-9a86fc86db84",
            "59cf51c8-23e8-41f0-bc97-60874ecb9ad9"
        ]
    }
    ```
- **Example Request**:
    ```sh
    POST http://localhost:8000/inventory/
    ```
- **Example Response**:
    ```json
    {
        "id": "8c743c13-7eb3-4688-99ef-a1c1e88a84cf",
        "suppliers": [
            {
                "id": "59cf51c8-23e8-41f0-bc97-60874ecb9ad9",
                "name": "Micheal Supplies",
                "email": "michealsupplies@example.com",
                "mobile_number": "+2348084950384",
                "address": "",
                "other_contact_info": "",
                "date_joined": "2024-06-12T16:18:07.627485Z"
            },
            {
                "id": "6ac7a550-b82b-424f-a93e-9a86fc86db84",
                "name": "Housing Supplies",
                "email": "house.supplies@example.com",
                "mobile_number": "08084950385",
                "address": "",
                "other_contact_info": "",
                "date_joined": "2024-06-12T16:23:57.371965Z"
            }
        ],
        "price": "5000.00",
        "name": "item 2",
        "description": "description for item 2",
        "created": "2024-06-12T16:38:41.754062Z"
    }
    ```

### 3. Get Inventory Item by UUID
- **Endpoint**: `GET /inventory/{uuid}/`
- **Description**: Get details of a specific inventory item by its UUID.
- **URL Parameters**:
    - `uuid` (required): The UUID of the inventory item.
- **Example Request**:
    ```sh
    GET http://localhost:8000/inventory/8c743c13-7eb3-4688-99ef-a1c1e88a84cf/
    ```
- **Example Response**:
    ```json
    {
        "id": "8c743c13-7eb3-4688-99ef-a1c1e88a84cf",
        "suppliers": [
            {
                "id": "59cf51c8-23e8-41f0-bc97-60874ecb9ad9",
                "name": "Micheal Supplies",
                "email": "michealsupplies@example.com",
                "mobile_number": "+2348084950384",
                "address": "",
                "other_contact_info": "",
                "date_joined": "2024-06-12T16:18:07.627485Z"
            },
            {
                "id": "6ac7a550-b82b-424f-a93e-9a86fc86db84",
                "name": "Housing Supplies",
                "email": "house.supplies@example.com",
                "mobile_number": "08084950385",
                "address": "Direction to my super patch address.",
                "other_contact_info": "",
                "date_joined": "2024-06-12T16:23:57.371965Z"
            }
        ],
        "price": "5000.00",
        "name": "item 2",
        "description": "description for item 2",
        "created": "2024-06-12T16:38:41.754062Z"
    }
    ```

### 4. Update Inventory Item
- **Endpoint**: `PUT /inventory/{uuid}/`
- **Description**: Update all details of an inventory item by its UUID. All fields must be provided.
- **URL Parameters**:
    - `uuid` (required): The UUID of the inventory item.
- **Request Body**:
    ```json
    {
        "name": "item 2",
        "description": "Modified description for item 2",
        "price": "20000",
        "supplier_ids": [
            "6ac7a550-b82b-424f-a93e-9a86fc86db84",
            "59cf51c8-23e8-41f0-bc97-60874ecb9ad9"
        ]
    }
    ```
- **Example Request**:
    ```sh
    PUT http://localhost:8000/inventory/8c743c13-7eb3-4688-99ef-a1c1e88a84cf/
    ```
- **Example Response**:
    ```json
    {
        "id": "8c743c13-7eb3-4688-99ef-a1c1e88a

84cf",
        "suppliers": [
            {
                "id": "59cf51c8-23e8-41f0-bc97-60874ecb9ad9",
                "name": "Micheal Supplies",
                "email": "michealsupplies@example.com",
                "mobile_number": "+2348084950384",
                "address": "",
                "other_contact_info": "",
                "date_joined": "2024-06-12T16:18:07.627485Z"
            },
            {
                "id": "6ac7a550-b82b-424f-a93e-9a86fc86db84",
                "name": "Housing Supplies",
                "email": "house.supplies@example.com",
                "mobile_number": "08084950385",
                "address": "Direction to my super patch address.",
                "other_contact_info": "",
                "date_joined": "2024-06-12T16:23:57.371965Z"
            }
        ],
        "price": "20000.00",
        "name": "item 2",
        "description": "Modified description for item 2",
        "created": "2024-06-12T16:38:41.754062Z"
    }
    ```

### 5. Update Inventory Item Partially
- **Endpoint**: `PATCH /inventory/{uuid}/`
- **Description**: Partially update details of an inventory item by its UUID. Only the provided fields will be updated.
- **URL Parameters**:
    - `uuid` (required): The UUID of the inventory item.
- **Request Body**:
    ```json
    {
        "description": "Patch modified description for item 2",
        "supplier_ids": [
            "6ac7a550-b82b-424f-a93e-9a86fc86db84",
            "59cf51c8-23e8-41f0-bc97-60874ecb9ad9",
            "44b21401-1552-4ae5-af85-f9567d959fa0"
        ]
    }
    ```
- **Example Request**:
    ```sh
    PATCH http://localhost:8000/inventory/8c743c13-7eb3-4688-99ef-a1c1e88a84cf/
    ```
- **Example Response**:
    ```json
    {
        "id": "8c743c13-7eb3-4688-99ef-a1c1e88a84cf",
        "suppliers": [
            {
                "id": "44b21401-1552-4ae5-af85-f9567d959fa0",
                "name": "Base Supplies",
                "email": "basesupplies@example.com",
                "mobile_number": "+2348084050385",
                "address": "",
                "other_contact_info": "",
                "date_joined": "2024-06-12T17:57:33.770020Z"
            },
            {
                "id": "59cf51c8-23e8-41f0-bc97-60874ecb9ad9",
                "name": "Micheal Supplies",
                "email": "michealsupplies@example.com",
                "mobile_number": "+2348084950384",
                "address": "",
                "other_contact_info": "",
                "date_joined": "2024-06-12T16:18:07.627485Z"
            },
            {
                "id": "6ac7a550-b82b-424f-a93e-9a86fc86db84",
                "name": "Housing Supplies",
                "email": "house.supplies@example.com",
                "mobile_number": "08084950385",
                "address": "Direction to my super patch address.",
                "other_contact_info": "",
                "date_joined": "2024-06-12T16:23:57.371965Z"
            }
        ],
        "price": "20000.00",
        "name": "item 2",
        "description": "Patch modified description for item 2",
        "created": "2024-06-12T16:38:41.754062Z"
    }
    ```

### 6. Delete Inventory Item
- **Endpoint**: `DELETE /inventory/{uuid}/`
- **Description**: Remove an item from the inventory by its UUID.
- **URL Parameters**:
    - `uuid` (required): The UUID of the inventory item.
- **Example Request**:
    ```sh
    DELETE http://localhost:8000/inventory/8c743c13-7eb3-4688-99ef-a1c1e88a84cf/
    ```
- **Example Response**: No content (204 status code).
