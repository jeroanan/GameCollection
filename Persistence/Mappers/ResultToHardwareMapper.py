from Hardware import Hardware
from Persistence.Exceptions.HardwareNotFoundException import HardwareNotFoundException


class ResultToHardwareMapper(object):

    def map(self, mongo_result):
        if mongo_result is None:
            raise HardwareNotFoundException()
        hardware = Hardware()
        hardware.id = mongo_result["_id"]
        hardware.name = mongo_result["_Hardware__name"]
        hardware.platform = mongo_result["_Hardware__platform"]
        hardware.num_owned = mongo_result["_Hardware__num_owned"]
        hardware.num_boxed = mongo_result["_Hardware__num_boxed"]

        if "_Hardware__notes" in mongo_result:
            hardware.notes = mongo_result["_Hardware__notes"]

        return hardware