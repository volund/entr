
def common_keys(dict1, dict2):
    keys1 = set(dict1.keys())
    keys2 = set(dict2.keys())
    return keys1.intersection(keys2)

def common_keys_with_common_values(dict1, dict2):
    common_keys = common_keys(dict1, dict2)
    common_kv = [key for key in common_keys if dict1[key] == dict2[key]]
    return common_kv

def dictionary_with_common_values(dict1, dict2):
    common_kvs = common_keys_with_common_values(dict1, dict2)
    common_dict = {key:dict1[key] for key in common_kvs}
    return common_dict

def apply_metadata_dictionary(metadata, unsorted_files):
    for unsorted_file in unsorted_files:
        unsorted_file.update(metadata)
