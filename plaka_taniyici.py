import time

class TuringMachinePlateRecognizer:
    def __init__(self, input_string):
        # Uzunluk denetimi için bandın sonuna boşluk (_) karakteri ekliyoruz.
        self.tape = list(input_string) + ['_']
        self.head = 0
        self.state = 'q0'
        self.step_count = 0
        self.transitions = {}
        self._generate_transition_matrix()

    def _generate_transition_matrix(self):
        """
        Geçiş Fonksiyonları (Transition Matrix)
        Dil Formatı: NNLLNNN (N: Rakam, L: Büyük Harf)
        Format: self.transitions[(mevcut_durum, okunan_kategori)] = (yeni_durum, yön)
        """
        # q0: 1. Karakter (Rakam bekleniyor)
        self.transitions[('q0', 'digit')] = ('q1', 'R')
        
        # q1: 2. Karakter (Rakam bekleniyor)
        self.transitions[('q1', 'digit')] = ('q2', 'R')
        
        # q2: 3. Karakter (Büyük Harf bekleniyor)
        self.transitions[('q2', 'upper_alpha')] = ('q3', 'R')
        
        # q3: 4. Karakter (Büyük Harf bekleniyor)
        self.transitions[('q3', 'upper_alpha')] = ('q4', 'R')
        
        # q4: 5. Karakter (Rakam bekleniyor)
        self.transitions[('q4', 'digit')] = ('q5', 'R')
        
        # q5: 6. Karakter (Rakam bekleniyor)
        self.transitions[('q5', 'digit')] = ('q6', 'R')
        
        # q6: 7. Karakter (Rakam bekleniyor)
        self.transitions[('q6', 'digit')] = ('q7', 'R')
        
        # q7: 8. Karakter (Bandın sonu '_' olmalı. Uzunluk tam 7 ise kabul et)
        self.transitions[('q7', 'blank')] = ('q_accept', 'R')

    def get_char_category(self, char):
        if char == '_':
            return 'blank'
        elif char.isdigit():
            return 'digit'
        elif char.isupper() and char.isalpha():
            return 'upper_alpha'
        else:
            return 'invalid' # Küçük harfler, semboller vb.

    def run_step(self):
        # Kafa bant dışına çıkarsa güvenlik durdurması
        if self.head >= len(self.tape):
            self.state = 'q_reject'
            return False

        current_symbol = self.tape[self.head]
        category = self.get_char_category(current_symbol)
        
        state_key = (self.state, category)

        # Eğer okunan karakterin mevcut durum için bir kuralı varsa ilerle
        if state_key in self.transitions:
            next_state, direction = self.transitions[state_key]
            
            self.display_step(current_symbol, direction)
            
            self.state = next_state
            if direction == 'R':
                self.head += 1
            elif direction == 'L':
                self.head -= 1
                
            self.step_count += 1
            return True
        else:
            # Beklenmeyen bir karakter geldiyse doğrudan RED durumuna geç, kafayı sabit tut (N)
            self.display_step(current_symbol, 'N')
            self.state = 'q_reject'
            return False

    def display_step(self, read_sym, direction):
        tape_visual = "".join(self.tape)
        pointer = " " * self.head + "^"
        print(f"Adım {self.step_count:02d} | Durum: {self.state:<10} | Okunan: {read_sym:<2} | Yön: {direction}")
        print(f"Bant:  {tape_visual}")
        print(f"Kafa:  {pointer}")
        print("-" * 55)

# === ANA PROGRAM AKIŞI (İNTERAKTİF KULLANIM) ===
if __name__ == "__main__":
    print("=" * 55)
    print(" TURING MAKİNESİ - ARAÇ PLAKA FORMAT TANIYICI")
    print("=" * 55)
    
    user_input = input("Test edilecek plakayı giriniz (Örn: 55AB123): ").strip()
    
    if not user_input:
        print("\n[HATA] Boş girdi algılandı! Program sonlandırılıyor.")
    else:
        print(f"\nSimülasyon Başlatılıyor... Girdi: {user_input}\n" + "-" * 55)
        
        tm = TuringMachinePlateRecognizer(user_input)
        
        # Otomat döngüsünü işletme
        is_running = True
        while is_running and tm.state not in ['q_accept', 'q_reject']:
            is_running = tm.run_step()
            
        print("\n" + "=" * 55)
        if tm.state == 'q_accept':
            print(" SONUÇ: KABUL (Plaka formatı ve uzunluğu tamamen geçerli)")
        else:
            print(" SONUÇ: RED (Plaka formatı veya uzunluğu geçersiz!)")
        print("=" * 55)