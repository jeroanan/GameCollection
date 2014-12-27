from Hardware import Hardware


class ResultToHardwareMapper(object):

    def map(self, mongo_result):
        hardware = Hardware()
        hardware.id = mongo_result["_id"]
        hardware.name = mongo_result["_Hardware__name"]
        hardware.platform = mongo_result["_Hardware__platform"]
        hardware.numowned = mongo_result["_Hardware__num_owned"]
        hardware.numboxed = mongo_result["_Hardware__num_boxed"]

        if "_Hardware__notes" in mongo_result:
            hardware.notes = mongo_result["_Hardware__notes"]

        return hardware