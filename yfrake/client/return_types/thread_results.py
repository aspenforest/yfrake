# ==================================================================================== #
#    thread_results.py - This file is part of the YFrake package.                      #
# ------------------------------------------------------------------------------------ #
#                                                                                      #
#    MIT License                                                                       #
#                                                                                      #
#    Copyright (c) 2022 Mattias Aabmets                                                #
#                                                                                      #
#    Permission is hereby granted, free of charge, to any person obtaining a copy      #
#    of this software and associated documentation files (the "Software"), to deal     #
#    in the Software without restriction, including without limitation the rights      #
#    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell         #
#    copies of the Software, and to permit persons to whom the Software is             #
#    furnished to do so, subject to the following conditions:                          #
#                                                                                      #
#    The above copyright notice and this permission notice shall be included in all    #
#    copies or substantial portions of the Software.                                   #
#                                                                                      #
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR        #
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,          #
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE       #
#    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER            #
#    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,     #
#    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE     #
#    SOFTWARE.                                                                         #
#                                                                                      #
# ==================================================================================== #
from .client_response import ClientResponse
from .base_results import BaseResults
from concurrent import futures


# ==================================================================================== #
class ThreadResults(BaseResults):
    """
    A custom iterable returned by the
    'batch_get' method in sync mode.
    """
    # ------------------------------------------------------------------------------------ #
    def __init__(self, requests: dict):
        super().__init__(requests)

    # ------------------------------------------------------------------------------------ #
    def wait(self) -> None:
        futures.wait(self._future_objects)

    # ------------------------------------------------------------------------------------ #
    def gather(self) -> ClientResponse:
        self.wait()
        for resp in self._response_objects:
            yield resp

    # ------------------------------------------------------------------------------------ #
    def as_completed(self) -> ClientResponse:
        for future in futures.as_completed(self._future_objects):
            result = future.result()
            yield result
