# initial data model

                    customers
                        │
                        │
                        ▼
                     orders
                    /      \
                   /        \
                  ▼          ▼
            order_items    payments
                 │
                 │
                 ▼
              products


customers
──────────────
customer_id PK
first_name
last_name
email
country
signup_date


products
──────────────
product_id PK
product_name
category
price


orders
──────────────
order_id PK
customer_id FK
order_date
status
total_amount


order_items
──────────────
order_item_id PK
order_id FK
product_id FK
quantity
unit_price


payments
──────────────
payment_id PK
order_id FK
payment_date
payment_method
amount
payment_status
