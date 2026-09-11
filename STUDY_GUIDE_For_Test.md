# STUDY GUIDE - Data Visualization & Analysis

## Complete Guide for Test Prep + Checking Classmates' Answers

---

# PART 1: PYTHON LIBRARIES — WHAT, WHY, WHEN TO USE

## 1. **PANDAS (pd)**

**What it is:** A library for working with data tables (like Excel but in Python)

**What we used it for:**

- Loading CSV files: `pd.read_csv("file.csv")`
- Creating DataFrames (tables with rows and columns)
- Checking data quality: `df.info()`, `df.describe()`, `df.head()`

**Why we need it:**

- Without pandas, working with data would be super hard
- It automatically handles missing values, data types, etc.
- Makes it easy to filter, sort, and group data

**When to use it:**

- Anytime you have data in CSV, Excel, or database
- You need to explore and clean data first
- You need to check for errors before visualizing

**Key functions to know:**

```python
df.head()              # See first 5 rows
df.info()              # Check data types and missing values
df.describe()          # Get stats (mean, min, max, etc.)
df.isnull().sum()      # Count missing values
df.duplicated().sum()  # Check for duplicate rows
df[df["column"] > 5000]  # Filter rows
df.groupby("column").mean()  # Group and calculate
```

---

## 2. **NUMPY (np)**

**What it is:** Library for math and numerical calculations

**What we used it for:**

- Creating arrays (lists of numbers)
- Math operations (like log transformation)
- Random number generation

**Why we need it:**

- Very fast for big calculations
- Needed for scientific computing
- Works behind the scenes in pandas and matplotlib

**When to use it:**

- Math transformations (square root, logarithm, etc.)
- When you need raw speed for calculations
- Working with arrays of numbers

**Key functions to know:**

```python
np.log(df["Order_Value"])      # Natural logarithm
np.sqrt(values)                # Square root
np.mean(values)                # Average
np.std(values)                 # Standard deviation
```

---

## 3. **MATPLOTLIB (plt)**

**What it is:** The basic library for drawing charts

**What we used it for:**

- Creating histogram
- Scatter plots
- Bar charts
- Box plots

**Why we need it:**

- It's the foundation for all Python visualization
- Low-level control (you can customize everything)
- Works with pandas dataframes easily

**When to use it:**

- Basic charts (histogram, scatter, bar)
- When you need full control over appearance
- Simple, quick plots

**Key functions to know:**

```python
plt.hist(data, bins=15)        # Histogram
plt.scatter(x, y)               # Scatter plot
plt.bar(categories, values)     # Bar chart
plt.title("Title")              # Add title
plt.xlabel("Label")             # X-axis label
plt.ylabel("Label")             # Y-axis label
plt.show()                       # Display chart
```

---

## 4. **SEABORN (sns)**

**What it is:** A beautiful layer on top of matplotlib (makes charts look professional)

**What we used it for:**

- Violin plots (show distribution by group)
- Box plots (show quartiles and outliers)
- Heatmaps (show relationships between many variables)
- Pairplots (see all relationships at once)
- Regression plots (show trend lines)

**Why we need it:**

- Makes professional-looking charts with less code
- Automatically uses good colors and styling
- Better for exploring relationships in data

**When to use it:**

- Multi-variable analysis (heatmaps, pairplots)
- Comparing distributions (violin, box plots)
- Showing relationships (regression plots)
- When you want charts to look good without much work

**Key functions to know:**

```python
sns.set_theme(style="whitegrid")       # Set style (background)
sns.heatmap(data)                      # Heatmap (color table)
sns.boxplot(x="column", y="value", data=df)  # Box plot by group
sns.violinplot(x="segment", y="profit", data=df)  # Violin plot
sns.pairplot(df)                       # All relationships
sns.regplot(x="X", y="Y", data=df)     # Regression plot with line
```

**Why seaborn is amazing:**

- One line of code gives you a professional chart
- Automatically picks good colors
- Makes patterns obvious
- Looks like something from a business presentation

---

## 5. **CORRELATION & STATISTICS (Not a library, but a concept)**

**What correlation means:**

