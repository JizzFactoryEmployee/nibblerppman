import nibbler.trading.collectors.futures_collector as futures
import nibbler.trading.collectors.MYSQL.pushtodb as push
import multiprocessing
import time
from lastversion import MyHandler
from nibbler.trading.collectors.poo import MyHandlerTHETA
# def CollectNPush():
#     BTCrun = multiprocessing.Process(target=futures.BinanceBTC.BTCcollector1m, name='BTCrun')
#     BTCpush = multiprocessing.Process(target=MyHandler.runner, name='BTCpush')
#     THETArun = multiprocessing.Process(target=futures.BinanceTHETA.THETAcollector1m,name='BTCrun')
#     THETApush = multiprocessing.Process(target=MyHandlerTHETA.runner, name='BTCpush')

  

if __name__ == "__main__":
    import multiprocessing
    BTCrun = multiprocessing.Process(target=futures.BinanceBTC.BTCcollector1m, name='BTCrun')
    BTCpush = multiprocessing.Process(target=MyHandler.runner, name='BTCpush')
    THETArun = multiprocessing.Process(target=futures.BinanceTHETA.THETAcollector1m,name='BTCrun')
    THETApush = multiprocessing.Process(target=MyHandlerTHETA.runner, name='BTCpush')

    BTCrun.start()
    BTCpush.start()
    THETArun.start()
    THETApush.start()
