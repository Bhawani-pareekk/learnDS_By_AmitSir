## Data Detective Challenge - My Answers

My solutions for Round 1-6 based on the e-commerce dataset analysis

---

## Round 1 - Evidence Hunt

### **Question 1: Influential Orders & Impact**

Looking at the histogram, I can see that most orders are pretty small (below ₹15,000), but then there are these few massive orders that stick out—like ₹85,000. These outliers really matter.

If we removed these big orders:

- The average would drop a lot (probably 15-20%)
- The histogram would look totally different—less skewed
- Total profit would take a big hit
- We'd basically go from "we get some huge corporate deals" to "we're just a regular small-order business"

The reason is simple—these outliers pull the whole average up. They're the ones making us look good on paper.

---

### **Question 2: Visually Strong but Numerically Weak Pattern**

In the discount vs. profit chart, it _looks_ like discounts are bad for profit—you can clearly see low-discount orders clustered at high profit. But when I check the actual numbers, the correlation is only -0.52, which isn't that strong.

Here's why it's not as dramatic as it looks:

- A correlation of -0.52 only explains about 27% of the profit change
- There's a lot of scatter—some 10% discount orders actually make more profit than some 0% discount orders
- It looks like a clear pattern, but it's actually pretty messy when you dig in
- Plus, Order_Value is probably influencing both (big orders get discounts AND make more profit)

---

### **Question 3: Confounding Variable**

The third variable messing up the relationship is **Order_Value**. Here's what's happening:

- Bigger orders get bigger discounts (because of negotiation power)
- But bigger orders also make bigger profits overall
- So when you just plot Discount vs. Profit, you're actually seeing two things at once:
  - The real effect: discounts actually hurt the profit margin
  - A hidden effect: large customers (who get discounts) make a lot of profit anyway
- The pairplot shows this clearly—when you color by Order_Value, the expensive orders bunch together at high profit AND high discount

To fix this, we'd need to either color the scatter plot by Order_Value or look at the data by category to separate out these effects.

---

### **Question 4: Strongest Predictor of Profit**

Before calculating anything, I predicted that **Order_Value** would be the strongest predictor.

My reasoning:

- The regression line between Order_Value and Profit is basically a straight line—super clean
- It makes sense logically—profit is usually some percentage of order value
- Other variables like Discount and Delivery_Days have a lot more noise around them
- When I looked at the pairplot, Order_Value seemed to separate the data best

**Turns out I was right:** The correlation is 0.99, which is basically perfect. Order_Value definitely drives profit.

---

## Round 2 - Competing Interpretations

### **Question 5: Do Discounts Destroy Profit or Do Bad Products Get Discounts?**

**Analyst A says:** Discounts destroy profit.

- The scatter plot clearly shows low-discount orders making more profit
- Correlation is -0.52, meaning each extra 5% discount costs us like ₹500-1000 in profit
- Profit margin gets hit even harder (correlation -0.84)
- Common sense—if we give less discount, we keep more money

**Analyst B says:** We give discounts to products that aren't selling well anyway.

- The heatmap shows Corporate-Furniture makes ₹9,325 with no discount, while Consumer-Books is low profit and has high discounts
- When you look at category, Electronics actually does well even with discounts in the corporate segment
- We probably discount because the product isn't competitive, not the other way around
- Different categories have different natural discount levels

**How to figure out who's right:**

1. Run an A/B test—give the same product two different prices and see what happens
2. Look at the timing—did we start discounting first, or did profit already drop?
3. Look at just one category and compare profit with vs. without discount
4. Use statistical regression and control for Order_Value and Category

**My take:** Both are kind of true. Discounts definitely hurt the profit margin on a per-order basis. But we're applying them to products that probably weren't that profitable anyway.

---

### **Question 6: Mean vs. Median - Which One Matters?**

Looking at Corporate-Furniture with a mean of ₹9,325—sounds good, right? But the violin plot shows something else entirely.

The data isn't evenly distributed. Some orders cluster near break-even (maybe even negative), while others make ₹8,000-14,000. That's actually two separate groups of orders, not one.

What I should report instead:

- The **median** is probably around ₹7,000-8,000—that's more representative than the mean
- The **IQR** (middle 50%) is probably around ₹4,000-10,000—that's a huge range
- About 25% of orders are making less than ₹4,000—that's a red flag

