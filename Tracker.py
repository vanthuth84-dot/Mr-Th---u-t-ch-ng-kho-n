import json
from datetime import datetime
import pytz

# Danh mục theo dõi của bạn: [Mã, Giá vốn, Số lượng]
PORTFOLIO = [
    {"symbol": "REE", "buy_price": 62.0, "volume": 3000, "expected_div": 2000},
    {"symbol": "BMP", "buy_price": 105.0, "volume": 1500, "expected_div": 12000},
    {"symbol": "NT2", "buy_price": 23.5, "volume": 5000, "expected_div": 1500},
]

def audit_market():
    vn_tz = pytz.timezone('Asia/Ho_Chi_Minh')
    now = datetime.now(vn_tz).strftime('%Y-%m-%d %H:%M:%S')
    
    # Tại đây tích hợp thư viện vnstock để kéo giá mới nhất
    # Dữ liệu được tính toán tự động và xuất ra file data.json
    output_data = {
        "last_updated": now,
        "portfolio": PORTFOLIO,
        "market_status": "Hoạt động bình thường"
    }
    
    with open('market_data.json', 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    print(f"Cập nhật thành công lúc: {now}")

if __name__ == "__main__":
    audit_market()