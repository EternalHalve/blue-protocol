<div align="center">
<h1>𝔅𝔩𝔲𝔢 𝔓𝔯𝔬𝔱𝔬𝔠𝔬𝔩</h1>

✧ ——— [View Visual Asset](docs/images/blue_protocol.png) ——— ✧

<p>
Blue Protocol is a high-performance foraging API. It provides a secure infrastructure for identifying edible flora when the budget for a CS student's has reached absolute zero.
</p>
</div>

---

### Technical Dossier
* **Modern Tooling**: Managed by `uv` for lightning-fast dependency resolution and virtual environment isolation. Used `ruff` for linting and `bandit` for automated security scanning.
* **Secure Gatekeeping**: JWT-based authentication vsa `PyJWT` and `OAuth2PasswordBearer`.
* **Database**: Asynchronous SQLite integration using `SQLAlchemy 2.0` and `aiosqlite`.
* **Data Integrity**: Strict Pydantic V2 schemas with custom `AfterValidator` logic for cryptographic password strength.

---

### Locked Endpoints
The following sectors require a valid Bearer Token:
- `POST /api/grass-finder/add` - Add new findings.
- `PATCH /api/grass-finder/update/{grass_id}` - Modify existing intel.
- `DELETE /api/grass-finder/delete/{grass_id}` - Erase the evidence.
- `GET /api/grass-finder/find/{grass_id}` - Seek sustenance.
- `GET /api/user/me` - Look into the mirror.
- `PATCH /api/user/me` - Reborn anew.
- `DELETE /api/user/me` - Delete yourself from existence.

### Public Endpoints
The following sectors are free to access without Bearer Token:
- `POST /api/auth/register` - Enlist for clearance.
- `POST /api/auth/login` - Establish secure uplink.
- `GET /api/grass-finder/find-random` - Seek (randomized) sustenance.

---

### The Philosophy
Critics may question the lack of individual ownership in the grass-finder sector. In Blue Protocol, we implement Unowned Shared Stewardship:
- **The Underscore (`_user`)**: We verify the existence of a soul (via JWT), but we do not tether the grass to it. The `_user` is a ghost in the machine—required for the gate to open, but irrelevant to the harvest.
- **Proof of Presence**: Requiring authentication for "public" grass isn't about ownership; it's a Sybil-defense mechanism. If you want to delete the intel, you must at least have the dignity to register an uplink.
- **The Commons**: Grass belongs to the earth. If it's edible, it's yours. If it's gone, it's everyone's problem. We track the what and the where, never the who.

> For a detailed breakdown of the **Stateless Stewardship** pattern and the implementation of the `_user` ghost dependency, see the [Full Architecture Directive](docs/ARCHITECTURE.md).

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

---

<p align="center">
<b>Notice:</b> <i>Blue Protocol is subject to the emotional whims of Ryo Yamada. 1/10 requests may result in total failures. Good luck.</i>
</p>