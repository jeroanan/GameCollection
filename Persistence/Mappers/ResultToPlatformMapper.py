from Platform import Platform


class ResultToPlatformMapper(object):
    def map(self, mongo_result):
        platform = Platform()
        platform.id = mongo_result["_id"]
        platform.name = mongo_result["_Platform__name"]
        platform.description = mongo_result["_Platform__description"]
        return platform