The real story is: "Yeah, corporate furniture makes good money on average, but 1 in 4 orders barely breaks even. We might have a pricing or cost problem with this segment."

---

### **Question 7: Wide Violin - Worst for Planning or Just Diverse?**

The widest violin is for Corporate orders. So what does that mean?

**One person says:** Wide = unpredictable = bad for planning. If the range is huge, how do I forecast inventory? How do I staff? That's chaos.

**Other person says:** Wide doesn't mean bad. It just means we're selling to different customer sizes. That's actually good—it means we serve both small and huge orders.

**I think the second person is right**, but we need to look at this differently. The real question isn't "how wide is the distribution?" but rather "how wide relative to the average?"

If we calculate Coefficient of Variation (standard deviation / mean):

- Consumer has a low CV (tight cluster of small orders)
- Corporate has a high CV (spread from small to huge)

But here's the thing: Corporate is actually better! A small order of ₹5,000 is predictable and boring. A huge order of ₹85,000 is risky but exciting. If we have the supply chain to handle it, the risk is worth it.

**So:** Corporate (wide, diverse) is better for our business than Consumer (narrow, limited), as long as we're prepared for the variation.

---

### **Question 8: Why the Darkest Cell Isn't Always the Best Investment**

The darkest cell in the heatmap is Corporate-Furniture at ₹9,325 average profit. Looks like the winner, right? Wrong.

The problems:

1. **Sample size matters.** That ₹9,325 is based on maybe 3-4 orders. Consumer-Electronics has 8-10 orders with lower average but way more profit total. A high average from a tiny sample is risky.

2. **Margin vs. absolute profit.** Corporate-Furniture makes ₹9,325 on an ₹80,000 order = 11.6% margin. Consumer-Electronics makes ₹1,579 on a ₹12,000 order = 13.2% margin. If we reinvest profits to grow, the higher margin scales better.

3. **Hidden costs.** Big corporate furniture orders probably need custom handling, special shipping, maybe assembly. That profit might already be squeezed.

4. **Risk.** Looking at the violin plot, some corporate orders barely break even or lose money. Consumer-Electronics is more stable.

A better strategy: Look at total profit (mean × number of orders), profit margin %, and how stable it is. Then invest there.

---

## Round 3 - Rebuild the Story

### **Question 9: Three-Sentence Story**

Here's what I'd tell an executive:

"Most of our orders are small (under ₹15,000), but we also get some massive corporate orders up to ₹85,000. Furniture and Electronics are our profit centers—making around ₹3,000-5,000 profit each, while Books and Food barely move the needle. The problem: profit scales almost perfectly with order value, but we're eroding that with discounts—we need to decide if we're going for volume or margin."

And the reality: This is based on 60 orders over 3 months. Seasons might change things, or a big marketing push could flip our strategy.

---

### **Question 10: Two Charts That Look Like They Disagree**

I looked at two different charts and got confused:

- One chart says Corporate-Electronics averages ₹4,820 profit (high)
- Another chart says overall Electronics average ₹4,820 but Consumer-Electronics is way lower at ₹1,579 (low)

Wait, how can both be true?

It's Simpson's Paradox. Here's why:

- Corporate orders are huge (₹50,000 each) with 9% margin = big profit
- Consumer orders are small (₹5,000 each) with 30% margin = small profit
- Corporate-Electronics orders are rare, so when we average them they look great
- Consumer-Electronics orders are more common, so they pull the overall average down

The lesson: Always check the sample size and order value when comparing segments. The numbers can be true at the same time—they're just answering different questions.

---

### **Question 11: Which Chart Should We Replace?**

The pie chart showing market share by customer segment is basically useless.

Why? Because:

- I can't tell if 40% is actually different from 32%—they look the same in a pie
- It doesn't answer any real business question. So what if 40% are consumers? What should I _do_ with that info?
- It hides all the important details (like which segments are most profitable)

I'd replace it with a stacked bar chart showing Segment × Product Category, sized by order count and colored by profit margin.

That actually tells a story:

- Which segment-category combinations are both common AND profitable?
- Should we market more to corporate furniture buyers?
- Where's our money really coming from?

The downside is that it's more complex. But that's okay—it answers real questions.

---

### **Question 12: Same Finding, Three Different Audiences**

My main finding is: **Order value drives profit (almost perfectly), but discounts are eating into it.**

**Talking to the Warehouse Manager:**