- How closely two variables move together
- Range: -1 to +1
  - **+1 = Perfect positive:** as X increases, Y always increases
  - **0 = No relationship:** X and Y are independent
  - **-1 = Perfect negative:** as X increases, Y always decreases

**Correlation strengths:**

- 0.9-1.0 = Very strong (almost perfect)
- 0.7-0.9 = Strong (clear pattern)
- 0.5-0.7 = Moderate (noticeable but not perfect)
- 0.3-0.5 = Weak (some relationship but lots of scatter)
- 0-0.3 = Very weak (basically random)

**Why this matters for your test:**

- Correlation ≠ Causation (most common mistake!)
- Just because two things move together doesn't mean one causes the other
- Example: Ice cream sales and drowning deaths are correlated (both happen in summer), but ice cream doesn't cause drowning

---

---

# PART 2: THE THINKING PROCESS — HOW I SOLVED EACH QUESTION TYPE

## HOW TO APPROACH EACH ROUND

### **ROUND 1: EVIDENCE HUNT**

**Goal:** Look at the charts and find patterns, but verify with numbers

**My thinking process:**

**Q1: Influential Outliers**

1. Look at histogram → spot the outliers (the ones sticking way out)
2. Calculate: what % are they? Are they extreme?
3. Think: "If I removed them, what would change?"
4. Answer: Describe what would be different (mean, shape, story)

**How to check if classmate is right:**

- Did they identify actual outliers? (Use box plot or histogram to verify)
- Can they describe the impact numerically? (Not just "would be different")
- Did they give a specific reason? ✓ Good

**Q2: Looks Strong but Weak Numerically**

1. Look at scatter plot → "Does it look like a clear pattern?"
2. Check correlation → "Is the number actually strong?"
3. If correlation is weak (<0.7), point out the scatter
4. Identify confounding variable (what else might explain this?)

**How to check if classmate is right:**

- Did they calculate correlation? (Must have a number)
- Did they explain why it looks strong but isn't? (Need to mention scatter or confounding)
- Do they understand what explains the relationship?

**Q3: Confounding Variable**

1. Look at the scatter plot and notice: "Two things seem related"
2. Ask: "What else could explain this relationship?"
3. Think about real-world logic (e.g., big orders get discounts)
4. Explain how this third variable creates the illusion

**How to check if classmate is right:**

- Is the variable they named actually related to both? ✓
- Did they explain HOW it confuses things?
- Can they name a way to separate the effects?

**Q4: Strongest Predictor (Before Looking)**

1. LOOK at all the charts BEFORE calculation
2. Which variable has the "cleanest" relationship with profit?
3. Make a prediction
4. Then check the correlation to verify

**How to check if classmate is right:**

- Did they make a prediction BEFORE calculating?
- Did they explain the reasoning?
- Did the actual number confirm or contradict? ✓ Good either way if they explain

---

### **ROUND 2: COMPETING INTERPRETATIONS**

**Goal:** Understand multiple viewpoints and find real evidence

**My thinking process:**

**Q5: Causality Debate (Does A cause B, or does B cause A?)**

1. Listen to both sides carefully
2. Find evidence for EACH side from the charts
3. Identify what's confounded
4. Suggest experiments that would prove one side

**Key insight:** Both can be partially true!

- Discounts might reduce profit (A causes B)
- Bad products might get discounts (C causes both A and B)
- Both could be happening at the same time

**How to check if classmate is right:**

- Did they find evidence for BOTH sides? ✓ Good thinking
- Do they acknowledge the confounding variable?
- Can they suggest a way to test which is true?
- Beware: Pure causality claims without evidence = probably wrong

**Q6: Mean vs. Median (Which number tells the real story?)**

1. Look at the distribution (violin plot)
2. Ask: "Is the data evenly spread or skewed?"
3. If there are outliers or two groups: use median or quartiles
4. If even distribution: mean is fine

**The rule:**

- **Mean:** Use when data is evenly distributed
- **Median:** Use when there are outliers or skewed data
- **Range/IQR:** Use when you want to show spread

**How to check if classmate is right:**

- Did they look at the distribution? (violin plot, box plot)
- Do they know the difference between mean and median?
- Can they explain WHY one is better? ✓ This shows real understanding

