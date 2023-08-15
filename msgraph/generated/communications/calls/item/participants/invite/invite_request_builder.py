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
    from ......models.invite_participants_operation import InviteParticipantsOperation
    from ......models.o_data_errors.o_data_error import ODataError
    from .invite_post_request_body import InvitePostRequestBody

class InviteRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the invite method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new InviteRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/communications/calls/{call%2Did}/participants/invite", path_parameters)
    
    async def post(self,body: Optional[InvitePostRequestBody] = None, request_configuration: Optional[InviteRequestBuilderPostRequestConfiguration] = None) -> Optional[InviteParticipantsOperation]:
        """
        Invite participants to the active call. For more information about how to handle operations, see commsOperation.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[InviteParticipantsOperation]
        Find more info here: https://learn.microsoft.com/graph/api/participant-invite?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.invite_participants_operation import InviteParticipantsOperation

        return await self.request_adapter.send_async(request_info, InviteParticipantsOperation, error_mapping)
    
    def to_post_request_information(self,body: Optional[InvitePostRequestBody] = None, request_configuration: Optional[InviteRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Invite participants to the active call. For more information about how to handle operations, see commsOperation.
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
    class InviteRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

