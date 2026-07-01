#!/usr/bin/env python3
"""
Classifier Agent
Phân loại topic → domain + capabilities
"""
import json
from pathlib import Path
from .config import CoreConfig


class Classifier:
    def __init__(self, project_dir=None):
        self.project_dir = Path(project_dir) if project_dir else CoreConfig.default_project_dir()
        self.domains = CoreConfig.DOMAINS
        self.capability_keywords = CoreConfig.CAPABILITY_KEYWORDS

    def classify(self, topic: str) -> dict:
        """
        Phân loại topic thành domain + capabilities
        Trả về: {domain, domain_label, capabilities, confidence, raw_topic}
        """
        print(f"\n🔍 Classifier: Analyzing '{topic}'")

        topic_lower = topic.lower()

        domain, domain_score = self._detect_domain(topic_lower)
        capabilities = self._detect_capabilities(topic_lower)

        result = {
            "raw_topic": topic,
            "domain": domain,
            "domain_label": self.domains[domain]["name"],
            "domain_style": self.domains[domain]["style"],
            "domain_pacing": self.domains[domain]["pacing"],
            "domain_tone": self.domains[domain]["tone"],
            "capabilities": capabilities,
            "confidence": domain_score,
        }

        self._save_classification(result)

        print(f"  Domain: {result['domain_label']} (score: {domain_score})")
        print(f"  Capabilities: {capabilities}")

        return result

    # ── Domain detection ─────────────────────────────────────

    def _detect_domain(self, topic_lower: str) -> tuple:
        """Phát hiện domain bằng keyword scoring"""
        scores = {}

        domain_keywords = {
            "documentary": [
                "documentary", "explore", "deep dive", "investigation",
                "true story", "real events", "explore the", "inside",
            ],
            "history": [
                "history", "ancient", "century", "era", "civilization",
                "war", "empire", "medieval", "revolution", "dynasty",
                "evolution of", "origins of", "rise and fall",
            ],
            "education": [
                "learn", "tutorial", "explained", "how to", "guide",
                "introduction to", "basics", "fundamentals", "course",
                "lesson", "understanding", "what is", "why",
            ],
            "horror": [
                "horror", "scary", "creepy", "terrifying", "haunted",
                "paranormal", "ghost", "demon", "curse", "nightmare",
                "dark", "mysterious", "unsolved",
            ],
            "marketing": [
                "product", "brand", "launch", "sale", "promotion",
                "advertisement", "commercial", "market", "customer",
                "startup", "business", "revenue", "growth hack",
            ],
        }

        for domain, keywords in domain_keywords.items():
            score = sum(1 for kw in keywords if kw in topic_lower)
            if score > 0:
                scores[domain] = score

        if not scores:
            return "education", 0.3

        best_domain = max(scores, key=scores.get)
        max_possible = len(domain_keywords[best_domain])
        confidence = min(round(scores[best_domain] / max_possible, 2), 1.0)

        return best_domain, confidence

    # ── Capability detection ──────────────────────────────────

    def _detect_capabilities(self, topic_lower: str) -> list:
        """Phát hiện capabilities cần thiết"""
        found = []
        for cap, keywords in self.capability_keywords.items():
            if any(kw in topic_lower for kw in keywords):
                found.append(cap)

        if not found:
            found = ["animation"]

        return found

    # ── Save ─────────────────────────────────────────────────

    def _save_classification(self, result: dict):
        meta_dir = self.project_dir / "metadata"
        meta_dir.mkdir(parents=True, exist_ok=True)

        with open(meta_dir / "classification.json", "w") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        print(f"  Saved to {meta_dir}/classification.json")


if __name__ == "__main__":
    classifier = Classifier("/home/ngovan960/Documents/remotion_ai_studio")

    tests = [
        "The History of Ancient Rome",
        "How to Learn Python Programming",
        "Top 10 Scary Ghost Stories",
        "Best Product Launch Strategy 2025",
        "Climate Change Documentary",
    ]

    for t in tests:
        r = classifier.classify(t)
        print(json.dumps(r, indent=2, ensure_ascii=False)[:300])
        print()