**Q7: Wide Distribution = Bad or Good?**

1. First instinct: "Wide = unpredictable = bad"
2. But think deeper: "Wide = diverse = opportunity"
3. The real measure: Coefficient of Variation (std dev / mean)
4. High CV + High mean = Best (profitable AND diverse)
5. Low CV + Low mean = Worst (stuck in a rut)

**How to check if classmate is right:**

- Do they just say "wide is bad"? = Incomplete thinking
- Do they measure relative to mean? = Better thinking
- Can they explain the trade-off? ✓ Great thinking

**Q8: Highest Value Cell ≠ Best Investment**

1. Heatmap shows MEAN, not TOTAL
2. Check sample size (how many orders in that cell?)
3. Check if it's sustainable (does it repeat?)
4. Look for hidden costs (payment terms, returns, etc.)

**How to check if classmate is right:**

- Did they mention sample size? ✓ Critical
- Do they think about total profit vs. average?
- Can they name hidden factors? ✓ Bonus points

---

### **ROUND 3: REBUILD THE STORY**

**Goal:** Tell a coherent story using multiple charts

**My thinking process:**

**Q9: Three-Sentence Executive Story**

1. Sentence 1: Distribution (what's typical?)
2. Sentence 2: Comparison (who wins?)
3. Sentence 3: Relationship (what's the connection?)
4. Add limitation: (what could change this?)

**Formula:**

- "Most orders are X, but we also get Y"
- "Category A and B lead, while C and D lag"
- "Profit connects to order size, but discounts erode it"
- "This is based on 60 orders; seasonal effects could change it"

**How to check if classmate is right:**

- Are all three elements present (distribution, comparison, relationship)?
- Do they mention a limitation? ✓ Shows sophistication
- Is the story clear enough for a non-technical person?

**Q10: Resolving Apparent Contradictions**

1. Look for Simpson's Paradox (same data, different grouping)
2. Check sample sizes (n) and averages separately
3. Explain how both can be true at the same time

**How to check if classmate is right:**

- Do they identify Simpson's Paradox or confounding?
- Do they check sample sizes?
- Can they explain the logic? = They understand

**Q11: Replace One Chart**

1. Why is it bad? (doesn't answer questions, wrong encoding, hides details)
2. What would be better? (different chart type that answers better questions)
3. What would the trade-off be? (what does new chart lose?)

**Chart types and what they show best:**

- **Histogram:** Distribution of one variable
- **Box plot:** Distribution by groups + outliers
- **Scatter plot:** Relationship between two variables
- **Heatmap:** Relationships between 3+ variables at once
- **Bar chart:** Comparison of categories
- **Pie chart:** Market share (but hard to read)
- **Violin plot:** Full distribution by groups

**How to check if classmate is right:**

- Is their replacement chart actually better for the questions?
- Do they explain what's lost? ✓ Shows thinking
- Do they justify it?

**Q12: Same Finding, Three Audiences**

1. For warehouse manager: Think about operations and efficiency
2. For finance: Think about margins, revenue, and ROI
3. For sales: Think about customer types and retention

**How to check if classmate is right:**

- Did they change the language for each audience?
- Does each version use the same evidence but different implications?
- Is it appropriate for that person's job? ✓

---

### **ROUND 4: BUSINESS DECISIONS**

**Goal:** Make real decisions with uncertainty

**My thinking process:**

**Q13: Budget Allocation (Choose A, B, or C)**

1. Calculate: total profit (mean × count), not just mean
2. Consider: addressable market (how many potential customers?)
3. Estimate: elasticity (will discount actually increase orders?)
4. Assess: risk (how fragile is this segment?)

**My logic:**

- Option A (highest mean): Ignores volume
- Option B (highest cell): Only 2-3 orders, too risky
- Option C (most orders): Proven demand, diverse customers, safe bet

**How to check if classmate is right:**

- Did they multiply mean by count? ✓
- Do they consider risk?
- Can they defend their choice with numbers?
- Did they explain what they're NOT choosing? ✓ Bonus

**Q14: Discount Policy (Three Tiers)**

1. Research: What does correlation tell us?
2. Calculate: Impact per % discount (correlation ÷ orders)
3. Design: Rules that balance margin protection and growth
4. Acknowledge: What we don't know yet?

**How to check if classmate is right:**

- Do their tiers make logical sense?
- Did they use correlation or evidence to set thresholds?
- Do they mention missing information? ✓
- Is it implementable? (Can management actually do this?)

**Q15: Pilot Program**

1. Choose: High-risk segment (intersection of bad metrics)
2. Intervention: One change that's testable
3. Metric: Single outcome that's easy to measure
4. Timeline: Realistic (3-6 months)

**How to check if classmate is right:**

- Is the target group actually high-risk?
- Can the intervention realistically change the outcome?
- Is the metric measurable? (Not vague)
- ✓ Can they explain why this one change helps?

---

### **ROUND 5: DATA INVESTIGATION**

**Goal:** Think like a data scientist about data quality and robustness

**My thinking process:**

**Q17: Outlier Identification**

1. Is it mathematically weird? (Use: profit/order value ratio)
2. Is it logically weird? (Do similar orders exist?)
3. Can I verify it's real? (Check for data entry patterns)

**How to check if classmate is right:**

- Did they verify it's not a typo? ✓
- Did they check if similar values exist?
- Do they distinguish between "extreme" and "error"?

**Q18: Fragile Conclusions**

1. Look at sample size (n) for each category
2. Small n = fragile (one outlier changes everything)
3. Big n = robust (trends hold even with new data)

**Key insight:** Books and Food have n=5-8, so their rankings are fragile.

**How to check if classmate is right:**

- Did they check sample sizes?
- Did they identify the most fragile?
- Can they explain why it's fragile?

**Q19: Strongest Correlation (Why ≠ Causation)**

1. Identify the correlation (0.99 Order_Value ↔ Profit)
2. List reasons it might NOT be causal:
   - Wrong direction? (Does profit cause order size?)
   - Confounding? (Does segment drive both?)
   - Threshold? (Does relationship change at certain point?)
   - Definition? (Is profit calculated as % of order value?)
3. Suggest test: stratify by category, calculate coefficient of variation

**How to check if classmate is right:**

- Do they mention at least 2-3 alternatives?
- Do they suggest a way to test?
- Do they avoid claiming causation without evidence? ✓

**Q20: Why Different Results?**
Most likely to least likely:

1. Different data (wrong file loaded)
2. Different version (matplotlib update)
3. Data filtered/modified
4. Random seed different

**How to diagnose:**

- `df.shape` → Check row/column count
- `df.head()` → Check data identity
- `matplotlib.__version__` → Check version
- `print(df.describe())` → Check statistics

**How to check if classmate is right:**

- Did they order by likelihood?
- Do they suggest diagnostic steps?
- Do they check multiple things? ✓

---

### **ROUND 6: HYPOTHESIS TESTING & REFLECTION**

**Goal:** Think about what we'd formally test and what we'd trust

**My thinking process:**

**Q21: Null vs. Alternative Hypothesis**

1. Null (H₀): "No relationship" or "no difference"
2. Alternative (H₁): "There IS a relationship"
3. Prediction: Based on evidence, which do we expect to reject?

**Example:**

- H₀: Discount and profit are independent
- H₁: Higher discounts correlate with lower profit
- Prediction: We'll reject H₀ (p < 0.05) because correlation is -0.52

**How to check if classmate is right:**

- Is H₀ clearly stated?
- Is H₁ the opposite of H₀?
- Did they make a prediction?
- Did they explain WHY?

**Q22: What Would Change Your Mind?**

1. New data contradicts old pattern
2. Hidden confounding variable discovered
3. Operational reality conflicts with analysis
4. Competitor/market changes

**How to check if classmate is right:**

- Can they name specific evidence that would flip their recommendation?
- Is it realistic and testable?
- Do they distinguish strong vs. weak contradicting evidence?

**Q23: Classifying Claims (Critical!)**
This is where you catch BS in classmates' answers:

**Descriptive claims:**

- "The average order is ₹15,000"
- ✓ Can verify by looking at data
- Usually safe unless numbers are wrong

**Comparative claims:**

- "Corporate profit is higher than consumer"
- ✓ Can verify by comparing groups
- Safe unless sample sizes are ignored

**Associational claims:**

- "Discount and profit are negatively correlated"
- ✓ Can verify with correlation coefficient
- Safe BUT might be confounded

**CAUSAL claims (DANGER ZONE):**

- "Discounts CAUSE profit to drop"
- ✗ Cannot verify without experiment
- Only safe if: (a) evidence is strong, (b) mechanism is clear, (c) confounding is ruled out

**RED FLAGS for causal claims:**

- No mechanism explanation
- Only one type of evidence
- Ignores alternative explanations
- Uses weak correlation as evidence

**How to check if classmate is right:**

- Did they classify correctly?
- Did they challenge causal claims? ✓
- Do they understand the distinction?

**Q24: 60-Second Pitch**
Must have 4 parts:

1. **Finding:** The key insight (15 sec)
2. **Evidence:** Numbers and chart references (15 sec)
3. **Action:** What should we do? (15 sec)
4. **Limitation:** What could be wrong? (15 sec)

**How to check if classmate is right:**

- Are all 4 parts present?
- Do they mention actual correlations/numbers?
- Is the action specific and actionable?
- Do they acknowledge uncertainty? ✓ Most important

**Q25-27: Reflection (Personal but grounded)**

- Least trustworthy: Pie chart (hard to read, hides variation)
- Act on despite uncertainty: Discount policy (low risk, high certainty)
- Next question: Is order value truly causal? (determines strategy)

**How to check if classmate is right:**

- Are their choices defensible?
- Do they think about risk?
- Can they explain their reasoning?

---

---

# PART 3: HOW TO EVALUATE CLASSMATES' ANSWERS

## CHECKLIST FOR EACH QUESTION TYPE

### **Quick Scoring Rubric:**

| Element           | Wrong                  | Incomplete                     | Correct                           |
| ----------------- | ---------------------- | ------------------------------ | --------------------------------- |
| Numbers           | No numbers, guesses    | Numbers but no interpretation  | Numbers + explanation             |
| Chart reference   | Doesn't mention charts | Mentions but doesn't explain   | References specific chart feature |
| Logic             | Contradictory          | Partial explanation            | Clear mechanism explained         |
| Alternative ideas | Doesn't consider       | Mentions one other possibility | Compares multiple explanations    |
| Actionability     | Vague                  | General direction              | Specific and measurable           |

---

## RED FLAGS THAT CLASSMATE IS PROBABLY WRONG

### **Red Flag 1: "The chart shows..." (without numbers)**

- ✗ "The scatter plot shows discounts hurt profit"
- ✓ "The scatter plot shows correlation -0.52 between discount and profit"

### **Red Flag 2: Only one type of evidence**

- ✗ "Correlation -0.52 proves discounts cause profit loss"
- ✓ "Correlation -0.52, and visually low-discount orders cluster at high profit"

### **Red Flag 3: Ignoring sample size**

- ✗ "Books category averages ₹79 profit"
- ✓ "Books category averages ₹79 profit, but only 5-8 orders, so this is fragile"

### **Red Flag 4: Mean without context**

- ✗ "Corporate-Furniture makes ₹9,325 average profit"
- ✓ "Corporate-Furniture makes ₹9,325 average on maybe 3-4 orders, not a large sample"

### **Red Flag 5: Correlation = Causation**

- ✗ "Because order value correlates with profit (0.99), order size causes profit"
- ✓ "Order value correlates with profit (0.99), but this might be because..."

### **Red Flag 6: No limitations**

- ✗ "Based on all data, clearly X is true"
- ✓ "Based on 60 orders over 3 months, X seems true, but seasonal variation could change this"

### **Red Flag 7: Vague recommendations**

- ✗ "We should focus on high-value customers"
- ✓ "We should raise minimum order to ₹5,000 with free shipping, targeting corporate segment"

---

## GREEN LIGHTS THAT CLASSMATE PROBABLY RIGHT

### **Green Light 1: Specific numbers with sources**

- ✓ "Correlation -0.52 between discount and profit" (can verify from heatmap)
- ✓ "Box plot shows 2-5 day delivery has fewer returns than >5 days"

### **Green Light 2: Multiple evidence sources**

- ✓ "Scatter plot shows pattern, correlation -0.52 confirms it, and business logic explains why"

### **Green Light 3: Acknowledges confounding**

- ✓ "Discount and profit are correlated, but Order_Value might be driving both"
- ✓ "Need to control for Category to isolate effect"

### **Green Light 4: Sample size awareness**

- ✓ "Corporate-Furniture has strong profit but only ~3 orders, so fragile"
- ✓ "Electronics has 16 orders, more stable evidence"

### **Green Light 5: Distinguishes correlation types**

- ✓ "This is associational (they move together), not causal (one causes the other)"

### **Green Light 6: Testable recommendations**

- ✓ "Implement policy, measure return rate for 3 months, compare to baseline"
- ✓ "Run A/B test: 10% discount vs. no discount, same product"

### **Green Light 7: Acknowledges uncertainty**

- ✓ "Based on current data, but could change with seasonal variations"
- ✓ "This is my recommendation, but we'd need to test before fully implementing"

---

---

# PART 4: FINAL TEST TIPS

## Before the test, memorize this:

### **The 3 Key Correlations:**

1. Order_Value ↔ Profit = **0.99** (nearly perfect)
2. Discount_Percent ↔ Profit = **-0.52** (moderate negative)
3. Discount_Percent ↔ Profit_Margin = **-0.84** (strong negative)

### **The 3 Key Segments:**

- Corporate-Furniture: ₹9,325 avg profit (high value, small sample, risky)
- Consumer-Electronics: ₹1,579 avg profit (lower value, more orders, stable)
- Books/Food: ₹79-385 profit (tiny, fragile data)

### **The 3 Key Concepts:**

1. **Confounding:** Third variable explains the relationship
2. **Simpson's Paradox:** Same data, different grouping, different conclusion
3. **Correlation ≠ Causation:** They move together ≠ one causes the other

### **The 3 Key Questions to Ask:**

1. "What's the sample size?" (Small n = fragile)
2. "What's being ignored?" (Confounding variables, hidden costs)
3. "Could this be tested?" (Actionable recommendations)

---

## During the test:

✓ **Always write your thinking, not just the answer**

- Show the steps
- Reference specific charts/numbers
- Explain WHY not just WHAT

✓ **When in doubt, calculate:**

- Correlation coefficient
- Mean vs. median
- Total profit (mean × count)
- Sample size

✓ **Avoid these mistakes:**

- Stating causation without evidence
- Using mean without checking for outliers
- Ignoring sample size
- Ignoring confounding variables
- Forgetting to mention limitations

✓ **If you're unsure about an answer:**

- Say "This could be checked by..."
- "Assuming the data is representative..."
- "More evidence would be needed to confirm..."

---

## How to know YOU'RE RIGHT:

1. ✓ Numbers + Logic + Uncertainty = High confidence
2. ✓ Can defend every claim with specific evidence
3. ✓ Acknowledge alternative explanations
4. ✓ Suggest ways to test/verify
5. ✓ Distinguish between what you know and what you're assuming

**If you have all 5, your answer is solid.**

---

## How to know YOU'RE WRONG:

1. ✗ Can't find the evidence in charts
2. ✗ Can't explain the mechanism
3. ✗ Ignoring confounding variables
4. ✗ Using correlation as proof of causation
5. ✗ No mention of uncertainty or limitations

**If you have any of these, reconsider your answer.**

---

---

# FINAL CHECKLIST BEFORE SUBMITTING YOUR TEST

- [ ] Did I reference specific numbers from the data?
- [ ] Did I explain WHY, not just WHAT?
- [ ] Did I distinguish between correlation and causation?
- [ ] Did I consider sample size and confounding variables?
- [ ] Did I mention limitations and uncertainty?
- [ ] Could someone else follow my logic?
- [ ] Did I avoid making unfounded causal claims?
- [ ] Is my recommendation specific and testable?

**If all are checked, you're ready!**
