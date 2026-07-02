from typing import Dict, Any

class SearchSynonymClient:
    def optimize_query(self, user_query: str) -> Dict[str, Any]:
        synonyms = {
            "mobile": "phone",
            "laptop": "computer",
            "earbuds": "headphones",
            "genspark": "genpark"
        }
        words = user_query.lower().split()
        optimized = []
        corrections = {}
        for w in words:
            if w in synonyms:
                optimized.append(synonyms[w])
                corrections[w] = synonyms[w]
            else:
                optimized.append(w)
        return {
            "original_query": user_query,
            "optimized_query": " ".join(optimized),
            "corrections_made": corrections
        }
