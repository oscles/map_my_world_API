# Map My World API

## Description

Map My World is a REST API built with FastAPI that allows users to explore and review different locations and categories around the world. The application offers an interactive map where users can discover new locations and receive recommendations based on specific categories such as restaurants, parks and museums.

## Main features

- Geographic location management with coordinates (latitude/longitude)
- Location categorization system
- Review system for locations and categories
- Intelligent recommender that suggests places not recently reviewed

## Technologies Used

- Python 3.13+
- FastAPI
- SQLModel (ORM)
- Poetry
- SQL Lite
- Pydantic for data validation
- Uvicorn as ASGI server

## Project Structure

```
map-my-world/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── commons/
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── entities/
│   │   └── repositories/
│   ├── infrastructure/
│   │   ├── __init__.py
│   │   ├── api/
│   │   |   ├── __init__.py
|   |   │   ├── routes/
|   |   │   │   ├── __init__.py
|   |   │   │   ├── locations.py
|   |   │   │   ├── categories.py
|   |   │   │   └── review.py
│   │   └── repositories/
│   ├── usecases/
│   │   ├── __init__.py
│   │   ├── location_usecase.py
│   │   ├── category_usecase.py
│   │   └── review_usecase.py
├── pyproject.toml
└── README.md
    ...
```

## Data Models

### Location

```python
class Location:
    id: int
    latitude: float
    longitude: float
    created_at: datetime
```

### Category

```python
class Category:
    id: int
    name: str
    description: str
    created_at: datetime
```

### LocationCategoryReviewed

```python
class LocationCategoryReviewed:
    id: int
    location_id: int
    category_id: int
    reviewed_at: datetime
```

## API Endpoints

### Location

- `GET /locations`: Get list of locations
- `POST /locations`: Create new location

### Category

- `GET /categories`: Get list of categories
- `POST /categories`: Create new category

### Recommendations

- `GET /recommendations`: Get 10 recommendations of locations-categories not reviewed in the last 30 days

## Installation and Configuration

1. Clone repository:

```bash
git clone https://github.com/oscles/map-my-world.git
cd map-my-world
```

2. Create and activate virtual environment:

```bash
poetry install
```

3. Execute application:

```bash
poetry run uvicorn app.main:app --reload
```

## Documentation API

Once the server is running, you can access:

- Swagger UI Documentation: `http://localhost:8000/docs`
- ReDoc documentation: `http://localhost:8000/redoc`

## Using the Recommender

The recommender system prioritizes:

1. locations that have never been reviewed 2.
2. Locations that have not been reviewed in the last 30 days.
3. Returns maximum 10 recommendations per query.

Sample response:

```json
{
  "recommendations": [
    {
      "location_id": 1,
      "category_id": 3,
      "last_reviewed": null,
      "location": {
        "latitude": 40.7128,
        "longitude": -74.006
      },
      "category": {
        "name": "Restaurante",
        "description": "Establecimiento gastronómico"
      }
    }
  ]
}
```

## Contribution

1. Fork the repository
2. Create a branch for your feature (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
