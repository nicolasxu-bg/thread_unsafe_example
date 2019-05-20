# thread_unsafe_example

Here is the callback chain for
InterventionRequestsObservable.process_intervention_request_state()
-> InterventionResolver
-> InterventionObserver
-> DistributedDictionary
-> PollingProducer
-> as_ioloop_callback() (bg_utils)
-> io_loop.add_callback (Tornado)

Here is the quote for add_callback document
https://www.tornadoweb.org/en/stable/ioloop.html
It is safe to call this method from any thread at any time, except from a signal handler. Note that this is the only method in IOLoop that makes this thread-safety guarantee; all other interaction with the IOLoop must be done from that IOLoop’s thread. add_callback() may be used to transfer control from other threads to the IOLoop’s thread.


