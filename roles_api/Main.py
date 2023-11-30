from flask import Flask,request,jsonify

app = Flask("__main__")

#add,remove,view 
#parameters

@app.route("/")
def home():
    return "<h1>server running</h1>"

@app.route("/lender",methods=["POST","GET"])
def add_item():
    if request.method == "POST":
        return ("<h1>added   </h1>")
    elif request.method == "GET":
        return ("<h1>Your Products</h1>")
    else:
        return("<h1>Sorry method not allowed </h1>")
    
#Description
#Cost/day
#Equipment Details:


#
equipment_list = [
     {
        "name": "Tractor 2000",
        "type": "tractor",
        "make": "John Deere",
        "model": "XYZ123",
        "year": 2020,
        "power": "100 HP",
        "fuel_type": "Diesel",
        "condition": "Used",
        "maintenance": "Recent service",
        "availability": "Available",
        "location": "Farm A",
        "rental_rates": "$50/day",
        "contact_info": "John Doe - john@example.com"
    }
]
@app.route("/addMachine",methods=["POST"])
def addEquipment():
    if request.method == "POST":
        try:
            # Get JSON data from the request body
            equipment_data = request.json
            
            # Validate required fields
            required_fields = ["name", "type", "make", "model", "year", "power", "fuel_type", "condition", "maintenance", "availability", "location", "rental_rates", "contact_info"]
            for field in required_fields:
                if field not in equipment_data:
                    return jsonify({"error": f"Missing required field: {field}"}), 400

            # Extract data from JSON
            name = equipment_data["name"]
            equipment_type = equipment_data["type"]
            make = equipment_data["make"]
            model = equipment_data["model"]
            year = equipment_data["year"]
            power = equipment_data["power"]
            fuel_type = equipment_data["fuel_type"]
            condition = equipment_data["condition"]
            maintenance = equipment_data["maintenance"]
            availability = equipment_data["availability"]
            location = equipment_data["location"]
            rental_rates = equipment_data["rental_rates"]
            contact_info = equipment_data["contact_info"]

            # Create a dictionary to represent the equipment
            new_equipment = {
                "name": name,
                "type": equipment_type,
                "make": make,
                "model": model,
                "year": year,
                "power": power,
                "fuel_type": fuel_type,
                "condition": condition,
                "maintenance": maintenance,
                "availability": availability,
                "location": location,
                "rental_rates": rental_rates,
                "contact_info": contact_info
            }

            # Add the equipment to the list (this can be replaced with a database operation)
            
            equipment_list.append(new_equipment)

            return jsonify({"success": True, "message": "Equipment added successfully"}), 201

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    else:
        return jsonify({"error": "Method not allowed"}), 405
    
    
@app.route("/viewMachinery",methods=["POST"])
def viewMachinery():
    if request.method == "POST":
        try:
            # Get JSON data from the request body
            request_data = request.json

            # Validate required fields
            if "type" not in request_data:
                return jsonify({"error": "Missing required field: type"}), 400

            # Extract type from the request data
            machinery_type = request_data["type"]

            # Filter machinery based on type
            filtered_machinery = [machinery for machinery in equipment_list if machinery["type"] == machinery_type]

            return jsonify({"success": True, "machinery": filtered_machinery}), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    else:
        return jsonify({"error": "Method not allowed"}), 405
    
@app.route("/deleteMachine")
def deleteMachine():
    if request.method == "POST":
        pass
    else:
        return jsonify({"error": "Method not allowed"}), 405
        
        
        


if __name__ == "__main__":
    app.run(debug=True)