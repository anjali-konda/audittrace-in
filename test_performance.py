import time
import requests

BASE_URL = "http://127.0.0.1:8000"

def test_single_screening():
    print("Testing single screening latency across invoices...")
    invoices = requests.get(f"{BASE_URL}/api/invoices").json()["invoices"]
    
    latencies = []
    for inv in invoices[:10]:
        t0 = time.perf_counter()
        res = requests.post(f"{BASE_URL}/api/screen/{inv['id']}")
        t1 = time.perf_counter()
        ms = (t1 - t0) * 1000
        latencies.append(ms)
        data = res.json()
        print(f"Invoice {inv['id']}: status={res.status_code}, verdict={data['rule_results']['verdict']}, time={ms:.2f}ms")
    
    avg_latency = sum(latencies) / len(latencies)
    print(f"\nAverage Single Screening Latency: {avg_latency:.2f}ms (Requirement: <300ms, target <50ms)")
    assert avg_latency < 300, f"Latency too high: {avg_latency}ms"

def test_batch_screening():
    print("\nTesting batch screening latency across all 35 invoices...")
    t0 = time.perf_counter()
    res = requests.post(f"{BASE_URL}/api/batch-screen")
    t1 = time.perf_counter()
    ms = (t1 - t0) * 1000
    data = res.json()
    print(f"Batch Screened {data['total_screened']} invoices in {ms:.2f}ms (Requirement: <200ms / 0.2s total)")
    assert ms < 200, f"Batch screening too slow: {ms}ms"

if __name__ == "__main__":
    test_single_screening()
    test_batch_screening()
