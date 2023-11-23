import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, jsonify, make_response
from io import BytesIO
import base64
import pandas as pd
import os
from datetime import datetime, timedelta
import random
import regex as re
import numpy as np
from datetime import datetime

app = Flask(__name__) 

df_s=pd.DataFrame()
for i in range(12,23):
    temp_df = pd.read_csv(f"Exchange_Rate_Report_20{i}.csv")
    df_s=pd.concat([df_s,temp_df], ignore_index=True)
df_s.set_index("Date")
df_s.index = pd.to_datetime(df_s.index)
df_s['Date'] = pd.to_datetime(df_s['Date'], format='%d-%b-%y')

df_s['Day'] = df_s['Date'].dt.day
df_s['Month'] = df_s['Date'].dt.month
df_s['Year'] = df_s['Date'].dt.year

df_s.columns = [re.sub(r'\s+', ' ', col) for col in df_s.columns]
df_s.columns = df_s.columns.str.strip()

df_2022 = df_s[ df_s['Year'] == 2021 ]
print(df_2022)



@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/get_amount', methods= ['GET', 'POST'])
def get_amount():
    if request.method == 'POST':
        currency1 = request.form['currency1']
        currency2 = request.form['currency2']
        amount = request.form['amount']

        df_curr1 = df_2022[df_2022[currency1].notnull()]

        last_value1 = df_curr1[currency1].iloc[-1]


        df_curr2 = df_2022[df_2022[currency2].notnull()]

        last_value2 = df_curr2[currency2].iloc[-1]

        conversion = (1/int(last_value1)) * int(last_value2)

        total_amount = int(amount) * float(conversion)
        print(total_amount)

        random_query_parameter = random.randint(1, 1000000)
        content = render_template('index.html', amount = "The predicted price is {}".format(total_amount) , random_query_parameter=random_query_parameter)

        # Create a response object
        response = make_response(content)
        
        
        return response
        



        


@app.route('/get_plot', methods=['GET','POST'])
def get_plot():

    if request.method =='POST':
        currency1 = request.form['currency1']
        currency2 = request.form['currency2']
        duration = request.form['duration']
        start_year = request.form['startDate']
        end_year  = request.form['endDate']

        df = df_s[(df_s['Year'] >= int(start_year)) & (df_s['Year'] <= int(end_year))]
        highest_rate = df[currency2].max()
        lowest_rate = df[currency2].min()
        average_rate = df[currency2].mean()


        file_path = "static/my_plot.png"
        if os.path.exists(file_path) :
            os.remove(file_path)
            print("hello")

        if(duration =="Yearly"):
            df_agg = df.groupby(['Date', 'Year'])[currency2].mean().reset_index()

            pivot_df = df_agg.pivot(index='Date', columns='Year', values=currency2)

            original_missing_mask = pivot_df.isna()
            window_size = 8

            pivot_df = pivot_df.apply(lambda col: col.fillna(col.rolling(window=window_size, min_periods=1).mean()))

            plt.figure(figsize=(12, 8))

            for col in pivot_df.columns:
                year_label = col
                print(year_label)
                plt.plot(pivot_df.index[original_missing_mask[col]], pivot_df[col][original_missing_mask[col]], 'o', label=f'Year {year_label} (Original Missing)', linestyle='None', markersize=5, color='red')

                plt.plot(pivot_df.index, pivot_df[col], label=f'Year {year_label} (Interpolated)')

            plt.xlabel('Year')
            plt.ylabel(currency2)
            plt.title(f'Line Plot for {currency2} - Yearly')
            
            plt.legend()

            plt.tight_layout()

            plt.savefig(file_path)
            plt.close()

        elif(duration == "Weekly"):
            #code
            df['Week'] = df_s['Date'].dt.to_period('W') 
            df_agg = df.groupby(['Date', 'Week'])[(currency2)].mean().reset_index()

            
            pivot_df = df_agg.pivot(index='Date', columns='Week', values=currency2)

            original_missing_mask = pivot_df.isna()

            window_size = 10

            pivot_df = pivot_df.apply(lambda col: col.fillna(col.rolling(window=window_size, min_periods=1).mean()))

            plt.figure(figsize=(12, 8))

            for col in pivot_df.columns:
                week_label = col

                plt.plot(pivot_df.index[original_missing_mask[col]], pivot_df[col][original_missing_mask[col]], 'o', label=f'Week {week_label} (Original Missing)', linestyle='None', markersize=2, color='red')

                plt.plot(pivot_df.index, pivot_df[col], label=f'Week {week_label} (Interpolated)')

            plt.xlabel('Date')
            plt.ylabel(currency2)
            plt.title(f'Line Plot for {currency2} - Weekly')

            plt.legend()
            
            plt.tight_layout()

            plt.savefig(file_path)
            plt.close()
    

        
        # elif(duration =="Quaterly"):
        #     #code
        #     df['Quarter'] = df['Date'].dt.to_period('Q')
        #     df_agg = df.groupby(['Date', 'Quarter'])[currency2].mean().reset_index()

        #     pivot_df = df_agg.pivot(index='Date', columns='Quarter', values=currency2)

        #     original_missing_mask = pivot_df.isna()

        #     window_size = 10

        #     pivot_df_interpolated = pivot_df.apply(lambda col: col.fillna(col.rolling(window=window_size, min_periods=1).mean()))

        #     plt.figure(figsize=(12, 8))

        #     colors = ['red', 'blue', 'green', 'purple']  # You can add more colors as needed

        #     for i, col in enumerate(pivot_df.columns):
        #         quarter_label = col

        #         plt.plot(pivot_df.index[original_missing_mask[col]], df_agg[col][original_missing_mask[col]], 'o', label=f'Quarter {quarter_label} (Original Missing)', linestyle='None', markersize=5, color=colors[i % len(colors)])

        #         plt.plot(pivot_df.index, pivot_df_interpolated[col], label=f'Quarter {quarter_label} (Interpolated)', color=colors[i % len(colors)])

        #     plt.xlabel('Date')
        #     plt.ylabel(currency2)
        #     plt.title(f'Line Plot for {currency2} - Quarterly')

        #     plt.legend()

        #     plt.tight_layout()


        #     plt.savefig(file_path)
        #     plt.close()


        elif(duration =="Monthly"):
            #cpde
            print()
        



        

        

        
        
        
        
        

        
    
        

        random_query_parameter = random.randint(1, 1000000)

        content = render_template('index.html', plot_url=file_path, random_query_parameter=random_query_parameter, highest_rate= "Highest value- {}".format(highest_rate), 
        lowest_rate = "Lowest value- {}".format(lowest_rate), average_rate = "FX value- {}".format(average_rate) )

        # Create a response object
        response = make_response(content)
        
        return response


        
    else:
        print("in post")
        return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)

