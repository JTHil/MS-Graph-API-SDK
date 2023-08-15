from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.o_data_errors.o_data_error import ODataError
    from .....models.update_recording_status_operation import UpdateRecordingStatusOperation
    from .update_recording_status_post_request_body import UpdateRecordingStatusPostRequestBody

class UpdateRecordingStatusRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the updateRecordingStatus method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new UpdateRecordingStatusRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/communications/calls/{call%2Did}/updateRecordingStatus", path_parameters)
    
    async def post(self,body: Optional[UpdateRecordingStatusPostRequestBody] = None, request_configuration: Optional[UpdateRecordingStatusRequestBuilderPostRequestConfiguration] = None) -> Optional[UpdateRecordingStatusOperation]:
        """
        Update the application's recording status associated with a call. This requires the use of the Teams policy-based recording solution.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[UpdateRecordingStatusOperation]
        Find more info here: https://learn.microsoft.com/graph/api/call-updaterecordingstatus?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.update_recording_status_operation import UpdateRecordingStatusOperation

        return await self.request_adapter.send_async(request_info, UpdateRecordingStatusOperation, error_mapping)
    
    def to_post_request_information(self,body: Optional[UpdateRecordingStatusPostRequestBody] = None, request_configuration: Optional[UpdateRecordingStatusRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Update the application's recording status associated with a call. This requires the use of the Teams policy-based recording solution.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.POST
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class UpdateRecordingStatusRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

