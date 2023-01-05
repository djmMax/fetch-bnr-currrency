Yet another Prompt experiment

Goal: fetch the Echange Rate from the National Bank of Rwanda
Approach: being lazy as possible, I use a LLM for the task but it's still require too much work in my point of view

I used [ChatGPT Dec 15 Version](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) I hope I will be able to be more lazy with the future version.

Let's go.

BEGGINING OF THE PROMPT
--------- 
I want to retrieve currency exchange on this page https://www.bnr.rw/currency/exchange-rate/
they display it a table with the follwing structure
```html
<table class="table table-bordered table-hover">
	<thead>
		<tr>
			<th>Country</th>
			<th>Code</th>
			<th>Date</th>
			<th>Buying Value</th>
			<th>Average Value</th>
			<th>Selling Value</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><img src="fileadmin/Flags/eur.png" alt="EUR" title="EUR"></td>
			<td>EUR</td>
			<td>2023-01-04</td>
			<td> 1,121.146230 </td>
			<td> 1,132.356560 </td>
			<td> 1,143.566890 </td>
		</tr>
```

with the this button next in the paggination
```html
<ul class="f3-widget-paginator">
	...
	<li class="next">
		<a rel="next"
			href="currency/exchange-rate/?tx_bnrcurrencymanager_master%5B%40widget_0%5D%5BcurrentPage%5D=2&amp;cHash=665767745609d788d6ad87b3a9b6a081"><span
				class="glyphicon glyphicon-chevron-right"></span></a>
	</li>
</ul>
```
1. get the page
2. extract the table content in tbody 
3. add the etracted row in a list
4. find the next button and extract the next page url
5. goes to the next page (repeat the extraction) until the next button is not find
6. save everything in a csv

Note:
- use python, pandas, ... any library you think it's usefull
- print progressively, data, page, error, ... 

------------- 
END OF THE PROMPT


I give to ChatGPT to produce this code be they where some, mistake that I tried to prompt with but he didn't fix them:
1. `soup` is not defined on this line `next_button = soup.find('li', {'class': 'next'})`
2. in the next button we have a relative url, you should convert it to absolute url

I had to fix it myself, I made some change in the number format.
I think the model can fix it but his attention is to spread, it should be more attentive on what it's generating at the moment he's generating, but instead it seams distracted by all the previous code (or maybe the whole conversation), lack of focus, it's common among us human.
