# Assignment 1: Ontology Design

## Task - 1: A plain text description of the domain of interest and a list of concrete pieces of knowledge you would like to capture in the domain. 


The domain of interest is **Financial Modeling**. The goal is to develop a basic ontology model which aids 

- **Equity research** by capturing limited details of current and historical information related to given equity instrument in order to assess a security/stock's financial health and also query and filter securities which satisfies certain financial ratio requirements.
- **Portfolio Management** - grouping securities which satisifies certain finacial ratios and market conditions


Developing ontological model will help in framing questions related to equity research in a systematic and concise manner. For example some sample questions are listed below

- Which Stocks are in GrowthStage has high return in last quarter?
- Which Banking stock gave most return in year YYYY?
- Current year Stock price > Last year stock price?
- List stocks that are eligible to be in X portfolio?

#### Knowledge to be captured:

- **Financial Instrument**

  - Equity - Stock of a **Company** listed in some Market

  - Etf - Collection of stock
  
  - MutualFund - Collection of one or more Equity or Etf
  
  - FundofFund - Collection of one or more Mutual Fund
  
- **Equity**

  An Equity has following properties/relation :

  - Name  (eg. APPL, SBI)
  - Company  (eg. Apple Inc, State Bank of India) - equity belongs to a company
  - Equity metrics
  - Risk metrics
  - Balance sheet metrics
  - Peers : Companies which are operating in same sectors or industry

- **Equity Metric**

  - Price : price of a stock
  - Return : return over specified period
  - Dividend

- **Risk Metric**

  - beta
  - volatility
  - sharpe ratio

- **Balance Sheet Metric**

  - **Balance Sheet Ratios**
    - Current : Measures solvency
    - Quick : Measures liquidity
    - Debt-to-Worth : Measures financial risk
  - **Efficiency Ratios**
    - Sales-To-Assets : Measures the efficiency of Total Assets in generating sales
    - Return On Assets : Measures the efficiency of Total Assets in generating Net Profit
    - Return On Investment : Measures the efficiency of Net Worth in generating Net Profit

- **Market structure**

  - Category (eg. SmallCap, MidCap, LargeCap, etc)
  - MarketIndex : Index/Equity to which the stock is benchmarked against
  - Sector : market classification of stock (Banking , IT , Manafacturing)
  - Stage : Lifecycle stage at which company is in (DevelopmentStage, GrowthStage, SustainabilityStage, ExpansionStage)

- **Time aspects**

  - Year (FY2022, FY2023 etc )
  - Quarter (Q2023-1, Q2023-2, Q2023-3, .....)

- **Portfolio** - collection of equity

  - Growth
  - Value
  - Balanced



## Task - 2 : the DL ontology (TBox) 

Now we will model the key concepts and relationships in order to capture above domain knowledge

#### Classes and Subclasses (Concept Inclusions -Subsumption Axiom)

- Company
  - HoldingCompany

- Name
  - CompanyName
  - StockName
- Category 
- BusinessStage 
- Sector 
- MarketIndex (Nifty, BankNifty)
- Instrument
  - Stock 
  - Etf
  - MutualFund
  - FundofFund
