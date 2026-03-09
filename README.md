<div align="center">
<h1>𝔅𝔩𝔲𝔢 𝔓𝔯𝔬𝔱𝔬𝔠𝔬𝔩</h1>

✧ ——— Grass Finder Engine ——— ✧

Blue Protocol is a high-performance foraging API. It provides a secure infrastructure for identifying edible flora when the budget for a CS student's has reached absolute zero.
</div>

---

### Technical Dossier
* **Modern Tooling**: Managed by `uv` for lightning-fast dependency resolution and virtual environment isolation. Used `ruff` for linting and `bandit` for automated security scanning.
* **Secure Gatekeeping**: JWT-based authentication via `PyJWT` and `OAuth2PasswordBearer`.
* **Persistence**: Asynchronous SQLite integration using `SQLAlchemy 2.0` and `aiosqlite`.
* **Data Integrity**: Strict Pydantic V2 schemas with custom `AfterValidator` logic for cryptographic password strength.
* **Survival Logic**: Randomized recommendation engine for foraging "intel".

---

### Locked Endpoints
The following sectors require a valid Bearer Token:
- `POST /api/grass-finder/add` - Add new findings.
- `PATCH /api/grass-finder/update/{grass_id}` - Modify existing intel.
- `DELETE /api/grass-finder/delete/{grass_id}` - Erase the evidence.
- `GET /api/grass-finder/find/{grass_id}` - Seek sustenance.

### Public Endpoints
The following sectors are free to access without Bearer Token:
- `GET /api/grass-finder/find-random` - Seek (randomized) sustenance.
- `GET /api/grass-finder/mood` - See Ryo mood (don't ask why).

---

### Technical Setup

```bash
# Clone
git clone https://github.com/EternalHalve/blue-protocol.git
cd blue-protocol

# Create environment and sync dependencies
uv sync

# Setup .env
cp .env.example .env

# Awaken the engine
uv run fastapi dev
```
