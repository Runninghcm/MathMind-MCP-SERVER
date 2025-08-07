import os 
import sys 

def remove_about_url(results:dict):
    if "aboutUrl" in results:
        del results["aboutUrl"]
    
    if "data" in results and "aboutUrl" in results.get("data",{}):
        
        del results["data"]["aboutUrl"]
    
    return results