"Focus your best people on high-value orders (₹40,000+). These are 3x more profitable and the customers won't complain about price. Use fast-track handling for Electronics and Furniture. For small orders, just automate them—we're not making much money anyway, so efficiency is everything."

**Talking to Finance:**

"The problem isn't volume, it's size. One ₹80,000 order with 11% margin makes ₹9,000 profit. Fifteen small ₹4,000 orders at 30% margin only make ₹1,800 total. Our discount strategy is killing us—we're cutting margin by 20-30% and not even getting volume growth. We should either require minimum order sizes with free shipping incentives, or raise prices on small orders."

**Talking to Sales/Customer Retention:**

"Your best customers are corporate and high-ticket buyers—they give 4-5 stars and come back. Your small-order customers give 2-3 stars and return stuff. This isn't a discount problem—these are just different customer types. Stop trying to convert cheap customers. Focus retention money on the high-value ones. For small customers, maybe bundle products to increase order size, but honestly the low-margin ones might not be worth keeping."

---

## Round 4 - Business Decisions

### **Question 13: Where Should I Spend My Marketing Budget?**

Three options:

- **A:** Furniture (highest average profit: ₹7,782)
- **B:** Corporate-Furniture combo (highest heatmap cell: ₹9,325)
- **C:** Electronics (most orders: 16)

I'm going with **C: Electronics.**

Here's why A and B don't work:

- Furniture A: Total profit is actually about the same as Electronics (10 orders × ₹7,782 ≈ 16 orders × ₹4,820). I'd be betting everything on products that might be saturated.
- B is way too risky. I'd basically be betting the whole budget on 2-3 orders from one small segment. What if they don't buy?

Why C is better:

- We already have 16 electronics orders, so there's clearly demand
- Both consumers AND corporations buy electronics, so I'm not locked into one customer type
- Looking at the pairplot, electronics sell at all discount levels, which suggests people want them
- If I run a small promotion and get 2-3 more orders, that's ₹10,000-15,000 extra profit
- Even if discounts eat into margin a bit, it's still less risky than betting on one category

---

### **Question 14: My Discount Policy**

I'm implementing three tiers:

**0-5% discount:** Auto-approve for all orders ≥₹5,000

- The profit hit is minimal (less than 5%)
- Customers feel they got a deal without us losing money

**6-12% discount:** Case-by-case review

- Only if Order_Value ≥₹20,000 OR it's Electronics OR Corporate segment
- Needs a real reason (bulk order, strategic customer, clearing old stock)
- Profit margin loss is bigger (5-10%), so we need to be selective

**>12% discount:** Not allowed (except CEO override)

- This kills profit—looking at the data, correlation between discount and margin is -0.84
- These orders barely break even anyway

Evidence:

- Each 1% discount costs us ₹100-200 in profit
- Corporate-Furniture with 0% discount makes ₹9,325
- Put 10% discount on it, we're down to ₹8,500

Things I'd need to know to improve this:

1. **Elasticity:** Does a 10% discount actually get us 10% more orders? (Probably not)
2. **Customer lifetime value:** Are discounted customers just one-time buyers or do they come back?
3. **Inventory:** Are we using discounts to clear old stock (good) or to sell products that should be profitable anyway (bad)?
4. **Competition:** Are we matching market prices or just being cheap?

---

### **Question 15: Returns-Reduction Pilot**

I'd target: **Consumer segment, orders taking >5 days to deliver, with high discounts (>10%)**

Why this group?

- Consumer orders are already low-margin, so a return really hurts
- Slow delivery (>5 days) correlates with more variance and probably more returns
- High discounts suggest the customer is price-sensitive and less committed to the purchase

My action: **Offer free fast shipping** (2-day instead of 7-day) if the order ships within 24 hours.

What to measure: **Return Rate (%)** for this segment over 3 months.

- Current baseline: check how many consumer orders with high discount/slow delivery are being returned
- Goal: reduce returns by 30%
- Cost: maybe ₹200-500 per order for faster shipping
- Payoff: if returns drop 30%, we save ₹100-300 margin per order + better customer satisfaction

---

## Round 5 - Data Investigation

### **Question 17: Is This an Outlier or an Error?**

There's an order for ₹85,000 profit ₹14,300. That's a massive order. Is it real or a data entry mistake?

**I think it's real.** Here's why:

- The profit of ₹14,300 makes sense (16.8% margin, which is normal for big corporate orders)
- The profit-to-order-value ratio is in line with other orders
- No red flags like profit > order value or negative values
- The violin plot shows a few orders in this range, so it's not completely alone

