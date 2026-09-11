## Data Detective Challenge - My Answers

My solutions for Round 1-6 based on the e-commerce dataset analysis

---

## Round 1 - Evidence Hunt

> **Round 1 Goal:**

### **Question 1: Influential Orders & Impact**

 Look at **Task B1 (Histogram)** and **Task A2 (Summary Statistics)** .

The histogram (B1) clearly shows that most orders cluster between ₹650 and ₹15,000, but there are a few massive outliers—particularly one order at ₹85,000. This single order could strongly influence the average.

**If we removed the big orders (say, anything >₹40,000):**

- **Average Order_Value would drop significantly** — The current mean is probably ₹15,000–20,000, but without these few large orders, it might drop to ₹8,000–10,000 
- **The histogram shape would change from right-skewed to nearly normal** — Right now, the right tail stretches far. Without it, the distribution would be more symmetric
- **Total profit would drop sharply** — One ₹85,000 order generates ₹14,000+ profit alone; lose that and total profit drops by 10–15%
- The story changes: We'd shift from "We serve corporate with massive orders AND small consumers" to "We're mostly a small-order business"

Why this matters: These outliers don't represent "typical" customers—they're the corporate bulk buyers. If we base decisions (like inventory or staffing) on the mean including outliers, we'll be unprepared for the average consumer order.

Graph Reference:
- Histogram (B1): See the tall bar on the right around ₹80,000–85,000
- Summary stats (A2): Compare mean vs. median in the `describe()` output. If mean is much higher than median, outliers are pulling it up

---

### **Question 2: Visually Strong but Numerically Weak Pattern**

 Look at **Task B2 (Scatter Plot: Discount vs Profit)** and later compare to **Task C6 (Correlation Heatmap)**.

In the scatter plot (B2), there's a _visual_ pattern: dots with 0% discount cluster at high profit, while dots with high discounts scatter lower. It _looks_ like a strong downward trend.

But when you check the actual correlation in the Heatmap (C6), it's only **-0.52**, which is moderate, not strong.


**Graph References:**
- **Scatter Plot (B2)**: Visual downward trend (looks strong)
- **Correlation Heatmap (C6)**: Actual strength (-0.52, moderate)
- **Pairplot (C5)**: When colored by Value_Tier, you can see that low-discount AND high-discount orders both cluster at high profit when order value is large

---

### **Question 3: Confounding Variable (Simpson's Paradox)**

Look at **Task B2 (Scatter: Discount vs Profit)**, then **Task C4 (Pivot Heatmap)**, then **Task C5 (Pairplot)**.

The confounding variable is **Order_Value** (or equivalently, **Customer_Segment** or **Product_Category**, which correlate with Order_Value).

**Here's how it creates a misleading relationship:**

1. **Big orders get bigger discounts** (because corporate customers negotiate better deals)
   - Example: Corporate-Furniture order = ₹80,000 order value with 8% discount
2. **Big orders also make bigger absolute profits** (even with discounts)
   - Same order: ₹80,000 × 11% margin = ₹9,000 profit
     (Prediction Before Calculation)\*\*

**Prediction:** **Order_Value** will have the strongest relationship with Profit. Direction: **POSITIVE** (higher order value → higher profit).


---

### **Question 4: Strongest Predictor of Profit**
## look at task c3  Swarm Plot 
Before calculating anything, I predicted that **Order_Value** would be the strongest predictor.

My reasoning:

- The regression line between Order_Value and Profit is basically a straight line—super clean
- It makes sense logically—profit is usually some percentage of order value
- Other variables like Discount and Delivery_Days have a lot more noise around them
- When I looked at the pairplot, Order_Value seemed to separate the data best

**Turns out I was right:** The correlation is 0.99, which is basically perfect. Order_Value definitely drives profit.

---

###### Round 2 - Competing Interpretation
#### Question 5 : "  Higher discounts destroy profit vs  Unprofitable products simply receive higher discounts."
## look at B2 scatter graph
We can say this in simple words:

 **The scatter plot supports both explanations to some extent.**
 For the first analyst, we can see that when the **discount increases, profit generally decreases**. At 0% discount, there are several products with very high profits, while at 15–25% discount, profits are mostly close to zero. This suggests that **higher discounts may reduce profit**.

 However, the second analyst could also be correct. The plot only shows **correlation, not causation**. It may be that products that are already **low-profit or difficult to sell are given higher discounts** to attract customers. In that case, low profit is causing higher discounts rather than discounts causing low profit.

 **To distinguish between the two explanations**, we need additional evidence such as the product's profit **before and after a discount change**, or compare similar products where some received higher discounts and others did not. Category-wise analysis would also help: if the negative discount–profit relationship remains within each category, it is stronger evidence that discounts are hurting profit. If high discounts are mainly concentrated in categories/products that were already unprofitable, that supports the second explanation.

 **Therefore, the scatter plot shows a strong negative relationship, but by itself it cannot prove that discounts cause lower profit.**
