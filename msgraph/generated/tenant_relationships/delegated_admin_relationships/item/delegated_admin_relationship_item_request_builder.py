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
    from ....models.delegated_admin_relationship import DelegatedAdminRelationship
    from ....models.o_data_errors.o_data_error import ODataError
    from .access_assignments.access_assignments_request_builder import AccessAssignmentsRequestBuilder
    from .operations.operations_request_builder import OperationsRequestBuilder
    from .requests.requests_request_builder import RequestsRequestBuilder

class DelegatedAdminRelationshipItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the delegatedAdminRelationships property of the microsoft.graph.tenantRelationship entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DelegatedAdminRelationshipItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/tenantRelationships/delegatedAdminRelationships/{delegatedAdminRelationship%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[DelegatedAdminRelationshipItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete a delegatedAdminRelationship object. A relationship can only be deleted if it's in the 'created' status. 
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/delegatedadminrelationship-delete?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[DelegatedAdminRelationshipItemRequestBuilderGetRequestConfiguration] = None) -> Optional[DelegatedAdminRelationship]:
        """
        Read the properties of a delegatedAdminRelationship object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DelegatedAdminRelationship]
        Find more info here: https://learn.microsoft.com/graph/api/delegatedadminrelationship-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.delegated_admin_relationship import DelegatedAdminRelationship

        return await self.request_adapter.send_async(request_info, DelegatedAdminRelationship, error_mapping)
    
    async def patch(self,body: Optional[DelegatedAdminRelationship] = None, request_configuration: Optional[DelegatedAdminRelationshipItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[DelegatedAdminRelationship]:
        """
        Update the properties of a delegatedAdminRelationship object. A relationship can only be updated if it's in the created status.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DelegatedAdminRelationship]
        Find more info here: https://learn.microsoft.com/graph/api/delegatedadminrelationship-update?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.delegated_admin_relationship import DelegatedAdminRelationship

        return await self.request_adapter.send_async(request_info, DelegatedAdminRelationship, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[DelegatedAdminRelationshipItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete a delegatedAdminRelationship object. A relationship can only be deleted if it's in the 'created' status. 
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[DelegatedAdminRelationshipItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Read the properties of a delegatedAdminRelationship object.
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
    
    def to_patch_request_information(self,body: Optional[DelegatedAdminRelationship] = None, request_configuration: Optional[DelegatedAdminRelationshipItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of a delegatedAdminRelationship object. A relationship can only be updated if it's in the created status.
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
    def access_assignments(self) -> AccessAssignmentsRequestBuilder:
        """
        Provides operations to manage the accessAssignments property of the microsoft.graph.delegatedAdminRelationship entity.
        """
        from .access_assignments.access_assignments_request_builder import AccessAssignmentsRequestBuilder

        return AccessAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def operations(self) -> OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.delegatedAdminRelationship entity.
        """
        from .operations.operations_request_builder import OperationsRequestBuilder

        return OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def requests(self) -> RequestsRequestBuilder:
        """
        Provides operations to manage the requests property of the microsoft.graph.delegatedAdminRelationship entity.
        """
        from .requests.requests_request_builder import RequestsRequestBuilder

        return RequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class DelegatedAdminRelationshipItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class DelegatedAdminRelationshipItemRequestBuilderGetQueryParameters():
        """
        Read the properties of a delegatedAdminRelationship object.
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
    class DelegatedAdminRelationshipItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[DelegatedAdminRelationshipItemRequestBuilder.DelegatedAdminRelationshipItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class DelegatedAdminRelationshipItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

