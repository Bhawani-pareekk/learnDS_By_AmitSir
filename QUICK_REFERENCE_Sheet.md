# QUICK REFERENCE SHEET

## 2-Minute Review Before Your Test

---

## LIBRARIES CHEAT SHEET

```
PANDAS (pd)      → Load & explore data
NUMPY (np)       → Math calculations
MATPLOTLIB (plt) → Basic charts
SEABORN (sns)    → Beautiful charts + relationships
```

| What to do       | Code                            | Result               |
| ---------------- | ------------------------------- | -------------------- |
| Load data        | `pd.read_csv()`                 | DataFrame            |
| Check data       | `df.info()`, `df.describe()`    | Data quality         |
| Find missing     | `df.isnull().sum()`             | Count nulls          |
| Check duplicates | `df.duplicated().sum()`         | Count dupes          |
| Histogram        | `plt.hist(df["col"], bins=15)`  | Distribution         |
| Scatter          | `plt.scatter(x, y)`             | Relationship         |
| Heatmap          | `sns.heatmap(corr)`             | All correlations     |
| Violin plot      | `sns.violinplot(x, y, data=df)` | By group             |
| Box plot         | `sns.boxplot()`                 | Quartiles + outliers |
| Pairplot         | `sns.pairplot(df)`              | Everything           |
| Correlation      | `df.corr()`                     | Number -1 to +1      |

---

## THE 5 KEY NUMBERS TO REMEMBER

| Relationship         | Correlation  | Meaning                 |
| -------------------- | ------------ | ----------------------- |
| Order_Value ↔ Profit | **0.99**     | Nearly perfect          |
| Discount ↔ Profit    | **-0.52**    | Moderate negative       |
| Discount ↔ Margin    | **-0.84**    | Strong negative         |
| Orders dataset size  | **60**       | Small (fragile)         |
| Time period          | **3 months** | Limited (seasonal risk) |

---

## CORRELATION STRENGTH GUIDE

- **0.9-1.0** = Very strong (obvious pattern)
- **0.7-0.9** = Strong (clear trend)
- **0.5-0.7** = Moderate (noticeable, not obvious)
- **0.3-0.5** = Weak (some connection)
- **0-0.3** = Very weak (basically random)

---

## CHART TYPE → USE FOR

| Chart       | Use For                           | Best For                     |
| ----------- | --------------------------------- | ---------------------------- |
| Histogram   | Distribution of 1 variable        | "What's typical?"            |
| Scatter     | Relationship between 2 variables  | "Do they move together?"     |
| Box plot    | Distribution by groups + outliers | "Are there groups?"          |
| Violin plot | Full distribution by groups       | "What's the shape by group?" |
| Heatmap     | Relationships in 3+ variables     | "What's significant?"        |
| Pairplot    | All relationships at once         | "See everything"             |
| Bar chart   | Compare categories                | "Who wins?"                  |
| Pie chart   | Market share                      | (But hard to read!)          |

---

## HOW TO SPOT A GOOD ANSWER vs. BAD ANSWER

### GOOD ANSWER HAS:

✓ Specific numbers ("correlation -0.52" not "negative correlation")
✓ Chart reference ("box plot shows..." not just "I think...")
✓ Logic ("because... leads to..." cause & effect)
✓ Sample size awareness ("10 orders is small" or "100 orders is robust")
✓ Confounding acknowledgment ("could also be because...")
✓ Limitation mention ("based on 60 orders over 3 months")
✓ Actionable ("test this by...")

### BAD ANSWER HAS:

✗ No numbers ("it looks like...")
✗ No chart source ("I think the data shows...")
✗ No logic ("correlation = causation")
✗ Ignores n ("this segment averages ₹10K" without mentioning 2 orders)
✗ One view only ("this proves it")
✗ False confidence ("definitely true because...")
✗ Vague ("we should focus better")

---

## QUESTION TYPES: QUICK ANSWERS

### Round 1: Evidence Hunt

- **Q1:** Outliers matter → remove them changes story
- **Q2:** Looks strong but -0.52 correlation = weak + scatter
- **Q3:** Order_Value confounds discount-profit relationship
- **Q4:** Order_Value is strongest (0.99 with profit)

### Round 2: Competing Interpretations

- **Q5:** Both true: discounts reduce margin AND bad products get discounted
- **Q6:** Use median, not mean, when outliers exist
- **Q7:** Wide is good if mean is high (high CV + high mean = best)
- **Q8:** Highest cell: ignore (sample size = 2-3, high risk)

