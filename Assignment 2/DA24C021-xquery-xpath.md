[TOC]

#### Count of Instruments in the IT Services Sector

This query counts how many instruments are in the "IT Services" sector.

###### XQUERY

```xquery
let $count := count(for $instrument in //instrument where $instrument/stock/hasSector='IT Services' return $instrument)
return
	$count
```

Result:

>  2

###### XPATH

```sql
count(//instrument[stock/hasSector = 'IT Services'])
```

Result:

>  2



#### List of All Unique Sectors

This query retrieves a list of all unique sectors from the instruments.

###### XQUERY

```xquery
let $uniqueSectors := distinct-values(for $instrument in //instrument return $instrument/stock/hasSector)
return
	<result>
  		<sectors>
	   		{
    			for $sector in $uniqueSectors
      				return <sector>{$sector}</sector>
  			}
  		</sectors>
	</result>
```



Result:

```xml
<result>
    <sectors>
        <sector>Energy</sector>
        <sector>IT Services</sector>
        <sector>Banking</sector>
        <sector>Automobile</sector>
        <sector>Conglomerate</sector>
        <sector>Finance</sector>
        <sector>FMCG</sector>
        <sector>Mining</sector>
    </sectors>
</result>
```



###### XPATH

```sql
distinct-values(//instrument/stock/hasSector)
```



**Result**:

Energy

IT Services

Banking

Automobile

Conglomerate

Finance

FMCG

Mining





#### Count the Number of Instruments per Issuer

This query counts and lists the number of instruments issued by each issuer, providing a summary of the market's offerings by organization.

###### XQUERY

```xml
for $issuer in distinct-values(//instrument/hasIssuer)
let $count := count(//instrument[hasIssuer = $issuer])
return <issuer>
		<name>{$issuer}</name>
    	<count>{$count}</count>
  	</issuer>
```



**RESULT:**

```xml
<issuer>
    <name>Government of India</name>
    <count>4</count>
</issuer>
<issuer>
    <name>Tata Steel</name>
    <count>1</count>
</issuer>
<issuer>
    <name>Reliance Industries</name>
    <count>1</count>
</issuer>
<issuer>
    <name>Municipal Corporation</name>
    <count>2</count>
</issuer>
<issuer>
    <name>HDFC Ltd</name>
    <count>1</count>
</issuer>
<issuer>
    <name>Infosys</name>
    <count>1</count>
</issuer>
```

#### Retrieve All Short-Term Debt Funds

This query retrieves the names and returns of all short-term debt funds, providing a quick overview of this category.

###### XQUERY

```xquery
for $fund in //instrument[debtFund/hasTermType='Short-Term']
return <fund>{$fund/hasName/text()} - {$fund/hasReturn/text()}</fund>
```

RESULT:

```xml
<fund>ICICI Prudential Short-Term Fund - 7.1</fund>
<fund>SBI Short-Term Debt Fund - 6.8</fund>
<fund>HDFC Short-Term Fund - 7.4</fund>
<fund>Axis Short-Term Debt Fund - 6.9</fund>
<fund>Kotak Short-Term Fund - 7.2</fund>
```

###### XPATH

```sql
//instrument[debtFund/hasTermType='Short-Term']/hasName | //instrument[debtFund/hasTermType='Short-Term']/hasReturn
```



**RESULT**:

```xml
<hasName>ICICI Prudential Short-Term Fund</hasName>
<hasReturn>7.1</hasReturn>
<hasName>SBI Short-Term Debt Fund</hasName>
<hasReturn>6.8</hasReturn>
```

#### Count Funds by Liquidity Type

This query counts how many funds exist for each liquidity type (High, Moderate, Low), providing insight into the distribution of liquidity across the catalog.

###### XQUERY

```xquery
for $liquidity in distinct-values(//instrument/hasLiquidity)
let $count := count(//instrument[hasLiquidity=$liquidity])
return <liquidity type="{$liquidity}" count="{$count}"/>
```



**RESULT**:

```xml
<liquidity type="High" count="10"/>
<liquidity type="Moderate" count="15"/>
<liquidity type="Low" count="5"/>
```



###### XPATH

```sql
distinct-values(//instrument/hasLiquidity)
```



**RESULT**:

High
Moderate
Low

#### Get all instrument names with returns greater than 12%

This query retrieves the names of all instruments where the return is greater than 12%.

###### XQUERY:

```xquery
for $instrument in //instrument[hasReturn > 12]
return $instrument/hasName
```



**RESULT**:

```xml
<hasName>HDFC Nifty 50 Index Fund</hasName>
<hasName>ICICI Prudential Nifty Next 50 Index Fund</hasName>
<hasName>Kotak Nifty 50 Index Fund</hasName>
<hasName>Axis Real Estate Index Fund</hasName>
```



###### XPATH:

```sql
//instrument[hasReturn > 12]/hasName
```



**RESULT**:

```xml
<hasName>HDFC Nifty 50 Index Fund</hasName>
<hasName>ICICI Prudential Nifty Next 50 Index Fund</hasName>
<hasName>Kotak Nifty 50 Index Fund</hasName>
<hasName>Axis Real Estate Index Fund</hasName>
```

