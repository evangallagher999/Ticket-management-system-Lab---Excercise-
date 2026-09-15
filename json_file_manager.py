import json 

class JSONFileManager:

    @staticmethod #fixed - does not change 
    def ReadJsonFile(file_path):
        with open(file_path, "r") as file:
            data = json.load(file)

        return data

    @staticmethod
    def LoadObjectsFromJSONFile(file_path, classname): # class name is hook 

        data = JSONFileManager.ReadJsonFile(file_path)
        data_s = json.dumps(data)
        object_list = json.loads(data_s, object_hook=classname)
        return object_list

    @staticmethod
    def WriteObjectToJSONFile(file_path, data):
        try: 
            with open(file_path, "x") as file:
                #create the file and write the first data
                json.dump([data], file, indent=4)
                print(f"{file_path} Created and data saved")
        except FileExistsError:
            with open(file_path, "r") as file:
                #load the existing data from the file
                existing_data = json.load(file)

            #append the new data to the existing data
            existing_data.append(data)

            with open(file_path, "w") as file: 
                #write the update data to the file 
                json.dump(existing_data, file, indent=4)
                print(f"\nData Appended to {file_path}")

#Can call whenever we want 


# JSON expects key and string values 
# "Name":"John" - has to always be a string. numbers in "", boolean, lists, null and dicts

# when saving - if self.__sport == Sport.Boxing: 
#               return "Boxing"


# when loaing - if sportStr == "Boxing": 
#               sport = Sport.Boxing


#User / JSON → "Boxing"
#        ↓
#Convert → Sport.BOXING   (your if/elif logic)
#        ↓
#Program logic runs safely
#        ↓
#Convert back → "Boxing"
#        ↓
#Saved to JSON