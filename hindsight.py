import os
import time
import requests
from typing import List, Dict, Any

HINDSIGHT_API_KEY = os.getenv("HINDSIGHT_API_KEY", "hsk_8092e82718e72428310083547b206cc2_b6f88331078e15e3")
HINDSIGHT_BASE_URL = os.getenv("HINDSIGHT_BASE_URL", "https://api.hindsight.vectorize.io").rstrip("/")

INITIAL_PRECEDENTS: List[Dict[str, Any]] = [
    {
        "id": "mem-001",
        "vendor_name": "Tata Cloud Communications",
        "title": "Form 13 Low-TDS Certificate Exemption (Sec 197 / 194Q)",
        "ruling_type": "FORM_13_EXEMPTION",
        "summary": "Verified Form 13 certificate issued by Assessing Officer (AO Circle 4, Mumbai). Grants 0.0% lower TDS rate for Tata Cloud Communications under Section 194Q for aggregate annual billing up to ₹10,00,00,000.",
        "legal_citation": "CBDT Notification & Income Tax Act Sec 197 read with Sec 194Q. Certificate Ref: IT-AO-MUM-2026-F13-889.",
        "statutory_code": "SEC_194Q_FORM13",
        "auditor_id": "CA-SENIOR-AUDITOR-99",
        "timestamp": "2026-04-15T10:30:00Z",
        "status": "ACTIVE_APPROVED"
    },
    {
        "id": "mem-002",
        "vendor_name": "Apex Logistics Pvt Ltd",
        "title": "MSME 60-Day Payment Agreement Safe Harbor (Sec 43B(h))",
        "ruling_type": "MSME_CUSTOM_AGREEMENT",
        "summary": "Pre-approved bipartite logistics service contract with Apex Logistics Pvt Ltd. Clause 14.2 establishes a valid written 60-day settlement cycle with quarterly interest reconciliation under statutory safe harbor.",
        "legal_citation": "MSMED Act 2006 Section 15 & Income Tax Act Section 43B(h) Safe Harbor Circular.",
        "statutory_code": "SEC_43BH_SAFE_HARBOR",
        "auditor_id": "CA-PARTNER-42",
        "timestamp": "2026-05-20T14:15:00Z",
        "status": "ACTIVE_APPROVED"
    },
    {
        "id": "mem-003",
        "vendor_name": "Infosys BPM",
        "title": "Form 194J Reimbursement Voucher Exemption",
        "ruling_type": "REIMBURSEMENT_EXEMPTION",
        "summary": "Pure reimbursement voucher for cloud server hosting and pass-through software licenses supported by original third-party tax invoices without markup.",
        "legal_citation": "CBDT Circular No. 715: No TDS applicable on pure reimbursements under Section 194J or 194C.",
        "statutory_code": "SEC_194J_REIMBURSEMENT",
        "auditor_id": "CA-TAX-LEAD-07",
        "timestamp": "2026-06-01T09:00:00Z",
        "status": "ACTIVE_APPROVED"
    },
    {
        "id": "mem-004",
        "vendor_name": "Reliance Digital Retail",
        "title": "Routine Hardware Procurement Safe Harbor",
        "ruling_type": "ROUTINE_LOW_RISK",
        "summary": "Standard retail IT hardware purchases with immediate warranty invoice and standard 15-day commercial terms under ₹5,00,000 threshold.",
        "legal_citation": "Standard Commercial Statutory Guidelines.",
        "statutory_code": "ROUTINE_SAFE_HARBOR",
        "auditor_id": "SYSTEM_AUTO_RETAIN",
        "timestamp": "2026-01-10T11:00:00Z",
        "status": "ACTIVE_APPROVED"
    },
    {
        "id": "mem-005",
        "vendor_name": "L&T Heavy Engineering",
        "title": "Section 194C Infrastructure Sub-Contractor Safe Harbor",
        "ruling_type": "CONTRACTOR_SAFE_HARBOR",
        "summary": "Turnkey fabrication sub-contracting agreement covered by Form 26Q Section 194C statutory 2.0% TDS deduction with pre-cleared WHT ledger.",
        "legal_citation": "Section 194C Income Tax Act - Works Contract Guidelines.",
        "statutory_code": "SEC_194C_WORKS",
        "auditor_id": "CA-INFRA-HEAD-11",
        "timestamp": "2026-03-18T16:45:00Z",
        "status": "ACTIVE_APPROVED"
    },
    {
        "id": "mem-006",
        "vendor_name": "Wipro Digital Solutions",
        "title": "Section 194J Professional & Technical Fee Ruling",
        "ruling_type": "TECH_FEE_PRECEDENT",
        "summary": "Dedicated software engineering resource allocation covered by Section 194J 10% WHT with valid Nil-TDS certificate for offshore modules.",
        "legal_citation": "Section 194J(1)(ba) Income Tax Act.",
        "statutory_code": "SEC_194J_PROFESSIONAL",
        "auditor_id": "CA-TAX-PARTNER-03",
        "timestamp": "2026-07-11T12:30:00Z",
        "status": "ACTIVE_APPROVED"
    },
    {
        "id": "mem-007",
        "vendor_name": "Mahindra Logistics",
        "title": "Form 13 Low-TDS Certificate (0.5% Reduced Rate)",
        "ruling_type": "FORM_13_EXEMPTION",
        "summary": "Valid Lower Deduction Certificate issued by AO Ward 2(1) Pune. Grants 0.5% reduced TDS rate for Mahindra Logistics under Section 194C for FY 2026-27.",
        "legal_citation": "Income Tax Act Sec 197 Certificate #PUN-AO-2026-F13-332.",
        "statutory_code": "SEC_194C_FORM13",
        "auditor_id": "CA-LOGISTICS-AUDITOR",
        "timestamp": "2026-08-05T08:15:00Z",
        "status": "ACTIVE_APPROVED"
    },
    {
        "id": "mem-008",
        "vendor_name": "Amazon Web Services India",
        "title": "Cloud Services Sec 194O & Equalisation Levy Exemption",
        "ruling_type": "EQUALISATION_LEVY_EXEMPTION",
        "summary": "AWS India cloud hosting billed by Indian entity (AISPL) with GSTIN verification. Exempt from 2% Equalisation Levy under domestic TDS rules.",
        "legal_citation": "CBDT Clarification Circular on E-commerce Operator TDS u/s 194O.",
        "statutory_code": "SEC_194O_CLOUD",
        "auditor_id": "CA-TECH-AUDITOR-88",
        "timestamp": "2026-02-28T14:00:00Z",
        "status": "ACTIVE_APPROVED"
    },
    {
        "id": "mem-009",
        "vendor_name": "Sterling & Wilson Solar",
        "title": "Sec 194C Solar Turnkey EPC Exemption",
        "ruling_type": "EPC_CONTRACT_SAFE_HARBOR",
        "summary": "Turnkey solar EPC procurement agreement pre-screened under Section 194C with 1% lower WHT allocation.",
        "legal_citation": "CBDT Circular No. 687 on Turnkey Solar Installations.",
        "statutory_code": "SEC_194C_SOLAR",
        "auditor_id": "CA-ENERGY-LEAD",
        "timestamp": "2026-05-10T11:20:00Z",
        "status": "ACTIVE_APPROVED"
    },
    {
        "id": "mem-010",
        "vendor_name": "Sun Pharmaceutical Industries",
        "title": "R&D Active Ingredient Pass-Through Safe Harbor",
        "ruling_type": "PHARMA_RD_EXEMPTION",
        "summary": "Bulk Active Pharmaceutical Ingredient (API) supply agreement with pre-approved Form 13 0.0% TDS certificate.",
        "legal_citation": "Income Tax Act Sec 197 Certificate #MUM-AO-2026-F13-902.",
        "statutory_code": "SEC_194Q_PHARMA",
        "auditor_id": "CA-PHARMA-AUDITOR",
        "timestamp": "2026-06-14T09:30:00Z",
        "status": "ACTIVE_APPROVED"
    }
]

