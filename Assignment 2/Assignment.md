**Submission By**

DA24C021 - Venkatesh Duraiarasan

CS24M033 - Pradeep Peter Murmu

# Assignment 2: XML Data Design

[TOC]

### Group task

#### DTD for  Stocks.xml

```xml
<!ELEMENT instruments (instrument+)>
<!ELEMENT instrument (hasName, hasReturn, hasIssuer, hasLiquidity, stock)>
<!ELEMENT hasName (#PCDATA)>
<!ELEMENT hasReturn (#PCDATA)>
<!ELEMENT hasIssuer (issuer)>
<!ELEMENT hasLiquidity (#PCDATA)>

<!ELEMENT stock (listedIn, hasTicker, hasPeType, hasVotingRight, hasSector, hasVolatilityType, hasMarketCapType, type)>
<!ELEMENT listedIn (#PCDATA)>
<!ELEMENT hasTicker (#PCDATA)>
<!ELEMENT hasPeType (#PCDATA)>
<!ELEMENT hasVotingRight (#PCDATA)>
<!ELEMENT hasSector (#PCDATA)>
<!ELEMENT hasVolatilityType (#PCDATA)>
<!ELEMENT hasMarketCapType (#PCDATA)>
<!ELEMENT type (#PCDATA)>
```



The DTD (Document Type Definition) defines the structure of an XML document that represents financial instruments, specifically stocks. Here’s a brief description:

1. **Root Element:**

   - The root element `<instruments>` is designed to contain one or more `<instrument>` elements. This is indicated by the `+` symbol, meaning that there must be at least one `<instrument>` element present in the XML document.

2. **Instrument Element:**

   - Each `<instrument>` element represents an individual financial instrument and is required to include the following child elements:
     - `<hasName>`: Contains the name of the instrument as text data (`#PCDATA`).
     - `<hasReturn>`: Represents the return rate of the instrument, also as text data.
     - `<hasIssuer>`: Specifies the issuer of the instrument.
     - `<hasLiquidity>`: Describes the liquidity level of the instrument.

   Additionally, each `<instrument>` must include a `<stock>` element that holds details specific to stock-type instruments.

3. **Stock Element:**

   - The `<stock>` element represents stock-specific properties and is composed of the following child elements:
     - `<listedIn>`: Describes the stock exchanges where the stock is listed.
     - `<hasTicker>`: Contains the stock's ticker symbol.
     - `<hasPeType>`: Refers to the Price-to-Earnings (P/E) type classification.
     - `<hasVotingRight>`: Indicates whether the stock provides voting rights.
     - `<hasSector>`: Represents the economic sector to which the stock belongs.
     - `<hasVolatilityType>`: Classifies the stock’s volatility level.
     - `<hasMarketCapType>`: Describes the stock's market capitalization category (e.g., large-cap, mid-cap).
     - `<type>`: Specifies the type of stock (e.g., common stock, preferred stock).

4. **PCDATA Elements:**

   - All the terminal elements (`hasName`, `hasReturn`, `hasIssuer`, `hasLiquidity`, etc.) contain `#PCDATA`, which means they hold parsed character data (i.e., textual content).

#### DTD for  Mutual fund.xml

```xml
    <!ELEMENT mutualFund (hasRisk, hasInstrument, hasManager, type)>
    <!ELEMENT hasRisk (#PCDATA)>
    <!ELEMENT hasInstrument (Instrument)>
    <!ELEMENT hasManager (#PCDATA)>
    <!ELEMENT type (#PCDATA)>
```

This DTD defines the structure of an XML document that represents financial instruments, specifically focusing on mutual funds. Here’s a brief description of its design:

1. **Mutual Fund Element:**
   - The `<mutualFund>` element represents mutual fund-specific attributes and includes four child elements:
     - `<hasRisk>`: Describes the risk level of the mutual fund (e.g., "Low", "High").
     - `<hasInstrument>`: Refers to the underlying instrument or asset the mutual fund is based on.
     - `<hasManager>`: Contains information about the fund manager.
     - `<type>`: Specifies the type of mutual fund (e.g., "Equity Fund", "Debt Fund").

#### DTD for Index.xml

```xml
<!DOCTYPE indices [
    <!ELEMENT indices (index+)>
    <!ELEMENT index (hasName, hasStock, hasReturn, hasType)>
    <!ELEMENT hasName (#PCDATA)>
    <!ELEMENT hasStock (stock)>
    <!ELEMENT hasReturn (#PCDATA)>
    <!ELEMENT hasType (#PCDATA)>
]>
```



The Document Type Definition (DTD) provided defines the structure for an XML document that represents a collection of financial indices. Here’s a breakdown of the components:

- **Root Element:**
  - This element serves as the container for multiple `<index>` elements, indicating that the document can have one or more indices.

- **Child Element:**
  - Each `<index>` element encapsulates information about a specific financial index. It includes four sub-elements that describe various attributes of the index.

- **Sub-elements of** 
  - `<hasName>`: Contains the name of the index (e.g., "Nifty 50"). This element is defined to hold parsed character data (PCDATA), allowing it to store textual information.

  - `<hasStock>`: Describes the type of stocks or assets tracked by the index (e.g., "Large Cap Stocks"). It also holds PCDATA.

  - `<hasReturn>`: Represents the average return of the index. This element is designed to hold PCDATA, allowing for numerical values or textual representations of returns.

  - `<hasType>`: Specifies the category of the index (e.g., "Equity Index"). It allows for textual data and is defined as PCDATA.

#### DTD for  Issuer.xml

```xml
<!DOCTYPE issuers [
    <!ELEMENT issuers (issuer+)>
    <!ELEMENT issuer (name, issuerType, hasCountry)>
    <!ELEMENT name (#PCDATA)>
    <!ELEMENT issuerType (#PCDATA)>
    <!ELEMENT hasCountry (#PCDATA)>
]>
```



The  DTD describes about the xml structure of financial issuers.

Structure Overview:

1. **Root Element:**
   - The root element is `<issuers>`, which serves as a container for one or more `<issuer>` elements. The use of `issuer+` indicates that there must be at least one `<issuer>` present within the `<issuers>` element, allowing for a flexible number of issuers.

2. **Issuer Element:**
   - Each `<issuer>` element represents a distinct financial issuer and includes three required child elements:
     - `<name>`: Contains the name of the issuer, represented as parsed character data (PCDATA), which allows for text content such as company names (e.g., "Reliance Industries").
     - `<issuerType>`: Defines the type of issuer (e.g., corporation, government), also as PCDATA. This allows for clarity in distinguishing different issuer categories.
     - `<hasCountry>`: Specifies the country of the issuer, again using PCDATA for textual representation (e.g., "India", "USA").

   

#### DTD about Bonds

```xml
    <!ELEMENT Bond (hasCouponRate, hasTermType)>
    <!ELEMENT hasCouponRate (#PCDATA)>
    <!ELEMENT hasTermType (#PCDATA)>
```



The Document Type Definition (DTD) provided outlines the structure for an XML document that represents a collection of  bonds. 

**Sub-elements of** **Bond**

- `<hasCouponRate>`: Specifies the coupon rate of the bond (e.g., "5.70"). This element holds PCDATA, allowing for numerical representation.
  
- `<hasTermType>`: Describes the type of term for the bond (e.g., "Fixed"). It uses PCDATA to store descriptive textual data.
