# MedConnect-Emergency-Healthcare-System
Listed directory core
Listed directory js
Searched for "threshold"
Searched for "const"
Viewed models.py:1-106
Viewed views.py:1-548
Viewed consumers.py:1-13
Viewed api-config.js:1-53

#### 🏥 MedConnect | The Clinical Emergency Infrastructure (v2.1)

**MedConnect** is a professional-grade, high-trust emergency healthcare platform designed to bridge the gap between patients and hospitals with clinical precision. This project moves beyond a simple "SOS app" into a full-scale clinical dispatch system with strict data protocols, real-time logistics, and HIPAA-compliant privacy layers.

---

### ⚡ Emergency Lifecycle & Logic Thresholds

Our system operates on a unique **Radially Expanding Dispatch (RED)** logic to ensure the fastest possible response times while optimizing hospital workload.

#### 1. SOS Radius Expansion Logic
When a user triggers an SOS, the backend does not ping every hospital in the database. Instead, it expands the search radius based on time elapsed to find the *closest* available care first:

| Time Elapsed | Search Radius | Clinical Priority |
| :--- | :--- | :--- |
| **0 - 5 Seconds** | **3 KM** | Primary Immediate Responders |
| **5 - 10 Seconds** | **6 KM** | Local Emergency Centers |
| **10 - 15 Seconds** | **9 KM** | Regional Hospitals |
| **15 - 20 Seconds** | **12 KM** | Specialized Trauma Centers |
| **> 20 Seconds** | **15 KM** (Max) | Wide-Net Emergency Broadcast |

#### 2. SOS State Machine
The system maintains a strict state machine to prevent data collisions:
*   **`SEARCHING`**: Rebroadcasts to hospitals within the current radius. User is locked from creating new requests.
*   **`ASSIGNED`**: A hospital has accepted. Private medical data (EHR) is decrypted/revealed to the specific provider.
*   **`RESOLVED`**: The clinical case is closed. The SOS is archived in the user's `Alert History`.

---

### 🛡️ Data Privacy & Compliance (HIPAA/ABDM)

MedConnect implements a **"Zero-Knowledge Dispatch"** protocol to protect Patient Identifiable Information (PII) during the critical search phase.

*   **Identity Masking**: While an SOS is in `SEARCHING` status, hospitals see the patient as **"Identity Protected (HIPAA)"** and the phone number is **"Hidden for Privacy"**.
*   **Selective Disclosure**: Full name, blood group, allergies, and contact details are **only revealed** to a hospital *after* they formally click "Accept Request," creating a legal audit trail.
*   **EHR Integrity**: Medical records (Allergies, Chronic Conditions) are stored in a structured format ready for ABDM (Ayushman Bharat Digital Mission) integration.

---

### 🚑 Advanced Clinical Features

#### 1. V2.0 Third-Party Victim Reporting
Users can report emergencies for others (e.g., a witness at a crash site).
*   **`is_for_self` Toggle**: If set to `false`, the system captures the victim's name, localized condition, and phone number separately from the caller's profile.
*   **Caller-Victim Mapping**: The hospital sees both the caller's location and the victim's immediate needs.

#### 2. Provider Command Center
*   **Real-time Ticker**: Uses WebSockets to stream inbound dispatches instantly without page refreshes.
*   **Bed Management**: Hospitals track `Total Beds` vs. `ICU Beds` to determine capacity for incoming trauma.
*   **Stabilization Workflows**: Electronic admission protocols once the patient reaches the facility.

---

### 🛠️ Technical Deep Dive

#### **The Backend (Django 5.1 + REST Framework)**
*   **Relational Mapping**: SQLite3 maintains complex relationships between `Users`, `Hospitals`, and `SOSRequests`.
*   **Real-time Layer**: `django-channels` provides the WebSocket infrastructure for the 15km broadcast net.
*   **Concurrency Control**: Uses `transaction.atomic()` and `select_for_update()` during hospital acceptance to ensure two hospitals cannot accept the same patient.

#### **The Frontend (Vanilla Engine)**
*   **No Framework Overload**: Built with pure HTML5/CSS3/JS for sub-second loading on low-bandwidth emergency connections.
*   **Geolocation Saturation**: Continually polls for high-accuracy GPS coordinates during an active SOS.
*   **Clinical UI**: Uses the **Inter** font family and a trust-based HSL color palette tailored for medical clarity.

---

### 📂 Detailed Directory Map

```text
├── medconnect_backend/
│   ├── core/
│   │   ├── models.py      # Schema for EHR, Hospitals, & SOS expansion
│   │   ├── views.py       # Logic for Radius Thresholds & HIPAA masking
│   │   ├── consumers.py   # WebSocket broadcast logic
│   │   └── routing.py     # Real-time URL patterns
├── user/
│   ├── sos.html           # High-stress emergency trigger interface
│   ├── dashboard.html     # Patient Health Hub (EHR)
│   └── contacts.html      # Emergency "Circle of Trust" management
├── hospital/
│   ├── dashboard.html     # Live trauma dispatch ticker
├── admin/                 # Provider onboarding & system audit
└── js/
    ├── api-config.js      # Self-healing API base URL discovery
    └── script.js          # Core UI animations & SOS polling logic
```

---

### 🚥 System Constants & Thresholds
*   **Max Active SOS**: 1 per user (prevents spam/confusion).
*   **Default Scale**: 1:1,000 (meters to KM conversion for radius logic).
*   **API Timeout**: 5000ms (configured for rapid failover between local/remote backends).
*   **UI Reveal Point**: 120px (standardized clinical dashboard scroll threshold).

---
*Developed by Devansh Kalwani for the MedConnect-Emergency-Healthcare-System.*
