import sys
import requests
import json

sys.stdout.reconfigure(encoding='utf-8')

BASE_URL = "http://localhost:8000"

print("--- 1. Testing GET /api/invoices ---")
res = requests.get(f"{BASE_URL}/api/invoices")
print("Status:", res.status_code)
data = res.json()
print("Invoices count:", data["count"])

print("\n--- 2. Testing POST /api/screen/INV-2026-002 (Offshore Shell - Invalid GSTIN) ---")
res = requests.post(f"{BASE_URL}/api/screen/INV-2026-002")
print("Status:", res.status_code)
dossier = res.json()
print("Verdict:", dossier["rule_results"]["verdict"])
print("GSTIN Valid:", dossier["rule_results"]["gstin_valid"])
print("Flags:", json.dumps(dossier["rule_results"]["flags"], indent=2))

print("\n--- 3. Testing POST /api/screen/INV-2026-001 (Tata Cloud Comms - Form 13 Exemption) ---")
res = requests.post(f"{BASE_URL}/api/screen/INV-2026-001")
print("Status:", res.status_code)
dossier_001 = res.json()
print("Verdict:", dossier_001["rule_results"]["verdict"])
print("Recalled precedents count:", len(dossier_001["recalled_precedents"]))

print("\n--- 4. Testing POST /api/retain (CA Override & Teach) ---")
retain_payload = {
    "invoice_id": "INV-2026-004",
    "vendor_name": "Kaveri Engineering",
    "title": "MSME Extended Credit Term Safe Harbor Exemption",
    "ruling_type": "MSME_CUSTOM_AGREEMENT",
    "summary": "CA Partner approved custom 55-day credit period with seasonal material supply clause under statutory safe harbor.",
    "legal_citation": "MSMED Act Section 15 & Income Tax Act Section 43B(h) Safe Harbor Circular 2026/04.",
    "statutory_code": "SEC_43BH_SAFE_HARBOR",
    "auditor_id": "CA-SENIOR-AUDITOR-01"
}
res = requests.post(f"{BASE_URL}/api/retain", json=retain_payload)
print("Status:", res.status_code)
retain_res = res.json()
print("Retain Success:", retain_res["success"])
print("Updated Invoice Status:", retain_res["updated_invoice"]["status"])

print("\n--- 5. Testing GET /api/metrics ---")
res = requests.get(f"{BASE_URL}/api/metrics")
print("Metrics:", res.json())
