from .. import models
import datetime

class IdDistributorService:
    @staticmethod
    def gen_next_id(prefix):
        records = models.IdDistributor.objects.select_for_update().filter(prefix = prefix)
        next_id = records[0].last_id + 1
        records.update(last_id=next_id, at=datetime.datetime.now())
        return '{}_{:=05d}'.format(prefix, next_id)