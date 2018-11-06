#! /usr/bin/env python
# -*- coding: utf-8 -*-

#net_sales = float(input('Net sales --- '))
#cost_goods_sold = float(input('Cost of goods sold --- '))
#average_inv = float(input('Average inventory --- '))
#goods_avail_cost = float(input('Goods available for sale at cost --- '))
#ending_inv_cost = float(input('Ending inventory at cost ---'))
#total_income = float(input('Total income --- '))
#total_revenue = float(input('Total revenue --- '))
#total_expenses = float(input('Total expenses --- '))

beg_mu_percent = float(input('Beginning Markup --- ')) / 100
beg_inv_retail = float(input('Beginning inventory at retail --- '))
beg_inv_cost = (beg_inv_retail - (beg_inv_retail * beg_mu_percent))
print(beg_inv_cost)
net_receipt_retail = float(input('Net receipt at retail --- '))
imu = float(input('Initial markups --- ')) / 100
net_receipt_cost = (net_receipt_retail - (net_receipt_retail * imu))
print(net_receipt_cost)
markups = float(input('Markups (not IMU or Beginning MU) --- '))


goods_avail_retail = (beg_inv_retail + net_receipt_retail + markups)
goods_avail_cost = (beg_inv_cost + net_receipt_cost)
adj_mu_percent = ((goods_avail_retail - goods_avail_cost) / goods_avail_retail) * 100
cost_complement = (100 - adj_mu_percent)
print(adj_mu_percent)
print(cost_complement)

'''

profit_margin = (total_income / total_revenue)
net_profit = (net_sales - total_expenses)
gross_margin = (net_sales - cost_goods_sold)
cogs = (goods_avail_cost - ending_inv_cost)
gmroi = (gross_margin / average_inv)
'''
'''
beg_mu needs to be calculated into a floating number.  Calculate percent and retail.

All percents need to be figured with a dollar amount and without
'''
