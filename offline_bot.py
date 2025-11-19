from fuzzywuzzy import process
import random
from datetime import datetime

class OfflineChatbot:
    def __init__(self):
        # Knowledge base: patterns and responses
        self.knowledge_base = {
            "hello": ["Halo! Ada yang bisa saya bantu?", "Hai! Senang bertemu denganmu.", "Halo! Apa kabar?"],
            "hi": ["Hai!", "Halo!", "Hi there!"],
            "siapa kamu": ["Saya adalah chatbot offline sederhana.", "Saya asisten virtual Anda yang berjalan tanpa internet."],
            "apa kabar": ["Saya baik-baik saja, terima kasih!", "Kabar baik! Bagaimana dengan Anda?"],
            "jam berapa": [self._get_time],
            "tanggal berapa": [self._get_date],
            "bantuan": ["Saya bisa menjawab pertanyaan sederhana. Coba tanya 'jam berapa' atau sapa saya."],
            "terima kasih": ["Sama-sama!", "Senang bisa membantu.", "Kembali kasih!"],
            "bye": ["Sampai jumpa!", "Dadah!", "Semoga harimu menyenangkan!"],
            "nama kamu": ["Panggil saja saya Bot.", "Saya belum punya nama resmi, tapi Anda bisa panggil saya Bot."],
            "bodoh": ["Maaf jika saya tidak mengerti. Saya masih belajar.", "Saya hanya program komputer, harap maklum."],
            "pintar": ["Terima kasih! Saya berusaha sebaik mungkin.", "Wah, Anda terlalu memuji."],
        }
        
        # Default responses when no match is found
        self.default_responses = [
            "Maaf, saya tidak mengerti maksud Anda.",
            "Bisa ulangi dengan kata-kata yang berbeda?",
            "Hmm, saya belum belajar tentang itu.",
            "Coba tanya 'bantuan' untuk melihat apa yang bisa saya lakukan."
        ]

    def _get_time(self):
        return f"Sekarang pukul {datetime.now().strftime('%H:%M')}."

    def _get_date(self):
        return f"Hari ini tanggal {datetime.now().strftime('%d %B %Y')}."

    def get_response(self, message: str) -> str:
        """
        Get a response for the given message using fuzzy matching.
        """
        message = message.lower().strip()
        
        # 1. Exact/Fuzzy Match
        # Get the best match from the keys in the knowledge base
        best_match, score = process.extractOne(message, self.knowledge_base.keys())
        
        # Threshold for accepting a match (e.g., 70%)
        if score > 70:
            responses = self.knowledge_base[best_match]
            response = random.choice(responses)
            
            # If the response is a function, call it
            if callable(response):
                return response()
            return response
            
        # 2. No match found
        return random.choice(self.default_responses)
