import requests
import pandas as pd
import json
import argparse
import pprint

#Runs a graphql query, parses the results into a dataframe, then dumps a CDS manifest file

def runGrapoQLQuery(url,query):
    #try:
    results = requests.post(url = url, json={"query":query})
    results = results.json()
    return results

def main(args):
    #The example query retrieves info for all WXS files in HTAN
    examplequery = """
    {
    study(phs_accession:"phs002371"){
        files(experimental_strategy_and_data_subtypes:"WXS"){
        file_name
        file_id
        md5sum
        samples{
            participant{
            participant_id
            }
        }
        }
    }
    }
    """
    CDSGraphQLUrl="https://dataservice.datacommons.cancer.gov/v1/graphql/"

    jsonres = runGrapoQLQuery(CDSGraphQLUrl, examplequery)
    pprint.pprint(jsonres)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--manifestfile", required=True, help="Name for the manifest file")
    parser.add_argument("-c", "--comment", required=True, help="Comment added to the manifest file")
    

    args = parser.parse_args()

    main(args)