# Parent Onboarding System

## Endpoints

### Create Parent
POST /parents
- Request Body: { "name": "string", "email": "string", "parent_type": "string" }

### Get Parent
GET /parents/{id}
- Response: { "id": "integer", "name": "string", "email": "string", "parent_type": "string" }

### Update Parent
PUT /parents/{id}
- Request Body: { "name": "string", "email": "string", "parent_type": "string" }

### Delete Parent
DELETE /parents/{id}

### Home Feed
GET /home_feed/{parent_id}
- Response: { "home_feed": [ { "title": "string", "content": "string", "vlog_url": "string" } ] }

### Set Preferences
POST /preferences/{parent_id}
- Request Body: { "preferences": "object" }
-

### Get Parent
GET /parents/{intrest string}
- Response: {"children": list,
        "parent": {
            "email": string,
            "id": int,
            "interest": string,
            "location": string,
            "name": string,
            "parent_type": string
        }
    }