- [TemporalEntity](https://spec.edmcouncil.org/fibo/ontology?query=https://www.omg.org/spec/Commons/DatesAndTimes/TemporalEntity) (referred from FIBO)
  - TimeInterval
    - CalendarPeriod
      - CalendarYear 
      - CalendarQuarter 
- Metric
  - EquityMetric
    - Return 
    - Dividend
    - MarketCapitalization
  - RiskMetric
    - Beta
    - Volatility  (Volatility ⊑ RiskMetric)
    - Sharpe ratio

  - MonetaryAmount

    - BalanceStatement
      - Profit
      - Price
      - Income
      - Asset
      - Liability


#### Some of the Relationships 

- Transitive Roles
  - owns : (Company$\to$Company) A company can own other company
  - has: (Instrument $\to$ Instrument) A instrument can be part of other instrument
  - hasPeer: (Company$\to$ Company)

- isInStage: (Company$\to$ BusinessStage)
- belongsTo: (Company$\to$ Sector), 
- benchmarkedBy: ( Instrument$\to$MarketIndex)
- isIn: (Stock$\to$Portfolio)
- holds: (Portfolio$\to$Stock)
- hasPrice : (Stock$\to$ Price)
- hasReturn : (Stock$\to$ Return)
- hasDividend : (Stock$\to$ Dividend)
- hasMarketCapitalization : (Stock $\to$ MarketCapitalization)
- observedIn : (Metric$\to$ TimePeriod)
- hasProfit : (Profit $\to$ Company)
- hasDividend : (Profit $\to$ Company)
- observedIn : (MonetaryAmount$\to$ TimePeriod)
- hasValue :  (Metric$\to$ NumericValue)

#### Axioms

- Company, Stock has always a unique name

  > Company $⊑ (=1$ hasName.Name$)$
  > Stock	 $⊑ (=1$ hasName.Name$)$ 

- CompanyName and StockName are disjoint

  > CompanyName $⊓$ StockName $⊑ ⊥$

- Company is part of a sector

  > Company $⊑∃$belongsTo.Sector

- Company must be in some growth stage

  > Company $⊑ ∃$isInStage.BusinessStage

- Heirarchial role of Instruments

  - Etf $⊑ ∃$has.Stock
  - MutualFund $⊑ ∃$has.Stock $⊔$ $∃$has.ETF
  - FundofFund $⊑∃$has.ETF $⊔$ $∃$has.MutualFund

- Portfolio holds at least one stock:

  > Portfolio $⊑ ∃$holds.Stock

- An stock must have a price, return, and volatility:

  > Stock $⊑ ∃$hasPrice.Price $⊓ ∃$hasReturn.Return $⊓ ∃$hasVolatility.Volatility

- Price, return, and volatility are observed in specific time periods:

> Price $⊑ ∃$observedIn.TimeInterval
> Return $⊑ ∃$observedIn.TimeInterval
> Volatility $⊑ ∃$observedIn.TimeInterval

- Midcap : companies with a moderate market capitalisation ranging from Rs. 5,000 crores to Rs. 20,000 crores

  > Midcap $⊑$  Stock ⊓ (hasMarketCapitalization ≥ 5000) ⊓ (hasMarketCapitalization ≤ 20000)

- Smallcap : company whose market capitalization is less than Rs 5,000 crores are known as small-cap companie

> 

- Largecap : company with market caps of ₹20,000 crore or more

> 

- Balanced portfolios cannot hold more than 30% of equities from the same sector:

  > BalancedPortfolio $⊑ ∃$ holds.(Stock $⊓$ (hasVolatility $≥$ 0.3)) $⊓$ ($\ge3$ holds.Stock)

- LowVolatile portfolios holds more than 3 equities each having volatility lesser than 0.3:

  > LowVolatile $⊑ ∃$ holds.(Equity $⊓$ (hasVolatility $<$ 0.3)) $⊓$ ($\ge3$ holds.Stock)

### Task - 3 : a write-up about the design choices made and the details of the design - the explanations for classes, properties, DL axioms, motivating situations/examples - of terms in the ontology. 




Design choices 

- Use of Transitive roles : The company can have ownership chain say CompnayA can own CompanyB and Company B owns Company C which was captured by transitive role `owns`. Similar transitive role `has` also captures relation like Etf has Stock and Mutual fund can have both Stock and ETFs
- Concept Disjointness -  TODO
- Inverse Role Axioms -  TODO
- Cardinality Restrictions  -  TODO
- Nominal Axioms (Individual Equality/Disjointness)  -  TODO

Classes
- Company - A registered business according to laws.


Note: Please keep the overall goal of the full set of assignments in mind while designing the ontology. You can plan to have members of the primitive symbols (concepts and relationships) available/ extractable from XML data you would generate later in Assignment 2.

















