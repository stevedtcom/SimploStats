'''
SimploStats app
'''
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.screenmanager import FadeTransition, SlideTransition, SwapTransition, WipeTransition, NoTransition

from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.filechooser import FileChooserIconView
from kivymd.uix.filemanager import MDFileManager
import random
import json
import calendar
import time
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from datetime import datetime, timedelta
from kivy.properties import StringProperty
from kivy.animation import Animation
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.textfield import MDTextField
from kivy.uix.textinput import TextInput
from kivy.uix.progressbar import ProgressBar
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.clipboard import Clipboard
from kivymd.uix.spinner import MDSpinner
from kivy.metrics import sp
from kivy.metrics import dp
import webbrowser
from kivy.properties import NumericProperty
from functools import partial
from kivy.graphics import Rectangle, Color, Line
from kivy.graphics import Ellipse, Color

from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.button import MDFlatButton

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.uix.rst import RstDocument
from kivy.uix.scatter import Scatter
from kivy.uix.scrollview import ScrollView
from kivy.uix.spinner import Spinner
import threading
import csv
import os
from kivy.graphics.texture import Texture
from kivy.uix.image import Image
from kivy.utils import platform
from kivymd.uix.label import MDLabel
from kivymd.toast import toast

from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior

from plyer import storagepath
from jnius import autoclass
from plyer import notification
import kivy

from kivy.uix.image import Image

kivy.require("2.2.1")


'''
app secret key and files updates

when updating files, remember:
	
on launching (load data) function ✓✓✓✓
replacing the main file function ✓✓✓✓
reseting the main file function ✓✓✓✓
closing the business fumction ✓✓✓✓
importing the file function ✓✓✓✓
(They are vital in global financial data and fin_data_file)

updating budgets, assets and accum depreciation files

deleting journal records ✓✓
reseting app ✓✓
deleting accounts ✓✓
shifting accounts ✓✓
'''

app_key = "ddjfj-d5i463iwourjd_rj0p4dkkkru-d43mhaphjfjj"

'''
load data saved in json file (.ssdata)
'''
global fin_data_file

'''
fin_data_file = '/storage/emulated/0/Documents/Pydroid3/Accounting Software/akauntin_financial_data_123.aknt'
back_to_app_file = '/storage/emulated/0/Documents/Pydroid3/Accounting Software/akauntin_financial_data_123.aknt'
'''

global back_to_app_file

'''
load financial data
'''


'''
simplostats help
'''

charts_help = '''The Chart of Accounts is a pivotal component within the accounting framework of the "SimploStats" app, 
serving as a structured and comprehensive repository for ledger accounts.

In the realm of accounting principles, the Chart of Accounts is fundamental to maintaining an organized and systematic approach to financial record-keeping.

It embodies a hierarchical structure that categorizes and classifies various accounts, facilitating the efficient management of financial transactions and ensuring adherence to accounting standards.

In essence, the Chart of Accounts is a dynamic tool that reflects the financial landscape of an organization, encompassing assets, liabilities, equity, revenues, and expenses.

Each account within the chart is assigned a unique space, enabling quick and precise identification.
This systematic arrangement aligns with the principle of consistency, fostering uniformity in financial reporting and analysis.

The "SimploStats" apps Chart of Accounts panel is designed with meticulous attention to detail, accommodating the diverse needs of users engaged in different business sectors. 
The panel embodies the principle of relevance by allowing users to tailor the chart to their specific industry, ensuring that the accounts listed are pertinent to their financial activities.
'''

about_categories =  '''Our Charts of Accounts has the following Spaces / Categories:

1. Capital:
Aimed to add accounts that relate to equity and reserves. e.g. shares, premiums, capital reserves e.t.c.

2. Non Current Assets:
Add all non current assets to this category. e.g. vehicles, land, building, property and machineries, investments e.t.c

3. Current Assets:
add your accounts receivables, inventories and marketable securities to this category. Create an account for each customer and any current asset you may have e.g. prepayments, SimploStats Debtor, marketable securities e.t.c.

4. Bank:
Add all your cash and bank accounts to this category and enhance management to your bank accounts

5. Operating Revenue:
Add all primary sources of incomes to this category, including sales account, other primary revenues e.t.c

6. Cost of Sales:
Add all costs associated with generation of Operating Revenue. e.g. purchases, opening stock, closing stock, carriage inwards e.t.c

7. Non Current Liabilities:
Add accounts that has liability for period over one year. e.g. bank loan, e.t.c

8. Current Liabilities:
Add all accounts.payables to this category and liabilities to be paid in less than one year. e.g. Accruals, suppliers e.t.c

9. Taxes:
Add all tax accounts to this category. e.g. corporate taxes, income taxes, e.t.c

10. Operating Expenses:
Add all accounts that are direct operational costs. e.g. Administrative costs, water, salaries, rent, electricity, transport e.t.c.

11. Other expenses:
Add accounts that have expenses that does not relate to direct operations. e.g. donations, social responsibility e.t.c

12: Other Incomes
Add all non operating incomes to this category. e.g. dividends income, proceeds from disposal of assets, e.t.c
'''

about_journal = '''We are delighted to share that making journal entries in our accounting app has never been more straightforward.

With our user-friendly interface, you can effortlessly record your financial transactions, ensuring accuracy and efficiency in your bookkeeping process.

When making a journal entry, simply input the relevant details such as the transaction date, a concise description, the transaction amount, and select the appropriate accounts.
Our app intuitively guides you through the process, making it easy for you to maintain meticulous financial records.

What sets our system apart is the issuance of a unique identifier for each transaction.

This transaction ID not only provides a distinct reference but also contributes to the traceability and audit trail of your financial activities.

It aligns with our commitment to ensuring transparency and accountability in your accounting practices.	
'''

about_view_journal =  '''Introducing our Ledger Accounts Panel, a powerful feature in our accounting app that provides a comprehensive view of your financial transactions with precision and ease.

This dynamic panel allows users to filter ledger accounts based on dates, offering a tailored perspective on financial activities within specific time frames.
What sets it apart is the automatic calculation of a Balance Brought Down figure (previous balances), simplifying the reconciliation process and ensuring accuracy in your financial records.

Moreover, our Ledger Accounts Panel presents a consolidated snapshot of totals in both credit and debit, providing instant insights into your financial standing. 
Balances are conveniently displayed, offering a holistic view of your financial position at a glance.

Effortlessly navigate through your ledger accounts, track balances, and make informed financial decisions with our user-friendly Ledger Accounts Panel
'''

about_income_statement =  '''Introducing our Income Statement Panel – a dynamic tool in our accounting app that enhances financial insights with precision and efficiency.
Tailor your view by filtering dates, enabling a focused analysis of income and expenses.

This specialized panel goes beyond conventional displays by automatically calculating both Gross and Net Profits. 
Witness a comprehensive breakdown of revenues, costs, and ultimately, your bottom line.

With clear, concise figures at your fingertips, our Income Statement Panel empowers you to make informed decisions and steer your financial strategy with confidence.
Simplify your financial analysis and elevate your understanding of profitability.

Explore the Income Statement Panel in our accounting app for a streamlined approach to tracking and optimizing your financial performance.
'''

about_balance_sheet = '''Introducing our Balance Sheet Panel, a pivotal feature in our accounting app designed to provide a snapshot of your financial position as of a specific date.
This dynamic tool allows users to filter data and view assets, liabilities, and equity in a clear and organized manner.

What sets our Balance Sheet Panel apart is its unique ability to calculate the Net Profit or Loss in the Capital category.
By effortlessly capturing and reconciling financial data, it ensures accurate representation of the companys financial health.

This feature aligns with our commitment to empowering users with real-time insights into their net worth.
'''

about_trial_balance =  '''Introducing our Trial Balance Panel in the accounting app – a robust feature offering a concise snapshot of your financial standing as of specific dates. 
With a user-friendly interface, this panel presents a balanced view of debit and credit accounts.

Effortlessly filter data to view Trial Balances, providing a comprehensive overview of your financial transactions.
This tool streamlines the reconciliation process, ensuring accuracy in your accounting records.

Simplify your financial analysis and enhance your decision-making process with our Trial Balance Panel.
Gain valuable insights into your financial health and streamline your accounting practices effortlessly.
'''

about_op_analysis = '''Operations Analysis:

In the accounting app, the dedicated function to compare and identify variances between two distinct periods, each further segmented into specific dates, holds significant importance for effective financial management and decision-making.

Here`s a summary to inform users about the significance of this comparison feature:

Performance Evaluation:
By comparing financial data across different periods, users gain valuable insights into the performance of their business. Identifying variances allows for a comprehensive assessment of revenue, expenses, and overall financial health.

Trend Analysis:
Periodic comparisons enable users to conduct trend analysis. Recognizing patterns and trends in financial data over time aids in making informed predictions and strategic decisions for the future.

Expense Management:
Users can pinpoint variations in expenses and revenue streams between periods.
This helps in identifying cost inefficiencies, optimizing resource allocation, and enhancing overall expense management strategies.

Budgeting and Planning:
Comparisons assist in evaluating the effectiveness of budgeting and planning efforts.
Users can assess whether they are meeting financial goals and make adjustments to budgets based on historical performance.

Decision-Making Support:
Armed with insights from period-to-period comparisons, users can make well-informed decisions.
Whether it`s adjusting pricing strategies, revising marketing plans, or optimizing operations, the data aids in decision-making processes.

Compliance and Reporting:
Periodic comparisons contribute to accurate financial reporting and compliance.
Users can easily track changes, ensuring that financial statements align with regulatory requirements and industry standards.
'''

about_balances =  '''The "Balances Analysis" panel in our accounting app is crucial as it empowers users to gain insights into their financial positions over specific timeframes.

By allowing users to input the number of days from today, they can analyze account balances dynamically, aiding in financial planning, tracking trends, and making informed decisions based on recent financial data.

This feature enhances the user`s ability to monitor and understand their financial health with flexibility and precision.

The Balances panel also enable users to view the Historical Costs of Non Current Assets and their Accumulated depreciation
'''

about_budget =  '''The accounting app features a comprehensive panel designed for budget management across various accounts.

Users can input budget allocations for each account within the App.

Additionally, the panel offers a functionality to compare actual expenditures or revenues with the set budgets.

This comparison can be conducted annually, semi-annually, or quarterly, providing users with insights into budget variances for each account over specified time frames.

Such analysis aids businesses in understanding financial performance, identifying discrepancies, and making informed decisions for future budgeting and resource allocation.
'''

about_storage_folder = '''In our ongoing commitment to provide you with a tailored and efficient accounting experience,

we`ve introduced a feature allowing you to select a dedicated backup folder for storing exported files and screenshots. 
Find this selection panel conveniently located in your business profile page.

Key Recommendations:

Folder Selection:
Take a moment to choose a backup folder that aligns with your organizational preferences.
This selected folder will serve as the dedicated space for storing backups, exported files, and screenshots.

Avoid Root Storage:
We strongly advise against using the root storage for these purposes.
Instead, create a new storage folder within your preferred directory—be it in the "Documents" or "Downloads" folder.

By adhering to these recommendations, you not only optimize the organization of your accounting data but also ensure easy access and retrieval when needed.
This small adjustment contributes to a more streamlined and user-friendly accounting journey.
'''

about_start_dates = '''Setting the correct financial start and end dates is paramount in maintaining accurate and meaningful financial records.

These dates serve as crucial parameters when calculating balances of transactions within a specific period.

By establishing the correct start date, businesses can accurately capture the commencement point for financial transactions.

This precision ensures that all relevant transactions from the beginning of the designated period are considered, preventing oversight and guaranteeing a comprehensive financial overview.

Likewise, defining an accurate end date is equally crucial. 
It demarcates the conclusion of the financial period and is instrumental in calculating balances, profits, and losses.
An incorrect end date may lead to miscalculations, potentially distorting financial statements and hindering the ability to make informed decisions based on the most up-to-date and relevant data

In the app, start and end dates are vital when closing the business and formulating financial information
'''

about_opening_bal =  '''"Opening Balance Equity" is a "temporary account" found within the Capital category in this app.

It is used to facilitate the recording of the double-entry system when transitioning from one accounting period to another, particularly during the startup of a new business or at the beginning of a fiscal year.

Opening Balance Equity helps maintain the integrity of the double-entry accounting system.

It serves as the counterpart to various accounts that receive opening balances, ensuring that the accounting equation: 
          (Assets = Liabilities + Equity)
remains balanced.

Once the opening balances are allocated to individual accounts, the Opening Balance Equity account should be closed or adjusted to zero.

This ensures that it does not impact financial reports or distort the company`s true equity position.
'''

about_cos_op =  '''The categories of "Operating Revenue" and "Cost of Sales" play a pivotal role in maintaining accurate and insightful financial records for our accounting app.

These categories serve as fundamental pillars for financial analysis, decision-making, and overall business performance evaluation.

Operating Revenue:
The category acts as a key indicator of a company`s primary income source, reflecting the total revenue generated from sales of goods or services.

Accurate tracking of sales/operating revenue is crucial for assessing the financial health of the business, determining growth trends, and identifying successful products or services.

Cost of Sales:
The category represents the direct costs associated with producing goods or services, including materials, labor, and other production-related expenses

Properly documenting cost of sales is essential for calculating gross profit margins, evaluating operational efficiency, and making informed pricing decisions to ensure profitability.
'''

about_passwords = '''
Users may protect their records using a password.

You should seek to remember the password at all times.

You can remove password protection and change it by entering new password from home panel "Business".

However, incase you forget your password, you can login to the app using a special combination of start and end dates of business financial year as follows:
        
        start_date,end_date
         e.g..   01-12-2025,30-11-2026
'''

about_taxes =  '''In compliance with government regulations, we have created a "Taxes" Category.

The category is aimed to add accounts to record taxes payments and liabilities, an automatic percentage of taxes account shall be calculated based on total incomes

On Financial Analysis page, we have created a simple calculator that give the taxable amount of total income based on a percentage entered by users.

Users can record taxes by debiting saved tax account from taxes category and crediting tax liability or bank account	
'''

about_depreciation = '''To maintain accurate financial records in your accounting app, please ensure that all depreciation entries are recorded exclusively in the designated "Depreciation" account within the Operating and Other Expenses category.

This specialized account is tailored to track accumulated depreciation effectively.

We have a special panel from "Special Journals" to help in recording Depreciation and Accumulated depreciation. 

Recording depreciation in other accounts may lead to incorrect financial information and distort your overall financial analysis.

Beware that our Balance sheet shows the Cost, Accumulated depreciation, and Net book value of Non Current Assets.
 
However, the above are shown only when viewing the Balance sheet as at today (Latest day).

Viewing balance sheet as at previous days show only the NBV of Non Current Assets
'''

about_accum_dep =  '''In our accounting app, we`ve implemented a unique method to accurately capture opening balances of Accounts, Assets and accumulated depreciation while adhering to the historical cost concept.

We have special panel in "Special Journals" to record the accumulated depreciation and opening balances.

However, to record accumulated depreciation as an opening balance for the financial year from Journal Entries page:

1. Initialize Debit-Credit Process:
Begin by debiting the asset account at its original cost and simultaneously crediting the "Opening Balance Equity" account.

This step ensures that the historical cost of the asset is appropriately recorded.(See help no. 8 to understand about "Opening Balance Equity")

2. Subsequent Entry:
Next, credit the asset account (offsetting its value) with accumulated depreciation and debit the "Opening Balance Equity" account.

3. Utilize Special Button:
To facilitate this specific recording, users must toggle a designated button from `journal entry` to `accum depreciation`.

This button is strategically positioned adjacent to the amounts text field within the `Make Journal Entry` screen.

This maneuver helps in reflecting the accumulated depreciation, albeit not in the current books, but rather as an opening balance adjustment.

4. Accounting Insight & Warning:
Adhering to this procedure is paramount to maintain the integrity of your financial records.
Failure to follow these steps meticulously may result in misrepresentation of asset values, accumulated depreciation, and overall financial health of the organization.

It`s crucial to understand that accumulated depreciation is not merely an entry but a reflection of an asset`s wear and tear over time.

Thus, by following our outlined steps and using the special button, users ensure that the asset`s net book value is correctly depicted, aligning with the principles of the historical cost concept.

Always exercise diligence and precision when recording such critical financial data
'''

about_retained_earnings =  '''We`re pleased to introduce a seamless feature in our accounting app designed to streamline your financial year-end processes.

Recognizing the significance of retained earnings in reflecting a company`s financial journey, we have incorporated an automatic year-end closing mechanism in "Files and Passwords"

Here`s what you need to know:

Effortless Transition: At the close of each financial year, our app automatically transfers current financial information balances to the subsequent year.

This transition is meticulously executed to ensure accuracy and continuity in your financial records.

Retained Earnings Recording: As part of this automated process, the app intelligently calculates and records the retained earnings for the year.

This feature alleviates the manual effort typically associated with year-end closing activities, enabling you to focus on strategic financial planning and analysis.

User-Friendly Interface: While the app handles the intricate calculations and adjustments behind the scenes, users will benefit from a user-friendly interface that provides transparency and control over their financial data.

By leveraging our automatic year-end closing feature, you can navigate the complexities of financial accounting with confidence, knowing that your retained earnings are accurately recorded and carried forward into the next fiscal year.

Embrace efficiency, accuracy, and convenience with our enhanced accounting app functionalities
'''

about_export_reports = '''Exporting functionality is only available to main financial reports, and not to splitted reports.

Instead, use our app to view splitted reports and only export main reports.

You can export:
1. Income statement between any splitted dates

2. Account journal entries between any splitted dates

3. Statement of Financial Position as at selected date, and as from saved start date of financial year

4. Trial balance the same as statement of financial position

5. The budget can be exported between splitted dates, either Annually, Semi-Annually or Quartely and for Only Expenses and Incomes

However, you can play around by changing the start date for your financial year to export specific reports between your desired time frame.

Please remember to change financial year settings date back to original in order to generate accurate dashboard items and other reports.
'''

about_summary = '''Date-based Analysis:
Use the date filter to narrow down financial records for specific periods.
Whether it`s a monthly overview or a detailed analysis for a particular date range, tailor your reports to fit your needs.

Category-based Segmentation:
Segment your financial records based on categories.
This allows you to focus on specific types of transactions, gaining a clearer understanding of where your money goes.

Budget Splitting Options:
Choose how you want to split your budget: annually, semi-annually, or quarterly.
This feature provides a comprehensive view of your budget distribution over time.

Customizable Display:
Adjust the font size and other display preferences to enhance readability.
Tailor the visual representation of your reports to suit your preferences and improve overall user experience.

Dynamic Filtering:
Combine multiple filters simultaneously to refine your reports further.
This dynamic filtering capability ensures that you precisely capture the financial data relevant to your analysis.
'''

about_show_tip = 'This is a help panel'

class SimploStatsHelp():
	def search_for_help(self, user_search):
		user_search = user_search.split()
		
		charts = ['charts', 'chart', 'list', 'lists']
		about_categories = ['operating', 'expenses', 'expense', 'asset', 'assets', 'income', 'incomes',
		'liability', 'liabilities', 'sales', 'revenue', 'cost', 'operating', 'non', 'capital', 'earning', 'earnings',
		'retained', 'reserves', 'account', 'accounts', 'sale', 'categories', 'category', 'add']
		about_journal = ['journal', 'journals', 'save', 'enter', 'record', 'delete', 'edit', 'debit', 'credit']
		about_view_journal = ['view', 'ledgers', 'ledger', 'balances', 'amount', 'amounts', 'date', 'dates', 'id', 'ids',
		 'total', 'totals', 'row', 'rows', 'column', 'columns', 'previous', 'prior']
		about_income_statement = ['comprehensive', 'statement', 'profit', 'profits', 'net', 'gross', 'generated']
		about_balance_sheet = ['balance', 'sheet', 'position', 'balancing']
		about_trial_balance = ['trial', 'trials', 'reconcile', 'debits', 'credits']
		about_op_analysis = ['operation', 'operations', 'periodic', 'comparison', 'group', 'groups', 'operate', 'compare']
		about_balances = ['day', 'days', 'prior', 'today', 'ago', 'trend']
		about_budget = ['budget', 'budgets', 'variances', 'variance', 'budgeting', 'allocate', 'allocation', 'percentage', '%', 'percent']
		about_storage_folder = ['storage', 'folder', 'store', 'save', 'documents', 'document', 'download',
		'downloads', 'root', 'export', 'screenshot', 'csv', 'file', 'excel']
		about_start_dates = ['start', 'end', 'year', 'period', 'financial', 'finance', 'accounting', 'one']
		about_opening_bal = ['open', 'opening', 'equity', 'adjust', 'adjusted', 'previous', 'brought', 'down', 'forward', 'last']
		about_cos_op = ['special', 'purchases', 'carriage', 'inwards', 'return', 'returns']
		about_passwords = ['password', 'pass', 'security', 'secure', 'secret', 'reset', 'forgot', 'forget', 'combination', 'passwords']
		about_taxes = ['tax', 'taxes', 'legal', 'government', 'corporate', '30', 'calculation', 'pay', 'remit', 'liability']
		about_depreciation = ['depreciation', 'depreciate', 'machinery', 'building', 'buildings', 'allocate', 'allocation']
		about_accum_dep = ['accumulated', 'accumulate', 'historical', 'at cost', 'over', 'net', 'book', 'value']
		about_retained_earnings = ['retain', 'retained', 'earning', 'earnings', 'close', 'business', 'next', 'profit']
		about_export_reports = ['export', 'backup', 'path', 'google', 'drive', 'csv', 'import', 'importing', 'capture', 'camera', 'capturing']
		about_summary = ['summary', 'summarize', 'periodic']
		
		for word in user_search:
			if word.lower() in charts:
				return self.get_help('charts_of_accounts')
			elif word.lower() in about_categories:
				return self.get_help('categories')
			elif word.lower() in about_journal:
				return self.get_help('Journal_entries')
			elif word.lower() in about_view_journal:
				return self.get_help('view_accounts')
			elif word.lower() in about_income_statement:
				return self.get_help('income_statement')
			elif word.lower() in about_balance_sheet:
				return self.get_help('balance_sheet')
			elif word.lower() in about_trial_balance:
				return self.get_help('trial_balance')
			elif word.lower() in about_op_analysis:
				return self.get_help('operations')
			elif word.lower() in about_balances:
				return self.get_help('balances')
			elif word.lower() in about_budget:
				return self.get_help('budget')
			elif word.lower() in about_storage_folder:
				return self.get_help('storage_folder')
			elif word.lower() in about_start_dates:
				return self.get_help('start_end_dates')
			elif word.lower() in about_opening_bal:
				return self.get_help('opening_balance')
			elif word.lower() in about_cos_op:
				return self.get_help('special_accounts')
			elif word.lower() in about_passwords:
				return self.get_help('passwords')
			elif word.lower() in about_taxes:
				return self.get_help('taxes')
			elif word.lower() in about_depreciation:
				return self.get_help('dep')
			elif word.lower() in about_accum_dep:
				return self.get_help('accum_dep')
			elif word.lower() in about_retained_earnings:
				return self.get_help('retained_earnings')
			elif word.lower() in about_export_reports:
				return self.get_help('export')
			elif word.lower() in about_summary:
				return self.get_help('summary')
				
		else:
			return 'Please navigate through our help panels to see more help tips'
		
	def get_help(self, help):
		if help == 'charts_of_accounts':
			return charts_help
		elif help == 'categories':
			return about_categories
		elif help == 'Journal_entries':
			return about_journal
		elif help == 'view_accounts':
			return about_view_journal
		elif help == 'income_statement':
			return about_income_statement
		elif help == 'balance_sheet':
			return about_balance_sheet
		elif help == 'trial_balance':
			return about_trial_balance
		elif help == 'operations':
			return about_op_analysis
		elif help == 'balances':
			return about_balances
		elif help == 'budget':
			return about_budget
		elif help == 'storage_folder':
			return about_storage_folder
		elif help == 'start_end_dates':
			return about_start_dates
		elif help == 'opening_balance':
			return about_opening_bal
		elif help == 'special_accounts':
			return about_cos_op
		elif help == 'passwords':
			return about_passwords
		elif help == 'taxes':
			return about_taxes
		elif help == 'dep':
			return about_depreciation
		elif help == 'accum_dep':
			return about_accum_dep
		elif help == 'retained_earnings':
			return about_retained_earnings
		elif help == 'export':
			return about_export_reports
		elif help == 'summary':
			return about_summary
		elif help == 'show_tip':
			return about_show_tip
		else:
			return 'For more information, email your queries to \n snjuguna184@gmail.com'


def load_data():
	if os.path.exists(fin_data_file):
		with open(fin_data_file, "r") as file:
			data = json.load(file)
	else:
		data = {
			"Capital": {},
			"Non Current Assets": {},
			"Current Assets": {},
			"Non Current Liabilities": {},
			"Current Liabilities": {},
			"Other Incomes": {},
			"Operating Expenses": {},
			"Other Expenses": {},
			"Bank": {},
			"Taxes": {},
			"Operating Revenue": {},
			"Cost of Sales": {},
			"other_information": {},
			# Add more main parts as needed
		}
		data['Capital']['Opening Balance Equity'] = {"transactions": []}
		data['other_information']['app_key'] = app_key
		data['other_information']['pass_word_protected'] = 'False'
		data['other_information']['user_agreement'] = 'False'
		data['other_information']['budgeted_accounts'] = {}
		data['other_information']['storage_folder'] = '/storage/emulated/0/Download/'
		data['other_information']['assets_at_cost'] = {}
		data['other_information']['accum_depreciation'] = {}
		data['Operating Expenses']['Depreciation'] = {"transactions": []}
		data['Other Expenses']['Depreciation'] = {"transactions": []}
		data['Capital']['Retained Earnings'] = {"transactions": []}
		data['other_information']['invoices'] = {}
	return data
	
	
'''
save into financial data
'''


def save_data(data):
	with open(fin_data_file, "w") as file:
		json.dump(data, file, indent=4)
		

'''
add accounts to fin data
'''


def add_account(data, category, account_name):
	if account_name not in data[category]:
		data[category][account_name] = {"transactions": []}
		save_data(data)
		return f"Account '{account_name}' added to '{category}'"
	else:
		return f"Account '{account_name}' already exists in '{category}'."
		
		
def add_account_to_new_business(data, category, account_name):
	if account_name not in data[category]:
		data[category][account_name] = {"transactions": []}
	else:
		pass
		
		
'''
view saved accounts
'''


def view_accounts(data, category):
	if category in data:
		return list(data[category].keys())
	else:
		return []
	
	
'''
delete accounts
'''


def delete_account(data, category, account_name):
	if account_name in data[category]:
		del data[category][account_name]
		save_data(data)
		return f"Account '{account_name}' deleted from '{category}'."
	else:
		return f"Account '{account_name}' not found in '{category}'."
		
		

'''
transaction ids generator
'''


def get_transaction_id(data):
	counter_key = f"auto_numbering_ids"

	if counter_key not in data["other_information"]:
		data["other_information"][counter_key] = 1
	else:
		data["other_information"][counter_key] += 1

	save_data(data)
	return data["other_information"][counter_key]
		
		
'''
add transactions
'''


def add_transaction(data, category, account_name, amount, description, side, double_entry, date, transaction_id):
	if account_name in data[category]:
		transaction = {"date": date, "id": transaction_id, "amount": amount, "memo": description, "side": side, "double_entry": double_entry}
		data[category][account_name]["transactions"].append(transaction)
		
		# Sort transactions by date
		data[category][account_name]["transactions"] = sorted(
            data[category][account_name]["transactions"], key=lambda x: x["date"]
        )
		save_data(data)
		return f"Transaction added to '{account_name}' in '{category}'."
	else:
		return f"Account '{account_name}' not found in '{category}'."
		
		
def add_transaction_to_new_business(data, category, account_name, amount, description, side, double_entry, date, transaction_id):
	if account_name in data[category]:
		transaction = {"date": date, "id": transaction_id, "amount": amount, "memo": description, "side": side, "double_entry": double_entry}
		data[category][account_name]["transactions"].append(transaction)
		
		# Sort transactions by date
		data[category][account_name]["transactions"] = sorted(
            data[category][account_name]["transactions"], key=lambda x: x["date"]
        )
	else:
		pass
		

'''
add budget amount
'''

def add_budget_amount(data, account_name, budgeted_amount):
		data['other_information']['budgeted_accounts'][account_name] = budgeted_amount
		save_data(data)
		return f"Budget amount '{budgeted_amount}' saved to '{account_name}'"
		

'''
get transaction by id
'''


def get_transaction_by_id(data, category, account_name, transaction_id):
	if account_name in data[category]:
		transactions = data[category][account_name]["transactions"]
		specific_transaction = next((t for t in transactions if t['id'] == transaction_id), None)
		return specific_transaction
	else:
		return f"Account '{account_name}' not found in '{category}'."


'''
edit a transaction by id
'''


def edit_transaction_by_id(data, category, account_name, transaction_id, edited_transaction):
	if account_name in data[category]:
		transactions = data[category][account_name]["transactions"]
		for transaction in transactions:
			if transaction['id'] == transaction_id:
				transaction.update(edited_transaction)
				save_data(data)  # Save the changes to the JSON file
				break
	else:
		return f"Account '{account_name}' not found in '{category}'."
	
	
'''
delete a transaction
'''

def delete_transaction_by_id(data, category, account_name, transaction_id):
	if account_name in data[category]:
		transactions = data[category][account_name]["transactions"]
		matching_transaction = next((t for t in transactions if t['id'] == transaction_id), None)
	
		if matching_transaction:
			transactions.remove(matching_transaction)
			save_data(data)  # Save the changes to the JSON file
			return f"Transaction id '{transaction_id}' deleted successfully."
		else:
			return f"Transaction id '{transaction_id}' not found."
	else:
		return f"Account '{account_name}' not found in '{category}'."
		
		
'''
delete sale list
'''


def delete_the_list_of_a_sale(data, category, account, id, sales_account):
	saved_ids = data['other_information']['invoices']
	matching_id = next((t for t in saved_ids if t == id), None)
	if matching_id:
		saved_ids.pop(matching_id)
		delete_transaction_by_id(data, category, account, int(id))
		delete_transaction_by_id(data, 'Operating Revenue', sales_account, int(id))
		save_data(data)
		return True
	else:
		return False
	
		
'''
return list of transactions to view, unfiltered
'''


def view_transactions(data, category, account_name):
	if account_name in data[category]:
		return data[category][account_name]["transactions"]
	else:
		return f"Account '{account_name}' not found in '{category}'."
		
		
'''
get filtered transactions
'''


def get_filtered_transactions(data, category, account_name, start_date, end_date):
	try:
		start_date = datetime.strptime(start_date, "%d-%m-%Y") if start_date else datetime.min
		end_date = datetime.strptime(end_date, "%d-%m-%Y") if end_date else datetime.max
	
		transactions = data[category][account_name]["transactions"]
		filtered_transactions = [t for t in transactions if start_date <= datetime.strptime(t['date'], "%d-%m-%Y") <= end_date]
	        
		# Sort transactions from past to recent
		sorted_transactions = sorted(filtered_transactions, key=lambda x: datetime.strptime(x['date'], "%d-%m-%Y"))
		return sorted_transactions
	except:
		return []
	
	
'''
filter records and get bal b/d sum totals
'''


def balance_bd_sub_totals(data, category, account_name, start_date, end_date):
	try:
		start_date = datetime.strptime(start_date, "%d-%m-%Y") if start_date else datetime.min
		end_date = datetime.strptime(end_date, "%d-%m-%Y") if end_date else datetime.max
	
		transactions = data[category][account_name]["transactions"]
		filtered_transactions = [t for t in transactions if start_date <= datetime.strptime(t['date'], "%d-%m-%Y") < end_date]
	        
		# Sort transactions from past to recent
		sorted_transactions = sorted(filtered_transactions, key=lambda x: datetime.strptime(x['date'], "%d-%m-%Y"))
		
		bal_bd = 0
		
		debit_categories = {'Non Current Assets', 'Current Assets', 'Operating Expenses', 'Other Expenses', 'Bank', 'Taxes', 'Cost of Sales'}
		
		for trans in sorted_transactions:
			if category in debit_categories:
				if trans['side'] == 'debit':
					bal_bd += trans['amount']
				else:
					bal_bd -= trans['amount']
			else:
				if trans['side'] == 'debit':
					bal_bd += trans['amount']
				else:
					bal_bd -= trans['amount']
					
		return bal_bd
	except:
		return 0
	
	
'''
income statement balances
'''


def income_statement_deractives(data, category, account_name, start_date, end_date):
	try:
		start_date = datetime.strptime(start_date, "%d-%m-%Y") if start_date else datetime.min
		end_date = datetime.strptime(end_date, "%d-%m-%Y") if end_date else datetime.max
	
		transactions = data[category][account_name]["transactions"]
		filtered_transactions = [t for t in transactions if start_date <= datetime.strptime(t['date'], "%d-%m-%Y") <= end_date]
	        
		# Sort transactions from past to recent
		sorted_transactions = sorted(filtered_transactions, key=lambda x: datetime.strptime(x['date'], "%d-%m-%Y"))
		
		bal_bd = 0
		
		debit_categories = {'Non Current Assets', 'Current Assets', 'Operating Expenses', 'Other Expenses', 'Bank', 'Taxes', 'Cost of Sales'}
		
		for trans in sorted_transactions:
			if category in debit_categories:
				if trans['side'] == 'debit':
					bal_bd += trans['amount']
				else:
					bal_bd -= trans['amount']
			else:
				if trans['side'] == 'debit':
					bal_bd += trans['amount']
				else:
					bal_bd -= trans['amount']
					
		return bal_bd
	except:
		return 0
	
	
'''
trial balance deractives
'''

def trial_balance_deractives(category, account_data, start_date, end_date):
	try:
		start_date = datetime.strptime(start_date, "%d-%m-%Y") if start_date else datetime.min
		end_date = datetime.strptime(end_date, "%d-%m-%Y") if end_date else datetime.max
	
		transactions = account_data.get("transactions", [])
		filtered_transactions = [t for t in transactions if start_date <= datetime.strptime(t['date'], "%d-%m-%Y") <= end_date]
	        
		# Sort transactions from past to recent
		sorted_transactions = sorted(filtered_transactions, key=lambda x: datetime.strptime(x['date'], "%d-%m-%Y"))
		
		bal_bd = 0
		
		debit_categories = {'Non Current Assets', 'Current Assets', 'Operating Expenses', 'Other Expenses', 'Bank', 'Taxes', 'Cost of Sales'}
		
		for trans in sorted_transactions:
			if category in debit_categories:
				if trans['side'] == 'debit':
					bal_bd += trans['amount']
				else:
					bal_bd -= trans['amount']
			else:
				if trans['side'] == 'debit':
					bal_bd += trans['amount']
				else:
					bal_bd -= trans['amount']
					
		return bal_bd
	except:
		return 0
		
		
def get_category_total(list_of_categories, start_date, end_date):
	category_total = []
	for category in list_of_categories:
		if category in financial_data and category != "other_information":
			category_data = financial_data[category]
			for account_name, account_data in category_data.items():
				if account_name != "transactions":
					account_total = income_statement_deractives(financial_data, category, str(account_name), start_date, end_date)
					category_total.append(account_total)
					
	return sum(category_total)
	
	
'''
return net income to balance sheet
'''


def generate_the_net_profit_for_balance_sheet(start_date, end_date):
	# trading account
	# total ooerating revenue		
	total_incomes = get_category_total(['Operating Revenue', 'Other Incomes'], start_date, end_date)
	
	# cost of sales	
	cost_of_sales = get_category_total(['Cost of Sales'], start_date, end_date)
	
	gross_profit = total_incomes + cost_of_sales
		
	#operating and other expenses and taxes
	total_expenses = get_category_total(['Operating Expenses', 'Other Expenses', 'Taxes'], start_date, end_date)
	
	net_income = gross_profit + total_expenses

	return net_income
	
	
'''
total income without tax
'''

def generate_total_income_without_taxes(start_date, end_date):
	total_incomes = get_category_total(['Operating Revenue', 'Other Incomes'], start_date, end_date)
	
	# cost of sales	
	cost_of_sales = get_category_total(['Cost of Sales'], start_date, end_date)
	
	gross_profit = total_incomes + cost_of_sales
		
	#operating and other expenses and taxes
	total_expenses = get_category_total(['Operating Expenses', 'Other Expenses'], start_date, end_date)
	
	total_income = gross_profit + total_expenses

	return total_income
	
	
'''
the dashboard items
'''

def generate_the_dashboard_items(dashboard, expenses_, incomes_, net_profit_, bank_):
	start_date = financial_data['other_information']['start_date']
	end_date = financial_data['other_information']['end_date']
	
	# total operating revenue
	total_sales = get_category_total(['Operating Revenue'], start_date, end_date)
	
	# cost of sales
	total_cos = get_category_total(['Cost of Sales'], start_date, end_date)
	
	net_profit = generate_the_net_profit_for_balance_sheet(start_date, end_date)
	
	# total bank accounts
	total_bank = get_category_total(['Bank'], start_date, end_date)
	
	total_operating_expenses = get_category_total(['Operating Expenses'], start_date, end_date)
	
	total_other_expenses = get_category_total(['Other Expenses'], start_date, end_date)
	
	total_other_income = get_category_total(['Other Incomes'], start_date, end_date)
	
	total_non_current_assets = get_category_total(['Non Current Assets'], start_date, end_date)
	
	total_current_assets = get_category_total(['Current Assets'], start_date, end_date)
	
	total_bank = get_category_total(['Bank'], start_date, end_date)
	
	total_current_assets_and_bank = total_current_assets + total_bank
	
	total_current_liabilities = get_category_total(['Current Liabilities'], start_date, end_date)
	
	total_non_current_liabilities = get_category_total(['Non Current Liabilities'], start_date, end_date)
	
	gross_profit = total_cos + total_sales
	
	total_cos = "{:,.2f}".format(total_cos)
	
	total_sales = "{:,.2f}".format(-total_sales)
	
	total_operating_expenses = "{:,.2f}".format(total_operating_expenses)
	
	total_other_expenses = "{:,.2f}".format(total_other_expenses)
	
	total_other_income = "{:,.2f}".format(-total_other_income)
	
	net_profit = "{:,.2f}".format(-net_profit)
	
	total_bank = "{:,.2f}".format(total_bank)
	
	total_non_current_assets = "{:,.2f}".format(total_non_current_assets)
	
	total_current_assets = "{:,.2f}".format(total_current_assets_and_bank)
	
	total_current_liabilities = "{:,.2f}".format(-total_current_liabilities)
	
	total_non_current_liabilities = "{:,.2f}".format(-total_non_current_liabilities)
	
	gross_profit = "{:,.2f}".format(-gross_profit)
	
	expenses_.text = f"Op Exps: {total_operating_expenses}"
	incomes_.text = f"Op Rev: {total_sales}"
	net_profit_.text = f"NP: {net_profit}"
	bank_.text = f"Bank: {total_bank}"
	
	dashboard_items = f'Cost of Sales: {total_cos}\nOther Incomes: {total_other_income}\n\nGross profit: {gross_profit}\n\nOther Expenses: {total_other_expenses}\n\nNon Current Assets: {total_non_current_assets}\nCurrent Assets: {total_current_assets}\nCurrent Liabilities: {total_current_liabilities}\n\nNon Current Liabilities: {total_non_current_liabilities}'
	dashboard.text = dashboard_items
	
	
'''
export income statement
'''

def export_income_statement(start_date, end_date):
	try:
		download_path = financial_data['other_information']['storage_folder']	
		# file name 
		now = datetime.now()
		current_year = now.strftime("%d%m%Y")
		name = financial_data['other_information']['business name']
		file_name = f"income statement ssdata{current_year}.csv"
		csv_filename = os.path.join(download_path, file_name)
		
		with open(csv_filename, mode='w', newline='') as file:
			writer = csv.writer(file)
			writer.writerow([name, ''])
			writer.writerow(['Income Statement', ''])
			writer.writerow([f"for period {start_date} to {end_date}", ''])
			writer.writerow(['', ''])
			# trading account
			# sales
			writer.writerow(['Sales/Operating Revenue', ''])
			
			# sales
			category_accounts = financial_data['Operating Revenue']
			total_sales = []
			for account_name,account_data in category_accounts.items():
				account_total = income_statement_deractives(financial_data, 'Operating Revenue', str(account_name), start_date, end_date)
				writer.writerow([account_name, -account_total])
					
				total_sales.append(account_total)
				
			total_sales = sum(total_sales)
			writer.writerow(['Total Sales', -total_sales])
			writer.writerow(['', ''])
			
			# cost of sales
			writer.writerow(['Cost of Sales', ''])
			
			category_accounts = financial_data['Cost of Sales']
			total_cos = []
			for account_name,account_data in category_accounts.items():
				account_total = income_statement_deractives(financial_data, 'Cost of Sales', str(account_name), start_date, end_date)
				writer.writerow([account_name, account_total])
					
				total_cos.append(account_total)
				
			total_cos = sum(total_cos)
			writer.writerow(['Cost of sales', total_cos])
			writer.writerow(['', ''])		
			
			trading_profits = total_sales + total_cos
			
			writer.writerow(['', ''])
			writer.writerow(['Gross profits', -trading_profits])
			writer.writerow(['', ''])
			
			writer.writerow(['Operating Expenses', ''])
			
			# Operating expenses
			category_accounts = financial_data['Operating Expenses']
			total_expenses = []
			for account_name,account_data in category_accounts.items():
				if account_name == 'leave_it_alone':
					pass
				else:
					account_total = income_statement_deractives(financial_data, 'Operating Expenses', str(account_name), start_date, end_date)
					writer.writerow([account_name, account_total])
					
					total_expenses.append(account_total)
			total_expenses = sum(total_expenses)
			writer.writerow(['Total operating expenses', total_expenses])
			
			operating_income = trading_profits + total_expenses
			writer.writerow(['', ''])
			writer.writerow(['Operating Income', -operating_income])
			'''income
			'''
			writer.writerow(['', ''])
			writer.writerow(['Other/ non-operating Incomes', ''])
			
			category_accounts = financial_data['Other Incomes']
			total_income = []
			for account_name,account_data in category_accounts.items():
				account_total = income_statement_deractives(financial_data, 'Other Incomes', str(account_name), start_date, end_date)
				writer.writerow([account_name, -account_total])
				total_income.append(account_total)
					
			total_income = sum(total_income)
			writer.writerow(['Total other/ non operating Incomes', -total_income])
			writer.writerow(['', ''])
			
			total_accounts_income = operating_income + total_income
			writer.writerow(['Generated Incomes', -total_accounts_income])
			
			writer.writerow(['', ''])
			
			writer.writerow(['Other/ non operating expenses', ''])
			
			# non Operating expenses
			category_accounts = financial_data['Other Expenses']
			total_other_expenses = []
			for account_name,account_data in category_accounts.items():
				if account_name == 'leave_it_alone':
					pass
				else:
					account_total = income_statement_deractives(financial_data, 'Other Expenses', str(account_name), start_date, end_date)
					writer.writerow([account_name, account_total])
					
					total_other_expenses.append(account_total)
			total_other_expenses = sum(total_other_expenses)
			writer.writerow(['Total other/ non operating expenses', total_other_expenses])
			
			writer.writerow(['', ''])
			
			profit_before_taxes = total_accounts_income + total_other_expenses
			
			writer.writerow(['Profit before taxes', -profit_before_taxes])
			
			taxes = get_category_total(['Taxes'], start_date, end_date)
			writer.writerow(['Taxes', taxes])
			writer.writerow(['', ''])
			
			# net profit
			net_profit = profit_before_taxes + taxes
			writer.writerow(['Net profit/Loss', -net_profit])
			
			return 'Income statement saved to "storage path"'
	
	except:
		return 'Error in exporting, check for "storage" path'
		
		
'''
export accounts records
'''


def export_ledger_accounts(category, account_name, transactions, start_date, end_date, balance_bd):
	try:
		download_path = financial_data['other_information']['storage_folder']
		name = financial_data['other_information']['business name']
		
		now = datetime.now()
		current_year = now.strftime("%d%m%Y")
		name = financial_data['other_information']['business name']
		file_name = f"{account_name} ssdata{current_year}.csv"
		csv_filename = os.path.join(download_path, file_name)
		
		with open(csv_filename, mode='w', newline='') as file:
			writer = csv.writer(file)
			
			writer.writerow(['', name])
			writer.writerow(['', f"{account_name} Account"])
			writer.writerow(['', f"for period {start_date} to {end_date}"])
			writer.writerow(['', ''])
			writer.writerow(['Date', 'Memo', 'Counter Account', 'ID', 'Amount', 'Balances'])
			writer.writerow(['', 'bal b/f', '', '', '', balance_bd])
			
			# totals and amounts
			total_amnt = 0
			total_debit = 0
			total_credit = 0

			# excel style
			for trans in transactions:
				if category == 'Non Current Assets' or category == 'Current Assets' or category == 'Expenses' or category == 'Bank' or category == 'Cost of Sales':
					if trans['side'] == 'debit':
						figure = str(trans['amount'])
						total_debit += trans['amount']
					else:
						figure = f'({str(trans["amount"])})'
						total_credit += trans['amount']
				else:
					if trans['side'] == 'debit':
						figure = str(trans['amount'])
						total_debit += trans['amount']
					else:
						figure = f'({str(trans["amount"])})'
						total_credit += trans['amount']
				
				# balances logic
				if figure[0] == '(':
					total_amnt -= float(figure[1:-1])
					balance_bd -= float(figure[1:-1])
				else:
					total_amnt += float(figure)
					balance_bd += float(figure)
					
				acc = trans['double_entry']
				double = acc.split('|')
				show = double[1]
					
				writer.writerow([trans['date'], trans['memo'], show, trans['id'], figure, balance_bd])
				
			writer.writerow(['', ''])
			
			writer.writerow(['', '', 'Total Amount', '', total_amnt, balance_bd])
			writer.writerow(['', ''])
			
			writer.writerow(['', '', 'Total Debit', '', total_debit, ''])
			writer.writerow(['', '', 'Total Credit', '', total_credit, ''])
			
			return 'Ledger account records saved to "storage path"'
	except:
		return 'Error in exporting, check for "storage" path'
			
			
			
'''
export trial balance
'''


def export_trial_balance(end_date):
	try:
		download_path = financial_data['other_information']['storage_folder']
		name = financial_data['other_information']['business name']
		
		now = datetime.now()
		current_year = now.strftime("%d%m%Y")
		name = financial_data['other_information']['business name']
		file_name = f"trial balance ssdata{current_year}.csv"
		start_date = str(financial_data['other_information']['start_date'])
		
		csv_filename = os.path.join(download_path, file_name)
		
		with open(csv_filename, mode='w', newline='') as file:
			writer = csv.writer(file)
			
			writer.writerow([name, ''])
			writer.writerow(['Trial balance', ''])
			writer.writerow([f"as at {end_date}", ''])
			writer.writerow(['', ''])
			writer.writerow(["Debit balances", ''])
			
			# debit balances
			debit_categories = ['Non Current Assets', 'Current Assets', 'Operating Expenses', 'Other Expenses', 'Bank', 'Taxes', 'Cost of Sales']
			total_debit_side = []
			for category in debit_categories:
				if category in financial_data and category != "other_information":
					category_data = financial_data[category]
					for account_name, account_data in category_data.items():
						if account_name != "transactions":
							account_total = trial_balance_deractives(category, account_data, start_date, end_date)
							total_debit_side.append(account_total)
							if account_total == 0:
								pass
							else:
								writer.writerow([account_name, account_total])					
			# total assets
			# sum total assests 
			total_debit_side =  sum(total_debit_side)
			writer.writerow(['', ''])
			writer.writerow(['Debit total', total_debit_side])
			writer.writerow(['', ''])
			writer.writerow(['Credit balances', ''])
			
			credit_categories = ['Capital', 'Non Current Liabilities', 'Current Liabilities', 'Other Incomes', 'Operating Revenue']
			total_credit_side = []
			for category in credit_categories:
				if category in financial_data and category != "other_information":
					category_data = financial_data[category]
					for account_name, account_data in category_data.items():
						if account_name != "transactions":
							account_total = trial_balance_deractives(category, account_data, start_date, end_date)
							total_credit_side.append(account_total)
							if account_total == 0:
								pass
							else:
								writer.writerow([account_name, -account_total])
								
			# total liabilitiew
			# sum total liabiloties 
			total_credit_side =  sum(total_credit_side)
			writer.writerow(['', ''])
			writer.writerow(['Credit total', -total_credit_side])
			
			return 'Trial balance saved to "storage path"'
	except:
		return 'error encountred in exporting'
		
		
		
def get_the_accum_dep(category, account):
	account = f'{category}|{account}'
	if account in financial_data['other_information']['accum_depreciation']:
		return financial_data['other_information']['accum_depreciation'][account]
	else:
		return 0
				
		
'''
export balance sheet
'''

def export_balance_sheet(end_date):
	try:
		download_path = financial_data['other_information']['storage_folder']
		name = financial_data['other_information']['business name']
		
		now = datetime.now()
		todays_dep = now.strftime("%d-%m-%Y")
		current_year = now.strftime("%d%m%Y")
		name = financial_data['other_information']['business name']
		file_name = f"balance sheet ssdata{current_year}.csv"
		start_date = str(financial_data['other_information']['start_date'])
		
		csv_filename = os.path.join(download_path, file_name)
		
		with open(csv_filename, mode='w', newline='') as file:
			writer = csv.writer(file)
			
			writer.writerow([name, ''])
			writer.writerow(['Balance Sheet', ''])
			writer.writerow([f"as at {end_date}", ''])
			writer.writerow(['', ''])
			writer.writerow(["Non Current Assets", ''])
			
			
			category_accounts = financial_data['Non Current Assets']
			total_non_current_assets = []
			for account_name,account_data in category_accounts.items():
				account_total = income_statement_deractives(financial_data, 'Non Current Assets', str(account_name), start_date, end_date)
				total_non_current_assets.append(account_total)
				if account_total == 0:
					pass
				else:
					accumulated_dep = get_the_accum_dep('Non Current Assets', account_name)
					asset_at_cost = accumulated_dep + account_total
					
					if end_date == todays_dep:
						cost_of_asset = asset_at_cost
						depreciation = accumulated_dep
					else:
						cost_of_asset = account_total
						depreciation = '-'
					
					writer.writerow([account_name, cost_of_asset])
					writer.writerow([f'Accum dep {account_name}', depreciation])
					writer.writerow([f'NBV {account_name}', account_total])
					
			# get total non current assets ui
			total_non_current_assets = sum(total_non_current_assets)
			writer.writerow(['Total Non Current Assets', total_non_current_assets])
			writer.writerow(['', ''])
			
			writer.writerow(['Current Assets', ''])
			
			category_accounts = financial_data['Current Assets']
			total_current_assets = []
			for account_name,account_data in category_accounts.items():
				account_total = income_statement_deractives(financial_data, 'Current Assets', str(account_name), start_date, end_date)
				total_current_assets.append(account_total)
				if account_total == 0:
					pass
				else:
					writer.writerow([account_name, account_total])
			
			# bank accounts
			category_accounts = financial_data['Bank']
			total_bank = []
			for account_name,account_data in category_accounts.items():
				account_total = income_statement_deractives(financial_data, 'Bank', str(account_name), start_date, end_date)
				total_bank.append(account_total)
				if account_total == 0:
					pass
				else:
					writer.writerow([account_name, account_total])			
			# sum bank
			total_bank = sum(total_bank)
			# get total current assets ui
			total_current_assets = sum(total_current_assets) + total_bank
			writer.writerow(['Total Current Assets', total_current_assets])
			# total assets
			# sum total assests 
			total_assets =  total_non_current_assets + total_current_assets
			writer.writerow(['', ''])
			writer.writerow(['Total Assets', total_assets])
			writer.writerow(['', ''])
			
			writer.writerow(['Capital and Liabilities', ''])
			writer.writerow(['Capital', ''])
			
			category_accounts = financial_data['Capital']
			total_capital = []
			for account_name,account_data in category_accounts.items():
				account_total = income_statement_deractives(financial_data, 'Capital', str(account_name), start_date, end_date)
				total_capital.append(account_total)
				if account_total == 0:
					pass
				else:
					writer.writerow([account_name, -account_total])
					
			net_profit = generate_the_net_profit_for_balance_sheet(start_date, end_date)
			writer.writerow(['Net Profit/Loss', -net_profit])	
			# get capital ui
			total_capital = sum(total_capital) + net_profit
			writer.writerow(['Total Capital', -total_capital])
			writer.writerow(['', ''])
			writer.writerow(['Non Current Liabilities', ''])
			
			category_accounts = financial_data['Non Current Liabilities']
			total_non_current_liabilities = []
			for account_name,account_data in category_accounts.items():
				account_total = income_statement_deractives(financial_data, 'Non Current Liabilities', str(account_name), start_date, end_date)
				total_non_current_liabilities.append(account_total)
				if account_total == 0:
					pass
				else:
					writer.writerow([account_name, -account_total])
					
			# total non current liabilities
			total_non_current_liabilities = sum(total_non_current_liabilities)
			writer.writerow(['Total Non Current Liabilities', -total_non_current_liabilities])
			writer.writerow(['', ''])
			writer.writerow(['Current Liabilities', ''])
			
			category_accounts = financial_data['Current Liabilities']
			total_current_liabilities = []
			for account_name,account_data in category_accounts.items():
				account_total = income_statement_deractives(financial_data, 'Current Liabilities', str(account_name), start_date, end_date)
				total_current_liabilities.append(account_total)
				if account_total == 0:
					pass
				else:
					writer.writerow([account_name, -account_total])
					
			# total non current liabilities
			total_current_liabilities = sum(total_current_liabilities)
			writer.writerow(['Total Current Liabilities', -total_current_liabilities])
			writer.writerow(['', ''])
			
			# total non current and current liabilities
			total_current_and_non_liabilities = total_non_current_liabilities + total_current_liabilities
			writer.writerow(['Total Liabilities', -total_current_and_non_liabilities])
			writer.writerow(['', ''])
			
			# total capital and liabilities
			# sum total all 
			total_capital_and_liabilites =  total_non_current_liabilities + total_current_liabilities + total_capital
			writer.writerow(['Total Capital and Liabilities', -total_capital_and_liabilites])
			return 'Balance sheet saved to "storage path"'
		
	except:
		return 'error encountred in exporting'

'''
financial ratios
'''


def generate_the_financial_ratios(start_date, end_date, ratio):
	# total operating revenue
	total_sales = get_category_total(['Operating Revenue'], start_date, end_date)
	
	# cost of sales
	total_cos = get_category_total(['Cost of Sales'], start_date, end_date)
	
	net_profit = generate_the_net_profit_for_balance_sheet(start_date, end_date)
	
	# total bank accounts
	total_bank = get_category_total(['Bank'], start_date, end_date)
	
	total_operating_expenses = get_category_total(['Operating Expenses'], start_date, end_date)
	
	total_other_expenses = get_category_total(['Other Expenses'], start_date, end_date)
	
	total_other_income = get_category_total(['Other Incomes'], start_date, end_date)
	
	total_non_current_assets = get_category_total(['Non Current Assets'], start_date, end_date)
	
	total_current_assets = get_category_total(['Current Assets'], start_date, end_date)
	
	total_bank = get_category_total(['Bank'], start_date, end_date)
	
	total_current_assets_and_bank = total_current_assets + total_bank
	
	total_current_liabilities = get_category_total(['Current Liabilities'], start_date, end_date)
	
	total_non_current_liabilities = get_category_total(['Non Current Liabilities'], start_date, end_date)
	
	gross_profit = total_cos + total_sales	
	
	if ratio == 'net_profit_margin':
		try:
			pm = net_profit/total_sales
			pm = pm * 100
			pm = f"{round(pm,2)} %"
			return pm
		except:
			return 'calculation error'
	elif ratio == 'return_on_assets':
		total_assets = total_current_assets_and_bank + total_non_current_assets
		try:
			roa = (net_profit/total_assets) * 100
			return f"{round(-roa, 2)} %"
		except:
			return 'calculation error'
			
	elif ratio == 'current_ratio':
		current_assets = total_current_assets_and_bank
		current_liabilities = total_current_liabilities
		try:
			current_ratio = (current_assets/current_liabilities)
			return f"{round(-current_ratio, 2)}"
		except:
			return 'calculation error'
			
'''
return user image
'''			
			
def display_profile_picture():
	if 'profile_picture' in financial_data['other_information']:
		return financial_data['other_information']['profile_picture']
	else:
		return ' '


'''
delete financial accounts
'''


class DeleteAccount(Popup):
	def __init__(self, **kwargs):
		super(DeleteAccount, self).__init__(**kwargs)
		
	def close_popup(self):
		self.dismiss()
		
	def undo_deletion_in_3_secs(self, action):
		if action == 'delete the account':
			Clock.schedule_once(self.delete_permanently, 4)
			
			def time_one(*args):
				self.delete_account.text = 'Undo deletion in (3s)'
				
			def time_two(*args):
				self.delete_account.text = 'Undo deletion in (2s)'
				
			def time_three(*args):
				self.delete_account.text = 'Undo deletion in (1s)'
				
			Clock.schedule_once(time_one, 1)
			Clock.schedule_once(time_two, 2)
			Clock.schedule_once(time_three, 3)
		else:
			Clock.unschedule(self.delete_permanently)
			self.dismiss()
		
	def delete_permanently(self, *args):
		# del related transactions
		if account_to_delete in financial_data[category_of_account]:
			temp_transaction_list = []
			del_related_to_account = view_transactions(financial_data, category_of_account, account_to_delete)
			for transaction in del_related_to_account:
				temp_transaction_dict = {
	                "id": transaction["id"],
	                "double_entry": transaction["double_entry"]
	            }
				temp_transaction_list.append(temp_transaction_dict)
				
			for temp_transaction in temp_transaction_list:
				account = temp_transaction['double_entry']
				other_account = account.split('|')
				delete_transaction_by_id(financial_data, other_account[0], other_account[1], temp_transaction['id'])
				
				if str(temp_transaction['id']) in financial_data['other_information']['invoices']:
					del financial_data['other_information']['invoices'][str(temp_transaction['id'])]
				
			# del the account
			show_complete.text = delete_account(financial_data, category_of_account, account_to_delete)
			# delete budgeted
			del_budget = f'{category_of_account}|{account_to_delete}'
			if del_budget in financial_data['other_information']['budgeted_accounts']:
				del financial_data['other_information']['budgeted_accounts'][del_budget]
				
			# delete more
			if category_of_account == 'Non Current Assets':
				if del_budget in financial_data['other_information']['assets_at_cost']:
					del financial_data['other_information']['assets_at_cost'][del_budget]
				if del_budget in financial_data['other_information']['accum_depreciation']:
					del financial_data['other_information']['accum_depreciation'][del_budget]
		
			save_data(financial_data)	
			list_of_accounts.clear_widgets()
			accounts = view_accounts(financial_data, category_of_account)
			app = App.get_running_app()
			color = app.return_theme_color()
			
			list_of_accounts.add_widget(
			Button(text=' ',
				size_hint=(1,None),
				height='5dp',
				background_color=app.theme_cls.primary_color,
				background_normal=''
			))
			
			list_items = 0
		
			start_date = financial_data['other_information']['start_date']
			end_date = financial_data['other_information']['end_date']
				
			category_total = get_category_total([category_of_account], start_date, end_date)
			debit_categories = {'Non Current Assets', 'Current Assets', 'Operating Expenses', 'Other Expenses', 'Bank', 'Taxes', 'Cost of Sales'}
				
			if category_of_account in debit_categories:
				formatted = "{:,.2f}".format(category_total)
			else:
				formatted = "{:,.2f}".format(-category_total)
			
			for acc in accounts:
				button = MDFlatButton(
					text=str(acc),
					size_hint=(1,None),
					on_press=self.on_button_press,
					font_size="16sp",
					theme_text_color="Custom",
					text_color=color,
					halign='center')
				list_of_accounts.add_widget(button)
				list_items += 1
			
			on_click_account_updated.text = 'Account'
			app = App.get_running_app()
							
			home = app.root.get_screen('home')
			charts = app.root.get_screen('charts_of_accounts')
			
			charts.ids.about_list_of_account.text = f"{category_of_account} > {list_items} account(s) > {formatted}"
			
			generate_the_dashboard_items(home.dashboard,home.expenses,home.incomes,home.net_profit,home.bank)
			toast("An Account was deleted")
			last_upated_date()
			self.dismiss()
		
	# account pressed		
	def on_button_press(self, instance):
		app = App.get_running_app()
		charts = app.root.get_screen('charts_of_accounts')
		on_click_account_updated.text = instance.text
		
		start_date = financial_data['other_information']['start_date']
		end_date = financial_data['other_information']['end_date']
		
		account_total = income_statement_deractives(financial_data, category_of_account, str(instance.text), start_date, end_date)
		
		debit_categories = {'Non Current Assets', 'Current Assets', 'Operating Expenses', 'Other Expenses', 'Bank', 'Taxes', 'Cost of Sales'}
		
		if category_of_account in debit_categories:
			formatted = "{:,.2f}".format(account_total)
		else:
			formatted = "{:,.2f}".format(-account_total)
		
		charts.ids.top_selection_display.text = f"{instance.text} > {formatted}"
		
	def show_account(self):
		return f"Are you sure to delete account\n'{account_to_delete}'"
		
		
'''
cost of assets
'''

class CostOfAssets(Popup):
	def __init__(self, **kwargs):
		super(CostOfAssets, self).__init__(**kwargs)
		
	# normal
	def to_normal(self):
		def normal(*args):
			self.error.text = 'All fields are required'
			
		Clock.schedule_once(normal, 3)
		
	def close_popup(self):
		self.dismiss()
		
	def add_cost_amount(self, cost_amount, category, account_name):
		if cost_amount == '0' or cost_amount == '':
			self.error.text = 'Enter a cost amount in the field below'
			self.to_normal()
		else:
			if account_name == 'Choose Account':
				self.error.text = 'Please select an account to add cost'
				self.to_normal()
			else:
				financial_data['other_information']['assets_at_cost'][f"{category}|{account_name}"] = round(float(cost_amount), 2)
				self.error.text = f"Cost amount of asset saved to '{account_name}'"
				self.to_normal()
				save_data(financial_data)
				self.cost_amount.text = '0'
				last_upated_date()
	
	def on_text_if_account_in_assets_cost(self, category, account_name):
		if f"{category}|{account_name}" in financial_data['other_information']['assets_at_cost']:
			self.cost_amount.text = str(financial_data['other_information']['assets_at_cost'][f"{category}|{account_name}"])
		else:
			self.cost_amount.text = '0'
						
	# view list of accounts	
	def load_current_saved_accounts(self, category, account_name):
		accounts = view_accounts(financial_data, category)
		account_name.text = 'Choose Account'
		account_name.values = accounts
		
	def get_the_cost_amount(self, category, account):
		account = f'{category}|{account}'
		if account in financial_data['other_information']['assets_at_cost']:
			return financial_data['other_information']['assets_at_cost'][account]
		else:
			return 0
		
		
'''
edit category of account
'''

class ChangeAccountCategory(Popup):
	def __init__(self, **kwargs):
		super(ChangeAccountCategory, self).__init__(**kwargs)
		
	def close_popup(self):
		self.dismiss()
		
	def update_change_button(self, category):
		self.change_to.text = f"change account to {category}"
		
	def get_the_accum_dep(self, category, account):
		account = f'{category}|{account}'
		if account in financial_data['other_information']['accum_depreciation']:
			return financial_data['other_information']['accum_depreciation'][account]
		else:
			return 0
			
	def save_the_accumulated_depreciation(self, category, account, dep_amount):
		accum_dep = self.get_the_accum_dep(category, account)
		if accum_dep == 0:
			previous_saved_dep = 0
		else:
			previous_saved_dep = accum_dep
			
		new_dep = previous_saved_dep + dep_amount
		financial_data['other_information']['accum_depreciation'][f'{category}|{account}'] = round(new_dep,2)
		
	# view list of accounts	
	def load_current_saved_accounts(self, category, account_name):
		accounts = view_accounts(financial_data, category)
		account_name.text = 'Choose Account'
		account_name.values = accounts
		
	def get_the_cost_amount(self, category, account):
		account = f'{category}|{account}'
		if account in financial_data['other_information']['assets_at_cost']:
			return financial_data['other_information']['assets_at_cost'][account]
		else:
			return 0
			
	def on_text_if_account_in_assets_cost(self, category, account_name):
		if f"{category}|{account_name}" in financial_data['other_information']['assets_at_cost']:
			self.cost_amount.text = str(financial_data['other_information']['assets_at_cost'][f"{category}|{account_name}"])
		else:
			self.cost_amount.text = '0'
			
	def add_cost_amount(self, cost_amount, category, account_name):
		if cost_amount == '0' or cost_amount == '':
			self.error.text = 'Enter a cost amount in the field below'
			self.to_normal()
		else:
			if account_name == 'Choose Account':
				self.error.text = 'Please select an account to add cost'
				self.to_normal()
			else:
				financial_data['other_information']['assets_at_cost'][f"{category}|{account_name}"] = round(float(cost_amount), 2)
				self.error.text = f"Cost amount of asset saved to '{account_name}'"
				self.to_normal()
				save_data(financial_data)
				self.cost_amount.text = '0'
		
	# normal
	def to_normal(self):
		def normal(*args):
			self.error.text = 'All fields are required'
			
		Clock.schedule_once(normal, 3)
		
	def shift_account_to(self, account_category):
		if account_category == 'Account Category':
			self.error.text = 'First select an account category'
			self.to_normal()
		else:
			debits = {'Non Current Assets', 'Current Assets', 'Operating Expenses', 'Other Expenses', 'Bank', 'Taxes', 'Cost of Sales'}
			credits = {'Capital', 'Non Current Liabilities', 'Current Liabilities', 'Other Incomes', 'Operating Revenue'}
			
			if category_of_account == 'Non Current Assets' or account_category == 'Non Current Assets':
				self.error.text = 'Unable to shift Non Current Assets'
				self.to_normal()
				toast("Non Current Assets Disabled")
			else:
				if category_of_account in debits and account_category in debits:
					self.perform_the_shift(account_category)
				elif category_of_account in credits and account_category in credits:
					self.perform_the_shift(account_category)
				else:
					self.error.text = 'Unable to shift between different treatments'
					self.to_normal()
				
				
	def perform_the_shift(self, account_category):
		if account_to_delete in financial_data[category_of_account]:
			if account_to_delete in financial_data[account_category]:
				self.error.text = 'account already exists in destination'
				self.to_normal()
				toast('Account already exists in the Category')
			else:
				financial_data[account_category][account_to_delete] = financial_data[category_of_account][account_to_delete]
						
				del financial_data[category_of_account][account_to_delete]
				
				# delete budgeted
				del_budget = f'{category_of_account}|{account_to_delete}'
				if del_budget in financial_data['other_information']['budgeted_accounts']:
					del financial_data['other_information']['budgeted_accounts'][del_budget]
				# delete more
				if category_of_account == 'Non Current Assets':
					if del_budget in financial_data['other_information']['assets_at_cost']:
						del financial_data['other_information']['assets_at_cost'][del_budget]
					if del_budget in financial_data['other_information']['accum_depreciation']:
						del financial_data['other_information']['accum_depreciation'][del_budget]
				
				save_data(financial_data)
				
				list_of_accounts.clear_widgets()
				accounts = view_accounts(financial_data, category_of_account)
				app = App.get_running_app()
				color = app.return_theme_color()
				
				list_of_accounts.add_widget(
				Button(text=' ',
					size_hint=(1,None),
					height='5dp',
					background_color=app.theme_cls.primary_color,
					background_normal=''
				))
				
				list_items = 0
		
				start_date = financial_data['other_information']['start_date']
				end_date = financial_data['other_information']['end_date']
				
				category_total = get_category_total([category_of_account], start_date, end_date)
				debit_categories = {'Non Current Assets', 'Current Assets', 'Operating Expenses', 'Other Expenses', 'Bank', 'Taxes', 'Cost of Sales'}
				
				if category_of_account in debit_categories:
					formatted = "{:,.2f}".format(category_total)
				else:
					formatted = "{:,.2f}".format(-category_total)
				
				for acc in accounts:
					button = MDFlatButton(
						text=str(acc),
						size_hint=(1,None),
						on_press=self.on_button_press,
						font_size="16sp",
						theme_text_color="Custom",
						text_color=color,
						halign='center')
					list_of_accounts.add_widget(button)
					list_items += 1
				
				on_click_account_updated.text = 'Account'
				app = App.get_running_app()
				charts = app.root.get_screen('charts_of_accounts')
			
				charts.ids.about_list_of_account.text = f"{category_of_account} > {list_items} account(s) > {formatted}"
							
				home = app.root.get_screen('home')
				generate_the_dashboard_items(home.dashboard,home.expenses,home.incomes,home.net_profit,home.bank)
				last_upated_date()
				
				self.error.text = 'account shifted successfuly'
				toast("Account shifted and exiting after 3 seconds")
				
				Clock.schedule_once(self.dismiss, 3)
		else:
			self.error.text = 'source account not found'
			self.to_normal()
			
	# account pressed		
	def on_button_press(self, instance):
		app = App.get_running_app()
		charts = app.root.get_screen('charts_of_accounts')
		on_click_account_updated.text = instance.text
		
		start_date = financial_data['other_information']['start_date']
		end_date = financial_data['other_information']['end_date']
		
		account_total = income_statement_deractives(financial_data, category_of_account, str(instance.text), start_date, end_date)
		
		debit_categories = {'Non Current Assets', 'Current Assets', 'Operating Expenses', 'Other Expenses', 'Bank', 'Taxes', 'Cost of Sales'}
		
		if category_of_account in debit_categories:
			formatted = "{:,.2f}".format(account_total)
		else:
			formatted = "{:,.2f}".format(-account_total)
		
		charts.ids.top_selection_display.text = f"{instance.text} > {formatted}"
		
	def show_account(self):
		return f"shift account '{account_to_delete}' from '{category_of_account}'"


'''
home screen that help access all accounting functions
'''

'''
logic globals
'''
global from_journal_to_home
from_journal_to_home = True
global the_double_entry
the_double_entry = ''
global selected_account_to_view
selected_account_to_view = ''
global the_view_account_side
the_view_account_side = ''
global from_view_records_to_home
from_view_records_to_home = True
global is_the_imported_file
is_the_imported_file = 'imported file will show here'

'''
password popup, replace main file and close business
'''

class PasswordSettings(Popup):
	def __init__(self, **kwargs):
		super(PasswordSettings, self).__init__(**kwargs)
		self.disallowed_chars = ['"', '|', '$', '%', '.']
		
	# show current date on homepage
	def show_date(self):
		now = datetime.now()
		today = now.strftime("%d-%m-%Y")
		return today
		
	def select_date(self, date_field):
		global on_date_field
		on_date_field = date_field
		popup = DatesPopup()
		popup.open()

	def on_text_account(self, value):
		# Function to filter or prevent certain characters
		characters  = value.text
		filtered_text = ''.join(char for char in characters if char not in self.disallowed_chars)
		value.text = filtered_text
		
	# normal
	def to_normal(self):
		def normal(*args):
			self.error.text = 'Enter a Password to be used in loging in'
			
		Clock.schedule_once(normal, 3)
		
	def replace_the_main_file(self, pass_key):
		global financial_data
		global fin_data_file
		global is_the_imported_file
		try:
			if len(pass_key) > 4:
				if financial_data['other_information']['pass_word_protected'] == 'False':
					self.error.text = 'You must first create a password to continue'
					self.to_normal()
					toast("No passwords found")
				else:
					if is_the_imported_file == 'imported file will show here':
						self.error.text = 'First import a file to be used in replacement'
						self.to_normal()
						toast('No file is imported')
					else:
						if financial_data['other_information']['app_key'] == 'account_created' and financial_data['other_information']['user_agreement'] == 'True' and financial_data['other_information']['pass_word'] == pass_key:
							internal_data = self.load_data()
							with open(back_to_app_file, 'w') as file:
								file.write(internal_data)
							self.dismiss()
							
							app = App.get_running_app()
							
							charts = app.root.get_screen('charts_of_accounts')
							charts.account_category.text = 'Account Category'
							charts.list_of_accounts_layout.clear_widgets()
							home = app.root.get_screen('home')
							home.import_file.text =  'Import  file'
							home.selected_file.text = 'imported file will show here'
							is_the_imported_file = 'imported file will show here'
							fin_data_file = back_to_app_file
							financial_data = load_data()
							home.view_status.text = ' '
								
							toast("main file replaced")
							log = App.get_running_app().root.get_screen('log_in')
							name = financial_data['other_information']['business name']
							hey_there = f"Nice to see you back, {name}!"	
							log.welcome_user.text = hey_there
				
							app.root.current = 'log_in'
			
						else:
							self.error.text = 'The password is wrong'
							toast('Incorrect password')
							self.to_normal()
			else:
				self.error.text = 'The password is too short'
				self.to_normal()
				toast('Too short password')
		except:
			self.error.text = 'We cannot replace the main file with the imported file'
			toast("unable to replace main file")
			self.to_normal()
		
	def set_password(self, pass_key):
		if len(pass_key) > 4:
			financial_data['other_information']['pass_word_protected'] = 'True'
			pass_key = pass_key
			financial_data['other_information']['pass_word'] = pass_key
			save_data(financial_data)
			self.dismiss()
			toast("Password Saved")
			last_upated_date()
		else:
			self.error.text = 'Too short password, try again'
			self.to_normal()
			
	def remove_password(self):
		financial_data['other_information']['pass_word_protected'] = 'False'
		save_data(financial_data)
		self.dismiss()
		toast("Password removed")
		
	def load_data(self):
		try:
			with open(is_the_imported_file, 'r') as file:
				return file.read()
		except FileNotFoundError:
			return None
		except:
			return None
			
	def load_new_business(self):
		data = {
			"Capital": {},
			"Non Current Assets": {},
			"Current Assets": {},
			"Non Current Liabilities": {},
			"Current Liabilities": {},
			"Other Incomes": {},
			"Operating Expenses": {},
			"Other Expenses": {},
			"Bank": {},
			"Taxes": {},
			"Operating Revenue": {},
			"Cost of Sales": {},
			"other_information": {},
			# Add more main parts as needed
		}
		data['Capital']['Opening Balance Equity'] = {"transactions": []}
		data['other_information']['app_key'] = app_key
		data['other_information']['pass_word_protected'] = 'False'
		data['other_information']['user_agreement'] = 'False'
		data['other_information']['budgeted_accounts'] = {}
		data['other_information']['storage_folder'] = financial_data['other_information']['storage_folder']
		#more data panels
		data['other_information']['assets_at_cost'] = financial_data['other_information']['assets_at_cost']
		data['other_information']['accum_depreciation'] = financial_data['other_information']['accum_depreciation'] 
		data['Operating Expenses']['Depreciation'] = {"transactions": []}
		data['Other Expenses']['Depreciation'] = {"transactions": []}
		data['Capital']['Retained Earnings'] = {"transactions": []}
		data['other_information']['invoices'] = {}
		return data
		
	def get_the_accum_dep(self, category, account):
		account = f'{category}|{account}'
		if account in financial_data['other_information']['accum_depreciation']:
			return financial_data['other_information']['accum_depreciation'][account]
		else:
			return 0
			
	def get_the_cost_amount(self, category, account):
		account = f'{category}|{account}'
		if account in financial_data['other_information']['assets_at_cost']:
			return financial_data['other_information']['assets_at_cost'][account]
		else:
			return 0
		
	def on_press_close_business(self, closing_date, pass_key):
		try:
			self.close_the_business(closing_date, pass_key)
		except:
			self.error.text = 'Unable to close business, change storage folder'
			self.to_normal()
			
	def close_the_business(self, closing_date, pass_key):
		if financial_data['other_information']['app_key'] == 'account_created' and financial_data['other_information']['user_agreement'] == 'True' and financial_data['other_information']['pass_word'] == pass_key:
			now = datetime.now()
			current_year = now.strftime("%d%m%Y")
			name = financial_data['other_information']['business name']
			
			download_path = financial_data['other_information']['storage_folder']
			file_name = f'closed {name} {current_year}.ssdata'
			filename = os.path.join(download_path, file_name)
			new_business = self.load_new_business()
			
			start_date = financial_data['other_information']['start_date']
			end_date = financial_data['other_information']['end_date']
			
			transaction_id = -1
			
			# debit balances
			debit_categories = ['Non Current Assets',  'Current Assets', 'Bank']
			for category in debit_categories:
				if category in financial_data and category != "other_information":
					category_data = financial_data[category]
					for account_name, account_data in category_data.items():
						if account_name != "transactions":
							account_total = trial_balance_deractives(category, account_data, start_date, end_date)
							if account_total == 0:
								pass
							else:
								add_account_to_new_business(new_business, category, str(account_name))
								if account_total < 0:
									if category == 'Non Current Assets':
										asset_at_cost = self.get_the_accum_dep('Non Current Assets', account_name) + account_total
										new_business['other_information']['assets_at_cost'][f"{category}|{account_name}"] = round(float(asset_at_cost), 2)
										if asset_at_cost < 0:
											record_amount = -asset_at_cost
										else:
											record_amount = asset_at_cost
									else:
										record_amount = -account_total				
									add_transaction_to_new_business(new_business, category, str(account_name), record_amount, 'opening balance equity', 'credit', 'Capital|Opening Balance Equity', closing_date, transaction_id)
								else:
									if category == 'Non Current Assets':
										asset_at_cost = self.get_the_accum_dep('Non Current Assets', account_name) + account_total
										new_business['other_information']['assets_at_cost'][f"{category}|{account_name}"] = round(float(asset_at_cost), 2)
										record_amount = account_total
									else:
										record_amount = account_total
									add_transaction_to_new_business(new_business, category, str(account_name), record_amount, 'opening balance equity', 'debit', 'Capital|Opening Balance Equity', closing_date, transaction_id)
			
			credit_categories = ['Capital', 'Non Current Liabilities', 'Current Liabilities']
			for category in credit_categories:
				if category in financial_data and category != "other_information":
					category_data = financial_data[category]
					for account_name, account_data in category_data.items():
						if account_name != "transactions":
							account_total = trial_balance_deractives(category, account_data, start_date, end_date)
							if account_total == 0:
								pass
							else:
								add_account_to_new_business(new_business, category, str(account_name))
								if account_total < 0:
									add_transaction_to_new_business(new_business, category, str(account_name), -account_total, 'opening balance equity', 'credit', 'Capital|Opening Balance Equity', closing_date, transaction_id)
								else:
									add_transaction_to_new_business(new_business, category, str(account_name), account_total, 'opening balance equity', 'debit', 'Capital|Opening Balance Equity', closing_date, transaction_id)
				
			net_profit_loss = generate_the_net_profit_for_balance_sheet(start_date, end_date)
			transaction_id = -2
			
			if net_profit_loss < 0:
				add_transaction_to_new_business(new_business, 'Capital', 'Retained Earnings', -net_profit_loss, 'profit b/d', 'credit', 'Capital|Opening Balance Equity', closing_date, transaction_id)
			else:
				add_transaction_to_new_business(new_business, 'Capital', 'Retained Earnings', net_profit_loss, 'loss b/d', 'debit', 'Capital|Opening Balance Equity', closing_date, transaction_id)
			new_business['other_information']['business name'] = ''
			new_business['other_information']['business email'] = ''
			new_business['other_information']['start_date'] = closing_date
			new_business['other_information']['end_date'] = ''
								
			with open(filename, "w") as file:
				json.dump(new_business, file, indent=4)
				
			self.error.text = 'Business closed successfully'
			toast("Business closed and new file saved")
			last_upated_date()
			Clock.schedule_once(self.dismiss, 3)
			
		else:
			self.error.text = 'The password is wrong'
			self.to_normal()
			toast("Enter correct password above")
			
	def close_popup(self):
		self.dismiss()
		
		
'''
donate
'''
class DonateToAkauntin(Popup):
	def __init__(self, **kwargs):
		super(DonateToAkauntin, self).__init__(**kwargs)
		
	def i_have_paypal_app(self):
		email_address = 'snjuguna184@gmail.com'
		mailto_url = f"mailto:{email_address}"
		webbrowser.open(mailto_url)
		
	def donate_with_paypal(self):
		try:
			email_address = 'snjuguna184@gmail.com'
			Clipboard.copy(email_address)
			paypal_url = f"https://www.paypal.com/sendmoney?recipient={email_address}"
			webbrowser.open(paypal_url)
			toast('paste the copied email address to send')
		except:
			toast('an error occurred')
		
	def copy_to_clipboard(self, text):
		text_to_copy = text
		Clipboard.copy(text_to_copy)
		self.error.text = 'copied to clipboard'
		self.to_normal()
		
	# normal
	def to_normal(self):
		def normal(*args):
			self.error.text = ''
			
		Clock.schedule_once(normal, 3)
	
		
'''
abouts and legality
'''	
							
class AboutsAndLegality(Popup):
	def __init__(self, **kwargs):
		super(AboutsAndLegality, self).__init__(**kwargs)
		
	def close_abouts_popup(self):
		self.dismiss()
		
		
'''
help popup

'''

global ask_for_help

class HelpPopup(Popup):
	def __init__(self, **kwargs):
		super(HelpPopup, self).__init__(**kwargs)
		
		self.ids.help_label.text = ask_for_help
		
	def close_popup(self):
		self.dismiss()
		
		
'''
backup
'''


class BackUpData(Popup):
	def __init__(self, **kwargs):
		super(BackUpData, self).__init__(**kwargs)
		
	 # normal
	def to_normal(self):
		def normal(*args):
			self.error.text = ''
			
		Clock.schedule_once(normal, 3)
		
	def backup_to_drive(self, *args):
		try:
			url = "https://drive.google.com"  # Google Drive URL
			self.back_up_to_download()
			webbrowser.open(url)
			toast('select your file from storage folder')
		except:
			toast('an error occured')
		
	def back_up_to_download(self):
		internal_data = self.load_data()
		
		if internal_data == None:
			self.error.text = 'Error in accessing app data'
			self.to_normal()
		else:
			try:
				download_path = financial_data['other_information']['storage_folder']	
				# file name 
				now = datetime.now()
				current_year = now.strftime("%d%m%Y")
				name = financial_data['other_information']['business name']
				file_name = f"{name} {current_year}.ssdata"
				external_file_path = os.path.join(download_path, file_name)
				
				with open(external_file_path, 'w') as file:
					file.write(internal_data)
					
				self.error.text = 'Local backup created successfully'
				#self.to_normal()
				Clock.schedule_once(self.dismiss, 2)
				toast("Local backup saved to storage path")
				#self.dismiss()
			except:
				self.error.text = 'Storage folder not found'
				self.to_normal()
				toast("Error in accessing storage folder")
		
		
	def load_data(self):
		try:
			with open(fin_data_file, 'r') as file:
				return file.read()
		except FileNotFoundError:
			return None
			
			
'''
exit popup
'''


class BackUpDataOrExit(Popup):
	def __init__(self, **kwargs):
		super(BackUpDataOrExit, self).__init__(**kwargs)
		
	 # normal
	def to_normal(self):
		def normal(*args):
			self.error.text = ''
			
		Clock.schedule_once(normal, 3)
		
	def return_theme_color(self):
		if "app_theme" in financial_data["other_information"]:
			theme = financial_data["other_information"]["app_theme"]
		else:
			theme = "Indigo"
		return theme
		
	def set_the_app_theme(self, theme):
		app = App.get_running_app()
		financial_data["other_information"]["app_theme"] = theme
		save_data(financial_data)
		app.theme_cls.primary_palette = theme
		
	def backup_to_drive(self, *args):
		try:
			url = "https://drive.google.com"  # Google Drive URL
			self.is_account_created()
			webbrowser.open(url)
			toast('select your file from storage folder')
		except:
			toast('an error occured')
		
	def close_app(self, *args):
		App.get_running_app().stop()
		toast("Exiting from app, thank you")
		
	def is_account_created(self):
		if financial_data['other_information']['app_key'] == "ddjfj-d5i463iwourjd_rj0p4dkkkru-d43mhaphjfjj":
			toast("account to backup not found")
		else:
			self.back_up_to_download()
		
	def back_up_to_download(self):
		internal_data = self.load_data()
		
		if internal_data == None:
			self.error.text = 'Error in accessing app data'
			self.to_normal()
		else:
			try:
				download_path = financial_data['other_information']['storage_folder']	
				# file name 
				now = datetime.now()
				current_year = now.strftime("%d%m%Y")
				name = financial_data['other_information']['business name']
				file_name = f"{name} {current_year}.ssdata"
				external_file_path = os.path.join(download_path, file_name)
				
				with open(external_file_path, 'w') as file:
					file.write(internal_data)
				#self.dismiss()
				self.error.text = 'Local backup created successfully'
				#self.to_normal()
				toast("Local backup saved to storage path")
			except:
				self.error.text = 'Storage folder not found'
				self.to_normal()
				toast("Error in accessing storage folder")
		
		
	def load_data(self):
		try:
			with open(fin_data_file, 'r') as file:
				return file.read()
		except FileNotFoundError:
			return None
			
			
			
'''
transfer funds
'''

class TransferFunds(Popup):
	def __init__(self, **kwargs):
		super(TransferFunds, self).__init__(**kwargs)
		
	# normal
	def to_normal(self):
		def normal(*args):
			self.error.text = 'All fields are required'
			
		Clock.schedule_once(normal, 3)
		
	# show current date on homepage
	def show_date(self):
		now = datetime.now()
		today = now.strftime("%d-%m-%Y")
		return today
		
	def select_date(self, date_field):
		global on_date_field
		on_date_field = date_field
		popup = DatesPopup()
		popup.open()
		
	def update_bank_accounts(self):
		accounts = view_accounts(financial_data, 'Bank')
		return accounts
		
	def return_balance_remaining(self, account_name):
		start_date = financial_data['other_information']['start_date']
		end_date = financial_data['other_information']['end_date']
		account_balance = income_statement_deractives(financial_data, 'Bank', account_name, start_date, end_date)
		
		return str(account_balance)
		
	def show_the_account_balance(self, account_name):
		start_date = financial_data['other_information']['start_date']
		end_date = financial_data['other_information']['end_date']
		account_balance = income_statement_deractives(financial_data, 'Bank', account_name, start_date, end_date)
		self.ids.account_balance.text = str(account_balance)
		
	def make_fund_transfer(self, from_account, to_account, account_balance, transfer_amount, transaction_date):
		if from_account == 'Select Bank' or to_account == 'Select Bank':
			self.error.text = 'Select from and to bank accounts'
			self.to_normal()
		else:
			if float(account_balance) <= 0:
				self.error.text = f'There are no enough funds in {from_account}'
				self.to_normal()
			else:
				if transfer_amount:
					if float(transfer_amount) <=0:
						self.error.text = f'Please enter a postive amount'
						self.to_normal()
					else:
						if from_account == to_account:
							self.error.text = f'You cannot transfer to same account'
							self.to_normal()
						else:
							self.transfer(from_account, to_account, transfer_amount, transaction_date)
				else:
					self.error.text = f'Please enter a transfer amount'
					self.to_normal()
					
	def transfer(self, from_account, to_account, transfer_amount, transaction_date):
		transaction_amount = round(float(transfer_amount), 2)
		transaction_id = get_transaction_id(financial_data)
		# debit
		add_transaction(financial_data, 'Bank', to_account, abs(transaction_amount), f"tansfer from {from_account}", 'debit', f"Bank|{from_account}", transaction_date, transaction_id)
		# credit
		add_transaction(financial_data, 'Bank', from_account, abs(transaction_amount), f"tansfer to {to_account}", 'credit', f"Bank|{to_account}", transaction_date, transaction_id)
		
		self.ids.transfer_amount.text = ''
		self.error.text = 'Fund Transfer Complete'
		self.to_normal()
		toast('Success on fund transfer')
		
		self.ids.account_balance.text = self.return_balance_remaining(from_account)
		
		'''saved popup'''
		saved_it = SavedPopup()
		saved_it.open()
							
		def close_event(*args):
			saved_it.dismiss()
			
		Clock.schedule_once(close_event, 3)
		
		app = App.get_running_app()
							
		home = app.root.get_screen('home')
		generate_the_dashboard_items(home.dashboard,home.expenses,home.incomes,home.net_profit,home.bank)
		last_upated_date()
		
		
'''
receive payment
'''


class ReceivePayment(Popup):
	def __init__(self, **kwargs):
		super(ReceivePayment, self).__init__(**kwargs)
		self.disallowed_chars = ['"', '|', "'"]
		
	# normal
	def to_normal(self):
		def normal(*args):
			self.error.text = 'All fields are required'
			
		Clock.schedule_once(normal, 3)
		
	def on_text_account(self, value):
		# Function to filter or prevent certain characters
		characters  = value.text
		filtered_text = ''.join(char for char in characters if char not in self.disallowed_chars)
		value.text = filtered_text
		
	# show current date on homepage
	def show_date(self):
		now = datetime.now()
		today = now.strftime("%d-%m-%Y")
		return today
		
	def select_date(self, date_field):
		global on_date_field
		on_date_field = date_field
		popup = DatesPopup()
		popup.open()
		
	def update_bank_accounts(self):
		accounts = view_accounts(financial_data, 'Bank')
		return accounts
		
	def update_receivable_accounts(self):
		accounts = view_accounts(financial_data, 'Current Assets')
		return accounts
		
	def receive_payment(self, transaction_date, account_receivable, to_account, amount, memo):
		if account_receivable == 'Select A/R' or to_account == 'Select Bank':
			self.error.text = 'please select both receivable and bank accounts'
			self.to_normal()
		else:
			if account_receivable == to_account:
				self.error.text = 'You cannot receive from same accounts'
				self.to_normal()
			else:
				if amount and memo:
					if float(amount) <= 0:
						self.error.text = 'enter a positive amount'
						self.to_normal()
					else:
						self.receive(transaction_date, account_receivable, to_account, amount, memo)
				else:
					self.error.text = 'Please enter an amount/ description'
					self.to_normal()
					
	def receive(self, transaction_date, account_receivable, to_account, amount, memo):
		transaction_amount = round(float(amount), 2)
		transaction_id = get_transaction_id(financial_data)
		# debit
		add_transaction(financial_data, 'Bank', to_account, abs(transaction_amount), memo, 'debit', f"Current Assets|{account_receivable}", transaction_date, transaction_id)
		# credit
		add_transaction(financial_data, 'Current Assets', account_receivable, abs(transaction_amount), memo, 'credit', f"Bank|{to_account}", transaction_date, transaction_id)
		
		self.ids.amount.text = ''
		self.ids.memo.text = ''
		self.error.text = 'Payment received successfully'
		self.to_normal()
		toast('Success on receiving payment')
		
		'''saved popup'''
		saved_it = SavedPopup()
		saved_it.open()
							
		def close_event(*args):
			saved_it.dismiss()
			
		Clock.schedule_once(close_event, 3)
		
		app = App.get_running_app()
							
		home = app.root.get_screen('home')
		generate_the_dashboard_items(home.dashboard,home.expenses,home.incomes,home.net_profit,home.bank)
		last_upated_date()
		
		
'''
make payment
'''


class MakePayment(Popup):
	def __init__(self, **kwargs):
		super(MakePayment, self).__init__(**kwargs)
		self.disallowed_chars = ['"', '|', "'"]
		
	# normal
	def to_normal(self):
		def normal(*args):
			self.error.text = 'All fields are required'
			
		Clock.schedule_once(normal, 3)
		
	# show current date on homepage
	def show_date(self):
		now = datetime.now()
		today = now.strftime("%d-%m-%Y")
		return today
		
	def on_text_account(self, value):
		# Function to filter or prevent certain characters
		characters  = value.text
		filtered_text = ''.join(char for char in characters if char not in self.disallowed_chars)
		value.text = filtered_text
		
	def select_date(self, date_field):
		global on_date_field
		on_date_field = date_field
		popup = DatesPopup()
		popup.open()
		
	def update_bank_accounts(self):
		accounts = view_accounts(financial_data, 'Bank')
		return accounts
		
	def update_payable_accounts(self):
		accounts = view_accounts(financial_data, 'Current Liabilities')
		return accounts
		
	def make_payment(self, transaction_date, account_payable, from_account, amount, memo):
		if account_payable == 'Select A/P' or from_account == 'Select Bank':
			self.error.text = 'please select both payable and bank accounts'
			self.to_normal()
		else:
			if account_payable == from_account:
				self.error.text = 'You cannot pay to same accounts'
				self.to_normal()
			else:
				if amount and memo:
					if float(amount) <= 0:
						self.error.text = 'enter a positive amount'
						self.to_normal()
					else:
						self.pay(transaction_date, account_payable, from_account, amount, memo)
				else:
					self.error.text = 'Please enter an amount/ description'
					self.to_normal()
					
	def pay(self, transaction_date, account_payable, from_account, amount, memo):
		transaction_amount = round(float(amount), 2)
		transaction_id = get_transaction_id(financial_data)
		# debit
		add_transaction(financial_data, 'Current Liabilities', account_payable, abs(transaction_amount), memo, 'debit', f"Bank|{from_account}", transaction_date, transaction_id)
		# credit
		add_transaction(financial_data, 'Bank', from_account, abs(transaction_amount), memo, 'credit', f"Current Liabilities|{account_payable}", transaction_date, transaction_id)
		
		self.ids.amount.text = ''
		self.ids.memo.text = ''
		self.error.text = 'Payment made successfully'
		self.to_normal()
		toast('Success on making payment')
		
		'''saved popup'''
		saved_it = SavedPopup()
		saved_it.open()
							
		def close_event(*args):
			saved_it.dismiss()
			
		Clock.schedule_once(close_event, 3)
		
		app = App.get_running_app()
							
		home = app.root.get_screen('home')
		generate_the_dashboard_items(home.dashboard,home.expenses,home.incomes,home.net_profit,home.bank)
		last_upated_date()
		
		
'''
write cheque
'''

class WriteCheques(Popup):
	def __init__(self, **kwargs):
		super(WriteCheques, self).__init__(**kwargs)
		self.disallowed_chars = ['"', '|', "'"]
		
	# normal
	def to_normal(self):
		def normal(*args):
			self.error.text = 'All fields are required'
			
		Clock.schedule_once(normal, 3)
		
	# show current date on homepage
	def show_date(self):
		now = datetime.now()
		today = now.strftime("%d-%m-%Y")
		return today
		
	def select_date(self, date_field):
		global on_date_field
		on_date_field = date_field
		popup = DatesPopup()
		popup.open()
		
	def update_bank_accounts(self):
		accounts = view_accounts(financial_data, 'Bank')
		return accounts
		
	def on_text_account(self, value):
		# Function to filter or prevent certain characters
		characters  = value.text
		filtered_text = ''.join(char for char in characters if char not in self.disallowed_chars)
		value.text = filtered_text
		
	def load_expenses_accounts(self, expense_category):
		accounts = view_accounts(financial_data, expense_category)
		self.expense_account.values = accounts
		self.expense_account.text = 'Expense Account'
		
	def confirm_cheque(self, transaction_date, expense_category, expense_account, from_account, amount, memo):
		if expense_account == 'Expense Account' or from_account == 'Select Bank':
			self.error.text = 'please select both expense and bank accounts'
			self.to_normal()
		else:
			if expense_account == from_account:
				self.error.text = 'You cannot cheque from same accounts'
				self.to_normal()
			else:
				if amount and memo:
					if float(amount) <= 0:
						self.error.text = 'enter a positive amount'
						self.to_normal()
					else:
						if expense_account == 'Depreciation':
							self.error.text = 'please use designated panels to record Depreciation'
							self.to_normal()
						else:
							self.write_cheque(transaction_date, expense_category, expense_account, from_account, amount, memo)
				else:
					self.error.text = 'Please enter an amount and a description'
					self.to_normal()
					
	def write_cheque(self, transaction_date, expense_category, expense_account, from_account, amount, memo):
		transaction_amount = round(float(amount), 2)
		transaction_id = get_transaction_id(financial_data)
		# debit
		add_transaction(financial_data, expense_category, expense_account, abs(transaction_amount), memo, 'debit', f"Bank|{from_account}", transaction_date, transaction_id)
		# credit
		add_transaction(financial_data, 'Bank', from_account, abs(transaction_amount), memo, 'credit', f"{expense_category}|{expense_account}", transaction_date, transaction_id)
		
		self.ids.amount.text = ''
		self.ids.memo.text = ''
		self.error.text = f'Cheque written to {expense_account}'
		self.to_normal()
		toast('Success on Writing Cheque')
		
		'''saved popup'''
		saved_it = SavedPopup()
		saved_it.open()
							
		def close_event(*args):
			saved_it.dismiss()
			
		Clock.schedule_once(close_event, 3)
		
		app = App.get_running_app()
							
		home = app.root.get_screen('home')
		generate_the_dashboard_items(home.dashboard,home.expenses,home.incomes,home.net_profit,home.bank)
		last_upated_date()
		
		
'''
quick journal
'''


class QuickJournal(Popup):
	def __init__(self, **kwargs):
		super(QuickJournal, self).__init__(**kwargs)
		self.disallowed_chars = ['"', '|', "'"]
		
	# normal
	def to_normal(self):
		def normal(*args):
			self.error.text = 'All fields are required'
			
		Clock.schedule_once(normal, 3)
		
	# show current date on homepage
	def show_date(self):
		now = datetime.now()
		today = now.strftime("%d-%m-%Y")
		return today
		
	def select_date(self, date_field):
		global on_date_field
		on_date_field = date_field
		popup = DatesPopup()
		popup.open()
		
	def on_text_account(self, value):
		# Function to filter or prevent certain characters
		characters  = value.text
		filtered_text = ''.join(char for char in characters if char not in self.disallowed_chars)
		value.text = filtered_text
		
	def load_category_accounts(self, category, side):
		if side == 'debit':
			accounts = view_accounts(financial_data, category)
			self.debit_account.values = accounts
			self.debit_account.text = 'Choose Account'
		else:
			accounts = view_accounts(financial_data, category)
			self.credit_account.values = accounts
			self.credit_account.text = 'Choose Account'
			
	def confirm_journal(self, transaction_date, debit_category, debit_account, credit_category, credit_account, amount, memo):
		if debit_account == 'Choose Account' or credit_account == 'Choose Account':
			self.error.text = 'please select both debit and credit accounts'
			self.to_normal()
		else:
			if f"{debit_category}{debit_account}" == f"{credit_category}{credit_account}":
				self.error.text = 'You cannot save journal to same accounts'
				self.to_normal()
			else:
				if amount and memo:
					if float(amount) <= 0:
						self.error.text = 'enter a positive amount'
						self.to_normal()
					else:
						if debit_account == 'Depreciation' or credit_account == 'Depreciation':
							self.error.text = 'please use designated panels to record Depreciation'
							self.to_normal()
						else:
							self.save_journal(transaction_date, debit_category, debit_account, credit_category, credit_account, amount, memo)
				else:
					self.error.text = 'Please enter an amount and a description'
					self.to_normal()
					
	def save_journal(self, transaction_date, debit_category, debit_account, credit_category, credit_account, amount, memo):
		transaction_amount = round(float(amount), 2)
		transaction_id = get_transaction_id(financial_data)
		double_debit = f"{credit_category}|{credit_account}"
		double_credit = f"{debit_category}|{debit_account}"
		
		# debit
		add_transaction(financial_data, debit_category, debit_account, abs(transaction_amount), memo, 'debit', double_debit, transaction_date, transaction_id)
		# credit
		add_transaction(financial_data, credit_category, credit_account, abs(transaction_amount), memo, 'credit', double_credit, transaction_date, transaction_id)
		
		self.ids.amount.text = ''
		self.ids.memo.text = ''
		self.error.text = f'Journal Saved to Books'
		self.to_normal()
		toast('Success on saving Journal')
		
		'''saved popup'''
		saved_it = SavedPopup()
		saved_it.open()
							
		def close_event(*args):
			saved_it.dismiss()
			
		Clock.schedule_once(close_event, 3)
		
		app = App.get_running_app()
							
		home = app.root.get_screen('home')
		generate_the_dashboard_items(home.dashboard,home.expenses,home.incomes,home.net_profit,home.bank)
		last_upated_date()
		
		
	
class OpeningBalance(Popup):
	def __init__(self, **kwargs):
		super(OpeningBalance, self).__init__(**kwargs)
		self.disallowed_chars = ['"', '|', "'"]
		
	# normal
	def to_normal(self):
		def normal(*args):
			self.error.text = 'All fields are required'
			
		Clock.schedule_once(normal, 3)
		
	# show current date on homepage
	def show_date(self):
		now = datetime.now()
		today = now.strftime("%d-%m-%Y")
		return today
		
	def select_date(self, date_field):
		global on_date_field
		on_date_field = date_field
		popup = DatesPopup()
		popup.open()
		
	def on_text_account(self, value):
		# Function to filter or prevent certain characters
		characters  = value.text
		filtered_text = ''.join(char for char in characters if char not in self.disallowed_chars)
		value.text = filtered_text
		
	def load_category_accounts(self, category):
		accounts = view_accounts(financial_data, category)
		self.account_name.values = accounts
		self.account_name.text = 'Choose Account'
		
	def load_credit_or_debit_categories(self, category_group):
		debits = ['Non Current Assets', 'Current Assets', 'Operating Expenses', 'Other Expenses', 'Bank', 'Taxes', 'Cost of Sales']
		credits = ['Capital', 'Non Current Liabilities', 'Current Liabilities', 'Other Incomes', 'Operating Revenue']
		if category_group == 'Dedit Account':
			self.account_category.values = debits
		elif category_group == 'Credit Account':
			self.account_category.values = credits
		else:
			self.account_category.values = []
		
		self.account_category.text = 'Account Category'
		self.account_name.text = 'Choose Account'
		self.account_name.values = []
		
	def confirm_opening_balance(self, transaction_date, debit_or_credit, account_category, account_name, amount):
		if debit_or_credit == 'Credit or Debit Account':
			self.error.text = 'Please Select if the account is credit or debit'
			self.to_normal()
		else:
			if account_name == 'Choose Account':
				self.error.text = 'Select both the category and account'
				self.to_normal()
			else:
				if f"{account_category}{account_name}" == 'CapitalOpening Balance Equity':
					self.error.text ='You cannot counter record Opening Balance Equity'
					self.to_normal()
				else:
					if amount:
						if float(amount) <= 0:
							self.error.text = 'enter a positive amount'
							self.to_normal()
						else:
							if account_name == 'Depreciation':
								self.error.text = 'please use designated panels to record Depreciation'
								self.to_normal()
							else:
								self.record_balance(transaction_date, debit_or_credit, account_category, account_name, amount)
					else:
						self.error.text = 'please enter opening amount'
						self.to_normal()
		
	def record_balance(self, transaction_date, debit_or_credit, account_category, account_name, amount):
		transaction_amount = round(float(amount), 2)
		transaction_id = get_transaction_id(financial_data)
		double_account = f"Capital|Opening Balance Equity"
		
		if debit_or_credit == 'Dedit Account':
			memo = f"opening balance {account_name}"
			double_debit = f"{account_category}|{account_name}"
			# debit
			add_transaction(financial_data, account_category, account_name, abs(transaction_amount), memo, 'debit', double_account, transaction_date, transaction_id)
			# credit
			add_transaction(financial_data, 'Capital', 'Opening Balance Equity', abs(transaction_amount), memo, 'credit', double_debit, transaction_date, transaction_id)
		else:
			memo = f"opening balance {account_name}"
			double_credit = f"{account_category}|{account_name}"
			# debit
			add_transaction(financial_data, 'Capital', 'Opening Balance Equity', abs(transaction_amount), memo, 'debit', double_credit, transaction_date, transaction_id)
			# credit
			add_transaction(financial_data, account_category, account_name, abs(transaction_amount), memo, 'credit', double_account, transaction_date, transaction_id)
		
		self.ids.amount.text = ''
		self.error.text = f'Opening balance Saved to Books'
		self.to_normal()
		toast('Success on saving opening balance')
		self.ids.debit_or_credit.text = 'Credit or Debit Account'
		
		'''saved popup'''
		saved_it = SavedPopup()
		saved_it.open()
							
		def close_event(*args):
			saved_it.dismiss()
			
		Clock.schedule_once(close_event, 3)
		
		app = App.get_running_app()
							
		home = app.root.get_screen('home')
		generate_the_dashboard_items(home.dashboard,home.expenses,home.incomes,home.net_profit,home.bank)
		last_upated_date()
		
		
'''
accumulated depreciation
'''


class AccumulatedDepreciation(Popup):
	def __init__(self, **kwargs):
		super(AccumulatedDepreciation, self).__init__(**kwargs)
		self.disallowed_chars = ['"', '|', "'"]
		
	# normal
	def to_normal(self):
		def normal(*args):
			self.error.text = 'All fields are required'
			
		Clock.schedule_once(normal, 3)
		
	# show current date on homepage
	def show_date(self):
		now = datetime.now()
		today = now.strftime("%d-%m-%Y")
		return today
		
	def select_date(self, date_field):
		global on_date_field
		on_date_field = date_field
		popup = DatesPopup()
		popup.open()
		
	def on_text_account(self, value):
		# Function to filter or prevent certain characters
		characters  = value.text
		filtered_text = ''.join(char for char in characters if char not in self.disallowed_chars)
		value.text = filtered_text
		
	def load_non_current_assets_accounts(self):
		accounts = view_accounts(financial_data, 'Non Current Assets')
		return accounts
		
	def get_the_accum_dep(self, category, account):
		account = f'{category}|{account}'
		if account in financial_data['other_information']['accum_depreciation']:
			return financial_data['other_information']['accum_depreciation'][account]
		else:
			return 0
			
	def save_the_accumulated_depreciation(self, category, account, dep_amount):
		accum_dep = self.get_the_accum_dep(category, account)
		if accum_dep == 0:
			previous_saved_dep = 0
		else:
			previous_saved_dep = accum_dep
			
		new_dep = previous_saved_dep + dep_amount
		financial_data['other_information']['accum_depreciation'][f'{category}|{account}'] = round(new_dep,2)
		save_data(financial_data)
		
	def confirm_accumulated_depreciation(self, transaction_date, non_current_asset, amount):
		if non_current_asset == 'Select Account':
			self.error.text = 'please select the affected non current asset'
			self.to_normal()
		else:
			if amount:
				if float(amount) <= 0:
					self.error.text = 'enter a positive amount'
					self.to_normal()
				else:
					self.save_accum_dep(transaction_date, non_current_asset, amount)
			else:
				self.error.text = 'please enter an amount'
				self.to_normal()
				
	def save_accum_dep(self, transaction_date, non_current_asset, amount):
		transaction_amount = round(float(amount), 2)
		transaction_id = get_transaction_id(financial_data)
		
		double_debit = f"Non Current Assets|{non_current_asset}"
		double_credit = f"Capital|Opening Balance Equity"
		memo = f"Accumulated depreciation {non_current_asset}"
		
		# debit
		add_transaction(financial_data, 'Capital', 'Opening Balance Equity', abs(transaction_amount), memo, 'debit', double_debit, transaction_date, transaction_id)
		# credit
		add_transaction(financial_data, 'Non Current Assets', non_current_asset, abs(transaction_amount), memo, 'credit', double_credit, transaction_date, transaction_id)
		
		self.save_the_accumulated_depreciation('Non Current Assets', non_current_asset, transaction_amount)
		
		self.ids.amount.text = ''
		self.error.text = f'Accum Dep Saved to Books'
		self.to_normal()
		toast('Success on saving Accum Dep')
		
		'''saved popup'''
		saved_it = SavedPopup()
		saved_it.open()
							
		def close_event(*args):
			saved_it.dismiss()
			
		Clock.schedule_once(close_event, 3)
		
		app = App.get_running_app()
							
		home = app.root.get_screen('home')
		generate_the_dashboard_items(home.dashboard,home.expenses,home.incomes,home.net_profit,home.bank)
		last_upated_date()
		
		
'''
normal depreciation
'''


class NormalDepreciation(Popup):
	def __init__(self, **kwargs):
		super(NormalDepreciation, self).__init__(**kwargs)
		self.disallowed_chars = ['"', '|', "'"]
		
	# normal
	def to_normal(self):
		def normal(*args):
			self.error.text = 'All fields are required'
			
		Clock.schedule_once(normal, 3)
		
	# show current date on homepage
	def show_date(self):
		now = datetime.now()
		today = now.strftime("%d-%m-%Y")
		return today
		
	def select_date(self, date_field):
		global on_date_field
		on_date_field = date_field
		popup = DatesPopup()
		popup.open()
		
	def on_text_account(self, value):
		# Function to filter or prevent certain characters
		characters  = value.text
		filtered_text = ''.join(char for char in characters if char not in self.disallowed_chars)
		value.text = filtered_text
		
	def load_non_current_assets_accounts(self):
		accounts = view_accounts(financial_data, 'Non Current Assets')
		return accounts
		
	def get_the_accum_dep(self, category, account):
		account = f'{category}|{account}'
		if account in financial_data['other_information']['accum_depreciation']:
			return financial_data['other_information']['accum_depreciation'][account]
		else:
			return 0
			
	def save_the_accumulated_depreciation(self, category, account, dep_amount):
		accum_dep = self.get_the_accum_dep(category, account)
		if accum_dep == 0:
			previous_saved_dep = 0
		else:
			previous_saved_dep = accum_dep
			
		new_dep = previous_saved_dep + dep_amount
		financial_data['other_information']['accum_depreciation'][f'{category}|{account}'] = round(new_dep,2)
		save_data(financial_data)
		
	def confirm_depreciation(self, transaction_date, operating_or_other, non_current_asset, amount):
		if operating_or_other == 'Operating or Other':
			self.error.text = 'please select the category of depreciation, operating/other'
			self.to_normal()
		else:
			if non_current_asset == 'Select Account':
				self.error.text = 'please select the affected non current asset'
				self.to_normal()
			else:
				if amount:
					if float(amount) <= 0:
						self.error.text = 'enter a positive amount'
						self.to_normal()
					else:
						self.save_depreciation(transaction_date, operating_or_other, non_current_asset, amount)
				else:
					self.error.text = 'please enter an amount'
					self.to_normal()
					
	def save_depreciation(self, transaction_date, operating_or_other, non_current_asset, amount):
		transaction_amount = round(float(amount), 2)
		transaction_id = get_transaction_id(financial_data)
		memo = f"Depreciation of {non_current_asset}"
		
		double_debit = f"Non Current Assets|{non_current_asset}"
		double_credit = f"{operating_or_other}|Depreciation"
		
		# debit
		add_transaction(financial_data, operating_or_other, 'Depreciation', abs(transaction_amount), memo, 'debit', double_debit, transaction_date, transaction_id)
		# credit
		add_transaction(financial_data, 'Non Current Assets', non_current_asset, abs(transaction_amount), memo, 'credit', double_credit, transaction_date, transaction_id)
		
		self.ids.amount.text = ''
		self.error.text = f'Depreciation Saved to Books'
		self.to_normal()
		toast('Success on saving Depreciation')
		
		self.save_the_accumulated_depreciation('Non Current Assets', non_current_asset, transaction_amount)
		
		'''saved popup'''
		saved_it = SavedPopup()
		saved_it.open()
							
		def close_event(*args):
			saved_it.dismiss()
			
		Clock.schedule_once(close_event, 3)
		
		app = App.get_running_app()
							
		home = app.root.get_screen('home')
		generate_the_dashboard_items(home.dashboard,home.expenses,home.incomes,home.net_profit,home.bank)
		last_upated_date()
		
		
'''
taxes payment
'''


class PayTaxes(Popup):
	def __init__(self, **kwargs):
		super(PayTaxes, self).__init__(**kwargs)
		self.disallowed_chars = ['"', '|', "'"]
		
	# normal
	def to_normal(self):
		def normal(*args):
			self.error.text = 'All fields are required'
			
		Clock.schedule_once(normal, 3)
		
	# show current date on homepage
	def show_date(self):
		now = datetime.now()
		today = now.strftime("%d-%m-%Y")
		return today
		
	def select_date(self, date_field):
		global on_date_field
		on_date_field = date_field
		popup = DatesPopup()
		popup.open()
		
	def on_text_account(self, value):
		# Function to filter or prevent certain characters
		characters  = value.text
		filtered_text = ''.join(char for char in characters if char not in self.disallowed_chars)
		value.text = filtered_text
		
	def return_taxes_accounts(self):
		accounts = view_accounts(financial_data, 'Taxes')
		return accounts
		
	def load_category_accounts(self, category):
		accounts = view_accounts(financial_data, category)
		self.ids.account_name.values = accounts
		self.ids.account_name.text = 'Choose Account'
		
	def confirm_taxes_payment(self, transaction_date, taxes_account, account_category, account_name, amount):
		if taxes_account == 'Select Account':
			self.error.text = 'please select the tax account to save taxes'
			self.to_normal()
		else:
			if account_name == 'Choose Account':
				self.error.text = 'please select the bank or liability account to pay taxes'
				self.to_normal()
			else:
				if amount:
					if float(amount) <= 0:
						self.error.text = 'enter a positive amount'
						self.to_normal()
					else:
						self.save_taxes(transaction_date, taxes_account, account_category, account_name, amount)
				else:
					self.error.text = 'please enter an amount'
					self.to_normal()
					
	def save_taxes(self, transaction_date, taxes_account, account_category, account_name, amount):
		transaction_amount = round(float(amount), 2)
		transaction_id = get_transaction_id(financial_data)
		memo = f"Paying taxes for {taxes_account}"
		
		double_debit = f"Taxes|{taxes_account}"
		double_credit = f"{account_category}|{account_name}"
		
		# debit
		add_transaction(financial_data, 'Taxes', taxes_account, abs(transaction_amount), memo, 'debit', double_credit, transaction_date, transaction_id)
		# credit
		add_transaction(financial_data, account_category, account_name, abs(transaction_amount), memo, 'credit', double_debit, transaction_date, transaction_id)
		
		self.ids.amount.text = ''
		self.error.text = f'Taxes Saved to Books'
		self.to_normal()
		toast('Success on paying Taxes')
		
		'''saved popup'''
		saved_it = SavedPopup()
		saved_it.open()
							
		def close_event(*args):
			saved_it.dismiss()
			
		Clock.schedule_once(close_event, 3)
		
		app = App.get_running_app()
							
		home = app.root.get_screen('home')
		generate_the_dashboard_items(home.dashboard,home.expenses,home.incomes,home.net_profit,home.bank)
		last_upated_date()
		
		
'''
make sales journal
'''


class MakeSaleJournal(Popup):
	def __init__(self, **kwargs):
		super(MakeSaleJournal, self).__init__(**kwargs)
		self.disallowed_chars = ['"', '|', "'"]
		
	# normal
	def to_normal(self):
		def normal(*args):
			self.error.text = 'All fields are required'
			
		Clock.schedule_once(normal, 3)
		
	# show current date on homepage
	def show_date(self):
		now = datetime.now()
		today = now.strftime("%d-%m-%Y")
		return today
		
	def select_date(self, date_field):
		global on_date_field
		on_date_field = date_field
		popup = DatesPopup()
		popup.open()
		
	def on_text_account(self, value):
		# Function to filter or prevent certain characters
		characters  = value.text
		filtered_text = ''.join(char for char in characters if char not in self.disallowed_chars)
		value.text = filtered_text
		
	def return_sales_accounts(self):
		accounts = view_accounts(financial_data, 'Operating Revenue')
		return accounts
		
	def load_category_accounts(self, category):
		accounts = view_accounts(financial_data, category)
		self.ids.account_name.values = accounts
		self.ids.account_name.text = 'Choose Account'
		
	def confirm_sales_journal(self, transaction_date, sales_account, account_category, account_name, amount, memo):
		if sales_account == 'Select Account':
			self.error.text = 'please select the sales account to save journal'
			self.to_normal()
		else:
			if account_name == 'Choose Account':
				self.error.text = 'please select the bank or customer from current assets'
				self.to_normal()
			else:
				if amount and memo:
					if float(amount) <= 0:
						self.error.text = 'enter a positive amount'
						self.to_normal()
					else:
						self.save_sale_journal(transaction_date, sales_account, account_category, account_name, amount, memo)
				else:
					self.error.text = 'please enter an amount/ description'
					self.to_normal()
					
	def save_sale_journal(self, transaction_date, sales_account, account_category, account_name, amount, memo):
		transaction_amount = round(float(amount), 2)
		transaction_id = get_transaction_id(financial_data)
		
		double_debit = f"Operating Revenue|{sales_account}"
		double_credit = f"{account_category}|{account_name}"
		
		# debit
		add_transaction(financial_data, account_category, account_name, abs(transaction_amount), memo, 'debit', double_debit, transaction_date, transaction_id)
		# credit
		add_transaction(financial_data, 'Operating Revenue', sales_account, abs(transaction_amount), memo, 'credit', double_credit, transaction_date, transaction_id)
		
		self.ids.amount.text = ''
		self.ids.memo.text = ''
		self.error.text = f'Sales Journal Saved to Books'
		self.to_normal()
		toast('Success on making sales journal')
		
		'''saved popup'''
		saved_it = SavedPopup()
		saved_it.open()
							
		def close_event(*args):
			saved_it.dismiss()
			
		Clock.schedule_once(close_event, 3)
		
		app = App.get_running_app()
							
		home = app.root.get_screen('home')
		generate_the_dashboard_items(home.dashboard,home.expenses,home.incomes,home.net_profit,home.bank)
		last_upated_date()
		
		
'''
purchase journal
'''


class MakePurchaseJournal(Popup):
	def __init__(self, **kwargs):
		super(MakePurchaseJournal, self).__init__(**kwargs)
		self.disallowed_chars = ['"', '|', "'"]
		
	# normal
	def to_normal(self):
		def normal(*args):
			self.error.text = 'All fields are required'
			
		Clock.schedule_once(normal, 3)
		
	# show current date on homepage
	def show_date(self):
		now = datetime.now()
		today = now.strftime("%d-%m-%Y")
		return today
		
	def select_date(self, date_field):
		global on_date_field
		on_date_field = date_field
		popup = DatesPopup()
		popup.open()
		
	def on_text_account(self, value):
		# Function to filter or prevent certain characters
		characters  = value.text
		filtered_text = ''.join(char for char in characters if char not in self.disallowed_chars)
		value.text = filtered_text
		
	def return_cosales_accounts(self):
		accounts = view_accounts(financial_data, 'Cost of Sales')
		return accounts
		
	def load_category_accounts(self, category):
		accounts = view_accounts(financial_data, category)
		self.ids.account_name.values = accounts
		self.ids.account_name.text = 'Choose Account'
		
	def confirm_purchase_journal(self, transaction_date, cos_account, account_category, account_name, amount, memo):
		if cos_account == 'Select Account':
			self.error.text = 'please select the Cost of Sales account to save journal'
			self.to_normal()
		else:
			if account_name == 'Choose Account':
				self.error.text = 'please select the bank or supplier from current liabilities'
				self.to_normal()
			else:
				if amount and memo:
					if float(amount) <= 0:
						self.error.text = 'enter a positive amount'
						self.to_normal()
					else:
						self.save_purchase_journal(transaction_date, cos_account, account_category, account_name, amount, memo)
				else:
					self.error.text = 'please enter an amount/ description'
					self.to_normal()
					
	def save_purchase_journal(self, transaction_date, cos_account, account_category, account_name, amount, memo):
		transaction_amount = round(float(amount), 2)
		transaction_id = get_transaction_id(financial_data)
		
		double_debit = f"Cost of Sales|{cos_account}"
		double_credit = f"{account_category}|{account_name}"
		
		# debit
		add_transaction(financial_data, 'Cost of Sales', cos_account, abs(transaction_amount), memo, 'debit', double_credit, transaction_date, transaction_id)
		# credit
		add_transaction(financial_data, account_category, account_name, abs(transaction_amount), memo, 'credit', double_debit, transaction_date, transaction_id)
		
		self.ids.amount.text = ''
		self.ids.memo.text = ''
		self.error.text = f'Purchase Journal Saved to Books'
		self.to_normal()
		toast('Success on making purchase journal')
		
		'''saved popup'''
		saved_it = SavedPopup()
		saved_it.open()
							
		def close_event(*args):
			saved_it.dismiss()
			
		Clock.schedule_once(close_event, 3)
		
		app = App.get_running_app()
							
		home = app.root.get_screen('home')
		generate_the_dashboard_items(home.dashboard,home.expenses,home.incomes,home.net_profit,home.bank)
		last_upated_date()
		
		
'''
enter bill
'''

class EnterBill(Popup):
	def __init__(self, **kwargs):
		super(EnterBill, self).__init__(**kwargs)
		self.disallowed_chars = ['"', '|', "'"]
		
	# normal
	def to_normal(self):
		def normal(*args):
			self.error.text = 'All fields are required'
			
		Clock.schedule_once(normal, 3)
		
	# show current date on homepage
	def show_date(self):
		now = datetime.now()
		today = now.strftime("%d-%m-%Y")
		return today
		
	def select_date(self, date_field):
		global on_date_field
		on_date_field = date_field
		popup = DatesPopup()
		popup.open()
		
	def update_current_liabilities(self):
		accounts = view_accounts(financial_data, 'Current Liabilities')
		return accounts
		
	def on_text_account(self, value):
		# Function to filter or prevent certain characters
		characters  = value.text
		filtered_text = ''.join(char for char in characters if char not in self.disallowed_chars)
		value.text = filtered_text
		
	def load_expenses_accounts(self, expense_category):
		accounts = view_accounts(financial_data, expense_category)
		self.ids.expense_account.values = accounts
		self.ids.expense_account.text = 'Expense Account'
		
	def confirm_bill(self, transaction_date, expense_category, expense_account, liability_account, amount, memo):
		if expense_account == 'Expense Account' or liability_account == 'Select Account':
			self.error.text = 'please select both expense and liability accounts'
			self.to_normal()
		else:
			if expense_account == liability_account:
				self.error.text = 'You cannot bill from same accounts'
				self.to_normal()
			else:
				if amount and memo:
					if float(amount) <= 0:
						self.error.text = 'enter a positive amount'
						self.to_normal()
					else:
						if expense_account == 'Depreciation':
							self.error.text = 'please use designated panels to record Depreciation'
							self.to_normal()
						else:
							self.save_bill(transaction_date, expense_category, expense_account, liability_account, amount, memo)
				else:
					self.error.text = 'Please enter an amount and a description'
					self.to_normal()
					
	def save_bill(self, transaction_date, expense_category, expense_account, liability_account, amount, memo):
		transaction_amount = round(float(amount), 2)
		transaction_id = get_transaction_id(financial_data)
		# debit
		add_transaction(financial_data, expense_category, expense_account, abs(transaction_amount), memo, 'debit', f"Current Liabilities|{liability_account}", transaction_date, transaction_id)
		# credit
		add_transaction(financial_data, 'Current Liabilities', liability_account, abs(transaction_amount), memo, 'credit', f"{expense_category}|{expense_account}", transaction_date, transaction_id)
		
		self.ids.amount.text = ''
		self.ids.memo.text = ''
		self.error.text = f'Bill entered to {expense_account}'
		self.to_normal()
		toast('Success on Entering Bill')
		
		'''saved popup'''
		saved_it = SavedPopup()
		saved_it.open()
							
		def close_event(*args):
			saved_it.dismiss()
			
		Clock.schedule_once(close_event, 3)
		
		app = App.get_running_app()
							
		home = app.root.get_screen('home')
		generate_the_dashboard_items(home.dashboard,home.expenses,home.incomes,home.net_profit,home.bank)
		last_upated_date()

			
'''last updated logic
'''

def last_upated_date():
	home = App.get_running_app().root.get_screen('home')
	
	now = datetime.now()
	today = now.strftime("%d-%m-%Y")
	current_time = now.strftime("%H:%M:%S")
	day_name = now.strftime("%A")
		
	print_date = f"Last updated: {day_name}, {today}, {current_time}"
	
	financial_data["other_information"]["last_updated"] = print_date
	save_data(financial_data)
		
	home.last_updated.text = print_date
	
	
def show_the_last_printed():
	home = App.get_running_app().root.get_screen('home')
	
	if "last_updated" in financial_data["other_information"]:
		print_date = financial_data["other_information"]["last_updated"]
	else:
		print_date = 'Last updated: _____'
	
	home.last_updated.text = print_date	
			

'''
home app panel
'''

global from_home_screen_to_listing
from_home_screen_to_listing = True


class HomeScreen(Screen):
	def __init__(self, **kwargs):
		super(HomeScreen, self).__init__(**kwargs)
		Window.bind(on_keyboard=self.on_key_down)
		self.file_manager = MDFileManager(
			exit_manager=self.exit_manager,
			select_path=self.select_path
		)
		Window.softinput_mode = 'below_target'
		Clock.schedule_once(self.display_current_day, 1)
		self.journal_action = 'None'
		self.special_action = 'None'
		self.report_action = 'None'
		self.analysis_action = 'None'
		self.sales_action = 'None'
		self.purchase_action = 'None'
		self.bill_action = 'None'
		#self.send_daily_notification()
		
	def on_enter(self, *args):
		if 'dark_mode' in financial_data['other_information']:
			mode = financial_data['other_information']['dark_mode']
			if mode == True:
				app = App.get_running_app()
				for child in self.ids.scroll_view.children:
					if isinstance(child, BoxLayout):
						app.traverse_widgets(child)
			else:
				pass
		else:
			pass
		
	def return_the_dark_mode(self):
		if 'dark_mode' in financial_data['other_information']:
			mode = financial_data['other_information']['dark_mode']
			if mode == True:
				return 'Light Mode'
			else:
				return 'Dark Mode'
		else:
			return 'Dark Mode'
			
	def set_dark_mode(self, mode):
		if mode == 'Dark Mode':
			financial_data['other_information']['dark_mode'] = True
			mode = 'Dark'
			self.ids.set_dark_mode.text = 'Light Mode'
			app = App.get_running_app()
			for child in self.ids.scroll_view.children:
				if isinstance(child, BoxLayout):
					app.traverse_widgets(child)
			toast(f"{mode} mode applied")
		else:
			financial_data['other_information']['dark_mode'] = False
			mode = 'Light'
			self.ids.set_dark_mode.text = 'Dark Mode'
			toast(f"{mode} mode applied. Restart app to configure to ligt mode")
		
		save_data(financial_data)
		
	def show_date(self):
		now = datetime.now()
		today = now.strftime("%d-%m-%Y")
		return today
		
	def display_current_day(self, *args):
		now = datetime.now()
		today = now.strftime("%d-%m-%Y")
		current_time = now.strftime("%H:%M:%S")
		day_name = now.strftime("%A")
		
		print_date = f"Logged in: {day_name}, {today}, {current_time}"
		self.date_and_time.text = print_date
		
	def layout_height(self):
		# Calculate the height based on the content dynamically
		total_height = sum(child.height for child in self.ids.functions_layout.children)
		return total_height
		
	def send_daily_notification(self, *args):
		notification.notify(
			title='SimploStats',
			message='Financial info in your fingertips',
			app_icon=None,  # e.g., 'path/to/icon.png'
			timeout=10,  # seconds
		)
        
	def go_back(self):
		self.manager.current = 'log_in'
		
	def open_the_selected_spinner(self, action):
		if action == 'Quick\nJournal':
			self.make_quick_jounal()
			self.journal_action = action
		elif action == 'Write\nCheques':
			self.write_cheques()
			self.journal_action = action
		elif action == 'Transfer\nfunds':
			self.make_funds_transfer()
			self.journal_action = action
		elif action == 'Receive\nPayment':
			self.receive_payment()
			self.journal_action = action
			self.sales_action = action
		elif action == 'Make\nPayment':
			self.make_payment()
			self.journal_action = action
			self.bill_action = action
			self.purchase_action = action
		elif action == 'Sale\nListing':
			self.go_to_invoicing()
			self.journal_action = action
			self.sales_action = action
		elif action == 'Journal\nEntries':
			self.go_to_journal_entries()
			self.journal_action = action
		elif action == 'Opening\nBalance':
			self.record_opening_balance()
			self.special_action = action
		elif action == 'Pay\nTaxes':
			self.pay_liability_taxes()
			self.special_action = action
		elif action == 'Normal\nDepreciation':
			self.record_normal_dep()
			self.special_action = action
		elif action == 'Accumulated\nDepreciation':
			self.record_accum_dep()
			self.special_action = action
		elif action == 'Sale\nJournal':
			self.make_sale_journal()
			self.sales_action = action
		elif action == 'Purchase\nJournal':
			self.make_purchase_journal()
			self.purchase_action = action
		elif action == 'Income\nStament':
			self.go_to_income_statement()
			self.report_action = action
		elif action == 'Balance\nSheet':
			self.go_to_balance_sheet()
			self.report_action = action
		elif action == 'Trial\nBalance':
			self.go_to_trial_balance()
			self.report_action = action
		elif action == 'Account\nRecords':
			self.go_to_accounts_viewing()
			self.report_action = action
		elif action == 'Budget\nAnalysis':
			self.go_to_budgeting()
			self.analysis_action = action
		elif action == 'Financial\nAnalysis':
			self.go_to_financial_analysis()
			self.analysis_action = action
		elif action == 'Balances\nAnalysis':
			self.go_to_balances_analysis()
			self.analysis_action = action
		elif action == 'Operations\nAnalysis':
			self.go_to_operation_analysis()
			self.analysis_action = action
		elif action == 'Enter\nBill':
			self.enter_bill()
			self.bill_action = action
			
	def main_journal_button_func(self):
		action = self.journal_action
		if action == 'Quick\nJournal':
			self.make_quick_jounal()
		elif action == 'Write\nCheques':
			self.write_cheques()
		elif action == 'Transfer\nfunds':
			self.make_funds_transfer()
		elif action == 'Receive\nPayment':
			self.receive_payment()
		elif action == 'Make\nPayment':
			self.make_payment()
		elif action == 'Sale\nListing':
			self.go_to_invoicing()
		elif action == 'Journal\nEntries':
			self.go_to_journal_entries()
		else:
			pass
			
	def main_special_button_func(self):
		action = self.special_action
		if action == 'Opening\nBalance':
			self.record_opening_balance()
		elif action == 'Pay\nTaxes':
			self.pay_liability_taxes()
		elif action == 'Normal\nDepreciation':
			self.record_normal_dep()
		elif action == 'Accumulated\nDepreciation':
			self.record_accum_dep()
			
	def main_sale_button_func(self):
		action = self.sales_action
		if action == 'Sale\nJournal':
			self.make_sale_journal()
		elif action == 'Receive\nPayment':
			self.receive_payment()
		elif action == 'Sale\nListing':
			self.go_to_invoicing()
			
	def main_purchase_button_func(self):
		action = self.purchase_action
		if action == 'Purchase\nJournal':
			self.make_purchase_journal()
		elif action == 'Make\nPayment':
			self.make_payment()
	
	def main_report_button_func(self):	
		action = self.report_action
		if action == 'Income\nStament':
			self.go_to_income_statement()
		elif action == 'Balance\nSheet':
			self.go_to_balance_sheet()
		elif action == 'Trial\nBalance':
			self.go_to_trial_balance()
		elif action == 'Account\nRecords':
			self.go_to_accounts_viewing()
			
	def main_analysis_button_func(self):	
		action = self.analysis_action
		if action == 'Budget\nAnalysis':
			self.go_to_budgeting()
		elif action == 'Financial\nAnalysis':
			self.go_to_financial_analysis()
		elif action == 'Balances\nAnalysis':
			self.go_to_balances_analysis()
		elif action == 'Operations\nAnalysis':
			self.go_to_operation_analysis()
			
	def main_bill_button_func(self):	
		action = self.bill_action
		if action == 'Enter\nBill':
			self.enter_bill()
		elif action == 'Make\nPayment':
			self.make_payment()
		
	def go_to_help(self, *args):
		self.manager.current = 'help'
		
	def make_funds_transfer(self, *args):
		popup = TransferFunds()
		popup.open()
	
	def receive_payment(self, *args):
		popup = ReceivePayment()
		popup.open()
		
	def make_payment(self, *args):
		popup = MakePayment()
		popup.open()
		
	def write_cheques(self, *args):
		popup = WriteCheques()
		popup.open()
		
	def make_quick_jounal(self, *args):
		popup = QuickJournal()
		popup.open()
		
	def record_opening_balance(self, *args):
		popup = OpeningBalance()
		popup.open()
		
	def record_accum_dep(self, *args):
		popup = AccumulatedDepreciation()
		popup.open()
		
	def record_normal_dep(self, *args):
		popup = NormalDepreciation()
		popup.open()
	
	def pay_liability_taxes(self, *args):
		popup = PayTaxes()
		popup.open()
		
	def make_sale_journal(self, *args):
		popup = MakeSaleJournal()
		popup.open()
		
	def make_purchase_journal(self, *args):
		popup = MakePurchaseJournal()
		popup.open()
		
	def enter_bill(self, *args):
		popup = EnterBill()
		popup.open()
	
	def go_to_financial_analysis(self, *args):
		self.manager.current = 'analysis'
		
	def go_to_balances_analysis(self, *args):
		self.manager.current = 'balances'
		
	def go_to_budgeting(self, *args):
		self.manager.current = 'budget'
			
	def go_to_charts_of_accounts(self, *args):
		self.manager.current = 'charts_of_accounts'
		
	def donate_to_us(self, *args):
		popup = DonateToAkauntin()
		popup.open()
		
	def open_about_popup(self, *args):
		popup = AboutsAndLegality()
		popup.open()
		
	def go_to_trial_balance(self, *args):
		self.manager.current = 'trial_balance'
		
	def set_password(self, *args):
		popup = PasswordSettings()
		popup.open()
		
	def backup_data(self, *args):
		popup = BackUpData()
		popup.open()
		
	def show_copy_write(self):
		now = datetime.now()
		today =  str(now.strftime("%Y"))
		return f"SimploStats © {today}"
		
	def exit_from_imported_file(self, function):
		if function == 'Import file':
			toast('No file is imported')
		else:
			self.show_file_manager(function)
		
	def show_file_manager(self, instance):
		function = instance.text
		global financial_data
		global fin_data_file
		global is_the_imported_file
		if function == 'Import file':
			self.import_file.text = 'Exit from imported file'
			self.file_manager.show(path="/storage/emulated/0/")
		else:
			charts = self.manager.get_screen('charts_of_accounts')
			charts.account_category.text = 'Account Category'
			charts.list_of_accounts_layout.clear_widgets()
			self.import_file.text =  'Import file'
			self.selected_file.text = 'imported file will show here'
			is_the_imported_file = 'imported file will show here'
			fin_data_file = back_to_app_file
			financial_data = load_data()
			self.view_status.text = ' '
			self.business.text = self.return_business_details()
			toast("Exited from imported file")
			log = self.manager.get_screen('log_in')
			
			if 'business name' in financial_data['other_information']:
				name = financial_data['other_information']['business name']
			else:
				name = 'New biz'
				
			hey_there = f"Nice to see you back, {name}!"	
			log.welcome_user.text = hey_there
			log.image.source = display_profile_picture()
			home = self.manager.get_screen('home')
			home.image.source = display_profile_picture()
			self.manager.current = 'log_in'
	
	def select_path(self, path):
		global financial_data
		global fin_data_file
		global is_the_imported_file
		
		if path.endswith(".ssdata"):
			self.selected_file.text = str(path)
			is_the_imported_file = str(path)
				
			try:	
				with open(path, "r") as file:
					data = json.load(file)
						
				financial_data = data
				fin_data_file = path
					
				self.business.text = self.return_business_details()
					
				self.view_status.text = '# working on imported file'
				self.file_manager.close()
				toast('File successfully imported')
			
				log = self.manager.get_screen('log_in')
				name = financial_data['other_information']['business name']
				hey_there = f"Nice to see you back, {name}!"	
				log.welcome_user.text = hey_there
				log.image.source = display_profile_picture()
				self.image.source = display_profile_picture()
					
				self.manager.current = 'log_in'
			except:
				self.view_status.text = 'Unable to load the file'
				self.file_manager.close()
				toast('File error')
		else:
			pass
			toast("only files with (.ssdata) are required")
			
	def return_business_details(self):
		name = financial_data['other_information']['business name']
		email = financial_data['other_information']['business email']
		start = financial_data['other_information']['start_date']
		end = financial_data['other_information']['end_date']
		return f"{name}\n{email}\nFrom:  {start} To:  {end}"

	def exit_manager(self, *args):
		self.file_manager.close()
		
	def show_user_picture(self):
		return display_profile_picture()
		
	def go_to_invoicing(self, *args):
		global from_home_screen_to_listing	
		screen = self.manager.get_screen('invoicing')
		
		with open(fin_data_file, 'r') as file:
			data = json.load(file)
			
		if 'invoices' in data['other_information']:
			invoices = list(data['other_information']['invoices'].keys())
			screen.list_of_invoices.values = invoices
		else:
			screen.list_of_invoices.values = []
			
		screen.status.text = "Status: Creating a list of sale"
		screen.invoice_id.text = ''
		screen.invoice_list.clear_widgets()
		screen.invoice_list.height = 10
		screen.total_amount.text = '0'
		screen.account_name.disabled = False
		screen.sales_account_name.disabled = False
		screen.sales_account_category.disabled = False
		screen.list_of_invoices.text = 'list of sale lists'
		
		self.manager.current = 'invoicing'
		from_home_screen_to_listing = True
			
	def go_to_journal_entries(self, *args):
		global from_journal_to_home
		from_journal_to_home = True
		journal = self.manager.get_screen('Journal_entries')
		journal.status.text = 'Status: Recording a Transaction'
		journal.trans_id.text = ''
		journal.transaction_amount.text = ''
		journal.memo.text = ''
		journal.search_id.text = ''
		journal.transaction_date.text = self.show_date()
		journal.account_category.disabled = False
		journal.account_name.disabled = False
		journal.is_accum_deprec.text = 'journal entry'
		journal.is_accum_deprec.disabled = False
		
		journal.save_button.disabled = False
		journal.edit_button.disabled = False
		journal.delete_button.disabled = False
		#journal.account_category.text = 'Account Category'
		#journal.account_name.text = 'Choose Account'
		#journal.debit_account.text = 'Account'
		#journal.credit_account.text = 'Account'
		#journal.side.text = 'None'
		self.manager.current = 'Journal_entries'
		
	def go_to_accounts_viewing(self, *args):
		global from_view_records_to_home
		self.manager.current = 'view_accounts'
		from_view_records_to_home = True
		
	def get_screen_width(self):
		return Window.width
		
	def go_to_income_statement(self, *args):
		self.manager.current = 'income_statement'
		
	def go_to_operation_analysis(self, *args):
		self.manager.current = 'operations'
		
	def view_expenses_incomes_and_np(self):
		view = self.manager.get_screen('income_statement')
		self.report_action = 'Income\nStament'
		
		def auto_update_income(*args):
			view.split_statement.text = 'Financial year report'
			
		self.manager.current = 'income_statement'
		Clock.schedule_once(auto_update_income, 1)
		
	def view_bank_and_assets_bal(self):
		global from_view_records_to_home
		view = self.manager.get_screen('balance_sheet')
		self.report_action = 'Balance\nSheet'
		
		def auto_update_balances(*args):
			view.split_statement.text = 'As at today'
			
		self.manager.current = 'balance_sheet'
		from_view_records_to_home = True
		Clock.schedule_once(auto_update_balances, 1)
		
	def go_to_balance_sheet(self, *args):
		global from_view_records_to_home
		self.manager.current = 'balance_sheet'
		from_view_records_to_home = True
		
	def go_to_edit_business(self, *args):
		account = self.manager.get_screen('account')
		account.business_name.text = financial_data['other_information']['business name']
		account.business_email.text = financial_data['other_information']['business email']
		account.business_address.text = financial_data['other_information']['business address']
		account.start_date.text = financial_data['other_information']['start_date']
		account.end_date.text = financial_data['other_information']['end_date']
		account.storage_folder.text = financial_data['other_information']['storage_folder']
		
		if "app_theme" in financial_data["other_information"]:
			theme = financial_data["other_information"]["app_theme"]
		else:
			theme = "Indigo"
			
		if 'app_transition' in financial_data["other_information"]:
			trans = financial_data["other_information"]['app_transition']
		else:
			trans = 'FadeTransition'
			
		account.theme.text = theme
		account.ids.app_transition.text = trans
		account.image.source = display_profile_picture()
		account.photo_path.text = str(display_profile_picture())
			
		self.manager.current = 'account'
		
	def on_key_down(self, window, key, *args):
		# Check if the pressed key is the back button (code 27)
		if key == 27:
			if self.manager.current == 'charts_of_accounts':
				self.manager.current = 'home'
			elif self.manager.current == 'Journal_entries':
				if from_journal_to_home == True:
					self.manager.current = 'home'
				else:
					self.manager.current = 'view_accounts'
			elif self.manager.current == 'view_accounts':
				view = self.manager.get_screen('view_accounts')
				if from_view_records_to_home ==True:
					if view.first_scroll_view.do_scroll_y == False:
						view.first_scroll_view.scroll_y = 1
						view.first_scroll_view.do_scroll_y = True
					else:		
						self.manager.current = 'home'
				else:
					if view.first_scroll_view.do_scroll_y == False:
						view.first_scroll_view.scroll_y = 1
						view.first_scroll_view.do_scroll_y = True
					else:		
						self.manager.current = 'income_statement'
			elif self.manager.current == 'income_statement':
				self.manager.current = 'home'
			elif self.manager.current == 'trial_balance':
				self.manager.current = 'home'
			elif self.manager.current == 'balance_sheet':
				self.manager.current = 'home'
			elif self.manager.current == 'home':
				self.manager.current = 'log_in'
			elif self.manager.current == 'account':
				self.manager.current = 'log_in'
			elif self.manager.current == 'analysis':
				self.manager.current = 'home'
			elif self.manager.current == 'balances':
				self.manager.current = 'home'
			elif self.manager.current == 'budget':
				self.manager.current = 'home'
			elif self.manager.current == 'operations':
				self.manager.current = 'home'
			elif self.manager.current == 'invoicing':
				if from_home_screen_to_listing == True:
					self.manager.current = 'home'
				else:
					self.manager.current = 'Journal_entries'
			elif self.manager.current == 'log_in':	
				popup = BackUpDataOrExit()
				popup.open()
			return True

		return False
		
		
'''
global variables used in updating and remembering in calendar
'''
global current_year
global current_month
		
now = datetime.now()
current_year = int(now.strftime("%Y"))
current_month = int(now.strftime("%m"))
	
		
'''
dates selection popup
'''


class DatesPopup(Popup):
	def __init__(self, **kwargs):
		super(DatesPopup, self).__init__(**kwargs)
		self.update_calendar()
		
	def see_month(self):
		if current_month == 1:
			return f"January\n{current_year}"
		elif current_month == 2:
			return f'February\n{current_year}'
		elif current_month == 3:
			return f'March\n{current_year}'
		elif current_month == 4:
			return f'April\n{current_year}'
		elif current_month == 5:
			return f'May\n{current_year}'
		elif current_month == 6:
			return f'June\n{current_year}'
		elif current_month == 7:
			return f'July\n{current_year}'
		elif current_month == 8:
			return f'August\n{current_year}'
		elif current_month == 9:
			return f'September\n{current_year}'
		elif current_month == 10:
			return f'October\n{current_year}'
		elif current_month == 11:
			return f"November\n{current_year}"
		elif current_month == 12:
			return f'December\n{current_year}'
			
	def on_day_press(self, instance):
		day = int(instance.text)
		instance.color = 'white'
		instance.background_color = 'red'
		if len(str(current_month)) == 2:
			month = str(current_month)
		else:
			month = f"0{str(current_month)}"
			
		if len(str(day)) == 2:
			day = str(day)
		else:
			day = f"0{day}"
			
		date = f"{day}-{month}-{current_year}"
		self.dateit.text = date
		on_date_field.text = date
		self.dismiss()
		
		
	def update_calendar(self, *args):
		# todays date
		now = datetime.now()
		today_month = int(now.strftime("%m"))
		today_year = int(now.strftime("%Y"))
		today_day = int(now.strftime("%d"))
		year = current_year
		month = current_month
		self.yr = year
		self.mn = month
		
		cal_layout = self.calendar_grid
		cal_layout.clear_widgets()
		self.days_grid_layout.clear_widgets()
		cal = calendar.monthcalendar(year, month)
		app = App.get_running_app()

		for week in cal:
			for day in week:
				if day == 0:
					cal_layout.add_widget(Button(text=' ', background_color=(255,255,255,1)))
				else:
					if month == today_month and int(day) == today_day and year == today_year:
						bg = app.theme_cls.primary_color
						clr = app.return_icon_color()
					else:
						bg = (255,255,255,1)
						clr = app.return_theme_color()
					day_button = Button(
						text=str(day),
						on_press=self.on_day_press,
						color=clr,
						background_normal='',
						size_hint=(1,None),
						size=("35dp","35dp"),
						background_color=bg,
						font_size="15sp")
					cal_layout.add_widget(day_button)
					
		# Add weekday labels
		for weekday in calendar.day_name:
			self.days_grid_layout.add_widget(
			Button(
				text=f"{weekday[0:3]}..",
				background_color=(255,255,255),
				color='black',
				size=("35dp","35dp"),
				font_size="15sp",
				bold=True))
				
			#cal_layout.add_widget(
			#Button(
			#text=f"{weekday[0:3]}..",
			#background_color='blue',
			#color='white',
			#font_size="14sp",
			#bold=True))
			
	def previous_month(self):
		global current_year
		global current_month
		
		self.mn -= 1
		current_month = self.mn
		if self.mn == 0:
			current_month = 12
			self.yr -= 1
			current_year = self.yr
	
		self.show_month_year.text = self.see_month()	
		self.update_calendar()
		
	def next_month(self):
		global current_year
		global current_month
		
		self.mn += 1
		current_month = self.mn
		if self.mn == 13:
			current_month = 1
			self.yr += 1
			current_year = self.yr
	
		self.show_month_year.text = self.see_month()	
		self.update_calendar()
		
	def on_year_enter(self, value):
		global current_year
		global current_month
		if len(value) == 4:
			current_year = int(value)
			current_month = self.mn
			self.show_month_year.text = self.see_month()
			self.update_calendar()
			
			
'''
invoicing
'''


class SaleListing(Screen):
	def __init__(self, **kwargs):
		super(SaleListing, self).__init__(**kwargs)
		self.disallowed_chars = ['"', '|', "'"]
		Window.softinput_mode = 'below_target'
		self.items_list = []
		self.the_total_amount = 0
		
	def go_back(self):
		if from_home_screen_to_listing == True:
			self.manager.current = 'home'
			self.items_list = []
			self.the_total_amount = 0
		else:
			self.manager.current = 'Journal_entries'
			self.items_list = []
			self.the_total_amount = 0
		
	def on_text_account(self, value):
		# Function to filter or prevent certain characters
		characters  = value.text
		filtered_text = ''.join(char for char in characters if char not in self.disallowed_chars)
		value.text = filtered_text
		
	# normal
	def to_normal(self):
		def normal(*args):
			self.error.text = 'All fields are required'
			
		Clock.schedule_once(normal, 4)
		
	# show current date on homepage
	def show_date(self):
		now = datetime.now()
		today = now.strftime("%d-%m-%Y")
		return today
		
	def select_date(self, date_field):
		global on_date_field
		on_date_field = date_field
		popup = DatesPopup()
		popup.open()
		
	def cash_or_credit_sale_on_text(self, which_one):	
		if self.status.text == "Status: Creating a list of sale":
			if which_one == 'Cash Sale':
				self.account_category.text = 'Bank'
			elif which_one == 'Credit Sale':
				self.account_category.text = 'Current Assets'
			else:
				self.account_category.text = 'Account Category'
		else:
			self.cash_or_credit.text = 'cash or credit sale'
			self.error.text = 'The panel does not support saving a list'
			self.to_normal()
		
	def update_lists_of_account(self, category):
		if self.status.text == "Status: Creating a list of sale":
			self.account_name.values = view_accounts(financial_data, category)
			self.account_name.text = 'Choose Account'
		else:
			self.error.text = 'The panel does not support saving a list'
			self.to_normal()
			
	def update_lists_of_account_sales_account(self, category):
		if self.status.text == "Status: Creating a list of sale":
			self.sales_account_name.values = view_accounts(financial_data, category)
			self.account_name.text = 'Choose Account'
		else:
			self.error.text = 'The panel does not support saving a list'
			self.to_normal()
			
	def update_the_list_of_ids(self):
		with open(fin_data_file, 'r') as file:
			data = json.load(file)
			
		if 'invoices' in data['other_information']:
			invoices = list(data['other_information']['invoices'].keys())
			self.list_of_invoices.values = invoices
		else:
			self.list_of_invoices.values = []
		
	def view_an_invoice(self, invoice_id):
		if invoice_id == 'list of sale lists':
			pass
		else:
			with open(fin_data_file, 'r') as file:
				data = json.load(file)
				
			invoice_data = data["other_information"]["invoices"][invoice_id]
			
			# Clear existing items from the invoice list
			self.invoice_list.clear_widgets()
			self.invoice_list.height = 10
			
			# Populate invoice list with items from loaded data
			for item in invoice_data["items"]:
				item_layout = BoxLayout(
					orientation='horizontal',
					size=((Window.width), '35dp')
				)
				
				item_details = Label(
					text=item["details"],
					size=((self.invoice_list.width*.5), '30dp'),
					size_hint=(None,None),
					color='black',
					font_size='14sp'
				)
				
				formatted = "{:,.2f}".format(float(item["amount"]))
				item_amount = Label(
					text=formatted,
					size=((self.invoice_list.width*.3), '30dp'),
					size_hint=(None,None),
					color='green',
					font_size='14sp'
				)
				
				remove_button = Button(
					text=' ',
					color='white',
					size=((self.invoice_list.width*.2), '30dp'),
					size_hint=(None,None),
					background_color=(255,0,0,0),
					font_size='14sp'
				)
				
				item_layout.add_widget(item_details)
				item_layout.add_widget(item_amount)
				item_layout.add_widget(remove_button)
				self.invoice_list.add_widget(item_layout)
		
			total_height = sum(child.height for child in self.invoice_list.children)
			self.invoice_list.height = total_height		
			# Update total amount label and others
			formatted = "{:,.2f}".format(invoice_data["total_amount"])
			self.total_amount.text = formatted
			
			self.status.text = 'Status: Viewing or editing a list of sale'
			self.invoice_id.text = invoice_id
			contra_account = invoice_data["account"]
			self.invoice_date.text = invoice_data["date"]
			contra_account = contra_account.split('|')
			self.account_category.text = contra_account[0]
			self.account_name.text = contra_account[1]
			
			self.sales_account_category.text = 'Operating Revenue'
			self.sales_account_name.text = invoice_data["sales_account"]
			self.account_name.disabled = True
			self.sales_account_category.disabled = True
			self.sales_account_name.disabled = True
			
			self.items_list = invoice_data["items"]
			self.the_total_amount = invoice_data["total_amount"]
			
			self.list_of_invoices.text = 'list of sale lists'
			self.cash_or_credit.text = 'cash or credit sale'
			
	def on_delete_confirm_popup(self):
		self.del_popup = Popup(title="Delete Journal")
		content = BoxLayout(orientation='vertical', spacing=30)
		content.add_widget(Button(
			text='Do you want to Delete the Sale list',
			size_hint_y=None,
			height='40dp',
			font_size='16sp',
			background_color=(0,0,255),
			color='white',
			pos_hint={'center_x': 0.5, 'center_y': 0.5}
		))
		yes_button = Button(
			text='Yes',
			size_hint_y=None,
			height='35dp',
			background_color=(255,0,0),
			color='white',
			on_press= self.del_button_pressed
		)
		
		content.add_widget(yes_button)
		
		content.add_widget(Button(
			text='No',
			size_hint_y=None,
			height='35dp',
			on_press=self.del_popup.dismiss)
		)
		content.add_widget(Widget())
		
		#self.del_popup.content = content
		self.del_popup.add_widget(content)
		self.del_popup.open()
	
	def del_button_pressed(self, instance):
		category = self.account_category.text
		account = self.account_name.text
		sales_account = self.sales_account_name.text
		id = self.invoice_id.text
		self.delete_the_invoice(category, account, id, sales_account)
		
	def delete_the_invoice(self, category, account, id, sales_account):
		if self.status.text == 'Status: Viewing or editing a list of sale' and id != '':
			if delete_the_list_of_a_sale(financial_data, category, account, id, sales_account) == True:
				self.update_the_list_of_ids()
				self.error.text = f'list Id: {id} deleted successfully'
				toast('A sale list was deleted')
				self.invoice_list.clear_widgets()
				self.invoice_list.height = 10
				self.list_of_invoices.text = 'list of sale lists'
				self.invoice_id.text = ''
				self.total_amount.text = '0'
				self.the_total_amount = 0
				self.items_list = []
				self.cash_or_credit.text = 'cash or credit sale'
				self.manager.current = 'view_accounts'
				view = self.manager.get_screen('view_accounts')
				if view.first_scroll_view.do_scroll_y == False:
					view.first_scroll_view.scroll_y = 1
					view.first_scroll_view.do_scroll_y = True
				home = self.manager.get_screen('home')
				generate_the_dashboard_items(home.dashboard,home.expenses,home.incomes,home.net_profit,home.bank)
				self.del_popup.dismiss()
				last_upated_date()
			else:
				self.error.text = 'Sale list can only be deleted after restarting app'
				self.to_normal()
				self.del_popup.dismiss()	
		else:
			self.error.text = 'deleting a list locked or no ID of sale list found'
			toast('Only create a sale list')
			self.del_popup.dismiss()
			self.to_normal()	
			
		
	def check_if_saving(self, cash_or_credit, category, account_name, date, sales_account, action):
		if self.status.text == "Status: Creating a list of sale":
			if action == 'save':
				self.save_invoice(cash_or_credit, category, account_name, date, sales_account)
			elif action == 'add_item':
				self.add_item()
		else:
			self.error.text = 'saving a list locked or no items added'
			toast('Only view, edit or delete a list')
			self.to_normal()	
	
	def save_invoice(self, cash_or_credit, category, account_name, date, sales_account):
		if cash_or_credit == 'cash or credit sale' or cash_or_credit == 'None' or self.the_total_amount == 0 or self.the_total_amount < 0:
			self.error.text = 'Select cash or credit sale or add items to list'
			self.to_normal()
		else:
			if cash_or_credit == 'Cash Sale':
				if account_name == 'Choose Account' or sales_account=='Choose Account':
					self.error.text = 'Select the Bank or sales account where the payment is to be made'
					self.to_normal()
				else:
					transaction_id = get_transaction_id(financial_data)
					financial_data["other_information"]["invoices"][transaction_id] = {
						"items": self.items_list,
						"total_amount": self.the_total_amount,
						"date": date,
						"account": f"{category}|{account_name}",
						"sales_account": sales_account
						}
					# debit
					credit_account = f"Operating Revenue|{sales_account}"
					debit_account = f"{category}|{account_name}"
					add_transaction(financial_data, category, account_name, abs(self.the_total_amount), 'cash sale', 'debit', credit_account, date, transaction_id)
					# credit
					add_transaction(financial_data, 'Operating Revenue', sales_account, abs(self.the_total_amount), 'cash sales', 'credit', debit_account, date, transaction_id)
					
					self.invoice_list.clear_widgets()
					self.invoice_list.height = 10
					self.items_list = []
					self.the_total_amount = 0
					
					self.error.text = 'Cash Sale recorded successfully'
					#self.to_normal()
					toast('Cash sale saved')
					self.total_amount.text = '0'
					self.update_the_list_of_ids()
					self.list_of_invoices.text = 'list of sale lists'
					self.cash_or_credit.text = 'cash or credit sale'
					home = self.manager.get_screen('home')
					generate_the_dashboard_items(home.dashboard,home.expenses,home.incomes,home.net_profit,home.bank)
					last_upated_date()
					
			elif cash_or_credit == 'Credit Sale':
				if account_name == 'Choose Account' or sales_account=='Choose Account':
					self.error.text = 'Select the customer or sales account to which the sale is being made'
					self.to_normal()
				else:
					transaction_id = get_transaction_id(financial_data)
					financial_data["other_information"]["invoices"][str(transaction_id)] = {
						"items": self.items_list,
						"total_amount": self.the_total_amount,
						"date": date,
						"account": f"{category}|{account_name}",
						"sales_account": sales_account
						}
					# debit
					credit_account = f"Operating Revenue|{sales_account}"
					debit_account = f"{category}|{account_name}"
					add_transaction(financial_data, category, account_name, abs(self.the_total_amount), 'credit sale', 'debit', credit_account, date, transaction_id)
					# credit
					add_transaction(financial_data, 'Operating Revenue', sales_account, abs(self.the_total_amount), 'credit sales', 'credit', debit_account, date, transaction_id)
					
					self.invoice_list.clear_widgets()
					self.invoice_list.height = 10
					self.items_list = []
					self.the_total_amount = 0
					
					self.error.text = 'Credit Sale recorded successfully'
					#self.to_normal()
					toast('Credit sale saved')
					self.total_amount.text = '0'
					self.update_the_list_of_ids()
					self.list_of_invoices.text = 'list of sale lists'
					self.cash_or_credit.text = 'cash or credit sale'
					home = self.manager.get_screen('home')
					generate_the_dashboard_items(home.dashboard,home.expenses,home.incomes,home.net_profit,home.bank)
					last_upated_date()
		
	def remove_item(self, instance):
		parent_layout = instance.parent
		# Inside the parent layout, the first child is the Label displaying the item details
		amount_label = parent_layout.children[1]
		details_label = parent_layout.children[2]
		# Extract details from the label text
		
		details = details_label.text 
		amount = amount_label.text
			
		# Remove item from the invoice dictionary and list
		self.items_list = [item for item in self.items_list if item["details"] != details]
		self.invoice_list.remove_widget(parent_layout)
		total_height = sum(child.height for child in self.invoice_list.children)
		self.invoice_list.height = total_height
		amount = amount.replace(',', '')
		self.the_total_amount -= float(amount)
		formatted = "{:,.2f}".format(self.the_total_amount)
		self.total_amount.text = formatted
		
	def add_item(self):
		details = self.particuars.text
		amount = self.amount.text

		if details and amount:
			item_details = Label(
				text=details,
				size=((self.invoice_list.width*.5), '30dp'),
				size_hint=(None,None),
				color='black',
				font_size='14sp'
			)
			
			formatted = "{:,.2f}".format(float(amount))
			item_amount = Label(
				text=formatted,
				size=((self.invoice_list.width*.3), '30dp'),
				size_hint=(None,None),
				color='green',
				font_size='14sp'
			)
			
			remove_button = Button(
				text='Remove',
				on_press=self.remove_item,
				color='white',
				size=((self.invoice_list.width*.2), '30dp'),
				size_hint=(None,None),
				background_color=(255,0,0),
				font_size='14sp'
			)
			
			item_layout = BoxLayout(
				orientation='horizontal',
				size=((self.invoice_list.width), '35dp')
			)
			item_layout.add_widget(item_details)
			item_layout.add_widget(item_amount)
			item_layout.add_widget(remove_button)
			
			self.invoice_list.add_widget(item_layout)
			total_height = sum(child.height for child in self.invoice_list.children)
			self.invoice_list.height = total_height
			# Add item to the invoice list
			
			item = {
				"details": details,
				"amount": amount
			}
			
			
			self.items_list.append(item)
			
			
			self.the_total_amount += float(amount)
			formatted = "{:,.2f}".format(self.the_total_amount)
			self.total_amount.text = formatted
			# Clear inputs
			self.particuars.text = ''
			self.amount.text = ''
			      
		else:
			self.error.text = 'Item details and amount should not be blank'
			self.to_normal()


'''
make journal entries into books of accounts
'''

class SavedPopup(Popup):
	def calculate_height(self):
		# Calculate total height of widgets
		return sum(widget.height for widget in self.content.children)



class MakeJournalEntries(Screen):
	def __init__(self, **kwargs):
		super(MakeJournalEntries, self).__init__(**kwargs)
		self.disallowed_chars = ['"', '|', '$', "'"]
		Window.softinput_mode = 'below_target'
		
	def on_enter(self, *args):
		if 'dark_mode' in financial_data['other_information']:
			mode = financial_data['other_information']['dark_mode']
			if mode == True:
				app = App.get_running_app()
				for child in self.ids.scroll_view.children:
					if isinstance(child, BoxLayout):
						app.traverse_widgets(child)
			else:
				pass
		else:
			pass
		
	def get_help(self):
		global ask_for_help
		ask_for_help = str(SimploStatsHelp().get_help('Journal_entries'))
		popup = HelpPopup()
		popup.title = 'Journal Entries'
		popup.open()
		
	def on_delete_confirm_popup(self, date, debit_account, credit_account, amount, memo, transaction_id, category, account_name, action, *args):
		if action == 'delete':
			text = 'Do you want to Delete the record'
			text2 = 'Delete Record'
		else:
			text = 'Do you want to Edit the record'
			text2 = 'Edit Record'
		self.del_popup = Popup(title="Delete Journal")
		content = BoxLayout(orientation='vertical', spacing=30)
		content.add_widget(Button(
			text=text,
			size_hint_y=None,
			height='40dp',
			font_size='16sp',
			background_color=(0,0,255),
			color='white',
			pos_hint={'center_x': 0.5, 'center_y': 0.5}
		))
		yes_button = Button(
			text=text2,
			background_color=(255,0,0),
			color='white',
			size_hint_y=None,
			height='35dp',
			on_press= self.del_button_pressed
		)
		
		content.add_widget(yes_button)
		
		content.add_widget(Button(
			text='No',
			size_hint_y=None,
			height='35dp',
			on_press=self.del_popup.dismiss)
		)
		content.add_widget(Widget())
		
		#self.del_popup.content = content
		self.del_popup.add_widget(content)
		self.del_popup.open()
	
	def del_button_pressed(self, instance):
		date = self.transaction_date.text
		debit_account = self.debit_account.text
		credit_account = self.credit_account.text
		amount = self.transaction_amount.text
		memo = self.memo.text
		transaction_id = self.trans_id.text
		category = self.account_category.text
		account_name = self.account_name.text
		
		if 'delete' in instance.text.lower():
			action = 'delete'
		else:
			action = 'edit'
		
		self.check_if_bal_bd(date, debit_account, credit_account, amount, memo, transaction_id, category, account_name, action)
		
	def on_text_account(self, value):
		# Function to filter or prevent certain characters
		characters  = value.text
		filtered_text = ''.join(char for char in characters if char not in self.disallowed_chars)
		value.text = filtered_text
		
	def go_back(self):
		if from_journal_to_home == True:
			self.manager.current = 'home'
		else:
			self.manager.current = 'view_accounts'
		
	# normal
	def to_normal(self):
		def normal(*args):
			self.error.text = 'All fields are required'
			
		Clock.schedule_once(normal, 3)
		
	def check_if_id_was_entered(self, user_id, search_category):
		if user_id:
			self.view_the_transaction_id(user_id, search_category)
		else:
			self.error.text = 'Please enter a valid ID'
			self.to_normal()
		
	# show ids trans
	def view_the_transaction_id(self, user_id, search_category):
		global the_double_entry
		global selected_account_to_view
		global the_view_account_side
		global the_global_amount_dep
		
		if search_category == 'Entire Books':
			search_from_data = ['Non Current Assets', 'Current Assets', 'Operating Expenses', 'Other Expenses', 'Bank', 'Taxes', 'Cost of Sales', 'Capital', 'Non Current Liabilities', 'Current Liabilities', 'Other Incomes', 'Operating Revenue']
			on_search = 'Books'
		else:
			search_from_data = [search_category]
			on_search = search_category
		
		for category in search_from_data:
			if category == 'other_information':
				pass
			else:
				accounts = financial_data[category]
				for account, details in accounts.items():
					transactions = details.get("transactions", [])
					for transaction in transactions:
						if transaction["id"] == int(user_id):
							self.status.text = 'Status: View, Edit and Delete transaction'
							self.transaction_date.text = transaction['date']
							self.trans_id.text = user_id
							self.memo.text = transaction['memo']
							self.transaction_amount.text = str(transaction['amount'])
							the_global_amount_dep = transaction['amount']
				
							if transaction['side'] == 'debit':
								self.debit_account.text = f"{category}|{account}"
								self.credit_account.text = transaction['double_entry']
								self.check_debit.active = True
								self.side.text = 'debit'
								the_view_account_side = 'debit'
								target_accum_dep_debit = f"{category}|{account}"
								target_accum_dep_credit = transaction['double_entry']
								self.debit_account.color = 'purple'
								self.debit_account.font_size = '20sp'
								self.credit_account.color = 'green'
								self.credit_account.font_size = '18sp'
								toast("Viewing debit record")
							else:
								self.credit_account.text = f"{category}|{account}"
								self.debit_account.text = transaction['double_entry']
								self.check_credit.active = True
								self.side.text = 'credit'
								the_view_account_side = 'credit'
								target_accum_dep_debit = transaction['double_entry']
								target_accum_dep_credit = f"{category}|{account}"
								self.debit_account.color = 'green'
								self.debit_account.font_size = '18sp'
								self.credit_account.color = 'purple'
								self.credit_account.font_size = '20sp'
								toast("Viewing credit record")
								
							selected_account_to_view = f"{category}|{account}"
							the_double_entry = transaction['double_entry']
							self.account_category.text = category
							self.account_name.text = account
								
							check_dep = the_double_entry.split('|')
							is_dep = check_dep[1]
							
							# check if depreciation and lock accounts
							if account == 'Depreciation' or is_dep == 'Depreciation':
								self.account_category.disabled = True
								self.account_name.disabled = True
							else:
								self.account_category.disabled = False
								self.account_name.disabled = False
								
							check_for_asset = target_accum_dep_credit.split('|')
							
							# if is accumulated depreciation
							if target_accum_dep_debit == f'Capital|Opening Balance Equity' and check_for_asset[0] == 'Non Current Assets':
								self.account_category.disabled = True
								self.account_name.disabled = True
								self.is_accum_deprec.text = 'accum depreciation'
								self.is_accum_deprec.disabled = True
							else:
								self.is_accum_deprec.text = 'journal entry'
								self.is_accum_deprec.disabled = True
					
							return
							
		self.error.text = f'ID: {user_id} not found in the {on_search}'
		self.to_normal()
		
	# show current date on homepage
	def show_date(self):
		now = datetime.now()
		today = now.strftime("%d-%m-%Y")
		return today
		
	def select_date(self, date_field):
		global on_date_field
		on_date_field = date_field
		popup = DatesPopup()
		popup.open()
		
	def upate_to_accum_depreciation(self, is_accum_deprec):
		debit_record = self.debit_account.text.split('|')
		credit_record = self.credit_account.text.split('|')
		if self.debit_account.text == 'Account' or self.credit_account.text == 'Account':
			self.error.text = 'First select journal accounts'
			is_accum_deprec.text = 'journal entry'
			self.to_normal()
		else:
			if debit_record[1] != '' and credit_record[1] != '':
				if debit_record[0] == 'Capital' and debit_record[1] == 'Opening Balance Equity' and credit_record[0] == 'Non Current Assets':
					is_accum_deprec.text = 'accum depreciation'
					toast('Accum depreciation detected')
				else:
					self.error.text = 'Transaction cannot be accumulated depreciation'
					is_accum_deprec.text = 'journal entry'
					self.to_normal()
			else:
				self.error.text = 'First select journal accounts'
				is_accum_deprec.text = 'journal entry'
				self.to_normal()
				
	def auto_detect_accum_depreciation(self, is_accum_deprec):
		debit_record = self.debit_account.text.split('|')
		credit_record = self.credit_account.text.split('|')
		if self.debit_account.text == 'Account' or self.credit_account.text == 'Account':
			return False
		else:
			if debit_record[1] != '' and credit_record[1] != '':
				if debit_record[0] == 'Capital' and debit_record[1] == 'Opening Balance Equity' and credit_record[0] == 'Non Current Assets':
					#is_accum_deprec.text = 'accum depreciation'
					return True
				else:
					return False
			else:
				return False
			
		
	def account_to_record(self, category, account_side):
		if account_side == 'None':
			self.error.text = 'First select the account side to record'
			self.account_category.text = 'Account Category'
			self.to_normal()
		else:
			self.account_name.text = 'Choose Account'
			self.account_name.values = view_accounts(financial_data, category)
			if account_side == 'debit':
				self.debit_account.text = f"{category}|"
			else:
				self.credit_account.text = f"{category}|"
			#toast(f"{category} seleted")
			
	def update_sub_account_to_add(self, account_side, account_name, category):
		if account_side == 'debit':
			self.debit_account.text = f"{category}|{account_name}"
			#toast(f"{account_name} seleted")
		else:
			self.credit_account.text = f"{category}|{account_name}"
			#toast(f"{account_name} seleted")
		self.is_accum_deprec.text = 'journal entry'
			
	def get_the_accum_dep(self, category, account):
		account = f'{category}|{account}'
		if account in financial_data['other_information']['accum_depreciation']:
			return financial_data['other_information']['accum_depreciation'][account]
		else:
			return 0
			
	def save_the_accumulated_depreciation(self, category, account, dep_amount):
		accum_dep = self.get_the_accum_dep(category, account)
		if accum_dep == 0:
			previous_saved_dep = 0
		else:
			previous_saved_dep = accum_dep
			
		new_dep = previous_saved_dep + dep_amount
		if new_dep < 0:
			depreciation = 0
		else:
			depreciation = round(new_dep,2)
		financial_data['other_information']['accum_depreciation'][f'{category}|{account}'] = depreciation
		save_data(financial_data)
		
	def check_if_depreciation_credited(self, date, debit_account, credit_account, transaction_amount, memo):
		if self.status.text == 'Status: Recording a Transaction':
			if debit_account == 'Account' or credit_account == 'Account':
				self.error.text = 'Please first select the accounts to record'
				self.to_normal()
				toast("Accounts not selected.")
			else:
				if transaction_amount == '':
					self.error.text = 'Please enter the transaction amount'
					self.to_normal()
					toast("Amount required")
				else:
					if len(memo) < 3:
						self.error.text = 'Please enter a memo'
						self.to_normal()
						toast("Memo required")
					else:
						# data, category, account, amount, memo, side, double_entry, date
						debit_record = debit_account.split('|')
						credit_record = credit_account.split('|')
						
						if debit_record[1] != '' and credit_record[1] != '':
							if credit_account == 'Other Expenses|Depreciation' or credit_account == 'Operating Expenses|Depreciation':
								self.error.text = 'App does not allow crediting Depreciation'
								self.to_normal()
								toast("Depreciation cannot be credited")
							else:
								if self.auto_detect_accum_depreciation(self.is_accum_deprec) == True and self.is_accum_deprec.text == 'journal entry':
									self.error.text = 'Accumulated Depreciation Detected.  Toogle to "accum depreciation"'
									#self.to_normal()
									toast("toogle to 'accum depreciation'")
								else:
									if debit_account == credit_account:
										self.error.text = 'Same Accounts cannot be recorded, observe double entry'
										self.to_normal()
										toast("Avoid counter recording to same account")
									else:
										if float(transaction_amount) < 0 or float(transaction_amount) == 0:
											self.error.text = 'An amount cannot be zero or negative'
											self.to_normal()
											toast("Amount can only be positive")
										else: 	
											self.on_press_save_entry_button(date, debit_account, credit_account, transaction_amount, memo)
						else:
							self.error.text = 'Please check if all accounts are correctly entered'
							self.to_normal()
							toast("Check your Accounts")
							
							
		else:
			self.error.text = 'The panel does not allow to save a record'
			self.to_normal()
			toast("Saving records disabled, view instead")			
			
	def on_press_save_entry_button(self, date, debit_account, credit_account, transaction_amount, memo):
		if self.status.text == 'Status: Recording a Transaction':
			if debit_account == 'Account' or credit_account == 'Account':
				self.error.text = 'Please first select the accounts to record'
				self.to_normal()
			else:
				if transaction_amount == '':
					self.error.text = 'Please enter the transaction amount'
					self.to_normal()
				else:
					if len(memo) < 3:
						self.error.text = 'Please enter a memo'
						self.to_normal()
					else:
						# data, category, account, amount, memo, side, double_entry, date
						debit_record = debit_account.split('|')
						credit_record = credit_account.split('|')
						
						if debit_record[1] != '' and credit_record[1] != '':
							# debit
							saved_it = SavedPopup()
							saved_it.open()
							
							def close_event(*args):
								saved_it.dismiss()
								
							Clock.schedule_once(close_event, 3)
								
							transaction_amount = round(float(transaction_amount), 2)
							transaction_id = get_transaction_id(financial_data)
							add_transaction(financial_data, debit_record[0], debit_record[1], abs(transaction_amount), memo, 'debit', credit_account, date, transaction_id)
							# credit
							add_transaction(financial_data, credit_record[0], credit_record[1], abs(transaction_amount), memo, 'credit', debit_account, date, transaction_id)
							
							# update accumulated depreciation
							if self.is_accum_deprec.text == 'journal entry':
								at_cost_accounts = view_accounts(financial_data, 'Non Current Assets')
								if debit_record[1] == 'Depreciation' or credit_record[1] == 'Depreciation':
									if debit_record[1] in at_cost_accounts:
										self.save_the_accumulated_depreciation(debit_record[0], debit_record[1], -transaction_amount)
										toast("Accum depreciation updated")
									elif credit_record[1] in at_cost_accounts:
										self.save_the_accumulated_depreciation(credit_record[0], credit_record[1], transaction_amount)
										toast("Accum depreciation updated")
									else:
										pass
								else:
									pass
							else:
								self.save_the_accumulated_depreciation(credit_record[0], credit_record[1], transaction_amount)
								toast("Accum depreciation saved")
							
							self.error.text = 'Transaction recorded successfully'
							toast("Transaction saved")
							self.to_normal()
							
							self.transaction_amount.text = ''
							self.memo.text = ''
							home = self.manager.get_screen('home')
							generate_the_dashboard_items(home.dashboard,home.expenses,home.incomes,home.net_profit,home.bank)
							last_upated_date()
						else:
							self.error.text = 'Please check if all accounts are correctly entered'
							self.to_normal()
							
		else:
			self.error.text = 'The panel does not allow to save a record'
			self.to_normal()
			
	def return_list_of_sale_lists(self, id):
		with open(fin_data_file, 'r') as file:
			data = json.load(file)
		if id in data['other_information']['invoices']:
			return True
		else:
			return False
			
	def check_if_bal_bd(self, date, debit_account, credit_account, amount, memo, transaction_id, category, account_name, action):
		global from_home_screen_to_listing
		if self.status.text == 'Status: Recording a Transaction':
			self.error.text = 'The panel does not allow to edit a record'
			self.to_normal()
			toast("Only save records")
			if action == 'delete' or action == 'edit':
				self.del_popup.dismiss()
		else:
			if int(transaction_id) == -1 or int(transaction_id) == -2:
				self.error.text = 'Unable to edit or delete opening balances'
				self.to_normal()
				toast("Opening balances locked")
				if action == 'edit' or action == 'delete':
					self.del_popup.dismiss()
			else:
				if amount == '':
					toast("Amount Required")
					if action == 'edit' or action == 'delete':
						self.del_popup.dismiss()
				else:
					if float(amount) <= 0:
						toast("Only positive amount required")
						if action == 'edit' or action == 'delete':
							self.del_popup.dismiss()
					else:
						if self.return_list_of_sale_lists(transaction_id) == True:
							screen = self.manager.get_screen('invoicing')
							screen.list_of_invoices.text = str(transaction_id)
							screen.list_of_invoices.values = []
							self.manager.current = 'invoicing'
							from_home_screen_to_listing = False
							
							if action == 'edit' or action == 'delete':
								self.del_popup.dismiss()
						else:
							if action == 'edit':
								self.on_press_edit_transaction_button(date, debit_account, credit_account, amount, memo, transaction_id, category, account_name)
								self.del_popup.dismiss()
							else:
								self.on_press_delete_transaction_popup(category, account_name, transaction_id)
								self.del_popup.dismiss()
	
	def on_press_edit_transaction_button(self, date, debit_account, credit_account, amount, memo, transaction_id, category, account_name):
		if self.status.text == 'Status: Recording a Transaction':
			self.error.text = 'The panel does not allow to edit a record'
			self.to_normal()
		else:
			if debit_account == 'Account' or credit_account == 'Account':
				self.error.text = 'Please first select the accounts to edit'
				self.to_normal()
			else:
				if amount == '':
					self.error.text = 'Please enter the edited transaction amount'
					self.to_normal()
				else:
					if len(memo) < 3:
						self.error.text = 'Please enter edited memo'
						self.to_normal()
					else:
						if the_view_account_side == 'debit':
							counter_account = credit_account
							double_side = 'credit'
						elif the_view_account_side == 'credit':
							counter_account = debit_account
							double_side = 'debit'
							
						if selected_account_to_view == f"{category}|{account_name}" and the_double_entry == counter_account:
							edit_double_entry = the_double_entry.split('|')
							
							# update accumulated depreciation
							if self.is_accum_deprec.text == 'journal entry':
								at_cost_accounts = view_accounts(financial_data, 'Non Current Assets')
								if account_name == 'Depreciation' or edit_double_entry[1] == 'Depreciation':
									dep_amount = round(float(amount), 2) - the_global_amount_dep
									if account_name in at_cost_accounts:
										self.save_the_accumulated_depreciation(category, account_name, dep_amount)
									elif edit_double_entry[1] in at_cost_accounts:
										self.save_the_accumulated_depreciation(edit_double_entry[0], edit_double_entry[1], dep_amount)
									else:
										pass
								else:
									pass
							else:
								credit_record = self.credit_account.text.split('|')
								dep_amount = round(float(amount), 2) - the_global_amount_dep
								self.save_the_accumulated_depreciation(credit_record[0], credit_record[1], dep_amount)
								
							
							edited_transaction = {"date": date, "amount": abs(round(float(amount), 2)), "memo": memo, "side": the_view_account_side, "double_entry": the_double_entry}
							# account side edit
							edit_transaction_by_id(financial_data, category, account_name, int(transaction_id), edited_transaction)
							# account double entry edit
							edited_transaction = {"date": date, "amount": abs(round(float(amount), 2)), "memo": memo, "side": double_side, "double_entry": f"{category}|{account_name}"}
							
							edit_transaction_by_id(financial_data, edit_double_entry[0], edit_double_entry[1], int(transaction_id), edited_transaction)
							home = self.manager.get_screen('home')
							generate_the_dashboard_items(home.dashboard,home.expenses,home.incomes,home.net_profit,home.bank)
							last_upated_date()
							view = self.manager.get_screen('view_accounts')
							if view.first_scroll_view.do_scroll_y == False:
								view.first_scroll_view.scroll_y = 1
								view.first_scroll_view.do_scroll_y = True
								
							home = self.manager.get_screen('home')
							generate_the_dashboard_items(home.dashboard,home.expenses,home.incomes,home.net_profit,home.bank)
							self.manager.current = 'view_accounts'
							toast("Record edited")
						else:
							debit_record = debit_account.split('|')
							credit_record = credit_account.split('|')
							
							if debit_record[1] != '' and credit_record[1] != '':
								# delete viewed entry
								del_viewed = selected_account_to_view.split('|')
								delete_transaction_by_id(financial_data, del_viewed[0], del_viewed[1], int(transaction_id))
								# delete double entry
								edit_double_entry = the_double_entry.split('|')
								delete_transaction_by_id(financial_data, edit_double_entry[0], edit_double_entry[1], int(transaction_id))
								
								# save into new accounts
								# debit
								transaction_amount = round(float(amount), 2)
								transaction_id = get_transaction_id(financial_data)
								add_transaction(financial_data, debit_record[0], debit_record[1], abs(transaction_amount), memo, 'debit', credit_account, date, transaction_id)
								# credit
								add_transaction(financial_data, credit_record[0], credit_record[1], abs(transaction_amount), memo, 'credit', debit_account, date, transaction_id)
								home = self.manager.get_screen('home')
								generate_the_dashboard_items(home.dashboard,home.expenses,home.incomes,home.net_profit,home.bank)
								
								view = self.manager.get_screen('view_accounts')
								if view.first_scroll_view.do_scroll_y == False:
									view.first_scroll_view.scroll_y = 1
									view.first_scroll_view.do_scroll_y = True
								home = self.manager.get_screen('home')
								generate_the_dashboard_items(home.dashboard,home.expenses,home.incomes,home.net_profit,home.bank)
								last_upated_date()
								toast("Record edited")
								self.manager.current = 'view_accounts'
							else:
								self.error.text = 'Please check if all edit accounts are correctly entered'
								self.to_normal()
			
	def on_press_delete_transaction_popup(self, category, account_name, transaction_id):
		if self.status.text == 'Status: Recording a Transaction':
			self.error.text = 'The panel does not allow to delete a record'
			self.to_normal()
		else:
			delete_double = the_double_entry.split('|')
			sel_account = selected_account_to_view.split('|')
			
			if account_name in financial_data[category]:
				transactions = financial_data[category][account_name]["transactions"]
				specific_transaction = get_transaction_by_id(financial_data, category, account_name, int(transaction_id))
				
				if specific_transaction:
					viewed = self.manager.get_screen('view_accounts')
					delete_transaction_by_id(financial_data, category, account_name, int(transaction_id))
					delete_transaction_by_id(financial_data, delete_double[0], delete_double[1], int(transaction_id))
					home = self.manager.get_screen('home')
					generate_the_dashboard_items(home.dashboard,home.expenses,home.incomes,home.net_profit,home.bank)
					
					# update accumulated depreciation
					if self.is_accum_deprec.text == 'journal entry':
						at_cost_accounts = view_accounts(financial_data, 'Non Current Assets')
						if sel_account[1] == 'Depreciation' or delete_double[1] == 'Depreciation':
							dep_amount = -the_global_amount_dep
							if sel_account[1] in at_cost_accounts:
								self.save_the_accumulated_depreciation(sel_account[0], sel_account[1], dep_amount)
							elif delete_double[1] in at_cost_accounts:
								self.save_the_accumulated_depreciation(delete_double[0], delete_double[1], dep_amount)
							else:
								pass
						else:
							pass
					else:
						credit_record = self.credit_account.text.split('|')
						self.save_the_accumulated_depreciation(credit_record[0], credit_record[1], -the_global_amount_dep)
						
					
					if viewed.first_scroll_view.do_scroll_y == False:
						viewed.first_scroll_view.scroll_y = 1
						viewed.first_scroll_view.do_scroll_y = True
						
					home = self.manager.get_screen('home')
					generate_the_dashboard_items(home.dashboard,home.expenses,home.incomes,home.net_profit,home.bank)
					toast("Record deleted")
					last_upated_date()
					self.manager.current = 'view_accounts'
					viewed.refresh_button.active = True
				else:
					self.error.text = f"Transaction id {transaction_id} not found in account {account_name}"
					self.to_normal()
			else:
				self.error.text = f"Unable to delete the transaction id {transaction_id}."
				self.to_normal()
			
		
'''
add ledger accounts to app
'''


class ChartsOfAccounts(Screen):
	def __init__(self, **kwargs):
		super(ChartsOfAccounts, self).__init__(**kwargs)
		self.disallowed_chars = ['"', '|', '$', '%']
		Window.softinput_mode = 'below_target'
		
	def go_back(self):
		self.manager.current = 'home'
		
	def get_help(self):
		global ask_for_help
		ask_for_help = str(SimploStatsHelp().get_help('charts_of_accounts'))
		popup = HelpPopup()
		popup.title = 'Chart of Accounts'
		popup.open()
		
	def about_categories(self):
		global ask_for_help
		ask_for_help = str(SimploStatsHelp().get_help('categories'))
		popup = HelpPopup()
		popup.title = 'Chart Categories of Accounts'
		popup.open()

	def on_text_account(self, value):
		# Function to filter or prevent certain characters
		characters  = value.text
		filtered_text = ''.join(char for char in characters if char not in self.disallowed_chars)
		value.text = filtered_text
		
	# normal
	def to_normal(self):
		def normal(*args):
			self.error.text = 'All fields are required'
			
		Clock.schedule_once(normal, 3)
		
	def on_press_account_button(self, category, account):
		global from_view_records_to_home
		start_date = str(financial_data['other_information']['start_date'])
		end_date = str(financial_data['other_information']['end_date'])
		
		if category == 'Account Category' or  account == 'Account':
			self.error.text = 'First select an account to view'
			self.to_normal()
		else:
			# bored to chance income statement names
			view_records = self.manager.get_screen('view_accounts')
			view_records.start_date.text = start_date
			view_records.end_date.text = end_date
			view_records.account_category.text = category
			view_records.account_name.text = account
			
			if view_records.first_scroll_view.do_scroll_y == False:
				view_records.first_scroll_view.scroll_y = 1
				view_records.first_scroll_view.do_scroll_y = True
			self.manager.current = 'view_accounts'
			from_view_records_to_home = True
		
	# add account
	def add_accounts_to_major_categories_button(self, account):
		disabled_accounts = {'opening balance equity', 'depreciation', 'retained earnings'}
		acc = self.account_name.text.lower()
		if self.account_category.text == 'Account Category':
			self.error.text = 'First select a category to add an account'
			self.to_normal()
		else:
			if len(self.account_to_add.text) < 3:
				self.error.text = 'Please create a longer name for the account'
				self.to_normal()
			elif acc == 'opening balance equity' or acc== 'depreciation' or acc== 'retained earnings':
				self.error.text = 'An account cannot be named as default account'
				self.to_normal()
			else:
				self.error.text = add_account(financial_data, self.account_category.text, self.account_to_add.text)
				self.account_to_add.text = ''
				self.to_normal()
				toast("New account added")
				self.load_current_saved_accounts(self.account_category.text)
				last_upated_date()
		
	# view list of accounts	
	def load_current_saved_accounts(self, category):
		self.list_of_accounts_layout.clear_widgets()
		accounts = view_accounts(financial_data, category)
		app = App.get_running_app()
		color = app.return_theme_color()
		self.list_of_accounts_layout.add_widget(
		Button(text=' ',
			size_hint=(1,None),
			height='5dp',
			background_color=app.theme_cls.primary_color,
			background_normal=''
		))
		
		list_items = 0
		
		start_date = financial_data['other_information']['start_date']
		end_date = financial_data['other_information']['end_date']
		
		category_total = get_category_total([category], start_date, end_date)
		debit_categories = {'Non Current Assets', 'Current Assets', 'Operating Expenses', 'Other Expenses', 'Bank', 'Taxes', 'Cost of Sales'}
		
		if category in debit_categories:
			formatted = "{:,.2f}".format(category_total)
		else:
			formatted = "{:,.2f}".format(-category_total)
		
		for acc in accounts:
			button = MDFlatButton(
				text=str(acc),
				size_hint=(1,None),
				on_press=self.on_button_press,
				halign='center',
				theme_text_color="Custom",
				text_color=color,
				font_size="16sp")
			self.list_of_accounts_layout.add_widget(button)
			list_items += 1
			
		self.account_name.text = 'Account'
		self.ids.about_list_of_account.text = f"{category} > {list_items} account(s) > {formatted}"
	
	# account pressed		
	def on_button_press(self, instance):
		self.account_name.text = instance.text
		
		start_date = financial_data['other_information']['start_date']
		end_date = financial_data['other_information']['end_date']
		
		account_total = income_statement_deractives(financial_data, str(self.account_category.text), str(instance.text), start_date, end_date)
		
		debit_categories = {'Non Current Assets', 'Current Assets', 'Operating Expenses', 'Other Expenses', 'Bank', 'Taxes', 'Cost of Sales'}
		
		if str(self.account_category.text) in debit_categories:
			formatted = "{:,.2f}".format(account_total)
		else:
			formatted = "{:,.2f}".format(-account_total)
		
		self.ids.top_selection_display.text = f"{instance.text} > {formatted}"
	
	# delete accounts	
	def confirm_deletion(self):
		global account_to_delete
		global category_of_account
		global show_complete
		global list_of_accounts
		global on_click_account_updated
		
		if self.account_name.text == 'Account':
			self.error.text = 'First press on account to delete'
			self.to_normal()
		elif self.account_name.text =='Opening Balance Equity':
			self.error.text = 'A default account cannot be deleted'
			self.to_normal()
		elif self.account_name.text == 'Depreciation':
			self.error.text = 'A default account cannot be deleted'
			self.to_normal()
		elif self.account_name.text == 'Retained Earnings':
			self.error.text = 'A default account cannot be deleted'
			self.to_normal()
		else:
			account_to_delete = self.account_name.text
			category_of_account = self.account_category.text
			show_complete = self.error
			list_of_accounts = self.list_of_accounts_layout
			on_click_account_updated = self.account_name
			popup = DeleteAccount()
			popup.open()
			toast("Confirm deletion of account")
			
	def cost_of_assets(self):
		if self.account_category.text == 'Non Current Assets':
			popup = CostOfAssets()
			popup.open()
		else:
			self.error.text = 'Select only Non Current Assets'
			self.to_normal()	
			
	# shift account	
	def shift_account(self):
		global account_to_delete
		global category_of_account
		global show_complete
		global list_of_accounts
		global on_click_account_updated
		
		if self.account_name.text == 'Account':
			self.error.text = 'First press on account to shift'
			self.to_normal()
		elif self.account_name.text =='Opening Balance Equity':
			self.error.text = 'A default account cannot be shifted'
			self.to_normal()
		elif self.account_name.text == 'Depreciation':
			self.error.text = 'A default account cannot be shifted'
			self.to_normal()
		elif self.account_name.text == 'Retained Earnings':
			self.error.text = 'A default account cannot be shifted'
			self.to_normal()
		else:
			if self.account_category.text == 'Non Current Assets':
				self.error.text = 'Non Current Assets cannot be shifted'
				self.to_normal()
			else:
				account_to_delete = self.account_name.text
				category_of_account = self.account_category.text
				show_complete = self.error
				list_of_accounts = self.list_of_accounts_layout
				on_click_account_updated = self.account_name
				popup = ChangeAccountCategory()
				popup.open()
			
			
			
'''
thread view 
'''


class MyThread():
	def __init__(self, screen):
		super(MyThread, self).__init__()
		self.screen = screen

	def run(self):
		# Simulate time-consuming task (replace with your actual button creation logic)
		popup = Popup(title='Loading...',size_hint=(0.25, 0.08), auto_dismiss=False)
		popup.open()
        
		time.sleep(2)
		popup.dismiss()
		
		
class LoadingPopup(Popup):
	def calculate_height(self):
		# Calculate total height of widgets
		return sum(widget.height for widget in self.content.children)


class ZoomableScrollView(ScrollView):
    pass
     

'''
view transactions in an account
'''

class DateLabel(Label):
	def __init__(self, text, font_size, height, **kwargs):
		super(DateLabel, self).__init__(**kwargs)
		self.text = text
		self.font_size = font_size
		self.height = height
		self.size_hint=(1,None)
		self.color='black'
		self.halign='left'		
		

class MemoLabel(Label):
	def __init__(self, text, font_size, height, **kwargs):
		super(MemoLabel, self).__init__(**kwargs)
		self.text = text
		self.font_size = font_size
		self.height = height
		self.size_hint=(1,None)
		self.color='black'
		self.halign='left'
		
		
class AmountLabel(Label):
	def __init__(self, text, font_size, height, color, **kwargs):
		super(AmountLabel, self).__init__(**kwargs)
		self.text = text
		self.font_size = font_size
		self.height = height
		self.size_hint=(1,None)
		self.color=color
		self.halign='left'
		
		
class BalancesLabel(Label):
	def __init__(self, text, font_size, height, color, **kwargs):
		super(BalancesLabel, self).__init__(**kwargs)
		self.text = text
		self.font_size = font_size
		self.height = height
		self.size_hint=(1,None)
		self.color=color
		self.halign='left'
		

class IdsButton(Button):
	def __init__(self, text, font_size, height, background_color, on_press, **kwargs):
		super(IdsButton, self).__init__(**kwargs)
		self.text = text
		self.font_size = font_size
		self.height = height
		self.size_hint=(1,None)
		self.color='black'
		self.halign='center'
		self.background_color=background_color
		self.bind(on_press=on_press)


class ViewAccounts(Screen):
	def __init__(self, **kwargs):
		super(ViewAccounts, self).__init__(**kwargs)
		self.popup = Popup(title='Loading...',size_hint=(0.25, 0.08), auto_dismiss=False)
		Window.softinput_mode = 'below_target'
		
	def on_enter(self, *args):
		if 'dark_mode' in financial_data['other_information']:
			mode = financial_data['other_information']['dark_mode']
			if mode == True:
				app = App.get_running_app()
				for child in self.ids.first_scroll_view.children:
					if isinstance(child, BoxLayout):
						app.traverse_widgets(child)
			else:
				pass
		else:
			pass
		
	def toggle_panel(self):
		animation = Animation(width=120 if self.action_label.width == 0 else 0, duration=0.3)
		animation.start(self.action_label)
		
	def get_help(self):
		global ask_for_help
		ask_for_help = str(SimploStatsHelp().get_help('view_accounts'))
		popup = HelpPopup()
		popup.title = 'View Accounts/ Ledgers'
		popup.open()
		
	def scroll_to_top(self, first_scroll_view, second_scroll_view):
		try:
			if second_scroll_view.scroll_y == 1:
				first_scroll_view.scroll_y = 1
				first_scroll_view.do_scroll_y = True
			else:
				second_scroll_view.scroll_y = 1
		except:
			pass
	
	def scroll_to_bottom(self, first_scroll_view, second_scroll_view):
		try:
			if first_scroll_view.do_scroll_y == True:
				first_scroll_view.scroll_y = 0
				#second_scroll_view.scroll_y = 0
				first_scroll_view.do_scroll_y = False
			else:
				second_scroll_view.scroll_y = 0
		except:
			pass
		
	def export_selected_account_to_csv(self, category, account, start_date, end_date):
		if category == 'Account Category' or account == 'Choose Account':
			self.error.text = 'First select an account to export records'
			self.to_normal()
			toast("Account to export required")
		else:
			year_end = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
			if len(start_date) == 10 and len(end_date) == 10 and start_date[0] in year_end and start_date[-1] in year_end and end_date[0] in year_end and end_date[-1] in year_end:
				if account in financial_data[category]:
					transactions = get_filtered_transactions(financial_data, category, account, start_date, end_date)
					bal_bd = balance_bd_sub_totals(financial_data, category, account,str(financial_data['other_information']['start_date']), start_date)
					self.error.text = export_ledger_accounts(category, account, transactions, start_date, end_date, bal_bd)
				else:
					self.error.text = f"Account '{account}' not found in '{category}'."
					self.to_normal()
					
			else:
				self.error.text = 'Error in dates selection, please check again'
				self.to_normal()
				toast("Dates required")		
		
	def export_displayed_as_pdf(self, category, account, start_date, end_date):
		if category == 'Account Category' or account == 'Choose Account':
			self.error.text = 'First select an account to screenshot records'
			self.to_normal()
		else:
			year_end = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
			if len(start_date) == 10 and len(end_date) == 10 and start_date[0] in year_end and start_date[-1] in year_end and end_date[0] in year_end and end_date[-1] in year_end:
				if account in financial_data[category]:
					try:
						download_path = financial_data['other_information']['storage_folder']
						
						now = datetime.now()
						current_year = now.strftime("%d%m%Y")
						
						file_name = f"{category} {account} ssdata{current_year}.png"
						screenshot_filename = os.path.join(download_path, file_name)
						
						self.exportation_layout.export_to_png(screenshot_filename)
						self.error.text = f'Screenshot saved to {download_path}'
						toast("Screenshot saved to storage path")
					except:
						toast("Error encountered, add storage folder")
						self.error.text = 'Error in saving screenshot'
				else:
					self.error.text = f"Account '{account}' not found in '{category}'."
					self.to_normal()
					
			else:
				self.error.text = 'Error in dates selection, please check again'
				self.to_normal()
				toast("Dates required")
		
	def go_back(self):
		if from_view_records_to_home ==True:
			if self.first_scroll_view.do_scroll_y == False:
				self.first_scroll_view.scroll_y = 1
				self.first_scroll_view.do_scroll_y = True
			else:		
				self.manager.current = 'home'
		else:
			if self.first_scroll_view.do_scroll_y == False:
				self.first_scroll_view.scroll_y = 1
				self.first_scroll_view.do_scroll_y = True
			else:		
				self.manager.current = 'income_statement'
		
	def to_normal(self):
		def normal(*args):
			self.error.text = 'All fields are required'
			
		Clock.schedule_once(normal, 3)
		
	def select_date(self, date_field):
		global on_date_field
		on_date_field = date_field
		popup = DatesPopup()
		popup.open()
		
	def get_screen_width(self):
		return Window.width
		
	def get_screen_height(self):
		return Window.height
			
	def update_lists_of_account(self, category):
		self.account_name.values = view_accounts(financial_data, category)
		self.account_name.text = 'Choose Account'
		
	def on_press_filter_account_button(self, category, account, start_date, end_date, *args):
		if category == 'Account Category' or account == 'Choose Account':
			self.error.text = 'First select an account to view records'
			self.to_normal()
			self.loading_popup.dismiss()
		else:
			year_end = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
			if len(start_date) == 10 and len(end_date) == 10 and start_date[0] in year_end and start_date[-1] in year_end and end_date[0] in year_end and end_date[-1] in year_end:
				if account in financial_data[category]:
					transactions = get_filtered_transactions(financial_data, category, account, start_date, end_date)
					bal_bd = balance_bd_sub_totals(financial_data, category, account,str(financial_data['other_information']['start_date']), start_date)
					self.build_transactions_ui(transactions, category, bal_bd)
				else:
					self.error.text = f"Account '{account}' not found in '{category}'."
					self.to_normal()
					self.loading_popup.dismiss()
					
			else:
				self.error.text = 'Error in dates selection, please check again'
				self.to_normal()
				self.loading_popup.dismiss()
				
	def open_and_view_transaction(self, instance):
		global from_journal_to_home
		global the_double_entry
		global selected_account_to_view
		global the_view_account_side
		global the_global_amount_dep
		if self.account_name.text in financial_data[self.account_category.text]:
			specific_transaction = get_transaction_by_id(financial_data, self.account_category.text, self.account_name.text, int(instance.text))
			if specific_transaction:
				view = self.manager.get_screen('Journal_entries')
				view.status.text = 'Status: View, Edit and Delete transaction'
				view.transaction_date.text = specific_transaction['date']
				view.trans_id.text = instance.text
				view.memo.text = specific_transaction['memo']
				view.transaction_amount.text = str(specific_transaction['amount'])
				the_global_amount_dep = specific_transaction['amount']
				
				if specific_transaction['side'] == 'debit':
					view.debit_account.text = f"{self.account_category.text}|{self.account_name.text}"
					view.credit_account.text = specific_transaction['double_entry']
					view.check_debit.active = True
					view.side.text = 'debit'
					the_view_account_side = 'debit'
					target_accum_dep_debit = f"{self.account_category.text}|{self.account_name.text}"
					target_accum_dep_credit = specific_transaction['double_entry']
					view.debit_account.color = 'purple'
					view.debit_account.font_size = '20sp'
					view.credit_account.color = 'green'
					view.credit_account.font_size = '18sp'
					toast("Viewing debit record")
				else:
					view.credit_account.text = f"{self.account_category.text}|{self.account_name.text}"
					view.debit_account.text = specific_transaction['double_entry']
					view.check_credit.active = True
					view.side.text = 'credit'
					the_view_account_side = 'credit'
					target_accum_dep_debit = specific_transaction['double_entry']
					target_accum_dep_credit = f"{self.account_category.text}|{self.account_name.text}"
					view.debit_account.color = 'green'
					view.debit_account.font_size = '18sp'
					view.credit_account.color = 'purple'
					view.credit_account.font_size = '20sp'
					toast("Viewing credit record")
					
				view.account_category.text = self.account_category.text
				view.account_name.text = self.account_name.text
				selected_account_to_view = f"{self.account_category.text}|{self.account_name.text}"
				view.search_id.text = ''
				the_double_entry = specific_transaction['double_entry']
				
				check_dep = the_double_entry.split('|')
				is_dep = check_dep[1]
				
				# check if depreciation and lock accounts
				if self.account_name.text == 'Depreciation' or is_dep == 'Depreciation':
					view.account_category.disabled = True
					view.account_name.disabled = True
				else:
					view.account_category.disabled = False
					view.account_name.disabled = False
					
				check_for_asset = target_accum_dep_credit.split('|')
				
				# if is accumulated depreciation
				if target_accum_dep_debit == f'Capital|Opening Balance Equity' and check_for_asset[0] == 'Non Current Assets':
					view.account_category.disabled = True
					view.account_name.disabled = True
					view.is_accum_deprec.text = 'accum depreciation'
					view.is_accum_deprec.disabled = True
				else:
					view.is_accum_deprec.text = 'journal entry'
					view.is_accum_deprec.disabled = True
					
				view.save_button.disabled = False
				view.edit_button.disabled = False
				view.delete_button.disabled = False
				
				self.manager.current = 'Journal_entries'
				from_journal_to_home = False
			else:
				self.error.text = f"Transaction id '{instance.text}' not found in account '{self.account_name.text}'."
				self.to_normal()
		else:
			self.error.text = f"Account '{self.account_name.text}' not found in '{self.account_category.text}'."
			self.to_normal()
			
	def show_popup(self, dt):
		self.popup.open()
		
	def close_popup(self, dt):
		self.popup.dismiss()
		
	def update_rect(self, instance, value):
		# Update the background color rectangle's position and size
		self.rect.pos = instance.pos
		self.rect.size = instance.size
		
	def split_records_to_view(self, category, account, function):
		if account == 'Choose Account':
			self.error.text = 'Please select an account to view'
			self.to_normal()
			toast('Please select an account')
			return
		else:
			pass
			
		if function == 'Past week report':
			today = datetime.now()
			date_format = "%d-%m-%Y"
			self.end_date.text = today.strftime(date_format)
			week_ago = today - timedelta(days=7)
			self.start_date.text = week_ago.strftime(date_format)
			
			self.show_loading_popup(category, account, self.start_date.text,self.end_date.text)
		elif function == 'Past month report':
			today = datetime.now()
			date_format = "%d-%m-%Y"
			self.end_date.text = today.strftime(date_format)
			week_ago = today - timedelta(days=30)
			self.start_date.text = week_ago.strftime(date_format)
			
			self.show_loading_popup(category, account, self.start_date.text,self.end_date.text)
		elif function == 'Today`s report':
			today = datetime.now()
			date_format = "%d-%m-%Y"
			self.end_date.text = today.strftime(date_format)
			self.start_date.text = today.strftime(date_format)
			
			self.show_loading_popup(category, account, self.start_date.text,self.end_date.text)
		elif function == 'Past 90 days report':
			today = datetime.now()
			date_format = "%d-%m-%Y"
			self.end_date.text = today.strftime(date_format)
			week_ago = today - timedelta(days=90)
			self.start_date.text = week_ago.strftime(date_format)
			
			self.show_loading_popup(category, account, self.start_date.text,self.end_date.text)
		else:
			pass
		
	def show_loading_popup(self, category, account, start_date, end_date):
		self.loading_popup = LoadingPopup(title='Loading...')
		self.loading_popup.open()
		
		partial_func = partial(self.on_press_filter_account_button, category, account, start_date, end_date)
		Clock.schedule_once(partial_func, 0.2)
				
	def build_transactions_ui(self, transactions, category, balance_bd):
		chars = int(self.the_characters.text)
		fnt = f"{self.the_font_size.text}sp"
		hght= f"{self.the_label_height.text}dp"
		self.total_entries.font_size = fnt
		self.total_amount.font_size = fnt
		self.balance_amount.font_size = fnt
		#Clock.schedule_once(self.show_popup, 0)
		#Clock.schedule_once(self.close_popup, 2)
		self.loading_popup.dismiss()
		# clear widgets
		self.date_column.clear_widgets()
		self.ids_column.clear_widgets()
		self.details_column.clear_widgets()
		self.amount_column.clear_widgets()
		self.balance_column.clear_widgets()
		self.debit_total.text = '0'
		self.credit_total.text = '0'
		self.total_amount.text = '0'
		self.bal_bd.text = '0'
		self.balance_amount.text = '0'
		app = App.get_running_app()
		debit_color = app.return_theme_color()
		
		# totals and amounts
		total_amnt = 0
		total_debit = 0
		total_credit = 0
		entries_made = 0
		formatted = "{:,.2f}".format(balance_bd)
		if balance_bd < 0:
			self.bal_bd.color = 'red'
		else:
			self.bal_bd.color = 'blue'
			
		self.bal_bd.text = formatted

		# excel style
		for i, trans in enumerate(transactions):
			entries_made += 1
			bg = (255,255,255,1) if i % 2 == 0 else (.5,.5,.5,.3)
			# date button	
			date = DateLabel(trans['date'],fnt,hght)
			self.date_column.add_widget(date)
			
			#ids button
			ids = IdsButton(str(trans['id']),fnt,hght,bg,self.open_and_view_transaction)
			self.ids_column.add_widget(ids)
			
			#memo
			if self.memo_or_account.text == 'Memo':
				the_details = f'{trans["memo"][0:chars]}..'
			else:
				split_account = trans["double_entry"].split('|')
				account_set = split_account[1]
				the_details = f'{account_set[0:16]}..'
			
			# memo button
			memo = MemoLabel(the_details,fnt,hght)
			self.details_column.add_widget(memo)
			
			# amount logic
			if category == 'Non Current Assets' or category == 'Current Assets' or category == 'Expenses' or category == 'Bank' or category == 'Cost of Sales':
				if trans['side'] == 'debit':
					figure = str(trans['amount'])
					total_debit += trans['amount']
				else:
					figure = f'({str(trans["amount"])})'
					total_credit += trans['amount']
			else:
				if trans['side'] == 'debit':
					figure = str(trans['amount'])
					total_debit += trans['amount']
				else:
					figure = f'({str(trans["amount"])})'
					total_credit += trans['amount']
			
			# balances logic
			if figure[0] == '(':
				total_amnt -= float(figure[1:-1])
				balance_bd -= float(figure[1:-1])
				formatted = "{:,.2f}".format(trans['amount'])
				formatted = f"({formatted})"
				clr = 'black'
				
			else:
				total_amnt += float(figure)
				balance_bd += float(figure)
				formatted = "{:,.2f}".format(trans['amount'])
				clr = debit_color
			
			#amount button	
			amount = AmountLabel(formatted,fnt,hght,clr)
			self.amount_column.add_widget(amount)
			
			formatted = "{:,.2f}".format(balance_bd)
			
			if balance_bd < 0:
				color = 'red'
			else:
				color = 'black'
				
			#balances button
			balance = BalancesLabel(formatted,fnt,hght,color)
			self.balance_column.add_widget(balance)
			
		# update totals
		formatted = "{:,.2f}".format(total_debit)	
		self.debit_total.text = formatted
		formatted = "{:,.2f}".format(total_credit)
		self.credit_total.text = formatted
		formatted = "{:,.2f}".format(total_amnt)
		self.total_amount.text = formatted
		formatted = "{:,.2f}".format(balance_bd)
		self.balance_amount.text = formatted
			
		self.ledger_account.text = f"Viewing ledger account '{self.account_name.text}'"
		# entries made
		self.total_entries.text = f'{entries_made} entries'
		
		# variance from budget
		budg = self.get_the_budgeted_amount(f"{category}|{self.account_name.text}")
		write_budg = "{:,.2f}".format(budg)
		variance = budg - abs(balance_bd)
		formatted = "{:,.2f}".format(variance)
		actual_amount = "{:,.2f}".format(balance_bd)
		
		if budg == 0:
			variance = f'Actual amount = {actual_amount}\n budgeted = None\n Variance = None'
		else:
			variance = f'Actual amount = {actual_amount}\n budgeted = {write_budg}\n Variance = {formatted}'
			
		self.variance_from_budget.text = variance
		self.first_scroll_view.scroll_y = 0
		self.first_scroll_view.do_scroll_y = False
		toast("Records loaded")
		
		
	def get_the_budgeted_amount(self, account):
		if account in financial_data['other_information']['budgeted_accounts']:
			return financial_data['other_information']['budgeted_accounts'][account]
		else:
			return 0
			
			
'''
income statement 
'''
class IncomeStatement(Screen):
	def __init__(self, **kwargs):
		super(IncomeStatement, self).__init__(**kwargs)
		Window.softinput_mode = 'below_target'
		
	def get_help(self):
		global ask_for_help
		ask_for_help = str(SimploStatsHelp().get_help('income_statement'))
		popup = HelpPopup()
		popup.title = 'Income Statement'
		popup.open()
		
	def export_selected_income_statement_to_csv(self, start_date, end_date):
		year_end = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
		if len(start_date) == 10 and len(end_date) == 10 and start_date[0] in year_end and start_date[-1] in year_end and end_date[0] in year_end and end_date[-1] in year_end:
			self.error.text = export_income_statement(start_date, end_date)	
		else:
			self.error.text = 'Error in dates selection, please check again'
			self.to_normal()
			toast("Date required")
		
	def export_displayed_as_pdf(self, start_date, end_date):
		year_end = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
		if len(start_date) == 10 and len(end_date) == 10 and start_date[0] in year_end and start_date[-1] in year_end and end_date[0] in year_end and end_date[-1] in year_end:
			try:
				download_path = financial_data['other_information']['storage_folder']
						
				now = datetime.now()
				current_year = now.strftime("%d%m%Y")
						
				file_name = f"income statement ssdata{current_year}.png"
				screenshot_filename = os.path.join(download_path, file_name)
				
				self.exportation_layout.export_to_png(screenshot_filename)
				self.error.text = f'Screenshot saved to {download_path}'
				toast("Screenshot saved to storage folder")
			except:
				toast("Screenshot error")
				self.error.text = 'Error in saving screenshot'
					
		else:
			self.error.text = 'Error in dates selection, please check again'
			self.to_normal()
			toast("Date required")
		
	def go_back(self):
		self.manager.current = 'home'
		
	def to_normal(self):
		def normal(*args):
			self.error.text = 'All fields are required'
			
		Clock.schedule_once(normal, 3)
		
	def select_date(self, date_field):
		global on_date_field
		on_date_field = date_field
		popup = DatesPopup()
		popup.open()
		
	def on_press_account_button(self, details, *args):
		global from_view_records_to_home			
		view_records = self.manager.get_screen('view_accounts')
		details = details.split('|')
		view_records.start_date.text = details[2]
		view_records.end_date.text = details[3]
		view_records.account_category.text = details[0]
		view_records.account_name.text = details[1]
		self.manager.current = 'view_accounts'
		from_view_records_to_home = False
		
	def on_text_show_date(self, function):
		if function == 'Past week report':
			today = datetime.now()
			date_format = "%d-%m-%Y"
			self.end_date.text = today.strftime(date_format)
			week_ago = today - timedelta(days=7)
			self.start_date.text = week_ago.strftime(date_format)
			
			self.show_loading_popup(self.start_date.text,self.end_date.text)
		elif function == 'Past month report':
			today = datetime.now()
			date_format = "%d-%m-%Y"
			self.end_date.text = today.strftime(date_format)
			week_ago = today - timedelta(days=30)
			self.start_date.text = week_ago.strftime(date_format)
			
			self.show_loading_popup(self.start_date.text,self.end_date.text)
		elif function == 'Today`s report':
			today = datetime.now()
			date_format = "%d-%m-%Y"
			self.end_date.text = today.strftime(date_format)
			self.start_date.text = today.strftime(date_format)
			
			self.show_loading_popup(self.start_date.text,self.end_date.text)
		elif function == 'Past 90 days report':
			today = datetime.now()
			date_format = "%d-%m-%Y"
			self.end_date.text = today.strftime(date_format)
			week_ago = today - timedelta(days=90)
			self.start_date.text = week_ago.strftime(date_format)
			
			self.show_loading_popup(self.start_date.text,self.end_date.text)		
		elif function == 'Financial year report':
			start_date_ = financial_data['other_information']['start_date']
			end_date_ = financial_data['other_information']['end_date']
			self.end_date.text = end_date_
			self.start_date.text = start_date_
			
			self.show_loading_popup(self.start_date.text,self.end_date.text)
		else:
			pass
			
	def show_loading_popup(self, start_date, end_date):
		self.loading_popup = LoadingPopup(title='Loading...')
		self.loading_popup.open()
		
		partial_func = partial(self.generate_income_statement, start_date, end_date)
		Clock.schedule_once(partial_func, 0.2)
		
	def generate_income_statement(self, start_date, end_date, *args):
		year_end = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
		if len(start_date) == 10 and len(end_date) == 10 and start_date[0] in year_end and start_date[-1] in year_end and end_date[0] in year_end and end_date[-1] in year_end:
			self.loading_popup.dismiss()
			self.accounts_column.clear_widgets()
			self.amounts_column.clear_widgets()
			app = App.get_running_app()
			color = app.return_theme_color()	
			
			# sales label
			sales_acc_btn = MDFlatButton(
				text='Sales/operating income',
				size_hint=(1,None),
				halign='left',
				theme_text_color="Custom",
				text_color=color,
				font_size="14sp")
			# pass button
			sales_amt_btn = MDFlatButton(
				text='  ',
				size_hint=(1,None),
				halign='left',
				font_size="14sp")
			# create buttons
			self.accounts_column.add_widget(sales_acc_btn)
			self.amounts_column.add_widget(sales_amt_btn)
				
			# make sales buttons
			category_accounts = financial_data['Operating Revenue']
			total_sales = []
			for account_name,account_data in category_accounts.items():
				if account_name == 'i donnot know321':
					pass
				else:
					account_total = income_statement_deractives(financial_data, 'Operating Revenue', str(account_name), start_date, end_date)
					total_sales.append(account_total)
					if account_total == 0:
						pass
					else:
						info = f"Operating Revenue|{account_name}|{start_date}|{end_date}"
						# accounts button
						account_button = MDFlatButton(
							text=str(account_name),
							size_hint=(1,None),
							halign='left',
							font_size="14sp")
							
						account_button.bind(on_press=partial(self.on_press_account_button, info))
						
						# amounts button
						formatted = "{:,.2f}".format(-account_total)
						amount_button = MDFlatButton(
							text=formatted,
							size_hint=(1,None),
							halign='left',
							font_size="14sp")
						# create buttons
						self.accounts_column.add_widget(account_button)
						self.amounts_column.add_widget(amount_button)
			# get total expenses ui
			total_sales = sum(total_sales)
			
			exp_button = MDFlatButton(
				text='Net Sales/operating income\n',
				size_hint=(1,None),
				theme_text_color="Custom",
				text_color=color,
				halign='left',
				font_size="14sp")
			# total expenses button
			formatted = "{:,.2f}".format(-total_sales)
			total_exp_button = MDFlatButton(
				text=f"{formatted}\n-----------------------",
				size_hint=(1,None),
				halign='left',
				theme_text_color="Custom",
				text_color=color,
				font_size="14sp")
			# create buttons
			self.accounts_column.add_widget(exp_button)
			self.amounts_column.add_widget(total_exp_button)
			
			# cost of sales label
			sales_acc_btn = MDFlatButton(
				text='Cost of Sales',
				size_hint=(1,None),
				halign='left',
				theme_text_color="Custom",
				text_color=color,
				font_size="14sp")
			# pass button
			sales_amt_btn = MDFlatButton(
				text='  ',
				size_hint=(1,None),
				halign='left',
				font_size="14sp")
			# create buttons
			self.accounts_column.add_widget(sales_acc_btn)
			self.amounts_column.add_widget(sales_amt_btn)
			
			# make cost of sales buttons
			category_accounts = financial_data['Cost of Sales']
			total_cos = []
			for account_name,account_data in category_accounts.items():
				if account_name == 'i donnot know321':
					pass
				else:
					account_total = income_statement_deractives(financial_data, 'Cost of Sales', str(account_name), start_date, end_date)
					total_cos.append(account_total)
					if account_total == 0:
						pass
					else:
						info = f"Cost of Sales|{account_name}|{start_date}|{end_date}"
						# accounts button
						account_button = MDFlatButton(
							text=str(account_name),
							size_hint=(1,None),
							halign='left',
							font_size="14sp")
							
						account_button.bind(on_press=partial(self.on_press_account_button, info))
						
						# amounts button
						formatted = "{:,.2f}".format(account_total)
						amount_button = MDFlatButton(
							text=formatted,
							size_hint=(1,None),
							halign='left',
							font_size="14sp")
						# create buttons
						self.accounts_column.add_widget(account_button)
						self.amounts_column.add_widget(amount_button)
			# get total expenses ui
			total_cos = sum(total_cos)
			
			exp_button = MDFlatButton(
				text='Total Cost of Sales\n',
				size_hint=(1,None),
				halign='left',
				theme_text_color="Custom",
				text_color=color,
				font_size="14sp")
			# total expenses button
			formatted = "{:,.2f}".format(total_cos)
			total_exp_button = MDFlatButton(
				text=f"{formatted}\n-----------------------",
				size_hint=(1,None),
				halign='left',
				theme_text_color="Custom",
				text_color=color,
				font_size="14sp")
			# create buttons
			self.accounts_column.add_widget(exp_button)
			self.amounts_column.add_widget(total_exp_button)
				
			trading_profits = total_sales + total_cos
			# update gross profit' account totals
			formatted = "{:,.2f}".format(-trading_profits)
			# Expenses label
			gross_prft_btn = MDFlatButton(
				text='Gross Profit\n',
				size_hint=(1,None),
				halign='left',
				theme_text_color="Custom",
				text_color=color,
				font_size="14sp")
			# pass button
			gross_amnt_btn = MDFlatButton(
				text=f"{formatted}\n-----------------------",
				size_hint=(1,None),
				halign='left',
				theme_text_color="Custom",
				text_color=color,
				font_size="14sp")
			# create buttons
			self.accounts_column.add_widget(gross_prft_btn)
			self.amounts_column.add_widget(gross_amnt_btn)
			
			# Expenses label
			pandlacc = MDFlatButton(
				text='Profit and Loss Account',
				size_hint=(1,None),
				theme_text_color="Custom",
				text_color='black',
				halign='left',
				font_size="14sp")
			# pass button
			pandlsep = MDFlatButton(
				text='  ',
				size_hint=(1,None),
				halign='left',
				font_size="14sp")
			# create buttons
			self.accounts_column.add_widget(pandlacc)
			self.amounts_column.add_widget(pandlsep)
			
			# Expenses label
			account_button = MDFlatButton(
				text='Operating Expenses',
				size_hint=(1,None),
				halign='left',
				theme_text_color="Custom",
				text_color=color,
				font_size="14sp")
			# pass button
			amount_button = MDFlatButton(
				text='  ',
				size_hint=(1,None),
				halign='left',
				font_size="14sp")
			# create buttons
			self.accounts_column.add_widget(account_button)
			self.amounts_column.add_widget(amount_button)
			
			# make expenses buttons
			category_accounts = financial_data['Operating Expenses']
			total_expenses = []
			for account_name,account_data in category_accounts.items():
				if account_name == 'what_ever_it_is':
					pass
				else:
					account_total = income_statement_deractives(financial_data, 'Operating Expenses', str(account_name), start_date, end_date)
					total_expenses.append(account_total)
					if account_total == 0:
						pass
					else:
						info = f"Operating Expenses|{account_name}|{start_date}|{end_date}"
						# accounts button
						account_button = MDFlatButton(
							text=str(account_name),
							size_hint=(1,None),
							halign='left',
							font_size="14sp")
							
						account_button.bind(on_press=partial(self.on_press_account_button, info))
						
						# amounts button
						formatted = "{:,.2f}".format(account_total)
						amount_button = MDFlatButton(
							text=formatted,
							size_hint=(1,None),
							halign='left',
							font_size="14sp")
						# create buttons
						self.accounts_column.add_widget(account_button)
						self.amounts_column.add_widget(amount_button)
			# get total expenses ui
			total_expenses = sum(total_expenses)
			# expenses text
			exp_button = MDFlatButton(
				text='Total Operating Expenses\n',
				size_hint=(1,None),
				halign='left',
				theme_text_color="Custom",
				text_color=color,
				font_size="14sp")
			# total expenses button
			formatted = "{:,.2f}".format(total_expenses)
			total_exp_button = MDFlatButton(
				text=f"{formatted}\n-----------------------",
				size_hint=(1,None),
				halign='left',
				theme_text_color="Custom",
				text_color=color,
				font_size="14sp")
			# create buttons
			self.accounts_column.add_widget(exp_button)
			self.amounts_column.add_widget(total_exp_button)
			
			# operating income
			op_income_button = MDFlatButton(
				text='Net Operating Income\n',
				size_hint=(1,None),
				halign='left',
				theme_text_color="Custom",
				text_color=color,
				font_size="14sp")
			# button
			operating_income = trading_profits + total_expenses
			formatted = "{:,.2f}".format(-operating_income)
			op_income_amount_button = MDFlatButton(
				text=f"{formatted}\n-----------------------",
				size_hint=(1,None),
				halign='left',
				theme_text_color="Custom",
				text_color=color,
				font_size="14sp")
			# create buttons
			self.accounts_column.add_widget(op_income_button)
			self.amounts_column.add_widget(op_income_amount_button)
			
			# income label
			account_button = MDFlatButton(
				text='Other/non-operating Incomes',
				size_hint=(1,None),
				halign='left',
				theme_text_color="Custom",
				text_color=color,
				font_size="14sp")
			# pass button
			amount_button = MDFlatButton(
				text='   ',
				size_hint=(1,None),
				halign='left',
				font_size="14sp")
			# create buttons
			self.accounts_column.add_widget(account_button)
			self.amounts_column.add_widget(amount_button)
			
			'''income buttons
			'''
			
			category_accounts = financial_data['Other Incomes']
			total_income = []
			for account_name,account_data in category_accounts.items():
				if account_name == 'what_ever_it_is':
					pass
				else:
					account_total = income_statement_deractives(financial_data, 'Other Incomes', str(account_name), start_date, end_date)
					total_income.append(account_total)
					if account_total == 0:
						pass
					else:
						info = f"Other Incomes|{account_name}|{start_date}|{end_date}"
						# accounts button
						account_button = MDFlatButton(
							text=str(account_name),
							size_hint=(1,None),
							halign='left',
							font_size="14sp")
							
						account_button.bind(on_press=partial(self.on_press_account_button, info))
						
						# amounts button
						formatted = "{:,.2f}".format(-account_total)
						amount_button = MDFlatButton(
							text=formatted,
							size_hint=(1,None),
							halign='left',
							font_size="14sp")
						# create buttons
						self.accounts_column.add_widget(account_button)
						self.amounts_column.add_widget(amount_button)
			# get total expenses ui
			total_income = sum(total_income)
			# note,, found it lazy to rename income buttons
			# expenses text
			exp_button = MDFlatButton(
				text='Total other/ non-op incomes\n',
				size_hint=(1,None),
				halign='left',
				theme_text_color="Custom",
				text_color=color,
				font_size="14sp")
			# total expenses button
			formatted = "{:,.2f}".format(-total_income)
			total_exp_button = MDFlatButton(
				text=f"{formatted}\n-----------------------",
				size_hint=(1,None),
				halign='left',
				theme_text_color="Custom",
				text_color=color,
				font_size="14sp")
			# create buttons
			self.accounts_column.add_widget(exp_button)
			self.amounts_column.add_widget(total_exp_button)
			
			# total income
			op_income_button = MDFlatButton(
				text='Generated Incomes\n',
				size_hint=(1,None),
				halign='left',
				theme_text_color="Custom",
				text_color=color,
				font_size="14sp")
			# button
			total_accounts_income = operating_income + total_income
			formatted = "{:,.2f}".format(-total_accounts_income)
			op_income_amount_button = MDFlatButton(
				text=f"{formatted}\n-----------------------",
				size_hint=(1,None),
				halign='left',
				theme_text_color="Custom",
				text_color=color,
				font_size="14sp")
			# create buttons
			self.accounts_column.add_widget(op_income_button)
			self.amounts_column.add_widget(op_income_amount_button)
			
			# other expenses label
			account_button = MDFlatButton(
				text='Other/ Non-operating Expenses',
				size_hint=(1,None),
				halign='left',
				theme_text_color="Custom",
				text_color=color,
				font_size="14sp")
			# pass button
			amount_button = MDFlatButton(
				text='  ',
				size_hint=(1,None),
				halign='left',
				font_size="14sp")
			# create buttons
			self.accounts_column.add_widget(account_button)
			self.amounts_column.add_widget(amount_button)
			
			# make expenses buttons
			category_accounts = financial_data['Other Expenses']
			total_other_expenses = []
			for account_name,account_data in category_accounts.items():
				if account_name == 'what_ever_it_is':
					pass
				else:
					account_total = income_statement_deractives(financial_data, 'Other Expenses', str(account_name), start_date, end_date)
					total_other_expenses.append(account_total)
					if account_total == 0:
						pass
					else:
						info = f"Other Expenses|{account_name}|{start_date}|{end_date}"
						# accounts button
						account_button = MDFlatButton(
							text=str(account_name),
							size_hint=(1,None),
							halign='left',
							font_size="14sp")
							
						account_button.bind(on_press=partial(self.on_press_account_button, info))
						
						# amounts button
						formatted = "{:,.2f}".format(account_total)
						amount_button = MDFlatButton(
							text=formatted,
							size_hint=(1,None),
							halign='left',
							font_size="14sp")
						# create buttons
						self.accounts_column.add_widget(account_button)
						self.amounts_column.add_widget(amount_button)
			# get total expenses ui
			total_other_expenses = sum(total_other_expenses)
			
			profit_before_taxes = total_accounts_income +total_other_expenses 
			# expenses text
			exp_button = MDFlatButton(
				text='Total Other/ non-op Expenses\n',
				size_hint=(1,None),
				halign='left',
				theme_text_color="Custom",
				text_color=color,
				font_size="14sp")
			# total expenses button
			formatted = "{:,.2f}".format(total_other_expenses)
			total_exp_button = MDFlatButton(
				text=f"{formatted}\n-----------------------",
				size_hint=(1,None),
				halign='left',
				theme_text_color="Custom",
				text_color=color,
				font_size="14sp")
			# create buttons
			self.accounts_column.add_widget(exp_button)
			self.amounts_column.add_widget(total_exp_button)
			
			# operating income
			op_income_button = MDFlatButton(
				text='Profit Before Taxes\n',
				size_hint=(1,None),
				halign='left',
				theme_text_color="Custom",
				text_color=color,
				font_size="14sp")
			# button
			formatted = "{:,.2f}".format(-profit_before_taxes)
			op_income_amount_button = MDFlatButton(
				text=f"{formatted}\n-----------------------",
				size_hint=(1,None),
				halign='left',
				theme_text_color="Custom",
				text_color=color,
				font_size="14sp")
			# create buttons
			self.accounts_column.add_widget(op_income_button)
			self.amounts_column.add_widget(op_income_amount_button)
			
			# taxes calculation
			taxes_paid = get_category_total(['Taxes'], start_date, end_date)
			if taxes_paid == 0:
				pass
			else:
				info = f"Taxes|Choose Account|{start_date}|{end_date}"
				formatted = "{:,.2f}".format(taxes_paid)
				percent = (taxes_paid/profit_before_taxes) * 100
				op_income_button = MDFlatButton(
					text=f'Taxes - ({round(-percent, 2)} %)\n',
					size_hint=(1,None),
					halign='left',
					theme_text_color="Custom",
					text_color=color,
					font_size="14sp")
					
				op_income_button.bind(on_press=partial(self.on_press_account_button, info))
				
				op_income_amount_button = MDFlatButton(
					text=f"{formatted}\n-----------------------",
					size_hint=(1,None),
					halign='left',
					theme_text_color="Custom",
					text_color=color,
					font_size="14sp")
				# create buttons
				self.accounts_column.add_widget(op_income_button)
				self.amounts_column.add_widget(op_income_amount_button)
			
			# net profit
			op_income_button = MDFlatButton(
				text='\nNet Profit/Loss\n',
				size_hint=(1,None),
				halign='left',
				theme_text_color="Custom",
				text_color=color,
				font_size="14sp")
			# button
			net_profit = profit_before_taxes + taxes_paid
			formatted = "{:,.2f}".format(-net_profit)
			op_income_amount_button = MDFlatButton(
				text=f"\n{formatted}\n-----------------------",
				size_hint=(1,None),
				halign='left',
				theme_text_color="Custom",
				text_color=color,
				font_size="14sp")
			# create buttons
			self.accounts_column.add_widget(op_income_button)
			self.amounts_column.add_widget(op_income_amount_button)
			toast("Income statement built")
			
		else:
			self.loading_popup.dismiss()
			self.error.text = 'Error in dates selection, please check again'
			self.to_normal()
			
			
'''
the statement of financial position
'''


class BalanceSheet(Screen):
	def __init__(self, **kwargs):
		super(BalanceSheet, self).__init__(**kwargs)
		Window.softinput_mode = 'below_target'
		
	def get_help(self):
		global ask_for_help
		ask_for_help = str(SimploStatsHelp().get_help('balance_sheet'))
		popup = HelpPopup()
		popup.title = 'Balance Sheet'
		popup.open()
		
	def export_selected_balance_sheet_to_csv(self, end_date):
		year_end = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
		if len(end_date) == 10 and end_date[0] in year_end and end_date[-1] in year_end:
			self.error.text = export_balance_sheet(end_date)		
		else:
			self.error.text = 'Error in dates selection, please check again'
			self.to_normal()
			toast("Date required")
		
	def export_displayed_as_pdf(self, end_date):
		year_end = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
		if len(end_date) == 10 and end_date[0] in year_end and end_date[-1] in year_end:
			try:
				download_path = financial_data['other_information']['storage_folder']
						
				now = datetime.now()
				current_year = now.strftime("%d%m%Y")
						
				file_name = f"balance sheet ssdata{current_year}.png"
				screenshot_filename = os.path.join(download_path, file_name)
				
				self.exportation_layout.export_to_png(screenshot_filename)
				self.error.text = f'Screenshot saved to {download_path}'
				toast("Screenshot saved to storage folder")
			except:
				toast("Screenshot error")
				self.error.text = 'Error in saving screenshot'
					
		else:
			self.error.text = 'Error in dates selection, please check again'
			self.to_normal()
			toast("Date required")
		
	def go_back(self):
		self.manager.current = 'home'
		
	def to_normal(self):
		def normal(*args):
			self.error.text = 'All fields are required'
			
		Clock.schedule_once(normal, 3)
		
	def select_date(self, date_field):
		global on_date_field
		on_date_field = date_field
		popup = DatesPopup()
		popup.open()
		
	def on_press_net_profit_button(self, instance):
		global from_view_records_to_home
		start_date = str(financial_data['other_information']['start_date'])
		end_date = self.end_date.text
		
		# bored to chance income statement names
		view_records = self.manager.get_screen('income_statement')
		view_records.start_date.text = start_date
		view_records.end_date.text = end_date
		self.manager.current = 'income_statement'
		from_view_records_to_home = True
		
	def on_press_non_current_assets_button(self, instance):
		global from_view_records_to_home
		account_name = instance.text
		category = 'Non Current Assets'
		start_date = str(financial_data['other_information']['start_date'])
		end_date = self.end_date.text
		
		view_records = self.manager.get_screen('view_accounts')
		view_records.start_date.text = start_date
		view_records.end_date.text = end_date
		view_records.account_category.text = category
		view_records.account_name.text = account_name
		self.manager.current = 'view_accounts'
		from_view_records_to_home = True
		
	def on_press_current_assets_button(self, instance):
		global from_view_records_to_home
		account_name = instance.text
		category = 'Current Assets'
		start_date = str(financial_data['other_information']['start_date'])
		end_date = self.end_date.text
		
		view_records = self.manager.get_screen('view_accounts')
		view_records.start_date.text = start_date
		view_records.end_date.text = end_date
		view_records.account_category.text = category
		view_records.account_name.text = account_name
		self.manager.current = 'view_accounts'
		from_view_records_to_home = True
		
	def on_press_bank_button(self, instance):
		global from_view_records_to_home
		account_name = instance.text
		category = 'Bank'
		start_date = str(financial_data['other_information']['start_date'])
		end_date = self.end_date.text
		
		view_records = self.manager.get_screen('view_accounts')
		view_records.start_date.text = start_date
		view_records.end_date.text = end_date
		view_records.account_category.text = category
		view_records.account_name.text = account_name
		self.manager.current = 'view_accounts'
		from_view_records_to_home = True
		
	def on_press_capital_button(self, instance):
		global from_view_records_to_home
		account_name = instance.text
		category = 'Capital'
		start_date = str(financial_data['other_information']['start_date'])
		end_date = self.end_date.text
		
		view_records = self.manager.get_screen('view_accounts')
		view_records.start_date.text = start_date
		view_records.end_date.text = end_date
		view_records.account_category.text = category
		view_records.account_name.text = account_name
		self.manager.current = 'view_accounts'
		from_view_records_to_home = True
		
	def on_press_non_current_liabilities_button(self, instance):
		global from_view_records_to_home
		account_name = instance.text
		category = 'Non Current Liabilities'
		start_date = str(financial_data['other_information']['start_date'])
		end_date = self.end_date.text
		
		view_records = self.manager.get_screen('view_accounts')
		view_records.start_date.text = start_date
		view_records.end_date.text = end_date
		view_records.account_category.text = category
		view_records.account_name.text = account_name
		self.manager.current = 'view_accounts'
		from_view_records_to_home = True
		
	def on_press_current_liabilities_button(self, instance):
		global from_view_records_to_home
		account_name = instance.text
		category = 'Current Liabilities'
		start_date = str(financial_data['other_information']['start_date'])
		end_date = self.end_date.text
		
		view_records = self.manager.get_screen('view_accounts')
		view_records.start_date.text = start_date
		view_records.end_date.text = end_date
		view_records.account_category.text = category
		view_records.account_name.text = account_name
		self.manager.current = 'view_accounts'
		from_view_records_to_home = True
		
	def on_text_show_date(self, function):
		if function == 'As at past week':
			today = datetime.now()
			date_format = "%d-%m-%Y"
			week_ago = today - timedelta(days=7)
			self.end_date.text = week_ago.strftime(date_format)
			
			self.show_loading_popup(self.end_date.text)
		elif function == 'As at past month':
			today = datetime.now()
			date_format = "%d-%m-%Y"
			week_ago = today - timedelta(days=30)
			self.end_date.text = week_ago.strftime(date_format)
			
			self.show_loading_popup(self.end_date.text)
		elif function == 'As at today':
			today = datetime.now()
			date_format = "%d-%m-%Y"
			self.end_date.text = today.strftime(date_format)
			
			self.show_loading_popup(self.end_date.text)
		elif function == 'As at past 90 days':
			today = datetime.now()
			date_format = "%d-%m-%Y"
			week_ago = today - timedelta(days=90)
			self.end_date.text = week_ago.strftime(date_format)
			
			self.show_loading_popup(self.end_date.text)
		else:
			pass
			
	def get_the_accum_dep(self, category, account):
		account = f'{category}|{account}'
		if account in financial_data['other_information']['accum_depreciation']:
			return financial_data['other_information']['accum_depreciation'][account]
		else:
			return 0
			
	def get_the_cost_amount(self, category, account):
		account = f'{category}|{account}'
		if account in financial_data['other_information']['assets_at_cost']:
			return financial_data['other_information']['assets_at_cost'][account]
		else:
			return 0
			
	def show_loading_popup(self, end_date):
		self.loading_popup = LoadingPopup(title='Loading...')
		self.loading_popup.open()
		
		partial_func = partial(self.generate_the_balance_sheet, end_date)
		Clock.schedule_once(partial_func, 0.2)
		
	def generate_the_balance_sheet(self, end_date, *args):
		year_end = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
		now = datetime.now()
		todays_dep = now.strftime("%d-%m-%Y")
		if len(end_date) == 10 and end_date[0] in year_end and end_date[-1] in year_end:
			start_date = str(financial_data['other_information']['start_date'])
			self.loading_popup.dismiss()
			self.accounts_column.clear_widgets()
			self.amounts_column.clear_widgets()
			
			app = App.get_running_app()
			color = app.return_theme_color()
			icon_color = app.return_icon_color()
			# non current assets
			# lazy to change button names
			# non current assets label
			account_button = MDFlatButton(
				text='Non Current Assets',
				size_hint=(1,None),
				theme_text_color="Custom",
				text_color=color,
				font_size="16sp",
				halign='left')
			# pass button
			amount_button = MDFlatButton(
				text='  ',
				size_hint=(1,None),
				font_size="16sp",
				halign='left')
			# create buttons
			self.accounts_column.add_widget(account_button)
			self.amounts_column.add_widget(amount_button)
			
			category_accounts = financial_data['Non Current Assets']
			total_non_current_assets = []
			for account_name,account_data in category_accounts.items():
				account_total = income_statement_deractives(financial_data, 'Non Current Assets', str(account_name), start_date, end_date)
				total_non_current_assets.append(account_total)
				if account_total == 0:
					pass
				else:
					accumulated_dep = self.get_the_accum_dep('Non Current Assets', account_name)
					asset_at_cost = accumulated_dep + account_total
					
					if end_date == todays_dep:
						cost_of_asset = "{:,.2f}".format(asset_at_cost)
						depreciation = "{:,.2f}".format(accumulated_dep)
					else:
						cost_of_asset = "{:,.2f}".format(account_total)
						depreciation = '-'
					# accounts button
					account_button = MDFlatButton(
						text=str(account_name),
						on_press=self.on_press_non_current_assets_button,
						size_hint=(1,None),
						font_size="14sp",
						halign="left")
					# amounts button
					
					amount_button = MDFlatButton(
						text=cost_of_asset,
						size_hint=(1,None),
						font_size="14sp",
						halign='left')
						
					# depreciation button
					dep_acc_button = MDFlatButton(
						text=f'accum dep {account_name}',
						size_hint=(1,None),
						font_size='12sp',
						halign='left')
					# amounts button
					
					dep_button = MDFlatButton(
						text=depreciation,
						size_hint=(1,None),
						font_size='12sp',
						halign='left')
						
					# Net book value 
					nbv_acc_button = MDFlatButton(
						text=f'NBV {account_name}\n',
						size_hint=(1,None),
						font_size='13sp',
						theme_text_color="Custom",
						text_color=color,
						halign='left')
					# amounts button
					formatted = "{:,.2f}".format(account_total)
					nbv_button = MDFlatButton(
						text=f'{formatted}\n-----------------------',
						size_hint=(1,None),
						theme_text_color="Custom",
						text_color=color,
						font_size='13sp',
						halign='left')
						
						
					# create buttons
					self.accounts_column.add_widget(account_button)
					self.amounts_column.add_widget(amount_button)
					self.accounts_column.add_widget(dep_acc_button)
					self.amounts_column.add_widget(dep_button)
					self.accounts_column.add_widget(nbv_acc_button)
					self.amounts_column.add_widget(nbv_button)
					
			# get total non current assets ui
			total_non_current_assets = sum(total_non_current_assets)
			# note,, found it lazy to rename income buttons
			# non current assets text
			exp_button = MDFlatButton(
				text='Total Non Current Assets\n',
				size_hint=(1,None),
				theme_text_color="Custom",
				text_color=color,
				font_size="14sp",
				halign='left')
			# total expenses button
			formatted = "{:,.2f}".format(total_non_current_assets)
			total_exp_button = MDFlatButton(
				text=f"{formatted}\n-----------------------",
				size_hint=(1,None),
				theme_text_color="Custom",
				text_color=color,
				font_size="14sp",
				halign='left')
			# create buttons
			self.accounts_column.add_widget(exp_button)
			self.amounts_column.add_widget(total_exp_button)
			
			
			# current assets
			# lazy to change button names
			# current assets label
			account_button = MDFlatButton(
				text='Current Assets',
				size_hint=(1,None),
				font_size="16sp",
				theme_text_color="Custom",
				text_color=color,
				halign='left')
			# pass button
			amount_button = MDFlatButton(
				text='  ',
				size_hint=(1,None),
				font_size="16sp",
				halign='left')
			# create buttons
			self.accounts_column.add_widget(account_button)
			self.amounts_column.add_widget(amount_button)
			
			category_accounts = financial_data['Current Assets']
			total_current_assets = []
			for account_name,account_data in category_accounts.items():
				account_total = income_statement_deractives(financial_data, 'Current Assets', str(account_name), start_date, end_date)
				total_current_assets.append(account_total)
				if account_total == 0:
					pass
				else:
					# accounts button
					account_button = MDFlatButton(
						text=str(account_name),
						on_press=self.on_press_current_assets_button,
						size_hint=(1,None),
						font_size="14sp",
						halign='left')
					# amounts button
					formatted = "{:,.2f}".format(account_total)
					amount_button = MDFlatButton(
						text=formatted,
						size_hint=(1,None),
						font_size="14sp",
						halign='left')
					# create buttons
					self.accounts_column.add_widget(account_button)
					self.amounts_column.add_widget(amount_button)
			
			# bank accounts
			category_accounts = financial_data['Bank']
			total_bank = []
			for account_name,account_data in category_accounts.items():
				account_total = income_statement_deractives(financial_data, 'Bank', str(account_name), start_date, end_date)
				total_bank.append(account_total)
				if account_total == 0:
					pass
				else:
					# accounts button
					account_button = MDFlatButton(
						text=str(account_name),
						on_press=self.on_press_bank_button,
						size_hint=(1,None),
						font_size="14sp",
						halign='left')
					# amounts button
					formatted = "{:,.2f}".format(account_total)
					amount_button = MDFlatButton(
						text=formatted,
						size_hint=(1,None),
						halign='left',
						font_size="14sp")
					# create buttons
					self.accounts_column.add_widget(account_button)
					self.amounts_column.add_widget(amount_button)
					
			# sum bank
			total_bank = sum(total_bank)
			# get total current assets ui
			total_current_assets = sum(total_current_assets) + total_bank
			# note,, found it lazy to rename income buttons
			# non current assets text
			exp_button = MDFlatButton(
				text='Total Current Assets\n',
				size_hint=(1,None),
				halign='left',
				theme_text_color="Custom",
				text_color=color,
				font_size="14sp")
			# total expenses button
			formatted = "{:,.2f}".format(total_current_assets)
			total_exp_button = MDFlatButton(
				text=f"{formatted}\n-----------------------",
				size_hint=(1,None),
				halign='left',
				font_size="14sp",
				theme_text_color="Custom",
				text_color=color)
			# create buttons
			self.accounts_column.add_widget(exp_button)
			self.amounts_column.add_widget(total_exp_button)
			
			# total assets
			# sum total assests 
			total_assets =  total_non_current_assets + total_current_assets
			op_income_button = MDFlatButton(
				text='Total Assets',
				size_hint=(1,None),
				halign='left',
				md_bg_color=app.theme_cls.primary_color,
				theme_text_color="Custom",
				text_color=icon_color,
				font_size="16sp")
			# button
			formatted = "{:,.2f}".format(total_assets)
			op_income_amount_button = MDFlatButton(
				text=formatted,
				size_hint=(1,None),
				halign='left',
				md_bg_color=app.theme_cls.primary_color,
				theme_text_color="Custom",
				text_color=icon_color,
				font_size="16sp")
			# create buttons
			self.accounts_column.add_widget(op_income_button)
			self.amounts_column.add_widget(op_income_amount_button)
			
			
			# capital
			# lazy to change button names
			# current assets label
			account_button = MDFlatButton(
				text='Capital and Liabilities',
				size_hint=(1,None),
				halign='left',
				theme_text_color="Custom",
				text_color=color,
				font_size="14sp")
			# pass button
			amount_button = MDFlatButton(
				text='  ',
				size_hint=(1,None),
				halign='left',
				font_size="14sp")
			# create buttons
			self.accounts_column.add_widget(account_button)
			self.amounts_column.add_widget(amount_button)
			
			category_accounts = financial_data['Capital']
			total_capital = []
			for account_name,account_data in category_accounts.items():
				account_total = income_statement_deractives(financial_data, 'Capital', str(account_name), start_date, end_date)
				total_capital.append(account_total)
				if account_total == 0:
					pass
				else:
					# accounts button
					account_button = MDFlatButton(
						text=str(account_name),
						on_press=self.on_press_capital_button,
						size_hint=(1,None),
						halign='left',
						font_size="14sp")
					# amounts button
					formatted = "{:,.2f}".format(-account_total)
					amount_button = MDFlatButton(
						text=formatted,
						size_hint=(1,None),
						halign='left',
						font_size="14sp")
					# create buttons
					self.accounts_column.add_widget(account_button)
					self.amounts_column.add_widget(amount_button)
					
			# net profit
			# accounts button
			account_button = MDFlatButton(
				text='Net Profit/loss',
				size_hint=(1,None),
				halign='left',
				on_press=self.on_press_net_profit_button,
				font_size="14sp",
				theme_text_color="Custom",
				text_color=color)
			# amounts button
			net_profit = generate_the_net_profit_for_balance_sheet(start_date, end_date)
			formatted = "{:,.2f}".format(-net_profit)
			amount_button = MDFlatButton(
				text=formatted,
				size_hint=(1,None),
				halign='left',
				theme_text_color="Custom",
				text_color=color,
				font_size="14sp")
				
			# create buttons
			self.accounts_column.add_widget(account_button)
			self.amounts_column.add_widget(amount_button)
					
			# get capital ui
			total_capital = sum(total_capital) + net_profit
			# note,, found it lazy to rename income buttons
			# capital text
			exp_button = MDFlatButton(
				text='Total Capital\n',
				size_hint=(1,None),
				halign='left',
				theme_text_color="Custom",
				text_color=color,
				font_size="14sp")
			# total expenses button
			formatted = "{:,.2f}".format(-total_capital)
			total_exp_button = MDFlatButton(
				text=f"{formatted}\n-----------------------",
				size_hint=(1,None),
				halign='left',
				theme_text_color="Custom",
				text_color=color,
				font_size="14sp")
			# create buttons
			self.accounts_column.add_widget(exp_button)
			self.amounts_column.add_widget(total_exp_button)
			
			
			# non current liabilities
			# lazy to change button names
			# Non current liabilities label
			account_button = MDFlatButton(
				text='Non Current Liabilities',
				size_hint=(1,None),
				halign='left',
				theme_text_color="Custom",
				text_color=color,
				font_size="14sp")
			# pass button
			amount_button = MDFlatButton(
				text='  ',
				size_hint=(1,None),
				halign='left',
				font_size="14sp")
			# create buttons
			self.accounts_column.add_widget(account_button)
			self.amounts_column.add_widget(amount_button)
			
			category_accounts = financial_data['Non Current Liabilities']
			total_non_current_liabilities = []
			for account_name,account_data in category_accounts.items():
				account_total = income_statement_deractives(financial_data, 'Non Current Liabilities', str(account_name), start_date, end_date)
				total_non_current_liabilities.append(account_total)
				if account_total == 0:
					pass
				else:
					# accounts button
					account_button = MDFlatButton(
						text=str(account_name),
						on_press=self.on_press_non_current_liabilities_button,
						size_hint=(1,None),
						halign='left',
						font_size="14sp")
					# amounts button
					formatted = "{:,.2f}".format(-account_total)
					amount_button = MDFlatButton(
						text=formatted,
						size_hint=(1,None),
						halign='left',
						font_size="14sp")
					# create buttons
					self.accounts_column.add_widget(account_button)
					self.amounts_column.add_widget(amount_button)
					
			# total non current liabilities
			total_non_current_liabilities = sum(total_non_current_liabilities)
			# note,, found it lazy to rename liabilities buttons
			# non current liabilities text
			exp_button = MDFlatButton(
				text='Total Non Current Liabilities\n',
				size_hint=(1,None),
				theme_text_color="Custom",
				text_color=color,
				halign='left',
				font_size="14sp")
			# total expenses button
			formatted = "{:,.2f}".format(-total_non_current_liabilities)
			total_exp_button = MDFlatButton(
				text=f"{formatted}\n-----------------------",
				size_hint=(1,None),
				halign='left',
				theme_text_color="Custom",
				text_color=color,
				font_size="14sp")
			# create buttons
			self.accounts_column.add_widget(exp_button)
			self.amounts_column.add_widget(total_exp_button)
			
			
			# current liabilities
			# lazy to change button names
			# current liabilities label
			account_button = MDFlatButton(
				text='Current Liabilities',
				size_hint=(1,None),
				halign='left',
				theme_text_color="Custom",
				text_color=color,
				font_size="14sp")
			# pass button
			amount_button = MDFlatButton(
				text='   ',
				size_hint=(1,None),
				halign='left',
				font_size="14sp")
			# create buttons
			self.accounts_column.add_widget(account_button)
			self.amounts_column.add_widget(amount_button)
			
			category_accounts = financial_data['Current Liabilities']
			total_current_liabilities = []
			for account_name,account_data in category_accounts.items():
				account_total = income_statement_deractives(financial_data, 'Current Liabilities', str(account_name), start_date, end_date)
				total_current_liabilities.append(account_total)
				if account_total == 0:
					pass
				else:
					# accounts button
					account_button = MDFlatButton(
						text=str(account_name),
						on_press=self.on_press_current_liabilities_button,
						size_hint=(1,None),
						halign='left',
						font_size="14sp")
					# amounts button
					formatted = "{:,.2f}".format(-account_total)
					amount_button = MDFlatButton(
						text=formatted,
						size_hint=(1,None),
						halign='left',
						font_size="14sp")
					# create buttons
					self.accounts_column.add_widget(account_button)
					self.amounts_column.add_widget(amount_button)
					
			# total non current liabilities
			total_current_liabilities = sum(total_current_liabilities)
			# note,, found it lazy to rename liabilities buttons
			# non current liabilities text
			exp_button = MDFlatButton(
				text='Total Current Liabilities\n',
				size_hint=(1,None),
				theme_text_color="Custom",
				text_color=color,
				halign='left',
				font_size="14sp")
			# total expenses button
			formatted = "{:,.2f}".format(-total_current_liabilities)
			total_exp_button = MDFlatButton(
				text=f"{formatted}\n-----------------------",
				size_hint=(1,None),
				halign='left',
				theme_text_color="Custom",
				text_color=color,
				font_size="14sp")
			# create buttons
			self.accounts_column.add_widget(exp_button)
			self.amounts_column.add_widget(total_exp_button)
			
			# total non current and current liabilities
			total_current_and_non_liabilities = total_non_current_liabilities + total_current_liabilities
			# note,, found it lazy to rename liabilities buttons
			# non current liabilities text
			exp_button = MDFlatButton(
				text='Total Liabilities\n',
				size_hint=(1,None),
				theme_text_color="Custom",
				text_color=color,
				halign='left',
				font_size="14sp")
			# total expenses button
			formatted = "{:,.2f}".format(-total_current_and_non_liabilities)
			total_exp_button = MDFlatButton(
				text=f"{formatted}\n-----------------------",
				size_hint=(1,None),
				halign='left',
				theme_text_color="Custom",
				text_color=color,
				font_size="14sp")
			# create buttons
			self.accounts_column.add_widget(exp_button)
			self.amounts_column.add_widget(total_exp_button)
			
			# total capital and liabilities
			# sum total all 
			total_capital_and_liabilites =  total_non_current_liabilities + total_current_liabilities + total_capital
			op_income_button = MDFlatButton(
				text='Total Capital and Liabilities',
				size_hint=(1,None),
				halign='left',
				md_bg_color=app.theme_cls.primary_color,
				theme_text_color="Custom",
				text_color=icon_color,
				font_size="14sp")
			# button
			formatted = "{:,.2f}".format(-total_capital_and_liabilites)
			op_income_amount_button = MDFlatButton(
				text=formatted,
				size_hint=(1,None),
				halign='left',
				md_bg_color=app.theme_cls.primary_color,
				theme_text_color="Custom",
				text_color=icon_color,
				font_size="14sp")
			# create buttons
			self.accounts_column.add_widget(op_income_button)
			self.amounts_column.add_widget(op_income_amount_button)
			toast("Balance sheet built")
		else:
			self.loading_popup.dismiss()
			self.error.text = 'Error in dates selection, please check again'
			self.to_normal()
			
			
'''
the trial balance
'''


class TrialBalance(Screen):
	def __init__(self, **kwargs):
		super(TrialBalance, self).__init__(**kwargs)
		Window.softinput_mode = 'below_target'
		
	def get_help(self):
		global ask_for_help
		ask_for_help = str(SimploStatsHelp().get_help('trial_balance'))
		popup = HelpPopup()
		popup.title = 'Trial Balance'
		popup.open()
		
	def export_selected_trial_balance_to_csv(self, end_date):
		year_end = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
		if len(end_date) == 10 and end_date[0] in year_end and end_date[-1] in year_end:
			self.error.text = export_trial_balance(end_date)
		else:
			self.error.text = 'Error in dates selection, please check again'
			self.to_normal()
			toast("Date required")
		
	def export_displayed_as_pdf(self, end_date):
		year_end = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
		if len(end_date) == 10 and end_date[0] in year_end and end_date[-1] in year_end:
			try:
				download_path = financial_data['other_information']['storage_folder']
						
				now = datetime.now()
				current_year = now.strftime("%d%m%Y")
						
				file_name = f"trial balance ssdata{current_year}.png"
				screenshot_filename = os.path.join(download_path, file_name)
				
				self.exportation_layout.export_to_png(screenshot_filename)
				self.error.text = f'Screenshot saved to {download_path}'
				toast("Screenshot saved to storage path")
			except:
				toast("Screenshot error")
				self.error.text = 'Error in saving screenshot'
					
		else:
			self.error.text = 'Error in dates selection, please check again'
			self.to_normal()
			toast("Date required")
		
	def go_back(self):
		self.manager.current = 'home'
		
	def to_normal(self):
		def normal(*args):
			self.error.text = 'All fields are required'
			
		Clock.schedule_once(normal, 3)
		
	def select_date(self, date_field):
		global on_date_field
		on_date_field = date_field
		popup = DatesPopup()
		popup.open()
	
	def on_text_show_date(self, function):
		if function == 'Past week transactions' or function == 'Past month transactions'or function == 'Past 90 days transactions' or function == 'As at date':
			today = datetime.now()
			date_days_ago = today
			date_format = "%d-%m-%Y"
			self.end_date.text = date_days_ago.strftime(date_format)
			
			self.show_loading_popup(self.end_date.text)
		else:
			pass
		
	def on_press_trial_balance(self, details, *args):			
		view_records = self.manager.get_screen('view_accounts')
		details = details.split('|')
		view_records.start_date.text = details[2]
		view_records.end_date.text = details[3]
		view_records.account_category.text = details[0]
		view_records.account_name.text = details[1]
		self.manager.current = 'view_accounts'
		
	def identify_positives(self, category):
		positives = {'Non Current Assets', 'Current Assets', 'Operating Expenses', 'Other Expenses', 'Bank', 'Taxes', 'Cost of Sales'}
		if category in positives:
			return True
		else:
			return False
		
	def show_loading_popup(self, end_date):
		self.loading_popup = LoadingPopup(title='Loading...')
		self.loading_popup.open()
		
		partial_func = partial(self.generate_the_trial_balance, end_date)
		Clock.schedule_once(partial_func, 0.2)
		
		
	def generate_the_trial_balance(self, end_date, *args):
		year_end = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
		if len(end_date) == 10 and end_date[0] in year_end and end_date[-1] in year_end:
			self.loading_popup.dismiss()
			what = self.trial_what_balance.text
			accounts_to_view = self.ids.accounts_to_view.text
			
			if what == 'As at date':
				start_date = str(financial_data['other_information']['start_date'])
			elif what == 'Date`s transactions':
				start_date = end_date
			elif what == 'Reset':
				toast('please select an option')
				return
			elif what == 'Past week transactions':
				try:
					today = datetime.strptime(end_date, "%d-%m-%Y")
					#today = datetime.now()
					date_days_ago = today - timedelta(days=7)
					date_format = "%d-%m-%Y"
					start_date = date_days_ago.strftime(date_format)
				except:
					start_date = end_date
			elif what == 'Past month transactions':
				try:
					today = datetime.strptime(end_date, "%d-%m-%Y")
					#today = datetime.now()
					date_days_ago = today - timedelta(days=30)
					date_format = "%d-%m-%Y"
					start_date = date_days_ago.strftime(date_format)
				except:
					start_date = end_date
			elif what == 'Past 90 days transactions':
				try:
					today = datetime.strptime(end_date, "%d-%m-%Y")
					#today = datetime.now()
					date_days_ago = today - timedelta(days=90)
					date_format = "%d-%m-%Y"
					start_date = date_days_ago.strftime(date_format)
				except:
					start_date = end_date
				
			# clear widgets
			self.accounts_debit.clear_widgets()
			self.amounts_debit.clear_widgets()
			app = App.get_running_app()
			color = app.return_theme_color()
			icon_color = app.return_icon_color()
			# debit balances
			
			if accounts_to_view == 'All Accounts':
				debit_categories = ['Non Current Assets', 'Current Assets', 'Operating Expenses', 'Other Expenses', 'Bank', 'Taxes', 'Cost of Sales']
				total_of_what = 'Total Debit'
			elif accounts_to_view == 'Expenses and Incomes':
				debit_categories = ['Operating Expenses', 'Other Expenses', 'Taxes', 'Cost of Sales']
				total_of_what = 'Total Debit'
			elif accounts_to_view == 'Sales and COS':
				debit_categories = ['Cost of Sales']
				total_of_what = 'Total Debit'
			else:
				debit_categories = [accounts_to_view]
				total_of_what = f'Total {accounts_to_view}'
			
			total_debit_side = []
			is_positive = True
			for category in debit_categories:
				if category in financial_data and category != "other_information":
					category_data = financial_data[category]
					for account_name, account_data in category_data.items():
						if account_name != "transactions":
							account_total = trial_balance_deractives(category, account_data, start_date, end_date)
							total_debit_side.append(account_total)
							if account_total == 0:
								pass
								is_positive = True
							else:
								# accounts button
								account_button = MDFlatButton(
									text=str(account_name),
									size_hint=(1,None),
									font_size='14sp',
									halign='left')
								info = f"{category}|{account_name}|{start_date}|{end_date}"
								account_button.bind(on_press=partial(self.on_press_trial_balance, info))
								# amounts button
								
								if self.identify_positives(category):
									formatted = "{:,.2f}".format(account_total)
									is_positive = True
								else:
									formatted = "{:,.2f}".format(-account_total)
									is_positive = False
									
								amount_button = MDFlatButton(
									text=formatted,
									text_color='blue',
									size_hint=(1,None),
									font_size='14sp',
									halign='left')
								# create buttons
								self.accounts_debit.add_widget(account_button)
								self.amounts_debit.add_widget(amount_button)
								
			# total assets
			# sum total assests 
			total_debit_side =  sum(total_debit_side)
			op_income_button = MDFlatButton(
				text=total_of_what,
				size_hint=(1,None),
				md_bg_color=app.theme_cls.primary_color,
				theme_text_color="Custom",
				text_color=icon_color,
				font_size='14sp',
				halign='left')
				
			# button
			if is_positive == True:
				formatted = "{:,.2f}".format(total_debit_side)
			else:
				formatted = "{:,.2f}".format(-total_debit_side)
				
			op_income_amount_button = MDFlatButton(
				text=formatted,
				size_hint=(1,None),
				md_bg_color=app.theme_cls.primary_color,
				theme_text_color="Custom",
				text_color=icon_color,
				font_size='14sp',
				halign='left')
			# create buttons
			self.accounts_debit.add_widget(op_income_button)
			self.amounts_debit.add_widget(op_income_amount_button)
			
			# return if not needed
			if accounts_to_view == 'Expenses and Incomes' or accounts_to_view == 'All Accounts' or accounts_to_view == 'Sales and COS':
				pass
			else:
				toast("Balances loaded")
				return
			
			account_button = MDFlatButton(
				text='Credit balances',
				size_hint=(1,None),
				font_size="16sp",
				theme_text_color="Custom",
				text_color=color,
				halign='left')
			# pass button
			amount_button = MDFlatButton(
				text='   ',
				size_hint=(1,None),
				font_size="16sp",
				halign='left')
			# create buttons
			self.accounts_debit.add_widget(account_button)
			self.amounts_debit.add_widget(amount_button)
			
			if accounts_to_view == 'All Accounts':
				credit_categories = ['Capital', 'Non Current Liabilities', 'Current Liabilities', 'Other Incomes', 'Operating Revenue']
			elif accounts_to_view == 'Expenses and Incomes':
				credit_categories = ['Other Incomes', 'Operating Revenue']
			elif accounts_to_view == 'Sales and COS':
				credit_categories = ['Operating Revenue']
				
			total_credit_side = []
			for category in credit_categories:
				if category in financial_data and category != "other_information":
					category_data = financial_data[category]
					for account_name, account_data in category_data.items():
						if account_name != "transactions":
							account_total = trial_balance_deractives(category, account_data, start_date, end_date)
							total_credit_side.append(account_total)
							if account_total == 0:
								pass
							else:
								# accounts button
								account_button = MDFlatButton(
									text=str(account_name),
									size_hint=(1,None),
									font_size="14sp",
									halign='left')
								# amounts button
								info = f"{category}|{account_name}|{start_date}|{end_date}"
								account_button.bind(on_press=partial(self.on_press_trial_balance, info))
								formatted = "{:,.2f}".format(-account_total)
								amount_button = MDFlatButton(
									text=formatted,
									text_color='blue',
									size_hint=(1,None),
									font_size="14sp",
									halign='left')
								# create buttons
								self.accounts_debit.add_widget(account_button)
								self.amounts_debit.add_widget(amount_button)
								
			# total assets
			# sum total assests 
			total_credit_side =  sum(total_credit_side)
			op_income_button = MDFlatButton(
				text='Total Credit',
				size_hint=(1,None),
				md_bg_color=app.theme_cls.primary_color,
				theme_text_color="Custom",
				text_color=icon_color,
				font_size="14sp",
				halign='left')
			# button
			formatted = "{:,.2f}".format(-total_credit_side)
			op_income_amount_button = MDFlatButton(
				text=formatted,
				size_hint=(1,None),
				md_bg_color=app.theme_cls.primary_color,
				theme_text_color="Custom",
				text_color=icon_color,
				font_size="14sp",
				halign='left')
			# create buttons
			self.accounts_debit.add_widget(op_income_button)
			self.amounts_debit.add_widget(op_income_amount_button)	
			toast("Trial Balance built")				
		else:
			self.loading_popup.dismiss()
			self.error.text = 'Error in dates selection, please check again'
			self.to_normal()
			
			
'''
operation analysis
'''


class OperationAnalysis(Screen):
	def __init__(self, **kwargs):
		super(OperationAnalysis, self).__init__(**kwargs)
		Window.softinput_mode = 'below_target'
		
	def go_back(self):
		self.manager.current = 'home'
		
	def get_help(self):
		global ask_for_help
		ask_for_help = str(SimploStatsHelp().get_help('operations'))
		popup = HelpPopup()
		popup.title = 'Periodic Comparison'
		popup.open()
		
	def to_normal(self):
		def normal(*args):
			self.error.text = 'All fields are required'
			
		Clock.schedule_once(normal, 3)
		
	def select_date(self, date_field):
		global on_date_field
		on_date_field = date_field
		popup = DatesPopup()
		popup.open()
		
	def on_press_trial_balance(self, details, *args):			
		view_records = self.manager.get_screen('view_accounts')
		details = details.split('|')
		view_records.start_date.text = details[2]
		view_records.end_date.text = details[3]
		view_records.account_category.text = details[0]
		view_records.account_name.text = details[1]
		self.manager.current = 'view_accounts'
		
	def export_displayed_as_pdf(self, start_date_1, end_date_1, start_date_2, end_date_2):
		if len(start_date_1) == 10 and len(end_date_1) == 10 and len(start_date_2) == 10 and len(end_date_2) == 10:
			try:
				download_path = financial_data['other_information']['storage_folder']
						
				now = datetime.now()
				current_year = now.strftime("%d%m%Y")
						
				file_name = f"ssdata operation analysis{current_year}.png"
				screenshot_filename = os.path.join(download_path, file_name)
				
				self.exportation_layout.export_to_png(screenshot_filename)
				self.error.text = f'Screenshot saved to {download_path}'
				toast("Screenshot saved to storage path")
			except:
				toast("Screenshot error")
				self.error.text = 'Error in saving screenshot'
					
		else:
			self.error.text = 'Error in dates selection, please check again'
			self.to_normal()
			toast("Date required")
		
	def show_loading_popup(self, compared_accounts, start_date_1, end_date_1, start_date_2, end_date_2):
		self.loading_popup = LoadingPopup(title='Loading...')
		self.loading_popup.open()
		
		if len(start_date_1) == 10 and len(end_date_1) == 10 and len(start_date_2) == 10 and len(end_date_2) == 10:
			partial_func = partial(self.build_the_comparison_interface, compared_accounts, start_date_1, end_date_1, start_date_2, end_date_2)
			Clock.schedule_once(partial_func, 0.2)
		else:
			self.loading_popup.dismiss()
			self.error.text = 'ensure all group dates are correctly selected'
			self.to_normal()
			toast('some dates are not selected')
		
	def build_the_comparison_interface(self, compared_accounts, start_date_1, end_date_1, start_date_2, end_date_2, *args):
		self.loading_popup.dismiss()
		
		accounts_column = self.ids.accounts_column
		group_one = self.ids.group_one
		group_two = self.ids.group_two
		variance_column = self.ids.variance_column
		fnt = f"{self.the_font_size.text}sp"
		press_option = self.ids.press_option.text
		variance_option = self.ids.variance_option.text
		
		accounts_column.clear_widgets()
		group_one.clear_widgets()
		group_two.clear_widgets()
		variance_column.clear_widgets()
		
		app = App.get_running_app()
		icon_color = app.return_icon_color()
		
		positive_bal = {'Non Current Assets', 'Current Assets', 'Operating Expenses', 'Other Expenses', 'Bank', 'Taxes', 'Cost of Sales'}
		negative_bal = {'Capital', 'Non Current Liabilities', 'Current Liabilities', 'Other Incomes', 'Operating Revenue'}
		
		if compared_accounts == 'Expenses and Incomes':
			debit_categories = ['Operating Expenses', 'Other Expenses', 'Taxes', 'Other Incomes', 'Operating Revenue']
		else:
			debit_categories = [compared_accounts]
			
			
		grand_total_1 = []
		grand_total_2 = []
		
		for category in debit_categories:
			category_data = financial_data[category]
			for account_name, account_data in category_data.items():
				if account_name != "transactions":
					if str(category) in positive_bal:
						group_1_total = trial_balance_deractives(category, account_data, start_date_1, end_date_1)
						group_2_total = trial_balance_deractives(category, account_data, start_date_2, end_date_2)
						formatted_group_1 = "{:,.2f}".format(group_1_total)
						formatted_group_2 = "{:,.2f}".format(group_2_total)
						grand_total_1.append(group_1_total)
						grand_total_2.append(group_2_total)
						
						variance_amount = group_2_total - group_1_total
						variance_rounded = round(variance_amount, 2)
						formatted_variances = "{:,.2f}".format(variance_rounded)
						if variance_amount < 0:
							text_color = 'green'
							icon = 'arrow-down'
						else:
							text_color = 'red'
							icon = 'arrow-up'
						
						try:
							proportion = (variance_amount/group_1_total) * 100
							variance_rate = f"{round(proportion, 2)} %"
						except:
							icon = 'cancel'
							variance_rate = '0 %'
					else:
						group_1_total = trial_balance_deractives(category, account_data, start_date_1, end_date_1)
						group_2_total = trial_balance_deractives(category, account_data, start_date_2, end_date_2)
						formatted_group_1 = "{:,.2f}".format(-group_1_total)
						formatted_group_2 = "{:,.2f}".format(-group_2_total)
						# to get net profit
						grand_total_1.append(group_1_total)
						grand_total_2.append(group_2_total)
						
						variance_amount = group_2_total - group_1_total
						variance_rounded = round(-variance_amount, 2)
						formatted_variances = "{:,.2f}".format(variance_rounded)
						if variance_amount < 0:
							text_color = 'green'
							icon = 'arrow-up'
						else:
							text_color = 'red'
							icon = 'arrow-down'
						
						try:
							proportion = (variance_amount/group_1_total) * 100
							variance_rate = f"{round(proportion, 2)} %"
						except:
							icon = 'cancel'
							variance_rate = '0 %'
					
					# normal indent		
					if press_option == 'group 1':
						info = f"{category}|{account_name}|{start_date_1}|{end_date_1}"
					else:
						info = f"{category}|{account_name}|{start_date_2}|{end_date_2}"
							
					account_button = MDFlatButton(
						text=str(account_name),
						size_hint=(1,None),
						font_size=fnt,
						halign='left')
					account_button.bind(on_press=partial(self.on_press_trial_balance, info))
								
					group_one_button = MDFlatButton(
						text=formatted_group_1,
						size_hint=(1,None),
						font_size=fnt,
						halign='left')
								
					group_two_button = MDFlatButton(
						text=formatted_group_2,
						size_hint=(1,None),
						font_size=fnt,
						halign='left')
						
					if variance_option == 'variance rate':
						option = variance_rate
						variance_button = MDRectangleFlatIconButton(
							icon=icon,
							text=option,
							size_hint=(1,None),
							font_size=fnt,
							theme_text_color="Custom",
							md_bg_color=(255,255,255,0),
							text_color=text_color,
							halign='left')
					else:
						option = formatted_variances
						variance_button = MDFlatButton(
							text=option,
							size_hint=(1,None),
							font_size=fnt,
							theme_text_color="Custom",
							text_color=text_color,
							halign='left')
							
					accounts_column.add_widget(account_button)
					group_one.add_widget(group_one_button)
					group_two.add_widget(group_two_button)
					variance_column.add_widget(variance_button)
					
		grand_total_1 = sum(grand_total_1)
		grand_total_2 = sum(grand_total_2)
		total_1 = "{:,.2f}".format(-grand_total_1)
		total_2 = "{:,.2f}".format(-grand_total_2)
		
		total_label = MDFlatButton(
			text='Total',
			size_hint=(1,None),
			font_size=fnt,
			theme_text_color="Custom",
			md_bg_color=app.theme_cls.primary_color,
			text_color=icon_color,
			halign='left')
		
		grand_one_total = MDFlatButton(
			text=total_1,
			size_hint=(1,None),
			font_size=fnt,
			theme_text_color="Custom",
			md_bg_color=app.theme_cls.primary_color,
			text_color=icon_color,
			halign='left')
		
		grand_two_total = MDFlatButton(
			text=total_2,
			size_hint=(1,None),
			font_size=fnt,
			theme_text_color="Custom",
			md_bg_color=app.theme_cls.primary_color,
			text_color=icon_color,
			halign='left')
			
		sep_button = MDFlatButton(
			text=' ',
			size_hint=(1,None),
			font_size=fnt,
			halign='left')
			
		accounts_column.add_widget(total_label)
		group_one.add_widget(grand_one_total)
		group_two.add_widget(grand_two_total)
		variance_column.add_widget(sep_button)
		toast('data loaded')
								
			
			
'''
financial analysis
'''


class FinancialAnalysis(Screen):
	def __init__(self, **kwargs):
		super(FinancialAnalysis, self).__init__(**kwargs)
		Window.softinput_mode = 'below_target'
		
	def go_back(self):
		self.manager.current = 'home'
		
	def to_normal(self):
		def normal(*args):
			self.error.text = 'All fields are required'
			
		Clock.schedule_once(normal, 3)
		
	def select_date(self, date_field):
		global on_date_field
		on_date_field = date_field
		popup = DatesPopup()
		popup.open()
		
	def calculate_depreciation(self, cost_of_asset, rate_of_dep, econ_life, depreciation_base, residue):
		if depreciation_base == 'straight line':
			if cost_of_asset == '' or econ_life == '':
				self.error.text = 'Some figures should be entered'
				self.to_normal()
			else:
				if residue != '':
					dep = (float(cost_of_asset) - float(residue)) / float(econ_life)
					dep = round(dep, 2)
					dep = "{:,.2f}".format(dep)
					self.solution.text = f'Answer: {dep} (where residue)'
					self.error.text = f'Answer: {dep}'
				
			if rate_of_dep != '' and residue != '':
				dep = (float(rate_of_dep)/100) * float(cost_of_asset)
				dep = round(dep, 2)
				dep = "{:,.2f}".format(dep)
				previous = self.solution.text
				self.solution.text = ''
				self.solution.text = f'{previous} or {dep} at {rate_of_dep}%'
			elif rate_of_dep != '' and residue == '':
				dep = (float(rate_of_dep)/100) * float(cost_of_asset)
				dep = round(dep, 2)
				dep = "{:,.2f}".format(dep)
				self.solution.text = f'Answer: {dep} at {rate_of_dep}%'
		else:
			self.solution.text = 'The reducing balance method calculates depreciation based on a fixed rate applied to the asset`s book value (Cost minus Accumulated Depreciation) at the beginning of each period.'
		
	def see_payable_tax_hint(self, rate):
		if rate != '':
			start_date = str(financial_data['other_information']['start_date'])
			end_date = str(financial_data['other_information']['end_date'])
			income = generate_total_income_without_taxes(start_date, end_date)
			tax = (float(rate)/100) * income
			tax = round(tax, 2)
			formatted = "{:,.2f}".format(-tax)
			self.error.text = f'The taxable income is {-income}\nA tax of {formatted} should be paid at {self.tax_rate.text} %'
			
		else:
			self.error.text = 'Enter a tax rate first in %'
			self.to_normal()
		
	def more_on_ratios_online(self):
		web_link = 'https://corporatefinanceinstitute.com/resources/accounting/financial-ratios/'
		webbrowser.open(web_link)
	
	def calculate_ratios_by_date(self, end_date):
		year_end = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
		if len(end_date) == 10 and end_date[0] in year_end and end_date[-1] in year_end:
			start_date = str(financial_data['other_information']['start_date'])	
			margin = generate_the_financial_ratios(start_date, end_date, 'net_profit_margin')
			self.net_proft_margin.text = margin
			roa = generate_the_financial_ratios(start_date, end_date, 'return_on_assets')
			self.return_on_assets.text = roa
			current_r = generate_the_financial_ratios(start_date, end_date, 'current_ratio')
			self.current_ratio.text = current_r
		else:
			self.error.text = 'Error in dates selection, please check again'
			self.to_normal()
			toast("Date required")
			
	def get_random_color(self):
		return random.random(), random.random(), random.random()
						
	def draw_pie_chart(self,start_date, end_date, scatter, splitted):
		scatter.clear_widgets()
		total_expenses = 0
		expense_categories = {}
		
		debit_categories = [splitted]
		for category in debit_categories:
			if category in financial_data and category != "other_information":
				category_data = financial_data[category]
				for account_name, account_data in category_data.items():
					if account_name != "transactions":
						account_total = trial_balance_deractives(category, account_data, start_date, end_date)
						if account_total == 0:
							pass
						else:
							total_expenses += account_total
							expense_categories[str(account_name)] = account_total
		
		# formulate definite colors
		list_of_colors = []
		random_colors = [self.get_random_color() for _ in range(len(expense_categories))]
		list_of_colors += random_colors
		
		# draw pie chart
		angle_start = 0
		
		sorted_categories = sorted(expense_categories.items(), key=lambda x: x[1], reverse=True)
		for account, amount in sorted_categories:
			angle_end = angle_start + 360 * amount / total_expenses
			
			# Set a random color for each category
			account_color = random_colors.pop()
			with scatter.canvas:
				Color(*account_color)
				Ellipse(
					#pos=scatter.center,
					pos_hint={'center_x': 0.5, 'center_y': 0.5},
					size=(dp(200), dp(200)),
					angle_start=angle_start,
					angle_end=angle_end
				)
			
			# Update the starting angle for the next category
			angle_start = angle_end
			
		# Display a key with category names
		self.ids.key_label.text = self.get_key_text_with_color(expense_categories, list_of_colors, total_expenses)
		
	def get_key_text_with_color(self, expense_categories, list_of_colors, total_expenses):
		# Generate a key with category names, colors, and amounts
		key_text = ""
		
		sorted_categories = sorted(expense_categories.items(), key=lambda x: x[1], reverse=True)
		
		for category, amount in sorted_categories:
			category_color = list_of_colors.pop()
			formatted = "{:,.2f}".format(amount)
			key_text += f"[color={self.rgb_to_hex(*category_color)}]{category}[/color]: {formatted}\n\n"
		
		formatted = "{:,.2f}".format(total_expenses)	
		key_text += f"**Grand Total:** {formatted}\n____________"
			
		return key_text

	def rgb_to_hex(self, r, g, b):
		# Convert RGB values to hexadecimal color code
		return "#{:02x}{:02x}{:02x}".format(int(r * 255), int(g * 255), int(b * 255))
		
		
		
class DollarSignWidget(Widget):
	def __init__(self, **kwargs):
		super(DollarSignWidget, self).__init__(**kwargs)
		with self.canvas:
			Color(0.2, 0.2, 0.2)  # Dark gray color
			Line(width=2, points=[50, 250, 80, 200, 110, 250, 80, 300, 50, 250, 110, 250])

			
			
'''
ask for password if any
'''	
'''
log in
'''
class LogInPage(Screen):
	def __init__(self, **kwargs):
		super(LogInPage, self).__init__(**kwargs)
		self.popup = Popup(
			title='LogIn',
			size_hint= (0.6,0.1)
		)
		self.boxlayout = BoxLayout(orientation='vertical')
		self.password_key = TextInput(
			hint_text='Enter password',
			size_hint=(1,None),
			multiline=False,
			font_size='18sp',
			password=True
		)
		self.password_key.bind(on_text_validate=self.allow_user)
		self.boxlayout.add_widget(self.password_key)
		self.popup.add_widget(self.boxlayout)
		
		Clock.schedule_once(self.show_slide_show, 2)
		
	def back_up_or_exit(self):
		popup = BackUpDataOrExit()
		popup.open()
		
	def show_user_picture(self):
		return display_profile_picture()
		
	def full_image_view(self, source):
		popup = Popup(title='Profile Picture',
			size_hint=(1,1),
			auto_dismiss=True)
		profile_photo = Image(source=source,
			size_hint=(1,1))
			
		popup.add_widget(profile_photo)
		popup.open()
		
	def open_about_popup(self, *args):
		popup = AboutsAndLegality()
		popup.open()
		
	def welcome_message(self):
		if financial_data['other_information']['app_key'] == "ddjfj-d5i463iwourjd_rj0p4dkkkru-d43mhaphjfjj":
			return "Welcome! create an account to access valuable book keeping"
		else:
			name = financial_data['other_information']['business name']
			return f"Nice to see you back, {name}!"
		
	def show_slide_show(self, *args):
		texts = {'Welcome to SimploStats App', 'Add charts of accounts that suit your business needs and requirements', 'Make journal entries simply in a guided user interface', 'Organize your financial records and access information in a click', 'View financial statements and ledger accounts records between selected date frames', 'Set budget amounts to accounts and track variances over time', 'Make informed decision on your business based on the financial data available', 'Accounting made easy as 123...', 'Please give us a 5 star review in Google PlayStore', 'Our app can be used by businesses and users from all sectors'}
		
		rn = random.choice(list(texts))
		self.text_to_type = rn
		self.slide_show.text = ''
		home = self.manager.get_screen('home')
		
		def type_letter(*args):
			if self.text_to_type:
				self.slide_show.text += self.text_to_type[0]
				self.text_to_type = self.text_to_type[1:]
			else:
				Clock.unschedule(type_letter)
				Clock.schedule_once(self.show_slide_show, 2)
				
		Clock.schedule_interval(type_letter, 0.03)
		
	def allow_user(self, instance):
		start_date = financial_data['other_information']['start_date']
		end_date = financial_data['other_information']['end_date']
		
		other_key = f'{start_date},{end_date}'
		password = str(financial_data['other_information']['pass_word'])
		if password == instance.text or instance.text == other_key:
			if financial_data['other_information']['user_agreement'] == 'False':
				self.manager.current = 'help'
				toast("please first agree with our services before using the app")
				self.request_permission()
			else:
				self.popup.dismiss()
				instance.text = ''
				home = self.manager.get_screen('home')
				home.business.text = self.return_business_details()
				generate_the_dashboard_items(home.dashboard,home.expenses,home.incomes,home.net_profit,home.bank)
				show_the_last_printed()
				self.manager.current = 'home'
				self.request_permission()
		else:
			toast('Wrong Password, enter special combo instead')
		
	def continue_to_business_records(self):
		try:
			if financial_data['other_information']['app_key'] == app_key:
				account = self.manager.get_screen('account')
				account.storage_folder.text = financial_data['other_information']['storage_folder']
				account.start_date.text = ''
				account.end_date.text = ''
				account.business_address.text = ''
				account.business_email.text = ''
				account.business_name.text = ''
				account.theme.text = "Indigo"
				account.ids.app_transition.text = 'FadeTransition'
				
				self.manager.current = 'account'
				show_the_last_printed()
				self.request_permission()
				account.image.source = display_profile_picture()
				account.photo_path.text = str(display_profile_picture())
				home = self.manager.get_screen('home')
				home.image.source = display_profile_picture()
			else:
				if financial_data['other_information']['pass_word_protected'] == 'False':
					if financial_data['other_information']['user_agreement'] == 'False':
						self.manager.current = 'help'
						toast("please first agree with our services before using the app")
						show_the_last_printed()
						self.request_permission()
					else:
						home = self.manager.get_screen('home')
						home.business.text = self.return_business_details()
						generate_the_dashboard_items(home.dashboard,home.expenses,home.incomes,home.net_profit,home.bank)
						show_the_last_printed()
						self.manager.current = 'home'
						self.request_permission()
				else:
					self.popup.open()
		except:
			pass
				
				
	def return_business_details(self):
		name = financial_data['other_information']['business name']
		email = financial_data['other_information']['business email']
		start = financial_data['other_information']['start_date']
		end = financial_data['other_information']['end_date']
		return f"{name}\n{email}\nFrom:  {start} To:  {end}"
		
	def request_permission(self, *args):
		PythonActivity = autoclass('org.kivy.android.PythonActivity')
		package_context = PythonActivity.mActivity.getApplicationContext()
		permission = 'android.permission.READ_EXTERNAL_STORAGE'
		has_permission = package_context.checkCallingOrSelfPermission(permission)
		
		if has_permission == -1:
			package_context.requestPermissions([permission], 1)
		else:
			storage_path = storagepath.get_external_storage_dir()
			toast('storage permissions granted')
				

'''
help and support
'''

class HelpAndSupport(Screen):
	def __init__(self, **kwargs):
		super(HelpAndSupport, self).__init__(**kwargs)
				
	def select_date(self, date_field):
		global on_date_field
		on_date_field = date_field
		popup = DatesPopup()
		popup.open()
		
	def find_the_help(self, help, title):
		global ask_for_help
		ask_for_help = str(SimploStatsHelp().get_help(help))
		popup = HelpPopup()
		popup.title = title
		popup.open()
		
	def copy_to_clipboard(self, text):
		text_to_copy = text
		try:
			subject = "SimploStats Support"
			body = "I would like to get help about"
			mailto_url = f"mailto:{text_to_copy}?subject={subject}&body={body}"
			webbrowser.open(mailto_url)
			Clipboard.copy(text_to_copy)
			toast("Email copied to clipboard")
		except:
			toast('an error occurred')
		
	def scroll_to_top(self, scroll_view):
		try:
			scroll_view.scroll_y = 1
		except:
			pass
		
	def check_active_status(self, my_checkbox, agree_button):
		if my_checkbox.active:
			#self.request_read_and_write_storage()
			self.agree_and_continue()
		else:
			my_checkbox.active = True
			
	def agree_and_continue(self):
		home = self.manager.get_screen('home')
		home.business.text = self.return_business_details()
		financial_data['other_information']['user_agreement'] = 'True'
		save_data(financial_data)
		toast("agreement saved")
		home = self.manager.get_screen('home')
		generate_the_dashboard_items(home.dashboard,home.expenses,home.incomes,home.net_profit,home.bank)
		self.manager.current = 'home'
		
		
	def return_business_details(self):
		name = financial_data['other_information']['business name']
		email = financial_data['other_information']['business email']
		start = financial_data['other_information']['start_date']
		end = financial_data['other_information']['end_date']
		return f"{name}\n{email}\nFrom:  {start} To:  {end}"
		
	def scroll_to_word(self, help):
		global ask_for_help
		result = SimploStatsHelp().search_for_help(str(help))
		ask_for_help = result
		popup = HelpPopup()
		popup.title = 'SimploStats Help Result'
		popup.open()
		self.ids.search_help.text = ''
	
			
'''
akauntin account
'''


class SimploStatsAccount(Screen):
	def __init__(self, **kwargs):
		super(SimploStatsAccount, self).__init__(**kwargs)
		self.disallowed_chars = ['"', '|', '$', '%']
		self.disallowed_chars_2 = ['"', '|', '$', '%', '.']
		self.file_manager = MDFileManager(
			exit_manager=self.exit_manager,
			select_path=self.select_path
		)
		Window.softinput_mode = 'below_target'
		
	def on_enter(self, *args):
		if 'dark_mode' in financial_data['other_information']:
			mode = financial_data['other_information']['dark_mode']
			if mode == True:
				app = App.get_running_app()
				for child in self.ids.scroll_view.children:
					if isinstance(child, BoxLayout):
						app.traverse_widgets(child)
			else:
				pass
		else:
			pass
		
	def about_storage_folder(self):
		global ask_for_help
		ask_for_help = str(SimploStatsHelp().get_help('storage_folder'))
		popup = HelpPopup()
		popup.title = 'Storage Folder'
		popup.open()
		
	def start_and_ends_dates(self):
		global ask_for_help
		ask_for_help = str(SimploStatsHelp().get_help('start_end_dates'))
		popup = HelpPopup()
		popup.title = 'Financial Year Period'
		popup.open()
		
	def go_back(self):
		self.manager.current = 'log_in'
		
	def exit_manager(self, *args):
		self.file_manager.close()
		
	def set_the_app_theme(self, theme):
		app = App.get_running_app()
		financial_data["other_information"]["app_theme"] = theme
		save_data(financial_data)
		app.theme_cls.primary_palette = theme
		toast("Theme Updated")
		
	def set_the_app_transition(self, app_transition):
		app = App.get_running_app()
		financial_data["other_information"]["app_transition"] = app_transition
		
		if app_transition == 'FadeTransition':
			trans = FadeTransition()
		elif app_transition == 'SlideTransition':
			trans = SlideTransition()
		elif app_transition == 'SwapTransition':
			trans = SwapTransition()
		elif app_transition == 'WipeTransition':
			trans = WipeTransition()
		elif app_transition == 'NoTransition':
			trans = NoTransition()
		else:
			trans = FadeTransition()
			
		app.root.transition = trans
		save_data(financial_data)
		
	def show_file_manager(self):
		self.file_manager.show(path="/storage/emulated/0/")
		
	def select_path(self, path):
		if path.endswith(".png") or path.endswith(".jpg") or path.endswith(".jpeg"):
			self.photo_path.text = str(path)
			financial_data['other_information']['profile_picture'] = f"{path}"
			save_data(financial_data)
			toast('profile updated')
			home = self.manager.get_screen('home')
			home.image.source = display_profile_picture()
			login = self.manager.get_screen('log_in')
			self.ids.image.source = str(path)
			login.image.source = str(path)
			self.file_manager.close()
		else:
			if '.' in str(path):
				toast("Press on bottom-right tick to select folder")
			else:
				self.storage_folder.text =f"{path}/"
				financial_data['other_information']['storage_folder'] = f"{path}/"
				save_data(financial_data)
				self.file_manager.close()
		
	def load_data(self):
		data = {
			"Capital": {},
			"Non Current Assets": {},
			"Current Assets": {},
			"Non Current Liabilities": {},
			"Current Liabilities": {},
			"Other Incomes": {},
			"Operating Expenses": {},
			"Other Expenses": {},
			"Bank": {},
			"Taxes": {},
			"Operating Revenue": {},
			"Cost of Sales": {},
			"other_information": {},
			# Add more main parts as needed
		}
		data['Capital']['Opening Balance Equity'] = {"transactions": []}
		data['other_information']['app_key'] = app_key
		data['other_information']['pass_word_protected'] = 'False'
		data['other_information']['user_agreement'] = 'False'
		data['other_information']['budgeted_accounts'] = {}
		data['other_information']['storage_folder'] = '/storage/emulated/0/Download/'
		data['other_information']['assets_at_cost'] = {}
		data['other_information']['accum_depreciation'] = {}
		data['Operating Expenses']['Depreciation'] = {"transactions": []}
		data['Other Expenses']['Depreciation'] = {"transactions": []}
		data['Capital']['Retained Earnings'] = {"transactions": []}
		data['other_information']['invoices'] = {}
		return data
		
	def reset_the_app(self, pass_key):
		global financial_data
		global fin_data_file
		if financial_data['other_information']['pass_word_protected'] == 'False':
			self.error.text = 'First create a password to reset app'
			self.to_normal()
		else:
			if len(pass_key) < 4:
				self.error.text = 'Enter a longer password to reset app'
				self.to_normal()
			else:
				if financial_data['other_information']['pass_word'] == pass_key:
					reset = self.load_data()
					
					with open(back_to_app_file, "w") as file:
						file.write('')
					file.close()
					with open(back_to_app_file, "w") as file:
						json.dump(reset, file, indent=4)
						
					fin_data_file = back_to_app_file
					financial_data = load_data()
					home = self.manager.get_screen('home')
					home.selected_file.text = 'imported file will show here'
					home.view_status.text = ' '
					home.import_file.text = 'Import file'
					self.start_date.text = ''
					self.end_date.text = ''
					self.business_address.text = ''
					self.business_email.text = ''
					self.business_name.text = ''
					log = self.manager.get_screen('log_in')
					log.welcome_user.text = "Welcome! create an account to access valuable book keeping"
					home = self.manager.get_screen('home')
					home.image.source = display_profile_picture()
					log.image.source = display_profile_picture()
					self.manager.current = 'log_in'
					toast("App set to default")
				else:
					self.error.text = 'Incorrect password, try again'
					self.to_normal()
					toast("Business address for password")
		
	def on_text_account(self, value):
		# Function to filter or prevent certain characters
		characters  = value.text
		filtered_text = ''.join(char for char in characters if char not in self.disallowed_chars)
		value.text = filtered_text
		
	def on_text_account_2(self, value):
		# Filter out special characters
		the_text = value.text
		filtered_value = ''.join(char for char in the_text if char.isalnum() or char.isspace())
        
		# Update the text in the TextInput widget
		value.text = filtered_value
		
	def to_normal(self):
		def normal(*args):
			self.error.text = 'All fields are required'
			
		Clock.schedule_once(normal, 3)
		
	def select_date(self, date_field):
		global on_date_field
		on_date_field = date_field
		popup = DatesPopup()
		popup.open()
		
	def create_business_account(self, name, email, address, start_date, end_date):
		year_end = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
		if len(start_date) == 10 and len(end_date) == 10 and start_date[0] in year_end and start_date[-1] in year_end and end_date[0] in year_end and end_date[-1] in year_end and len(name) > 4:
			financial_data['other_information']['business name'] = name
			financial_data['other_information']['business email'] = email
			financial_data['other_information']['business address'] = address
			financial_data['other_information']['start_date'] = start_date
			financial_data['other_information']['end_date'] = end_date
			financial_data['other_information']['app_key'] = 'account_created'
			save_data(financial_data)
			
			home = self.manager.get_screen('home')
			generate_the_dashboard_items(home.dashboard,home.expenses,home.incomes,home.net_profit,home.bank)
			toast("Business information updated.")
			last_upated_date()
			self.manager.current = 'help'
		else:
			self.error.text = 'Please select correctly the dates for financial year'
			self.to_normal()
			
			
'''
balances analysis
'''


class BalancesAnalysis(Screen):
	def __init__(self, **kwargs):
		super(BalancesAnalysis, self).__init__(**kwargs)
		Window.softinput_mode = 'below_target'
		
	def get_help(self):
		global ask_for_help
		ask_for_help = str(SimploStatsHelp().get_help('balances'))
		popup = HelpPopup()
		popup.title = 'Balances Analysis'
		popup.open()
		
	def go_back(self):
		self.manager.current = 'home'
		
	def clear_display(self):
		app = App.get_running_app()
		
		self.ids.display_panel.clear_widgets()
		
		self.ids.display_panel.add_widget(Button(
		size_hint=(1,None),
		height=1,
		background_color=app.theme_cls.primary_color,
		background_normal=''
		))
		
	def show_date(self):
		now = datetime.now()
		today = now.strftime("%d-%m-%Y")
		return str(today)
		
	def select_date(self, date_field):
		global on_date_field
		on_date_field = date_field
		popup = DatesPopup()
		popup.open()
		
	def to_normal(self):
		def normal(*args):
			self.error.text = 'All fields are required'
			
		Clock.schedule_once(normal, 3)
		
		
	def view_accum_dep(self):
		self.display_panel.clear_widgets()
		category_accounts = list(financial_data['other_information']['accum_depreciation'].keys())
		fnt = f"{self.the_font_size.text}sp"
		
		app = App.get_running_app()
		color = app.return_theme_color()
		
		self.ids.display_panel.add_widget(Button(
		size_hint=(1,None),
		height=1,
		background_color=app.theme_cls.primary_color,
		background_normal=''
		))
		
		for account_name in category_accounts:
			amount = financial_data['other_information']['accum_depreciation'][account_name]
			formatted = "{:,.2f}".format(amount)
			text = f'{account_name} = {formatted}'
			button = MDFlatButton(
				text=text,
				halign='left',
				theme_text_color="Custom",
				text_color=color,
				size_hint=(1,None),
				font_size=fnt)
			# amounts button
			self.display_panel.add_widget(button)
			
	def view_assets_at_costs(self):
		self.display_panel.clear_widgets()
		category_accounts = list(financial_data['other_information']['assets_at_cost'].keys())
		fnt = f"{self.the_font_size.text}sp"
		app = App.get_running_app()
		color = app.return_theme_color()
		
		self.ids.display_panel.add_widget(Button(
		size_hint=(1,None),
		height=1,
		background_color=app.theme_cls.primary_color,
		background_normal=''
		))
		
		for account_name in category_accounts:
			amount = financial_data['other_information']['assets_at_cost'][account_name]
			formatted = "{:,.2f}".format(amount)
			text = f'{account_name} = {formatted}'
			button = MDFlatButton(
				text=text,
				halign='left',
				theme_text_color="Custom",
				text_color=color,
				size_hint=(1,None),
				font_size=fnt)
			# amounts button
			self.display_panel.add_widget(button)
		
	def update_lists_of_account(self, category):
		self.account_name.values = view_accounts(financial_data, category)
		self.account_name.text = 'Choose Account'
		
	def on_press_balance_button(self, instance):
		global from_view_records_to_home
		info = instance.text
		info = info.split('|')
		
		start_date = str(financial_data['other_information']['start_date'])
		end_date = info[0]
		category = info[2]
		account_name = info[3]
		
		view_records = self.manager.get_screen('view_accounts')
		view_records.start_date.text = start_date
		view_records.end_date.text = end_date
		view_records.account_category.text = category
		view_records.account_name.text = account_name
		self.manager.current = 'view_accounts'
		from_view_records_to_home = True
		
	def find_account_balance(self, days_ago, category, account_name):
		if account_name == 'Choose Account':
			self.error.text = 'Please select an Account'
			self.to_normal()
			toast("Account required")
		else:
			if days_ago == '':
				self.error.text = 'Please enter number of days'
				self.to_normal()
			else:
				start_date = str(financial_data['other_information']['start_date'])
				
				today = datetime.strptime(self.is_today.text, "%d-%m-%Y")
				
				date_days_ago = today - timedelta(days=int(days_ago))
				date_format = "%d-%m-%Y"
				end_date = date_days_ago.strftime(date_format)
			
				account_total = income_statement_deractives(financial_data, category, account_name, start_date, end_date)
				fnt = f"{self.the_font_size.text}sp"
				if category == 'Current Assets' or category == 'Non Current Assets' or category == 'Expenses' or category == 'Bank':
					formatted = "{:,.2f}".format(account_total)
				else:
					formatted = "{:,.2f}".format(-account_total)
				
				text = f"{end_date}| {days_ago} days ago,\n|{category}|{account_name}| had a balance of {formatted}"
				app = App.get_running_app()
				color = app.return_theme_color()
		
				button = MDFlatButton(
					text=text,
					halign='left',
					theme_text_color="Custom",
					text_color=color,
					on_press=self.on_press_balance_button,
					size_hint=(1,None),
					font_size=fnt)
				# amounts button
				self.display_panel.add_widget(button)
				
				
'''
budget mode
'''


class BudgetScreen(Screen):
	def __init__(self, **kwargs):
		super(BudgetScreen, self).__init__(**kwargs)
		Window.softinput_mode = 'below_target'
		
	def go_back(self):
		self.manager.current = 'home'
		
	def get_help(self):
		global ask_for_help
		ask_for_help = str(SimploStatsHelp().get_help('budget'))
		popup = HelpPopup()
		popup.title = 'Budget Analysis'
		popup.open()
		
	def export_the_budget_to_csv(self, start_date, end_date, split_budget, accounts_to_view):
		year_end = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
		if len(end_date) == 10 and len(start_date) == 10 and end_date[0] in year_end and end_date[-1] in year_end:
			self.do_export_the_budget_to_csv(start_date, end_date, split_budget, accounts_to_view)				
		else:
			self.error.text = 'Error in dates selection, please check again'
			self.to_normal()
			toast("Date required")
		
	
	def do_export_the_budget_to_csv(self, start_date, end_date, split_budget, accounts_to_view):
		if split_budget == 'Enter Ratio':
			ratio_1 = self.ids.budget_amount.text
			if ratio_1:
				if float(ratio_1) <= 1 and float(ratio_1) > 0:
					pass
				else:
					toast('a ratio should be between zero and one')
					return
			else:
				toast('please enter a ratio in budget textfield above')
				return
		else:
			pass
		try:
			download_path = financial_data['other_information']['storage_folder']
			name = financial_data['other_information']['business name']
			
			now = datetime.now()
			current_year = now.strftime("%d%m%Y")
			name = financial_data['other_information']['business name']
			file_name = f"budget {split_budget} ssdata{current_year}.csv"
			start_date = start_date
			
			csv_filename = os.path.join(download_path, file_name)
			
			with open(csv_filename, mode='w', newline='') as file:
				writer = csv.writer(file)
				
				writer.writerow([name, ''])
				writer.writerow(['Budget Analysis', ''])
				writer.writerow([split_budget, ''])
				writer.writerow([f"as between {start_date} and {end_date}", ''])
				writer.writerow(['', '', '', ''])
				writer.writerow(["Debit Accounts", 'Amount', 'Budgeted', 'Variance (B)'])
					
				# debit balances
				if accounts_to_view == 'Expenses and Incomes':
					debit_categories = ['Operating Expenses', 'Other Expenses', 'Taxes', 'Cost of Sales']
				elif accounts_to_view == 'All Accounts':
					debit_categories = ['Non Current Assets', 'Current Assets', 'Operating Expenses', 'Other Expenses', 'Bank', 'Taxes', 'Cost of Sales']
				else:
					debit_categories = ['Non Current Assets', 'Current Assets', 'Operating Expenses', 'Other Expenses', 'Bank', 'Taxes', 'Cost of Sales']
				
				total_debit_side = []
				total_budget_debit = []
				total_variance_debit = []
				
				for category in debit_categories:
					if category in financial_data and category != "other_information":
						category_data = financial_data[category]
						for account_name, account_data in category_data.items():
							if account_name != "transactions":
								account_total = trial_balance_deractives(category, account_data, start_date, end_date)
								total_debit_side.append(account_total)
								if account_total == 0:
									pass
								else:
									if split_budget == 'Annually':
										budg = self.get_the_budgeted_amount(f"{category}|{account_name}")
									elif split_budget == 'Semi Annually':
										budg = self.get_the_budgeted_amount(f"{category}|{account_name}") * 0.5
									elif split_budget == 'Quarterly':
										budg = self.get_the_budgeted_amount(f"{category}|{account_name}") * 0.25
									else:
										budg = self.get_the_budgeted_amount(f"{category}|{account_name}") * float(self.ids.budget_amount.text)
									
									total_budget_debit.append(budg)
									variance = budg - account_total
									total_variance_debit.append(variance)
									writer.writerow([account_name, account_total, budg, round(variance, 2)])					
				# total assets
				# sum total assests 
				total_debit_side =  sum(total_debit_side)
				total_budget_debit = sum(total_budget_debit)
				total_variance_debit = sum(total_variance_debit)
				writer.writerow(['', ''])
				writer.writerow(['Debit total', total_debit_side, total_budget_debit, round(total_variance_debit, 2)])
				writer.writerow(['', ''])
				writer.writerow(['Credit Accounts', ''])
				
				if accounts_to_view == 'Expenses and Incomes':
					credit_categories = ['Other Incomes', 'Operating Revenue', 'Cost of Sales']
				elif accounts_to_view == 'All Accounts':
					credit_categories = ['Capital', 'Non Current Liabilities', 'Current Liabilities', 'Other Incomes', 'Operating Revenue']
				else:
					credit_categories = ['Capital', 'Non Current Liabilities', 'Current Liabilities', 'Other Incomes', 'Operating Revenue']
				
				total_credit_side = []
				total_budget_credit = []
				total_variance_credit = []
				for category in credit_categories:
					if category in financial_data and category != "other_information":
						category_data = financial_data[category]
						for account_name, account_data in category_data.items():
							if account_name != "transactions":
								account_total = trial_balance_deractives(category, account_data, start_date, end_date)
								total_credit_side.append(account_total)
								if account_total == 0:
									pass
								else:
									if split_budget == 'Annually':
										budg = self.get_the_budgeted_amount(f"{category}|{account_name}")
									elif split_budget == 'Semi Annually':
										budg = self.get_the_budgeted_amount(f"{category}|{account_name}") * 0.5
									elif split_budget == 'Quarterly':
										budg = self.get_the_budgeted_amount(f"{category}|{account_name}") * 0.25
									else:
										budg = self.get_the_budgeted_amount(f"{category}|{account_name}") * float(self.ids.budget_amount.text)
										
									total_budget_credit.append(budg)
									variance = budg + account_total
									total_variance_credit.append(variance)
									writer.writerow([account_name, -account_total, budg, round(-variance, 2)])
									
				# total liabilitiew
				# sum total liabiloties 
				total_credit_side =  sum(total_credit_side)
				total_budget_credit = sum(total_budget_credit)
				total_variance_credit = sum(total_variance_credit)
				writer.writerow(['', ''])
				writer.writerow(['Credit total', -total_credit_side, total_budget_credit, round(total_variance_credit, 2)])
				
				self.error.text =  'Budget saved to "storage path"'
		except:
			self.error.text = 'error encountred in exporting'	
		
	def export_displayed_as_pdf(self, end_date, split):
		year_end = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
		if len(end_date) == 10 and end_date[0] in year_end and end_date[-1] in year_end:
			try:
				download_path = financial_data['other_information']['storage_folder']
						
				now = datetime.now()
				current_year = now.strftime("%d%m%Y")
						
				file_name = f"budget {split} ssdata{current_year}.png"
				screenshot_filename = os.path.join(download_path, file_name)
				
				self.exportation_layout.export_to_png(screenshot_filename)
				self.error.text = f'Screenshot saved to {download_path}'
				toast("Screenshot saved to storage folder")
			except:
				toast("Screenshot error")
				self.error.text = 'Error in saving screenshot'
					
		else:
			self.error.text = 'Error in dates selection, please check again'
			self.to_normal()
			toast("Date required")
		
	def to_normal(self):
		def normal(*args):
			self.error.text = 'All fields are required'
			
		Clock.schedule_once(normal, 3)
		
	def select_date(self, date_field):
		global on_date_field
		on_date_field = date_field
		popup = DatesPopup()
		popup.open()
		
	def on_press_trial_balance(self, details, *args):
		view_records = self.manager.get_screen('view_accounts')
		details = details.split('|')
		view_records.start_date.text = details[2]
		view_records.end_date.text = details[3]
		view_records.account_category.text = details[0]
		view_records.account_name.text = details[1]
		self.manager.current = 'view_accounts'
		
	def update_lists_of_account(self, category):
		self.account_name.values = view_accounts(financial_data, category)
		self.account_name.text = 'Choose Account'
		
	def on_text_if_account_in_budget(self, category, account_name):
		if f"{category}|{account_name}" in financial_data['other_information']['budgeted_accounts']:
			self.budget_amount.text = str(financial_data['other_information']['budgeted_accounts'][f"{category}|{account_name}"])
		else:
			self.budget_amount.text = '0'
			
	def add_budget_amount(self, budgeted_amount, category, account_name):
		if budgeted_amount == '0' or budgeted_amount == '':
			self.error.text = 'Enter a budget amount in the field below'
			self.to_normal()
		else:
			if account_name == 'Choose Account':
				self.error.text = 'Please select an account to add budget'
				self.to_normal()
			else:
				financial_data['other_information']['budgeted_accounts'][f"{category}|{account_name}"] = round(float(budgeted_amount), 2)
				self.error.text = f"Budget amount saved to '{account_name}'"
				toast("budget amount saved")
				self.to_normal()
				save_data(financial_data)
				self.budget_amount.text = '0'
				last_upated_date()
				
	def delete_the_budget_amount(self, budgeted_amount, category, account_name):
		if budgeted_amount == '0' or budgeted_amount == '':
			self.error.text = 'Budget amount is already zero'
			self.to_normal()
		else:
			if account_name == 'Choose Account':
				self.error.text = 'Please select an account to delete budget'
				self.to_normal()
			else:
				financial_data['other_information']['budgeted_accounts'][f"{category}|{account_name}"] = 0
				self.error.text = f"Budget amount set to zero in '{account_name}'"
				toast("budget amount set to zero")
				self.to_normal()
				save_data(financial_data)
				self.budget_amount.text = '0'
				
	def get_the_budgeted_amount(self, account):
		if account in financial_data['other_information']['budgeted_accounts']:
			return financial_data['other_information']['budgeted_accounts'][account]
		else:
			return 0
			
	def identify_positives(self, category):
		positives = {'Non Current Assets', 'Current Assets', 'Operating Expenses', 'Other Expenses', 'Bank', 'Taxes', 'Cost of Sales'}
		if category in positives:
			return True
		else:
			return False
			
	def show_loading_popup(self, start_date, end_date, split_budget, accounts_to_view):
		self.loading_popup = LoadingPopup(title='Loading...')
		self.loading_popup.open()
		
		partial_func = partial(self.generate_the_budget_view, start_date, end_date, split_budget, accounts_to_view)
		Clock.schedule_once(partial_func, 0.2)
				
	def generate_the_budget_view(self, start_date, end_date, split_budget, accounts_to_view, *args):
		year_end = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
		if len(end_date) == 10 and len(start_date) == 10 and end_date[0] in year_end and end_date[-1] in year_end:
			start_date = start_date
			self.loading_popup.dismiss()
			# clear widgets
			self.accounts_debit.clear_widgets()
			self.amounts_debit.clear_widgets()
			self.budget_column.clear_widgets()
			self.variance_column.clear_widgets()
			fnt = f"{self.the_font_size.text}sp"
			app = App.get_running_app()
			color = app.return_theme_color()
			icon_color = app.return_icon_color()
			
			if split_budget == 'Enter Ratio':
				ratio_1 = self.ids.budget_amount.text
				if ratio_1:
					if float(ratio_1) <= 1 and float(ratio_1) > 0:
						pass
					else:
						toast('a ratio should be between zero and one')
						return
				else:
					toast('please enter a ratio in budget textfield above')
					return
			else:
				pass
			
			# debit balances
			if accounts_to_view == 'Expenses and Incomes':
				debit_categories = ['Operating Expenses', 'Other Expenses', 'Taxes', 'Cost of Sales']
				total_of_what = 'Total Debit'
			elif accounts_to_view == 'Sales and COS':
				debit_categories = ['Cost of Sales']
				total_of_what = 'Total Debit'
			elif accounts_to_view == 'All Accounts':
				debit_categories = ['Non Current Assets', 'Current Assets', 'Operating Expenses', 'Other Expenses', 'Bank', 'Taxes', 'Cost of Sales']
				total_of_what = 'Total Debit'
			else:
				debit_categories = [accounts_to_view]
				total_of_what = f'Total {accounts_to_view}'
				
			total_debit_side = []
			total_budget_debit = []
			total_variance_debit = []
			is_positive = True
			for category in debit_categories:
				if category in financial_data and category != "other_information":
					category_data = financial_data[category]
					for account_name, account_data in category_data.items():
						if account_name != "transactions":
							account_total = trial_balance_deractives(category, account_data, start_date, end_date)
							
							total_debit_side.append(account_total)
							if account_total == 0:
								pass
								is_positive = True
							else:
								if split_budget == 'Annually':
									budg = self.get_the_budgeted_amount(f"{category}|{account_name}")
								elif split_budget == 'Semi Annually':
									budg = self.get_the_budgeted_amount(f"{category}|{account_name}") * 0.5
								elif split_budget == 'Quarterly':
									budg = self.get_the_budgeted_amount(f"{category}|{account_name}") * 0.25
								else:
									budg = self.get_the_budgeted_amount(f"{category}|{account_name}") * float(self.ids.budget_amount.text)
									
								total_budget_debit.append(budg)
								# accounts button
								account_button = MDFlatButton(
									text=str(account_name),
									size_hint=(1,None),
									halign='left',
									font_size=fnt)
								info = f"{category}|{account_name}|{start_date}|{end_date}"
								account_button.bind(on_press=partial(self.on_press_trial_balance, info))
								
								# amounts button
								if self.identify_positives(category):
									formatted = "{:,.2f}".format(account_total)
									is_positive = True
								else:
									formatted = "{:,.2f}".format(-account_total)
									is_positive = False
									
								amount_button = MDFlatButton(
									text=formatted,
									size_hint=(1,None),
									halign='left',
									font_size=fnt)	
								# budgeted button
								formatted = "{:,.2f}".format(budg)
								budg_button_debit = MDFlatButton(
									text=formatted,
									size_hint=(1,None),
									halign='left',
									font_size=fnt)
								# variance button
								
								if self.identify_positives(category):
									variance = budg - account_total
									total_variance_debit.append(variance)
									formatted = "{:,.2f}".format(variance)
									is_positive = True
									if self.rate_or_amount.text == 'variance rate':
										if variance < 0:
											text_color = 'red'
											icon = 'arrow-up'
										else:
											text_color = 'green'
											icon = 'arrow-down'
											
										try:
											variance_rate = (variance/budg)*100
											perc_variance = f"{round(variance_rate, 2)} %"
										except:
											perc_variance = '0 %'
											icon = 'cancel'
											
										variance_debit_button = MDRectangleFlatIconButton(
											icon=icon,
											text=perc_variance,
											size_hint=(1,None),
											font_size=fnt,
											theme_text_color="Custom",
											md_bg_color=(255,255,255,0),
											text_color=text_color,
											halign='left')
									else:
										variance_debit_button = MDFlatButton(
											text=formatted,
											size_hint=(1,None),
											halign='left',
											font_size=fnt)
								else:
									variance = budg + account_total
									total_variance_debit.append(variance)
									formatted = "{:,.2f}".format(-variance)
									is_positive = False
									
									if self.rate_or_amount.text == 'variance rate':
										if variance < 0:
											text_color = 'green'
											icon = 'arrow-up'
										else:
											text_color = 'red'
											icon = 'arrow-down'
											
										try:
											variance_rate = (variance/budg)*100
											perc_variance = f"{round(-variance_rate, 2)} %"
										except:
											perc_variance = '0 %'
											icon = 'cancel'
											
										variance_debit_button = MDRectangleFlatIconButton(
											icon=icon,
											text=perc_variance,
											size_hint=(1,None),
											font_size=fnt,
											theme_text_color="Custom",
											md_bg_color=(255,255,255,0),
											text_color=text_color,
											halign='left')
									else:
										variance_debit_button = MDFlatButton(
											text=formatted,
											size_hint=(1,None),
											halign='left',
											font_size=fnt)
									
								# create buttons
								self.accounts_debit.add_widget(account_button)
								self.amounts_debit.add_widget(amount_button)
								self.budget_column.add_widget(budg_button_debit)
								self.variance_column.add_widget(variance_debit_button)
								
			# total assets
			# sum total assests 
			total_debit_side =  sum(total_debit_side)
			total_budget_debit = sum(total_budget_debit)
			total_variance_debit = sum(total_variance_debit)
			op_income_button = MDFlatButton(
				text=total_of_what,
				size_hint=(1,None),
				halign='left',
				md_bg_color=app.theme_cls.primary_color,
				theme_text_color="Custom",
				text_color=icon_color,
				font_size=fnt)
			# button
			
			if is_positive == True:
				formatted = "{:,.2f}".format(total_debit_side)
			else:
				formatted = "{:,.2f}".format(-total_debit_side)
				
			op_income_amount_button = MDFlatButton(
				text=formatted,
				size_hint=(1,None),
				halign='left',
				md_bg_color=app.theme_cls.primary_color,
				theme_text_color="Custom",
				text_color=icon_color,
				font_size=fnt)
			# separate budget column
			formatted = "{:,.2f}".format(total_budget_debit)
			total_budget_debit = MDFlatButton(
				text=formatted,
				size_hint=(1,None),
				halign='left',
				md_bg_color=app.theme_cls.primary_color,
				theme_text_color="Custom",
				text_color=icon_color,
				font_size=fnt)
			# total varience debit
			formatted = "{:,.2f}".format(total_variance_debit)
			total_variance_debit_button = MDFlatButton(
				text=formatted,
				size_hint=(1,None),
				halign='left',
				md_bg_color=app.theme_cls.primary_color,
				theme_text_color="Custom",
				text_color=icon_color)
			# create buttons
			self.accounts_debit.add_widget(op_income_button)
			self.amounts_debit.add_widget(op_income_amount_button)
			self.budget_column.add_widget(total_budget_debit)
			self.variance_column.add_widget(total_variance_debit_button)
			
			# return if not needed
			if accounts_to_view == 'Expenses and Incomes' or accounts_to_view == 'All Accounts' or accounts_to_view == 'Sales and COS':
				pass
			else:
				toast("Balances loaded")
				return
			
			account_button = MDFlatButton(
				text='Credit balances',
				size_hint=(1,None),
				halign='left',
				theme_text_color="Custom",
				text_color=color,
				font_size=fnt)
			# pass button
			amount_button = MDFlatButton(
				text='  ',
				size_hint=(1,None),
				halign='left',
				font_size=fnt)
			separate_button = MDFlatButton(
				text='  ',
				size_hint=(1,None),
				halign='left',
				font_size=fnt)
			separate_variance = MDFlatButton(
				text='  ',
				size_hint=(1,None),
				halign='left',
				font_size=fnt)
			# create buttons
			self.accounts_debit.add_widget(account_button)
			self.amounts_debit.add_widget(amount_button)
			self.budget_column.add_widget(separate_button)
			self.variance_column.add_widget(separate_variance)
			
			if accounts_to_view == 'Expenses and Incomes':
				credit_categories = ['Other Incomes', 'Operating Revenue']
			elif accounts_to_view == 'All Accounts':
				credit_categories = ['Capital', 'Non Current Liabilities', 'Current Liabilities', 'Other Incomes', 'Operating Revenue']
			elif accounts_to_view == 'Sales and COS':
				credit_categories = ['Operating Revenue']
				
			total_credit_side = []
			total_budget_credit = []
			total_variance_credit = []
			for category in credit_categories:
				if category in financial_data and category != "other_information":
					category_data = financial_data[category]
					for account_name, account_data in category_data.items():
						if account_name != "transactions":
							account_total = trial_balance_deractives(category, account_data, start_date, end_date)
							total_credit_side.append(account_total)
							if account_total == 0:
								pass
							else:
								if split_budget == 'Annually':
									budg = self.get_the_budgeted_amount(f"{category}|{account_name}")
								elif split_budget == 'Semi Annually':
									budg = self.get_the_budgeted_amount(f"{category}|{account_name}") * 0.5
								elif split_budget == 'Quarterly':
									budg = self.get_the_budgeted_amount(f"{category}|{account_name}") * 0.25
								else:
									budg = self.get_the_budgeted_amount(f"{category}|{account_name}") * float(self.ids.budget_amount.text)
								total_budget_credit.append(budg)
								# accounts button
								account_button = MDFlatButton(
									text=str(account_name),
									size_hint=(1,None),
									halign='left',
									font_size=fnt)
								# amounts button
								info = f"{category}|{account_name}|{start_date}|{end_date}"
								account_button.bind(on_press=partial(self.on_press_trial_balance, info))
								formatted = "{:,.2f}".format(-account_total)
								amount_button = MDFlatButton(
									text=formatted,
									size_hint=(1,None),
									halign='left',
									font_size=fnt)
								# budgeted button
								formatted = "{:,.2f}".format(budg)
								budget_credit = MDFlatButton(
									text=formatted,
									size_hint=(1,None),
									halign='left',
									font_size=fnt)		
								variance = budg + account_total
								total_variance_credit.append(variance)
								# variance button
								formatted = "{:,.2f}".format(-variance)
								
								if self.rate_or_amount.text == 'variance rate':
									if variance < 0:
										text_color = 'green'
										icon = 'arrow-up'
									else:
										text_color = 'red'
										icon = 'arrow-down'
											
									try:
										variance_rate = (variance/budg)*100
										perc_variance = f"{round(-variance_rate, 2)} %"
									except:
										perc_variance = '0 %'
										icon = 'cancel'
											
									variance_credit_button = MDRectangleFlatIconButton(
										icon=icon,
										text=perc_variance,
										size_hint=(1,None),
										font_size=fnt,
										theme_text_color="Custom",
										md_bg_color=(255,255,255,0),
										text_color=text_color,
										halign='left')
								else:
									variance_credit_button = MDFlatButton(
										text=formatted,
										size_hint=(1,None),
										halign='left',
										font_size=fnt)
											
								# create buttons
								self.accounts_debit.add_widget(account_button)
								self.amounts_debit.add_widget(amount_button)
								self.budget_column.add_widget(budget_credit)
								self.variance_column.add_widget(variance_credit_button)
								
			# total assets
			# sum total assests 
			total_credit_side =  sum(total_credit_side)
			total_budget_credit = sum(total_budget_credit)
			total_variance_credit = sum(total_variance_credit)
			op_income_button = MDFlatButton(
				text='Total Credit',
				size_hint=(1,None),
				halign='left',
				md_bg_color=app.theme_cls.primary_color,
				theme_text_color="Custom",
				text_color=icon_color,
				font_size=fnt)
			# button
			formatted = "{:,.2f}".format(-total_credit_side)
			op_income_amount_button = MDFlatButton(
				text=formatted,
				size_hint=(1,None),
				halign='left',
				md_bg_color=app.theme_cls.primary_color,
				theme_text_color="Custom",
				text_color=icon_color,
				font_size=fnt)
			# separate budget column
			formatted = "{:,.2f}".format(total_budget_credit)
			total_credit_budget = MDFlatButton(
				text=formatted,
				size_hint=(1,None),
				halign='left',
				md_bg_color=app.theme_cls.primary_color,
				theme_text_color="Custom",
				text_color=icon_color,
				font_size=fnt)
			# separate budget column
			formatted = "{:,.2f}".format(-total_variance_credit)
			total_variance_credit_button = MDFlatButton(
				text=formatted,
				size_hint=(1,None),
				halign='left',
				md_bg_color=app.theme_cls.primary_color,
				theme_text_color="Custom",
				text_color=icon_color,
				font_size=fnt)
			# create buttons
			self.accounts_debit.add_widget(op_income_button)
			self.amounts_debit.add_widget(op_income_amount_button)
			self.budget_column.add_widget(total_credit_budget)
			self.variance_column.add_widget(total_variance_credit_button)
			toast("Budget mode built")		
		else:
			self.loading_popup.dismiss()
			self.error.text = 'Error in dates selection, please check again'
			self.to_normal()
		
		

'''build all screens defined above and navigate through them
'''


class ScreenBuilder(ScreenManager):
	def __init__(self, **kwargs):
		super(ScreenBuilder, self).__init__(**kwargs)
		
		if 'app_transition' in financial_data["other_information"]:
			trans = financial_data["other_information"]["app_transition"]
			if trans == 'FadeTransition':
				trans = FadeTransition()
			elif trans == 'SlideTransition':
				trans = SlideTransition()
			elif trans == 'SwapTransition':
				trans = SwapTransition()
			elif trans == 'WipeTransition':
				trans = WipeTransition()
			elif trans == 'NoTransition':
				trans = NoTransition()
		else:
			trans = FadeTransition()
			
		self.transition = trans
		

'''
SimploStatsApp  app launch
'''


class SimploStatsApp(MDApp):
	def build(self,):
		global fin_data_file
		global back_to_app_file
		global financial_data
		
		Builder.load_file('/storage/emulated/0/SimploStats/simploui.kv')
		
		# Get the path to the user-specific data directory
		user_data_dir = self.user_data_dir
		
		
		# Create a file path within the user_data_dir for storage
		# in app file name
		#simplostats_data_file
		app_ssdata_file = "advanced_simplostats_2.ssdata"
		file_path = os.path.join(user_data_dir, app_ssdata_file)
		toast("Please wait...loading app main file")
		
		fin_data_file = file_path
		back_to_app_file = file_path
		financial_data = load_data()
		
		if "app_theme" in financial_data["other_information"]:
			theme = financial_data["other_information"]["app_theme"]
		else:
			theme = "Indigo"
			
		self.theme_cls.primary_palette = theme
		self.sm = ScreenBuilder()
		return self.sm
		
	def return_theme_color(self,):
		#['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 'DeepOrange', 'Brown']
		if "app_theme" in financial_data["other_information"]:
			theme = financial_data["other_information"]["app_theme"]
			if theme == 'Red':
				return 'red'
			elif theme == 'Pink':
				return '#E99491'
			elif theme == 'Purple':
				return 'purple'
			elif theme == 'DeepPurple':
				return "#4B0082" #'purple'
			elif theme == 'Indigo':
				return '#4B0082'
			elif theme == 'Blue':
				return 'blue'
			elif theme == 'Cyan':
				return 'darkcyan'
			elif theme == 'LightBlue':
				return 'blue'
			elif theme == 'Green':
				return 'darkgreen'
			elif theme == 'LightGreen':
				return 'green'
			elif theme == 'Teal':	
				return 'teal'
			elif theme == 'DeepOrange':
				return 'darkorange'
			elif theme == 'Brown':
				return 'brown'
			else:
				return 'green'
		else:
			return '#4B0082'
			
	def return_icon_color(self,):
		#['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 'DeepOrange', 'Brown']
		if "app_theme" in financial_data["other_information"]:
			theme = financial_data["other_information"]["app_theme"]
			if theme == 'Red':
				return 'white'
			elif theme == 'Pink':
				return 'white'
			elif theme == 'Purple':
				return 'white'
			elif theme == 'DeepPurple':
				return 'white'
			elif theme == 'Indigo':
				return 'white'
			elif theme == 'Blue':
				return 'white'
			elif theme == 'Cyan':
				return 'black'
			elif theme == 'LightBlue':
				return 'black'
			elif theme == 'Green':
				return 'black'
			elif theme == 'LightGreen':
				return 'black'
			elif theme == 'Teal':	
				return 'white'
			elif theme == 'DeepOrange':
				return 'white'
			elif theme == 'Brown':
				return 'white'
			else:
				return 'black'
		else:
			return 'white'
			
	def app_image_file(self):
		return '/storage/emulated/0/SimploStats/simplo_background.png'
			
	def change_colors(self, widget):
		if hasattr(widget, 'rgba'):
			widget.rgba = (0, 0, 0, 1)  # Change rgba to black
		if hasattr(widget, 'rgb'):
			widget.rgb = (0, 0, 0)
		if hasattr(widget, 'background_color'):
			widget.background_color = (0, 0, 0, 1)  # Change background color to black
		if hasattr(widget, 'md_bg_color'):
			widget.md_bg_color = (0, 0, 0, 1)
		if hasattr(widget, 'color'):
			widget.color = 'white'  # Change text color to white
		if hasattr(widget, 'text_color'):
			widget.text_color = 'white'

	def traverse_widgets(self, widget):     
		if isinstance(widget, BoxLayout):
			#self.traverse_widgets(widget)
			with widget.canvas.before:
				widget.canvas.before.clear()
				Color(0, 0, 0, 1)
				Rectangle(pos=widget.pos, size=widget.size)
				
			for child in widget.children:
				self.traverse_widgets(child)
				
		elif isinstance(widget, Label) or isinstance(widget, Button) or isinstance(widget, MDRectangleFlatIconButton) or isinstance(widget, MDLabel) or isinstance(widget, MDFlatButton):
			self.change_colors(widget)
			
	def transverse_canvas(self, widget):
		with widget.canvas.before:
			widget.canvas.before.clear()
			Color(0, 0, 0, 1)
			Rectangle(pos=widget.pos, size=widget.size)
			
	def perform_transverse(self):
		#dark_theme_box
		home = self.root.get_screen('home').ids.scroll_view
		journals = self.root.get_screen('Journal_entries').ids.scroll_view
		charts = self.root.get_screen('charts_of_accounts').ids.dark_theme_box
		
		for child in home.children:
			if isinstance(child, BoxLayout):
				self.traverse_widgets(child)
		'''	
		for child in journals.children:
			if isinstance(child, BoxLayout):
				self.traverse_widgets(child)'''
				

# launch the app.	
if __name__ == '__main__':
	SimploStatsApp().run()
	