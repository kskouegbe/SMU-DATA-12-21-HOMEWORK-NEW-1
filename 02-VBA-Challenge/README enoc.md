# The VBA of Wall Street

VBA Stock Market analysis 

**Background**

To be able to evaluate years of stock market data, a VBA script was created. Within a workbook, each year is divided into its own tab.

I used the test excel document to develop the script and then pasted it into the final excel document to verify it was done correctly.

**How to use the Script**

The script is in the repository labeled VBA Script
To test this, first you will need multiple pages of stock data that include, a ticker symbol, yearly open, yearly close, date, stock range.
Once you have this excel document, open the developer tool and add in a module. Paste the script in and press run. 
This should loop through as many pages as you have. It will calculate the data and will give you information on the ticker, yearly change, yearly percent change, and total stock. 
    This can be broken down by year, or in the test was done by alphabetical Ticker
    There is conditional formatting added in to highlight negative trends in red and positive trends in green. 
There is also a calculation to show the greatest percent increase & decrease as well as greatest total volume. 
