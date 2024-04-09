from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...........models.o_data_errors.o_data_error import ODataError
    from .image_with_width_with_height_with_fitting_mode_get_response import ImageWithWidthWithHeightWithFittingModeGetResponse

class ImageWithWidthWithHeightWithFittingModeRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the image method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]], fitting_mode: Optional[str] = None, height: Optional[int] = None, width: Optional[int] = None) -> None:
        """
        Instantiates a new ImageWithWidthWithHeightWithFittingModeRequestBuilder and sets the default values.
        param fitting_mode: Usage: fittingMode='{fittingMode}'
        param height: Usage: height={height}
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        param width: Usage: width={width}
        Returns: None
        """
        if isinstance(path_parameters, dict):
            path_parameters['fittingMode'] = str(fitting_mode)
            path_parameters['height'] = str(height)
            path_parameters['width'] = str(width)
        super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/worksheets/{workbookWorksheet%2Did}/charts/itemAt(index={index})/image(width={width},height={height},fittingMode='{fittingMode}')", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[ImageWithWidthWithHeightWithFittingModeGetResponse]:
        """
        Invoke function image
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ImageWithWidthWithHeightWithFittingModeGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .image_with_width_with_height_with_fitting_mode_get_response import ImageWithWidthWithHeightWithFittingModeGetResponse

        return await self.request_adapter.send_async(request_info, ImageWithWidthWithHeightWithFittingModeGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Invoke function image
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> ImageWithWidthWithHeightWithFittingModeRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ImageWithWidthWithHeightWithFittingModeRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return ImageWithWidthWithHeightWithFittingModeRequestBuilder(self.request_adapter, raw_url)
    

