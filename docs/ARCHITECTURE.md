### 1. The Stateless Forager Philosophy
Traditional REST APIs focus on Resource Ownership. Blue Protocol focuses on Resource Availability.
In this system, data is treated as a "Common Good." We have deliberately decoupled the `User` from the `Grass`.
- **Logic**: A user must be authenticated to interact with the database (Security), but the database does not care which user performed the action (Anonymity).
- **Implementation**: The `_user: CurrentUser` dependency acts as a Gatekeeper, not a Locker. It ensures the request originates from a verified agent without staining the data with individual ownership.

---

### 2. Data Flow
The system operates on a "High-Trust, High-Risk" model.
- **Uplink**: Client requests a JWT via `/auth/login`.
- **Verification**: The `ryo_mood_guard` evaluates the request. If Ryo is in a foul mood, the request is discarded (10% failure rate).
- **Validation**: Pydantic V2 schemas enforce strict data integrity before the database is touched.
- **Execution**: Asynchronous SQLAlchemy 2.0 commits the findings to SQLite.

---

### 3. ERD (Mental Model)
| Entity | Relation    | Attribute                     |
|-------|-------------|-------------------------------|
| User  | Independent | Validates the session.       |
| Grass | Universal   | Exists for everyone.         |

Directive: If a user is deleted, the grass they found remains. The forage is more important than the forager.