class HindsightMemoryClient:
    """Long-term Precedent Vector Memory Client."""

    def __init__(self, api_key: str = HINDSIGHT_API_KEY, base_url: str = HINDSIGHT_BASE_URL):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "X-API-Key": self.api_key,
            "Content-Type": "application/json",
            "User-Agent": "AuditTrace-IN/2.5"
        }
        self.memory_bank: List[Dict[str, Any]] = list(INITIAL_PRECEDENTS)

    def recall(self, query: str, vendor_name: str = "", sync_remote: bool = False) -> List[Dict[str, Any]]:
        recalled = []
        vendor_lower = vendor_name.lower() if vendor_name else ""
        query_lower = query.lower() if query else ""
        
        # Fast local precedent store search (<1ms)
        for mem in self.memory_bank:
            mem_vendor = mem.get("vendor_name", "").lower()
            mem_title = mem.get("title", "").lower()
            mem_summary = mem.get("summary", "").lower()
            
            if (vendor_lower and (vendor_lower in mem_vendor or mem_vendor in vendor_lower)) or \
               (query_lower and (query_lower in mem_title or query_lower in mem_summary or query_lower in mem_vendor)):
                if not any(r["title"] == mem["title"] for r in recalled):
                    recalled.append(mem)

        # Dispatch optional remote vector bank synchronization asynchronously (non-blocking)
        if sync_remote:
            def _async_sync():
                try:
                    url = f"{self.base_url}/v1/memories/recall"
                    payload = {"query": f"{vendor_name} {query}", "top_k": 5, "threshold": 0.65}
                    resp = requests.post(url, json=payload, headers=self.headers, timeout=1.5)
                    if resp.status_code == 200:
                        data = resp.json()
                        cloud_memories = data.get("memories", []) or data.get("results", [])
                        for m in cloud_memories:
                            m_title = m.get("title", "Recalled Precedent Ruling")
                            if not any(r["title"] == m_title for r in self.memory_bank):
                                self.memory_bank.append({
                                    "id": m.get("id", f"cloud-{time.time()}"),
                                    "vendor_name": m.get("vendor_name", vendor_name),
                                    "title": m_title,
                                    "ruling_type": m.get("ruling_type", "CA_RULING"),
                                    "summary": m.get("summary", m.get("text", "")),
                                    "legal_citation": m.get("legal_citation", "Precedent Memory Stored Ruling"),
                                    "status": "ACTIVE_APPROVED"
                                })
                except Exception:
                    pass

            import threading
            threading.Thread(target=_async_sync, daemon=True).start()

        return recalled

    def retain(self, memory_data: Dict[str, Any]) -> Dict[str, Any]:
        new_id = f"mem-{int(time.time()*1000)}"
        memory_record = {
            "id": new_id,
            "vendor_name": memory_data.get("vendor_name", "Unknown Vendor"),
            "title": memory_data.get("title", "CA Auditor Precedent Override"),
            "ruling_type": memory_data.get("ruling_type", "CA_OVERRIDE_PRECEDENT"),
            "summary": memory_data.get("summary", ""),
            "legal_citation": memory_data.get("legal_citation", "Income Tax Act / GST Statutory Precedent"),
            "statutory_code": memory_data.get("statutory_code", "CUSTOM_CA_RULING"),
            "auditor_id": memory_data.get("auditor_id", "CA-AUDITOR-LEAD"),
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "status": "ACTIVE_APPROVED"
        }

        self.memory_bank.insert(0, memory_record)

        cloud_synced = False
        try:
            url = f"{self.base_url}/v1/memories"
            payload = {
                "text": f"Precedent for {memory_record['vendor_name']}: {memory_record['title']}. {memory_record['summary']} Citation: {memory_record['legal_citation']}",
                "metadata": memory_record
            }
            resp = requests.post(url, json=payload, headers=self.headers, timeout=3.0)
            if resp.status_code in (200, 201):
                cloud_synced = True
        except Exception:
            cloud_synced = False

        return {
            "success": True,
            "memory": memory_record,
            "cloud_synced": cloud_synced,
            "total_precedents": len(self.memory_bank)
        }

    def reflect(self, invoice: Dict[str, Any], recalled_precedents: List[Dict[str, Any]], rule_results: Dict[str, Any]) -> Dict[str, Any]:
        verdict = rule_results["verdict"]
        has_precedent = len(recalled_precedents) > 0
        
        reflection_summary = ""
        if verdict == "AUTO_CLEARED_BY_PRECEDENT" and has_precedent:
            p = recalled_precedents[0]
            reflection_summary = f"Reflected against precedent '{p['title']}'. Hard statutory checks passed with pre-cleared CA authorization."
        elif verdict == "CRITICAL_TAX_ALERT":
            if not rule_results["gstin_valid"]:
                reflection_summary = "CRITICAL DRIFT ALERT: Vendor GSTIN checksum validation failed. Pattern indicates potential corporate spoofing / shell entity."
            elif rule_results["sec_43bh_breached"]:
                reflection_summary = "CRITICAL STATUTORY BREACH: MSME payment term exceeds 45 days. High tax disallowance risk under Section 43B(h)."
            else:
                reflection_summary = "CRITICAL ALERT: Statutory anomaly detected requiring immediate CFO / Tax Head escalation."
        elif verdict == "ESCALATE_TO_CA":
            reflection_summary = "ESCALATED TO CA: Section 194Q threshold (> ₹50 Lakhs) reached without active Form 13 exemption certificate on file."
        else:
            reflection_summary = "Routine transaction evaluated against standard statutory parameters."

        return {
            "verdict": verdict,
            "reflection_summary": reflection_summary,
            "precedent_count": len(recalled_precedents),
            "recalled_precedents": recalled_precedents
        }

hindsight_client = HindsightMemoryClient()
