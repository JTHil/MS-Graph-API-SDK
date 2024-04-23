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
    from ....models.o_data_errors.o_data_error import ODataError
    from .export_personal_data_post_request_body import ExportPersonalDataPostRequestBody

class ExportPersonalDataRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the exportPersonalData method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new ExportPersonalDataRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/exportPersonalData", path_parameters)
    
    async def post(self,body: Optional[ExportPersonalDataPostRequestBody] = None, request_configuration: Optional[RequestConfiguration] = None) -> None:
        """
        Submit a data policy operation request from a company administrator or an application to export an organizational user's data. This data includes the user's data stored in OneDrive and their activity reports. For more information about exporting data while complying with regulations, see Data Subject Requests and the GDPR and CCPA.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/user-exportpersonaldata?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    def to_post_request_information(self,body: Optional[ExportPersonalDataPostRequestBody] = None, request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Submit a data policy operation request from a company administrator or an application to export an organizational user's data. This data includes the user's data stored in OneDrive and their activity reports. For more information about exporting data while complying with regulations, see Data Subject Requests and the GDPR and CCPA.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> ExportPersonalDataRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ExportPersonalDataRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return ExportPersonalDataRequestBuilder(self.request_adapter, raw_url)
    

