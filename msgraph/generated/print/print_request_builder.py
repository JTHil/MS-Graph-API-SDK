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
    from ..models.o_data_errors.o_data_error import ODataError
    from ..models.print import Print
    from .connectors.connectors_request_builder import ConnectorsRequestBuilder
    from .operations.operations_request_builder import OperationsRequestBuilder
    from .printers.printers_request_builder import PrintersRequestBuilder
    from .services.services_request_builder import ServicesRequestBuilder
    from .shares.shares_request_builder import SharesRequestBuilder
    from .task_definitions.task_definitions_request_builder import TaskDefinitionsRequestBuilder

class PrintRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the print singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new PrintRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/print{?%24select,%24expand}", path_parameters)
    
    async def get(self,request_configuration: Optional[PrintRequestBuilderGetRequestConfiguration] = None) -> Optional[Print]:
        """
        Get print
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Print]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.print import Print

        return await self.request_adapter.send_async(request_info, Print, error_mapping)
    
    async def patch(self,body: Optional[Print] = None, request_configuration: Optional[PrintRequestBuilderPatchRequestConfiguration] = None) -> Optional[Print]:
        """
        Update print
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Print]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.print import Print

        return await self.request_adapter.send_async(request_info, Print, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[PrintRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get print
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[Print] = None, request_configuration: Optional[PrintRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update print
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def connectors(self) -> ConnectorsRequestBuilder:
        """
        Provides operations to manage the connectors property of the microsoft.graph.print entity.
        """
        from .connectors.connectors_request_builder import ConnectorsRequestBuilder

        return ConnectorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def operations(self) -> OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.print entity.
        """
        from .operations.operations_request_builder import OperationsRequestBuilder

        return OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def printers(self) -> PrintersRequestBuilder:
        """
        Provides operations to manage the printers property of the microsoft.graph.print entity.
        """
        from .printers.printers_request_builder import PrintersRequestBuilder

        return PrintersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def services(self) -> ServicesRequestBuilder:
        """
        Provides operations to manage the services property of the microsoft.graph.print entity.
        """
        from .services.services_request_builder import ServicesRequestBuilder

        return ServicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def shares(self) -> SharesRequestBuilder:
        """
        Provides operations to manage the shares property of the microsoft.graph.print entity.
        """
        from .shares.shares_request_builder import SharesRequestBuilder

        return SharesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def task_definitions(self) -> TaskDefinitionsRequestBuilder:
        """
        Provides operations to manage the taskDefinitions property of the microsoft.graph.print entity.
        """
        from .task_definitions.task_definitions_request_builder import TaskDefinitionsRequestBuilder

        return TaskDefinitionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PrintRequestBuilderGetQueryParameters():
        """
        Get print
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class PrintRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[PrintRequestBuilder.PrintRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class PrintRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