### Round 3: Rebuild Story

- **Q9:** 3 sentences: distribution + comparison + relationship + limit
- **Q10:** Simpson's Paradox (same data, different grouping)
- **Q11:** Replace pie chart with heatmap or stacked bar
- **Q12:** Same numbers, different audience implications

### Round 4: Business Decisions

- **Q13:** Choose Electronics (volume, proven demand, safe)
- **Q14:** Policy: 0-5% safe, 6-12% review, >12% banned
- **Q15:** Target: consumer + slow delivery + high discount = returns risk

### Round 5: Data Investigation

- **Q17:** ₹85K order is real (profit ratio checks out)
- **Q18:** Books ranking is fragile (n=5-8)
- **Q19:** 0.99 ≠ causal (could be confounding, direction, definition)
- **Q20:** Wrong file most likely (check df.shape, df.head())

### Round 6: Hypothesis & Reflection

- **Q21:** H₀: no relationship, H₁: relationship exists, predict p<0.05
- **Q22:** Would reconsider if: next batch shows ₹2K profit instead of ₹9K
- **Q23:** Causal claims need experiments, correlation claims need numbers
- **Q24:** Need: Finding + Evidence + Action + Limitation

---

## THE 3 BIGGEST MISTAKES (AVOID AT ALL COSTS)

### MISTAKE 1: "High correlation = Causation"

- ✗ "Correlation 0.99 proves order size causes profit"
- ✓ "Correlation 0.99, but profit is calculated as % of order size, so definition might explain it"

### MISTAKE 2: "Ignoring sample size"

- ✗ "Books category averages ₹79 profit, so it's bad"
- ✓ "Books has only 5-8 orders, so ₹79 average is fragile"

### MISTAKE 3: "Mean without context"

- ✗ "Corporate-Furniture makes ₹9,325 average"
- ✓ "Corporate-Furniture makes ₹9,325 on ~3-4 orders (check if sustainable)"

---

## WHEN YOU'RE STUCK ON A QUESTION

**Ask yourself these 3 things:**

1. **Can I point to a number?**
   - No → Go back to charts, find the data
   - Yes → Write it down, explain it

2. **Can I explain WHY?**
   - No → Think about the mechanism
   - Yes → Write the logic

3. **What could be wrong with my answer?**
   - Confounding variable? → Mention it
   - Outliers? → Acknowledge it
   - Small sample? → Note it
   - Yes → Your answer is now better

---

## LAST-MINUTE MENTAL CHECKLIST

Before you write each answer:

□ Do I have a number or specific reference?
□ Does this make logical sense?
□ Am I confusing correlation with causation?
□ Did I consider sample size?
□ Did I mention a limitation?
□ Can I defend this claim?

**If all 6 are checked → write the answer**

---

## IF YOUR CLASSMATE SAYS THIS... RED FLAGS!

| Red Flag Statement                  | What's Wrong         | How to Challenge                            |
| ----------------------------------- | -------------------- | ------------------------------------------- |
| "The correlation proves it"         | Could be confounding | "Did you check for other variables?"        |
| "The average is X"                  | Ignores outliers     | "What's the median and quartiles?"          |
| "Only 2 orders but average is ₹10K" | Fragile data         | "How stable is this with more data?"        |
| "We should definitely do X"         | No uncertainty       | "What if this assumption is wrong?"         |
| "The chart shows Y"                 | No numbers           | "What's the specific correlation or count?" |
| "Segment A is best"                 | Ignores confounding  | "Could segment size or mix explain this?"   |
| "Because correlation = causation"   | Major error          | "Could Z be driving both A and B?"          |

---

## CONFIDENCE LEVELS FOR ANSWERS

- **95-98% confident:** Numbers match charts, logic is clear, alternatives checked
- **85-90% confident:** Good reasoning, one limitation mentioned, could verify
- **70-85% confident:** Makes sense, but not fully tested, could be confounded
- **50-70% confident:** Possible, but weak evidence or ignored alternatives
- **<50% confident:** Guess, or major logical flaw

**Goal: Get to 85%+ on most questions**

---

## YOUR TEACHER WILL LOOK FOR:

1. **Thinking over memorization** (show your work!)
2. **Evidence over opinion** (numbers matter!)
3. **Nuance over certainty** (acknowledge limits!)
4. **Logic over luck** (explain mechanisms!)
5. **Testing over claiming** (suggest verification!)

**Focus on these 5 → You'll do great**
