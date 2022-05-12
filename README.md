# Faustian

Faustian là công cụ tích hợp các công cụ phân tích lỗi hợp đồng thông minh, được xây dựng trong khóa luận tốt nghiệp đại học hệ chính quy Trường Đại học Công nghệ - Đại học Quốc gia Hà Nội.

## Tính năng
-   Kết hợp kết quả phân tích của các công cụ để đưa ra kết quả chính xác hơn.
-   Dễ dàng tích hợp các công cụ mới thông qua cấu hình file cấu hình YAML và docker image.
-   Thực thi các công cụ song song để giảm thời gian chạy.

## Requirement:
-   Unix-like system
-   [Docker](https://docs.docker.com/install)
-   [Python3](https://www.python.org)

## Cài đặt
1. Clone [repo Faustian](https://github.com/ultoxtung/Faustian):

HTTP:
```
git clone https://github.com/ultoxtung/Faustian.git
```

SSH:
```
git clone git@github.com:ultoxtung/Faustian.git
```

2. Cài đặt các thư viện Python:

```
pip3 install -r requirements.txt
```

## Sử dụng

Chạy lệnh:
```
python faustian.py <solidity-file>
```

File cấu hình của các công cụ phân tích được tích hợp được lưu trong thư mục `/config/`. Khi chạy, Faustian sẽ tự động phát hiện các file này và khởi chạy công cụ tương ứng. Kết quả phân tích của từng công cụ được lưu trong thư mục `/logs/`.

## Các công cụ được tích hợp sẵn

Hiện tại Faustian đang tích hợp sẵn 5 công cụ:
-   [Oyente](https://github.com/enzymefinance/oyente)
-   [Osiris](https://github.com/christoftorres/Osiris)
-   [HoneyBadger](https://github.com/christoftorres/HoneyBadger)
-   [Mythril](https://github.com/ConsenSys/mythril)
-   [SmartCheck](https://github.com/smartdec/smartcheck)

## Kết quả thử nghiệm

Thử nghiệm Faustian với 5 công cụ ở trên được tích hợp sẵn trên bộ dữ liệu [SB Curated](https://github.com/smartbugs/smartbugs/tree/master/dataset) thu được kết quả:

|  Category                 |    Oyente   |    Osiris   | HoneyBadger |   Mythril   | SmartCheck  |    Total    |
| ------------------------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| Reentrancy                | 20/31   65% | 20/31   65% |  1/31    3% | 20/31   65% | 19/31   61% | 23/31   74% |
| Access Control            |  0/18    0% |  0/18    0% |  0/18    0% |  4/18   22% |  2/18   11% |  4/18   22% |
| Arithmetic Issues         |  9/15   60% |  9/15   60% |  0/15    0% | 10/15   67% |  2/15   13% | 12/15   80% |
| Unchecked Low Level Calls |  0/52    0% |  0/52    0% |  0/52    0% | 23/52   44% | 22/52   42% | 25/52   48% |
| Denial of Service         |  0/6     0% |  0/6     0% |  0/6     0% |  0/6     0% |  0/6     0% |  0/6     0% |
| Bad Randomness            |  0/8     0% |  0/8     0% |  0/8     0% |  4/8    50% |  0/8     0% |  4/8    50% |
| Front Running             |  0/4     0% |  0/4     0% |  0/4     0% |  1/4    25% |  0/4     0% |  1/4    25% |
| Time Manipulation         |  0/5     0% |  0/5     0% |  0/5     0% |  0/5     0% |  1/5    20% |  1/5    20% |
| Short Address Attack      |  0/1     0% |  0/1     0% |  0/1     0% |  0/1     0% |  0/1     0% |  0/1     0% |
| Unknown Unknowns          |  0/3     0% |  0/3     0% |  2/3    67% |  0/3     0% |  0/3     0% |  2/3    67% |
| Total                     | 29/143  20% | 29/143  20% |  3/143   2% | 62/143  44% | 46/143  32% | 72/143  50% |