**But I'd run these checks:**

1. Is profit_margin reasonable? (Should be 10-20%, not 50%+)
2. Are there other corporate furniture orders around this size? (Yes, so it fits the pattern)
3. Does delivery_days make sense? (If it says 1 day for a huge order, that's suspicious)
4. Did this customer place any other orders? (If yes, they're real; if no, might be a typo)

---

### **Question 18: Which Finding Would Most Likely Change?**

The ranking of categories by profit is the most fragile conclusion.

Current ranking: Furniture (₹7,782) > Electronics (₹4,820) > Clothing (₹445) > Food (₹385) > Books (₹79)

Why it could flip:

- Books and Food have tiny sample sizes (5-8 orders each)
- One big corporate book order would totally change the Books average
- If we run a "Food promotion" and get 20 new corporate food orders, the ranking reverses

Why other findings are solid:

- **Order_Value ↔ Profit (0.99):** Based on 60 data points and a clear mechanism. Won't flip.
- **Discount ↔ Profit (-0.52):** Moderate correlation across all 60 orders. Could change but unlikely to flip directions.
- **Customer Segment split:** Based on 60 orders. Would need 15-20 new orders to move significantly, but 100+ orders would stabilize it.

**The lesson:** Categories with small sample sizes are fragile. I'd wait for 200+ orders before making big category decisions.

---

### **Question 19: Strongest Correlation - Why Isn't It Causation?**

Order_Value and Profit have a 0.99 correlation. That looks like causation. But it might not be.

Possible reasons:

1. **Wrong direction:** Maybe high profit causes customers to buy more (they trust us more), not the other way around
2. **Third variable:** Maybe "Customer_Segment" is driving both. Corporate customers place large orders AND generate profit (not because of order size, but because they're corporate)
3. **Threshold effect:** Maybe profit increases with order value up to ₹40,000, then plateaus. The correlation hides this—it looks linear but isn't
4. **Data artifact:** Maybe our system records profit as a % of order value by definition, making them mathematically linked

**How to investigate:**

1. Filter to just one category (e.g., Electronics) and re-calculate correlation. If it's still 0.99, segment confounding is ruled out.
2. Calculate profit_margin (profit / order_value) and plot it. If margin is constant (flat line), then causation is straightforward. If margin varies, something else is going on.
3. Order the data chronologically. Did order size increase before profit increased, or the other way around?

---

### **Question 20: Why Is My Classmate Getting a Different Chart?**

Possible reasons (most to least likely):

1. **Different data file** (40% chance)
   - Check: `print(df.shape)` and `print(df.head())`
   - If they have different row counts or their Order_IDs don't match ours, they loaded the wrong file

2. **Different software version** (25% chance)
   - Check: `print(matplotlib.__version__)`
   - Older matplotlib has different colors, fonts, sizes
   - Ask: "Are the colors different?" If yes, version mismatch

3. **They filtered or modified the data** (20% chance)
   - Check: `print(df.describe())`
   - If their mean Order_Value is ₹5,000 and ours is ₹15,000, they filtered to small orders
   - Ask them to run the describe() function and compare numbers

4. **Random seed difference** (15% chance)
   - Check for `.sample()` or randomness in their code
   - If they re-ran the code and got different output, it's random
   - Fix: add `np.random.seed(42)` to lock it down

- Corporate segment naturally generates high-value orders (seen in violin plot)
- No logical inconsistency (e.g., profit > order value)
- Segment has 2–3 orders in this range; they cluster, so not isolated

**Check to run:**

1. **Profit_Margin validation:** Is (Profit / Order_Value) within 2 std devs of the mean? (If profit_margin is 31%, and mean is 15% ± 10%, then it's an outlier in margin, not value)
2. **Segment sanity:** Filter by Segment='Corporate' and Product_Category='Furniture'. Are all large orders in this cell, or is the ₹85,000 a true singleton? (Violin plot suggests others; likely legitimate)
3. **Customer repeat rate:** Does this customer have multiple orders? If yes, not an error (real, high-value customer). If no, could be a data entry typo (e.g., someone entered ₹850,000 by mistake).
4. **Delivery check:** Does delivery_days align with typical logistics for large orders? (Should be 5–8 days; if it says 1 day, might be entry error)

---

### **Question 18: Most Fragile Conclusion**

**Most likely to change with new sample:** The rank order of product categories by profit.

**Why:**

- Current ranking: Furniture (₹7,782) > Electronics (₹4,820) > Clothing (₹445) > Food (₹385) > Books (₹79).
- But order counts are small: Furniture (13), Electronics (16), Clothing (9), Food (5), Books (8).
- Books and Food are especially fragile (n=5–8). One new high-value book order flips the ranking.
- Example: If next 100 orders are a "Books bundle promotion" with 20 corporate customers buying ₹30,000 bundles, Books suddenly becomes ₹5,000 avg profit, leaping above Electronics.

**Why other conclusions are robust:**

- Profit ↔ Order_Value correlation (0.99) is based on 60 data points and a clear mechanism (profit is markup on order value). New data won't flip this.
- Discount ↔ Profit correlation (-0.52) is moderate but across all categories. 100 new points won't reverse it to +0.52.
- Customer Segment split (40% Consumer, 32% Corporate, 28% Home Office) is based on 60 orders. Needs only 15–20 new orders to shift by 10%—moderately fragile but not as bad as Food ranking.

**Mechanism of fragility:**

1. **Small n per stratum:** Some groups have 5–8 orders; 1 outlier shifts the mean by 20%
2. **High variance:** Categories with high std dev (like Furniture) can have a few huge orders pulling the mean

**How to make robust:**

- Report median instead of mean (less susceptible to outliers)
- Report confidence intervals (e.g., "Furniture avg profit ₹7,782 ± ₹3,000 at 95% CI")
- Wait for n=200+ orders before declaring Furniture as the profit leader

---

### **Question 19: Strongest Correlation & Causality**

**Strongest positive correlation in heatmap:** **Order_Value ↔ Profit = 0.99**.

**Why correlation ≠ causation:**

- Correlation ≠ direction of causation: Does high order value _cause_ profit, or does high profitability _cause_ customers to place larger orders?
- Confounding: Both might be caused by a third variable, e.g., "customer segment." Corporate customers (who generate large orders) might use suppliers who are inherently higher-margin, so the real driver is "Segment," not "Order_Value."
- Reverse causality: Maybe our company, seeing a ₹50,000 order coming in, works extra hard to maximize profit on it (bundles, add-ons). So profit is "caused" by effort, and order value is just an artifact.
- Nonlinearity: What if profit increases with order value only until ₹40,000, then plateaus due to discount pressure? Correlation of 0.99 obscures this threshold effect.

**Small follow-up analysis to improve causal story:**

1. **Stratify by Category:**
   - Filter dataset to single category (e.g., Electronics only)
   - Recompute Order_Value ↔ Profit correlation
   - If correlation remains 0.99, then Segment confounding is ruled out (causation is strengthened)
   - If correlation drops to 0.70, then Category choice and segmentation are the real drivers (causation weakened)

2. **Compute Profit_Margin (Profit / Order_Value):**
   - Regress Profit_Margin vs. Order_Value
   - If margin is constant (slope ≈ 0), then causation is straightforward: "profit scales linearly with order value due to fixed markup %"
   - If margin decreases with order value (slope < 0), then causation is more complex: "large orders get discounts, reducing margin"
   - Actual result from pairplot: margin _is_ lower for very large orders (see heatmap: Profit_Margin ↔ Order_Value correlation = 0.08, nearly flat). This contradicts simple causality and supports "discount pressure" hypothesis.

3. **Temporal analysis (if data has dates):**
   - Order chronologically: O001, O002, ..., O060
   - Did our Order_Value increase over time? (Indicates growth strategy)
   - Did profit margin decrease over time? (Indicates competitive pressure leading to discounts, not profitability causing order size)
   - Time order helps establish causality direction

---

### **Question 20: Classmate Gets Different Chart — Four Possible Causes**

A classmate runs the same notebook code but gets a different-looking chart. Probable causes:

| Cause                                                   | Likelihood              | Diagnosis                                                                                                                                                                                                                                                    |
| ------------------------------------------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Different data file (wrong CSV loaded)**              | Most likely (40%)       | `print(df.shape)` — if different shape, wrong file. Check file path in `pd.read_csv()`. Also check first few rows: `df.head()`. Our data has Order_ID O001–O060; if theirs starts O100, wrong file.                                                          |
| **Different matplotlib/seaborn version**                | Likely (25%)            | `import matplotlib; print(matplotlib.__version__)`. Older versions (2.2) have different default colors and font sizes. Ask: "Are the colors different?" If yes, likely version mismatch.                                                                     |
| **Data was modified (filtered, sorted, or duplicated)** | Moderately likely (20%) | `print(df.describe())` — compare summary stats. If their mean Order_Value is ₹5,000 and ours is ₹15,000, they filtered to low-value orders. Check: `print(df[df["Order_Value"] > 50000].shape)` to count high-value orders. If different, data was filtered. |
| **Different random seed or sampling**                   | Least likely (15%)      | If code has `.sample()` or random-seed-dependent logic, randomness could change output. Check for `np.random.seed()` in the code. If missing, re-running produces different output. Diagnosis: Run twice, compare. If different, likely randomness.          |

**Diagnosis workflow:**

1. Ask: "Do you have 60 rows?" (if not, different data or filtering)
2. Ask: "What's your mean Order_Value?" (if not ₹15,635, different data)
3. Ask: "What color are the bars?" (if not blue, likely version mismatch)
4. Ask: "Run `print(df.head())`—what does O001 show?" (confirms data integrity)

---

## Round 6 - Prediction and Peer Review (20 minutes)

### **Question 21: Null and Alternative Hypotheses**

**Team's claim:** "Discounts reduce profit."

**Null Hypothesis (H₀):** "Discount_Percent and Profit are independent. A 10% discount does not result in lower profit than a 0% discount (on average)."

**Alternative Hypothesis (H₁):** "Discounts reduce profit. Higher Discount_Percent is associated with lower Profit (inverse relationship)."

**Prediction:** p-value will be **below 0.05** (reject H₀).

**Why:**

- Correlation is already -0.52, a moderate inverse relationship
- Scatter plot visually shows this trend
- With n=60 orders, even moderate correlations (r > ±0.25) achieve p < 0.05
- So H₀ (independence) is very unlikely; we'll likely reject it

**Test to use:** Pearson correlation test or simple linear regression (Profit ~ Discount).

---

### **Question 22: Evidence That Would Weaken the Recommendation**

**Strongest finding:** "High-value corporate furniture orders are most profitable (₹9,325 avg), so prioritize this segment."

**Evidence that would weaken this:**

1. **New data:** Next 20 corporate furniture orders average ₹2,000 profit (vs. historical ₹9,325). _Means the trend was a fluke, not sustainable._
2. **Customer churn data:** 60% of corporate furniture customers are one-time buyers (vs. 10% for consumer electronics). _Means high profit is offset by acquisition cost and low lifetime value._
3. **Supply chain analysis:** Corporate furniture orders require 40-day lead times and 20% returns, vs. 5-day lead for consumer electronics with 5% returns. _Means operational cost and risk exposure makes this segment unprofitable when fully loaded._
4. **Competitor intelligence:** A competitor launches a furniture line at 20% lower price, and our corporate customers start switching. _Means the profit is at risk, requiring immediate strategy shift._
5. **Profit composition analysis:** Detailed cost breakdown shows that ₹9,325 profit is driven by a single supplier deal ending next quarter. _Means it's temporary, not structural._

**Weakest evidence that wouldn't change recommendation:**

- "Consumer-Electronics has higher Profit_Margin (31% vs. 11.6%)." _Margin ≠ absolute profit. We care about total profit, not %. If consumer orders are smaller, margin doesn't help._
- "Box plot shows variability in corporate furniture orders." *Variability is expected; it doesn't mean the *average* profitability is wrong.*

---

---

## Round 6 - Hypothesis Testing & Review

### **Question 21: Hypotheses for My Finding**

My claim: "Discounts reduce profit."

**Null Hypothesis:** There's no real relationship between discounts and profit. The pattern I'm seeing is just random noise.

**Alternative Hypothesis:** Higher discounts actually lead to lower profit. It's a real relationship, not chance.

**My prediction:** The p-value will be **less than 0.05**, meaning we reject the null and confirm discounts really do hurt profit.

**Why:**

- The correlation is already -0.52
- With 60 data points, that's strong enough to be significant
- The scatter plot clearly shows the pattern

---

### **Question 22: What Would Make Me Change My Mind?**

My biggest recommendation is: "Focus on high-value corporate furniture orders—they make ₹9,325 profit, more than anything else."

But this would be wrong if:

1. **Next batch of corporate furniture orders only make ₹2,000 profit.** Would mean it was a fluke.
2. **90% of corporate furniture customers never buy again.** Would mean high profit but low lifetime value = not actually valuable.
3. **Corporate furniture requires 40-day lead times and we have 20% returns.** Would mean the ₹9,325 doesn't account for all the extra costs.
4. **A competitor undercuts us on furniture and steals our customers.** The profit disappears.

The evidence that wouldn't really matter:

- "Consumer-Electronics has higher profit margin (31% vs 11%)." — Margins don't matter if order values are smaller. Total profit is what counts.
- "Corporate furniture orders are more variable." — Variance is normal. It doesn't mean the average is wrong.

---

### **Question 23: Reviewing What My Classmates Claim**

When I review other people's answers, I should check: is this a fact, a comparison, a correlation, or a causal claim?

Examples:

- **"The median order value is ₹8,500"** = Descriptive (just a fact about the data) ✓
- **"Corporate segment makes 3x more profit than Consumer"** = Comparative (comparing two groups) ✓
- **"Delivery days and ratings are negatively correlated"** = Associational (they move together) ✓
- **"We should discount more because it increases volume"** = Causal ✗ (not proven!)

For causal claims, I'd look for evidence: Did they test it? Do they have before/after data? Or are they just assuming?

---

### **Question 24: The 60-Second Pitch**

If I had to present this in 60 seconds:

**Finding (15 sec):**
"Order value is almost the only thing that matters for profit—it's 0.99 correlated. But discounts are ruining it. The more we discount, the less profit we make."

**Evidence (15 sec):**
"The scatter plot shows low-discount orders making way more profit. The correlation is -0.52. Corporate-Furniture with zero discount makes ₹9,325; Consumer-Books with high discounts makes ₹79. The numbers back it up."

**Action (15 sec):**
"Stop giving discounts under ₹5,000 orders. Only approve 6-12% discounts case-by-case for bigger orders. Over 12% is banned. This should protect our margins while we grow."

**Limitation (15 sec):**
"This is based on 60 orders over 3 months. Could change with seasons or marketing campaigns. Books and Food only have 5-8 orders each, so those categories are fragile. We need more data to be really confident."

**One question for later:**
"Is the discount-profit relationship actually causal, or is it just because we discount bad products anyway?"

---

## Final Reflection

### **Question 25: Least Trustworthy Finding**

The **pie chart showing market share** is basically useless.

Why:

- I can't tell if 40% is actually different from 32%—they look the same visually
- It doesn't answer any business question. Who cares if we serve 40% consumers?
- It hides what actually matters (like which segment is most profitable)
- It makes me overconfident in numbers I can't actually read accurately

---

### **Question 26: What I'd Act On Despite Being Uncertain**

I'd implement the **discount policy immediately** (0-5% safe, 6-12% review, >12% banned).

Why take the risk:

- If I'm wrong, worst case is we lose a few orders but keep more margin. Margin > volume in this business.
- The evidence is pretty solid. Even if future data changes things, the negative relationship between discount and profit probably won't flip.
- Every month I delay, I'm leaving money on the table—maybe ₹500-1000 per order × 60 orders = ₹30,000-50,000 wasted
- It's reversible. If it goes bad, I can go back to the old way in 2-3 months

What I wouldn't act on without more proof:

- Dropping all consumer orders. That's too risky and permanent. These might be valuable long-term.

---

### **Question 27: What Should We Test Next?**

The biggest question left unanswered: **"Is Order_Value truly causing Profit, or is Customer_Segment/Category actually driving both?"**

Why this matters:

- If Order_Value is truly causal, I should focus on growing average order size (₹15K → ₹25K)
- If Segment is actually the driver, I should focus on getting more Corporate customers
- These lead to totally different strategies

To test this:

- Look at one category only (say, Electronics) and see if the correlation is still 0.99
- Calculate profit margin—if it's constant, Order_Value is causal; if it varies, something else is driving it
- Look at which category/segment combinations we should really invest in

---

## Bottom Line

**What drives profit:** Order size, mostly. Which segment/category you're in also matters. Discounts hurt, period.

**What's risky:** Giving discounts to small orders, low-margin products, and impatient customers.

**What I'd do first:** Lock down the discount policy, focus marketing on electronics (proven volume), and stop worrying about tiny customer segments.

**What we need to know:** Is the order size thing actually causal? And can we really cut discounts without losing volume?
