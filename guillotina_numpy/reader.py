import numpy
import io


def reader(result):
    buff = io.BytesIO(result['state'])
    from guillotina_numpy.field import NumPyData
    obj = NumPyData()
    obj.value = numpy.load(buff)['v']
    obj._p_oid = result['zoid']
    obj._p_serial = result['tid']
    obj.__name__ = result['id']
    return obj
