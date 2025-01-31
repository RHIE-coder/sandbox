# designpattern

Describe your project here.

```mermaid
erDiagram
    CUSTOMER {
        string name
        string email
    }
    ORDER {
        int order_id
        string product
    }
    CUSTOMER ||--o| ORDER : places
```