def convert_string_for_req(query):
    return "+".join(query.split())

def convert_string_from_req(query):
    return " ".join(query.split("+"))