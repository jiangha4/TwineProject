import math
from .csv_reader import csv_file

csv_file = csv_file()

def get_all_companies():
    """
        Returns a list of all companies in the CSV file
    """
    return csv_file.companies

def get_metric_value(company, metric):
    """
        Returns the average value of the metric with 5 decimal places
    """
    buf = list()
    index = csv_file._valid_csv_fields.index(metric)
    for row in csv_file.reader:
        if company in row:
                if row[index] != '':
                    try:
                        val = float(row[index])
                        buf.append(val)
                    except Exception as e:
                        print("Error with data field")
                        print("...Skipping")
    value = float(sum(buf))/float(len(buf))
    return "{0:.5f}".format(value)

def _get_headcounts():
    """
        Returns a dict key as company name and value as the headcount of that company
    """
    headcount = dict()
    for company in csv_file.companies:
        headcount[company] = 0

    for item in csv_file.reader:
        company_name = item[csv_file._valid_csv_fields.index(company)]
        headcount[company_name] = headcount[company_name] + 1

    return headcount

def find_closest_headcounts(target_company, company_list):
    """
        Returns the company that has the most similiar head count from a list
        of companies that match the industry of the target company
    """
    head_count = _get_headcounts()
    target_count = head_count[target_company]
    closest = math.inf
    closest_company = None
    for company in company_list:
        count = abs(target_count - head_count[company])
        if count < closest:
            closest = count
            closest_company = company
    return closest_company

def get_target_company(company):
    """
        Returns the info for a specific company
    """
    for row in csv_file.companyInfo:
        if company in row:
            return row

def get_same_industry(company, field):
    """
        Returns a list of companies that matches the industry of the target company
    """
    buf = list()
    # Switch for the two peer groups
    if field == 'industry':
        index = csv_file._company_fields.index('industry')
    else:
        index = csv_file._company_fields.index('geography')
    name_index = csv_file._company_fields.index('company')

    target_industry = get_target_company(company)[index]
    for row in csv_file.companyInfo:
        if row[index] == target_industry and row[name_index] != company:
            buf.append(row[name_index])
    return buf

def find_closest_industry(company, metric, field):
    """
        Returns a tuple of (company, average metric) for the company that is closest
        in head count
        If a company is in an industry that has no other companies, we return a string
        signifying that.
    """
    similiar_industry = get_same_industry(company, field)
    if similiar_industry == []:
        return (company, "No similiar industry companies")
    else:
        closest_headcount = find_closest_headcounts(company, similiar_industry)
        value = get_metric_value(closest_headcount, metric)
        return (closest_headcount, value)

def response_object(company, metric):
    """
        Returns a contructed JSON obj for the endpoint to render
    """
    # Get Target company info and average metric
    target_company_info = get_target_company(company)
    value = get_metric_value(company, metric)

    # Index Values
    industry_index = csv_file._company_fields.index('industry')
    geo_index = csv_file._company_fields.index('geography')

    # Industry
    closest_company_value = find_closest_industry(company, metric, 'industry')
    # Location
    closest_company_location = find_closest_industry(company, metric, 'geography')

    peer_group_one = {'peer_group_attribute': 'industry',
                      'peer_group_attribute_value': target_company_info[industry_index],
                      'average_peer_group_value': closest_company_value[1]
                      }

    peer_group_two =  {'peer_group_attribute': 'geography',
                      'peer_group_attribute_value': target_company_info[geo_index],
                      'average_peer_group_value': closest_company_location[1]
                      }

    resp_obj = {'company_name': company.lower().capitalize(),
                'query_metric': metric,
                'value': value,
                'benchmarks': [peer_group_one, peer_group_two]}

    return resp_obj

