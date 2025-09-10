# Greedy Algorithm

|         | Flour | Barley | Pulses | Saffron | Vanilla | Clove |
| ------- | ----- | ------ | ------ | ------- | ------- | ----- |
| weight  | 10    | 3      | 2      | 1       | 5       | 2     |
| Tot Val | 3     | 2      | 2      | 6       | 4       | 3     |

```json
"bag" = { 
        "Iteration 1" : {
            "content" : [],
            "weight" : "0kg",
            "value" : 0
        },
        "Iteration 2" : {
            "content" : ["saffron"],
            "weight" : "1kg",
            "value" : 6
        },
        "Iteration 2" : {
            "content" : ["saffron", "vanilla"],
            "weight" : "6kg",
            "value" : 10
        }
    }
```

## Methods to find the optimal solution
1. Add only the max valuable items
2. Find the ratio of `weight/value`
3. Find the `value/weight`