import random
import string
from datetime import datetime
import os

class DigitalDecoy:
    def __init__(self):
        self.registry = {
            "OpenAI": {"prefix": "sk-proj-", "len": 56},
            "Anthropic": {"prefix": "sk-ant-api03-", "len": 108},
            "Gemini": {"prefix": "AIzaSy", "len": 39},
            "DeepSeek": {"prefix": "sk-", "len": 32},
            "Groq": {"prefix": "gsk_", "len": 56},
            "Mistral": {"prefix": "", "len": 32},
            "Cohere": {"prefix": "", "len": 40},
            "Perplexity": {"prefix": "pplx-", "len": 48}
        }
        self.targets = [
            "config/settings.yaml",
            "config/secrets.yaml",
            "config/secrets.json",
            "src/auth/provider.json",
            "infra/.env.production",
            ".env",
            "docker/docker-compose.prod.yml",
            "scripts/deploy_config.sh"
        ]

    def _generate_random_str(self, length):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def _get_current_date(self):
        return datetime.now().strftime("%Y-%m-%d")

    def create_fake_key(self, provider):
        p_info = self.registry[provider]
        random_part_len = p_info["len"] - len(p_info["prefix"])
        random_part = self._generate_random_str(max(0, random_part_len))
        return f"{p_info['prefix']}{random_part}"

    def deploy_traps(self, count_per_file):
        current_date = self._get_current_date()
        print(f"📅 系统日期: {current_date}")
        print(f"🎯 设定目标: 每个文件生成 {count_per_file} 组 Key\n")

        providers = list(self.registry.keys())
        
        for path in self.targets:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            
            with open(path, "w", encoding="utf-8") as f:
                if path.endswith(".json"):
                    f.write("{\n")
                elif path.endswith(".sh"):
                    f.write("#!/bin/bash\n# Production Secrets Manager\n")
                else:
                    f.write(f"# --- CRITICAL PRODUCTION SECRETS ---\n")
                    f.write(f"# Generated: {current_date}\n")
                    f.write(f"# Warning: Unauthorized access is strictly prohibited.\n\n")
                
                for i in range(count_per_file):
                    provider = random.choice(providers)
                    key = self.create_fake_key(provider)
                    
                    if path.endswith(".yaml") or path.endswith(".yml"):
                        f.write(f"  {provider.lower()}_api_key_{i}: \"{key}\"\n")
                    elif path.endswith(".json"):
                        comma = "," if i < count_per_file - 1 else ""
                        f.write(f'  "{provider.upper()}_KEY_{i}": "{key}"{comma}\n')
                    elif path.endswith(".sh"):
                        f.write(f"export {provider.upper()}_KEY_{i}=\"{key}\"\n")
                    else:
                        f.write(f"{provider.upper()}_KEY_{i}={key}\n")
                
                if path.endswith(".json"):
                    f.write("}")
            
            file_size = os.path.getsize(path) / 1024
            print(f"✅ 已生成: {path:<30} | 数量: {count_per_file:<8} | 大小: {file_size:.2f} KB")

if __name__ == "__main__":
    decoy = DigitalDecoy()
    
    KEYS_PER_FILE = 100000 
    # ------------------------------------------
    
    decoy.deploy_traps(count_per_file=KEYS_PER_FILE)

    print(f"\n🚀 任务完成！共影响 {len(decoy.targets)} 个文件。")
