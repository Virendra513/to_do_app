from bson import ObjectId
def serialize_document(document):
    return{
        **document,
        "_id": str(document["_id"]),

        "id": str(document["_id"]),  # map MongoDB _id to id
        "name": document["name"],    # include other fields you need
        # include more fields if needed
    }

