from fastapi import APIRouter, Query, HTTPException
from fastapi_utils.cbv import cbv
from services.spectrum_service.srv_spectrum import get_spectrum

router = APIRouter()
'''
Call cbv for class based 
'''
@cbv(router)
class GetSpectrum:
    @router.get("/")
    async def spectrum(self, nperseg: int = Query(..., description="Number of samples per segment."),
                    window: str = Query(..., description="Window to use.")):
        
        '''
        Checks input data for crash avoiding (test results)
        
        For window i choose to lock hann type only for convenience, but the ideal is
        to make an array or list with all valid types described in 
        https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.get_window.html
        '''

        if nperseg <= 0 or nperseg > 100000:
            raise HTTPException(status_code=422, detail="nperseg must be a positive integer and between 1 and 100000")
        if window != "hann":
            raise HTTPException(status_code=422, detail="window must be hann")
        
        """
        Endpoint to retrieve the spectrum of a processed signal

        Parameters:
        - nperseg: Number of samples per segment
        - window: Window function to use

        Returns:
        - A JSON object containing the status of the request, frequencies, and amplitudes
        """
        
        f, Pxx = get_spectrum(nperseg, window)
        return {"status": "success", "frequencies": f.tolist(), "amplitudes": Pxx.tolist()}