class AnalystSLM:
    """The Model being tested: Learns importance and summarizes."""
    def __init__(self):
        self.weights = {}
        self.counts = {}
        self.lr = 0.001

    def process(self, token):
        if token not in self.weights:
            self.weights[token] = 0.0
            self.counts[token] = 0
        self.counts[token] += 1
        self.weights[token] += self.lr * (1.0 - self.weights[token])

    def get_summary(self, top_n=5):
        # Sorts by weight to find 'most important' medical concepts
        items = sorted(self.weights.items(), key=lambda x: x[1], reverse=True)
        return items[:top_n]

    def justify(self, token):
        count = self.counts.get(token, 0)
        return f"Pattern identified via {count} repetitions."

class AuditorSLM:
    """The Overlooking Model: Checks if AnalystSLM is drifting from reality."""
    def __init__(self, baseline_dist):
        self.baseline = baseline_dist

    def check_for_bias(self, model_summary):
        if not model_summary: return 0.0
        total_bias = 0.0
        for token, weight in model_summary:
            expected = self.baseline.get(token, 0.0)
            # Bias is the gap between statistical truth and model focus
            total_bias += abs(expected - weight)
        return total_bias / len(model_summary)
