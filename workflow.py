import json

FLOW_REQUIREMENTS = {
    "credit_card_eligibility": [
        {"field": "age", "type": int, "prompt": "What is your age?"},
        {"field": "monthly_income", "type": int, "prompt": "What is your monthly income ?"},
        {"field": "employment_type", "type": str, "prompt": "What is your employment type? (salaried/self_employed)"},
        {"field": "credit_score", "type": int, "prompt": "What is your credit score?"},
        {"field": "is_ntc", "type": bool, "prompt": "Are you new to credit?"}
    ],
    
    "loan_eligibility": [
        {"field": "age", "type": int, "prompt": "What is your age?"},
        {"field": "employment_type", "type": str, "prompt": "What is your employment type? (salaried/self_employed)"},
        {"field": "personal_income", "type": int, "prompt": "What is your monthly income?"},
        {"field": "credit_score", "type": int, "prompt": "What is your CIBIL score?"},
        {"field": "new_to_cibil", "type": bool, "prompt": "Are you new to CIBIL?"}
    ]
}

#mislenicous functions 

# converting input to expected type
def convert_input(value, expected_type):
    if expected_type == bool:
        return value.lower() in ['yes', 'y', 'true', '1']
    elif expected_type == int:
        return int(value)
    elif expected_type == str:
        return str(value)
    else:
        return value

# flow type input + returns collected data
def collect_flow_data(flow_name):
    
    print(f"Starting {flow_name.replace('_', ' ').title()} Flow")
    
    if flow_name not in FLOW_REQUIREMENTS:
        print(f"Flow '{flow_name}' not found")
        return None
    
    requirements = FLOW_REQUIREMENTS[flow_name]
    collected_data = {}
    
    # flow questions input
    for req in requirements:
        field_name = req["field"]
        field_type = req["type"]
        prompt_text = req["prompt"]
        
        while True:
            try:
                user_input = input(f"{prompt_text} ")
                converted_value = convert_input(user_input, field_type)
                collected_data[field_name] = converted_value
                break
            except ValueError:
                print(f"Invalid input. Please enter a valid {field_type.__name__}")
    
    return collected_data

# credit card eligiblity flow

def credit_card_eligibility_flow(user_data):
    age = user_data.get("age")
    monthly_income = user_data.get("monthly_income")
    employment_type = user_data.get("employment_type")
    credit_score = user_data.get("credit_score")
    is_ntc = user_data.get("is_ntc", False)
    
    reasons = []
    
    #age check 
    if age < 21:
        reasons.append("min age required is 21 years")
    elif age > 60:
        reasons.append("max age limit is 60 years")
        
    #income check 
    min_income = 20000 if employment_type == "salaried" else 25000
    if monthly_income < min_income:
        reasons.append(f"min monthonly income {min_income} required for {employment_type}")
    
    #check credit score 
    if not is_ntc and credit_score < 720:
        reasons.append("min credit score of 720 is required")   
    
    #result 
    if reasons:
        return {
            "status": "success",
            "eligible": False,
            "message": "NOT eligible",
            "reasons": reasons
        }
    else:
        return {
            "status": "success",
            "eligible": True,
            "message": "eligible",
            "reasons": []
        }    
    
# loan eligibility flow 
def loan_eligibility_flow(user_data):
    age = user_data.get("age")
    employment_type = user_data.get("employment_type")
    personal_income = user_data.get("personal_income")
    credit_score = user_data.get("credit_score")
    new_to_cibil = user_data.get("new_to_cibil", False)
    
    reasons = []
    
    # age check
    if age < 21:
        reasons.append("min age requirement is 21 years")
    elif age > 60:
        reasons.append("max age limit is 60 years")
    
    # income check
    min_income = 25000 if employment_type == "salaried" else 30000
    if personal_income < min_income:
        reasons.append(f"min monthly income of {min_income} required for {employment_type}")
    
    # CIBIL check
    if not new_to_cibil and credit_score < 700:
        reasons.append("min CIBIL score - 700 is required")
    
    # Result
    if reasons:
        return {
            "status": "success",
            "eligible": False,
            "message": "Data not given properly or not eligible ",
            "reasons": reasons
        }
    else:
        return {
            "status": "success",
            "eligible": True,
            "message": "Proper data collected + eligible",
            "reasons": []
        }

# main workflow 

def run_workflow(flow_name, user_data):
    workflows = {
        "credit_card_eligibility": credit_card_eligibility_flow,
        "loan_eligibility": loan_eligibility_flow   
    }
    if flow_name not in workflows:
        return {
            "status": "error",
            "message": f"Unknown workflow: {flow_name}",
            "available_workflows": list(workflows.keys())
        }        
    try:
        workflow_function = workflows[flow_name]
        result = workflow_function(user_data)
        return result
    except Exception as e:
        return {
            "status": "error",
            "message": f"Workflow execution failed: {str(e)}"
        }
        
        
def main():
    available_flows = list(FLOW_REQUIREMENTS.keys())
    print("\nAvailable Flows:")
    for i, flow in enumerate(available_flows, 1):
        print(f"  {i}. {flow.replace('_', ' ').title()}")
    
    flow_choice = input("\nEnter flow name (or number): ").strip().lower()
    
    # handle numeric input
    if flow_choice.isdigit():
        flow_index = int(flow_choice) - 1
        if 0 <= flow_index < len(available_flows):
            flow_name = available_flows[flow_index]
        else:
            print("Invalid selection")
            return
    else:
        flow_name = flow_choice.replace(" ", "_")
    
    #collect data 
    user_data = collect_flow_data(flow_name)
    
    if user_data is None:
        return
    
    # return collected data 
    print("\nCollected Data:")
    print(json.dumps(user_data, indent=2))
    
    # run the workflow
    print("\n running workflow...")
    result = run_workflow(flow_name, user_data)
    
    #result
    print(f"\n{result['message']}\n")
    
    if result.get('reasons'):
        print("Reasons:")
        for reason in result['reasons']:
            print(f"  • {reason}")

    print("\nFull Result:")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()