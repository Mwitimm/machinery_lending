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
@app.route("/")
def viewAll():
    from flask import Flask, request, jsonify

app = Flask(__name__)



@app.route("/viewAllMachines", methods=["POST"])
def viewMachinery():
    if request.method == "POST":
        try:
            
            all_machinery = equipment_list

            return jsonify({"success": True, "machinery": all_machinery}), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    else:
        return jsonify({"error": "Method not allowed"}), 405

if __name__ == "__main__":
    app.run(debug=True)

    
@app.route("/deleteMachine",methods=["POST"])
def deleteMachine():
    if request.method == "POST":
        try:
            # Get data from the request body
            request_data = request.json

            # Validate required parameter
            if "machine_name" not in request_data:
                return jsonify({"error": "Missing required parameter: machine_name"}), 400

            # Extract machine name from the request data
            machine_name = request_data["machine_name"]

            # Find and remove the equipment with the specified name
            equipment_to_book = [machine for machine in equipment_list if machine["name"] == machine_name]

            if not equipment_to_book:
                return jsonify({"error": "Machine not found"}), 404

            # Remove the equipment from the list (this can be replaced with a database operation)
            equipment_list.remove(equipment_to_book[0])

            return jsonify({"success": True, "message": f"Equipment '{machine_name}' booked successfully"}), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    else:
        return jsonify({"error": "Method not allowed"}), 405
    
booked_machinery_list = []
@app.route("/bookMachine",methods=["POST"])
def bookMachine():
    if request.method == "POST":
        try:
            # Get JSON data from the request body
            request_data = request.json

            # Validate required parameters
            required_fields = ["machine_name", "user_name", "booking_date"]
            for field in required_fields:
                if field not in request_data:
                    return jsonify({"error": f"Missing required parameter: {field}"}), 400

            # Extract data from the request
            machine_name = request_data["machine_name"]
            user_name = request_data["user_name"]
            booking_date = request_data["booking_date"]

            # Perform booking logic (update database, add to booked_machinery_list, etc.)
            # For simplicity, just add it to a list in this example
            booked_machinery_list.append({
                "machine_name": machine_name,
                "user_name": user_name,
                "booking_date": booking_date
            })

            return jsonify({"success": True, "message": "Booking successful"}), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    else:
        return jsonify({"error": "Method not allowed"}), 40


    

        
        
        
        


if __name__ == "__main__":
    app.run(debug=True)