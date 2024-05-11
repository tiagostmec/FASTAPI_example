from fastapi import APIRouter, Query
from fastapi_utils.cbv import cbv
from schema.schema_spectrum_proc import SpectrumRequest, SpectrumResponse
from services.spectrum_service.srv_spectrum_proc import classify

router = APIRouter()
'''
Call cbv for class based 
'''
@cbv(router)
class ProcessSpectrum:
    @router.post("/", response_model=SpectrumResponse)
    async def spectrumpost(self, params: SpectrumRequest):
        """
        Endpoint to classify the data ("processing") the spectrum of a signal with a dummy dataset
        using a SVM.

        Parameters:
        - frequencies: Frequencys from data processing (List[float])
        - amplitudes: Amplitude data from signal (List[float])

        Returns:
        - A JSON object containing the status of the request, and accuracy
        """
        accuracy = classify(params.frequencies, params.amplitudes)
        return {"status": "success", "accuracy": accuracy}