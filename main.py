from engine import AnalystSLM, AuditorSLM
from streamer import universal_streamer

def run_medic_experiment():
    data_folder = "data"
    
    # 1. Auditor establishes Baseline (First 10,000 tokens across all files)
    print("--- 🩺 AuditorSLM: Establishing Baseline ---")
    baseline_counts = {}
    stream = universal_streamer(data_folder)
    for _ in range(50):
        try:
            token = next(stream)
            baseline_counts[token] = baseline_counts.get(token, 0) + 1
        except StopIteration:
            break
    
    total = sum(baseline_counts.values())
    baseline_dist = {k: v/total for k, v in baseline_counts.items()}

    # 2. Initialize Models
    analyst = AnalystSLM()
    auditor = AuditorSLM(baseline_dist)
    
    # 3. Processing Loop
    print("--- 🚀 AnalystSLM: Commencing Data Analysis ---")
    count = 0
    checkpoint = 5 # Adjusted for your current data size
    
    for token in universal_streamer(data_folder):
        analyst.process(token)
        count += 1
        
        if count % checkpoint == 0:
            summary = analyst.get_summary()
            bias = auditor.check_for_bias(summary)
            
            print(f"\n[Volume: {count} tokens] | Bias Score: {bias:.6f}")
            for item, weight in summary:
                print(f" - Summary Point: {item} | {analyst.justify(item)}")

if __name__ == "__main__":
    run_medic_experiment()
