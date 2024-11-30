from flask import Flask, render_template, request
import pandas as pd
from searchspace import findSearchSpace

app = Flask(__name__)

@app.route('/course_info')
def course_info():
    return render_template('course_info.html')

@app.route('/', methods=['GET', 'POST'])
def search_colleges():
    if request.method == 'POST':
        name = request.form['name']
        dob = request.form['dob']
        phone = request.form['phone']
        region = request.form['region']
        reservation_category = request.form['reservation_category']
        subcategory = request.form.get('subcategory', '')
        subsubcategory = request.form.get('subsubcategory', '')
        kannada_medium = request.form['kannada_medium']
        rural_reservation = request.form['rural_reservation']
        cet_rank = int(request.form['cet_rank'])
        course = request.form['course']
        limit=max(0,int(request.form['limit']))
        # Get search space based on user input
        search_space = findSearchSpace(reservation_category, subcategory, subsubcategory, kannada_medium, rural_reservation)

        # Call the appropriate function based on region
        if region == 'Hyd-Kar':
            eligible_colleges = search_colleges_in_hyd_kar(cet_rank, search_space, course,limit)
        else:
            eligible_colleges = search_colleges(cet_rank, search_space, course,limit)

        return render_template('college_list.html', eligible_colleges=eligible_colleges)

    return render_template('college_search.html')

def filterDf(df, cet_rank, search_space, course, limit):
    # Replace '--' with 0 and ensure numerical types for search_space columns
    df.replace('--', 0, inplace=True)
    df[search_space] = df[search_space].apply(pd.to_numeric, errors='coerce')
    
    # Filter DataFrame based on the specified course and search criteria
    filtered_df = df.loc[df['Course Code'] == course, ['College Code', 'College Name', 'Course Code', 'Course Name'] + search_space]
    filtered_df = filtered_df[(filtered_df[search_space] >= cet_rank).any(axis=1)]
    if limit:
        filtered_df = filtered_df.sort_values(by=search_space[-1], ascending=True)[:limit]
    else:
        filtered_df = filtered_df.sort_values(by=search_space[-1], ascending=True)
    return filtered_df.to_dict(orient='records')

def search_colleges(cet_rank, search_space, course, limit):
    # Define file paths and names for Hyd-Kar region
    files = {
        "2023-R1": "2023-R1.xlsx",
        "2023-R2": "2023-R2.xlsx",
        "2023-R3": "2023-R3.xlsx",
        "2022-R1": "2022-R1.xlsx",
        "2022-R2": "2022-R2.xlsx",
        "2022-R3": "2022-R3.xlsx",
        "2021-R1": "2021-R1.xlsx",
        "2021-R2": "2021-R2.xlsx",
        "2021-R3": "2021-R3.xlsx"
    }
    
    # Prepare results dictionary with file name as key
    results = {file_name: [] for file_name in files.keys()}
    
    # Filter each file and populate the results dictionary
    for file_name, file_path in files.items():
        df = pd.read_excel(file_path)
        filtered_colleges = filterDf(df, cet_rank, search_space, course, limit)
        results[file_name] = filtered_colleges  # Store results under the corresponding file name
    return results

def search_colleges_in_hyd_kar(cet_rank, search_space, course, limit):
    # Define file paths and names for other regions
    files = {
        "2023-R1": "Hyd-2023-R1.xlsx",
        "2023-R2": "Hyd-2023-R2.xlsx",
        "2023-R3": "Hyd-2023-R3.xlsx",
        "2022-R1": "Hyd-2022-R1.xlsx",
        "2022-R2": "Hyd-2022-R2.xlsx",
        "2022-R3": "Hyd-2022-R3.xlsx",
        "2021-R1": "Hyd-2021-R1.xlsx",
        "2021-R2": "Hyd-2021-R2.xlsx",
        "2021-R3": "Hyd-2021-R3.xlsx"
    }

    # Prepare results dictionary with file name as key
    results = {file_name: [] for file_name in files.keys()}
    
    # Filter each file and populate the results dictionary
    for file_name, file_path in files.items():
        df = pd.read_excel(file_path)
        filtered_colleges = filterDf(df, cet_rank, search_space, course, limit)
        results[file_name] = filtered_colleges  # Store results under the corresponding file name
    return results

if __name__ == '__main__':
    app.run(debug=True)
