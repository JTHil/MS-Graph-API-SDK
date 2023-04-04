from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models import delegated_admin_relationship
    from ....models.o_data_errors import o_data_error
    from .access_assignments import access_assignments_request_builder
    from .access_assignments.item import delegated_admin_access_assignment_item_request_builder
    from .operations import operations_request_builder
    from .operations.item import delegated_admin_relationship_operation_item_request_builder
    from .requests import requests_request_builder
    from .requests.item import delegated_admin_relationship_request_item_request_builder

class DelegatedAdminRelationshipItemRequestBuilder():
    """
    Provides operations to manage the delegatedAdminRelationships property of the microsoft.graph.tenantRelationship entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DelegatedAdminRelationshipItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/tenantRelationships/delegatedAdminRelationships/{delegatedAdminRelationship%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def access_assignments_by_id(self,id: str) -> delegated_admin_access_assignment_item_request_builder.DelegatedAdminAccessAssignmentItemRequestBuilder:
        """
        Provides operations to manage the accessAssignments property of the microsoft.graph.delegatedAdminRelationship entity.
        Args:
            id: Unique identifier of the item
        Returns: delegated_admin_access_assignment_item_request_builder.DelegatedAdminAccessAssignmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .access_assignments.item import delegated_admin_access_assignment_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["delegatedAdminAccessAssignment%2Did"] = id
        return delegated_admin_access_assignment_item_request_builder.DelegatedAdminAccessAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[DelegatedAdminRelationshipItemRequestBuilderDeleteRequestConfiguration] = None) -> bytes:
        """
        Delete navigation property delegatedAdminRelationships for tenantRelationships
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    async def get(self,request_configuration: Optional[DelegatedAdminRelationshipItemRequestBuilderGetRequestConfiguration] = None) -> Optional[delegated_admin_relationship.DelegatedAdminRelationship]:
        """
        The details of the delegated administrative privileges that a Microsoft partner has in a customer tenant.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[delegated_admin_relationship.DelegatedAdminRelationship]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models import delegated_admin_relationship

        return await self.request_adapter.send_async(request_info, delegated_admin_relationship.DelegatedAdminRelationship, error_mapping)
    
    def operations_by_id(self,id: str) -> delegated_admin_relationship_operation_item_request_builder.DelegatedAdminRelationshipOperationItemRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.delegatedAdminRelationship entity.
        Args:
            id: Unique identifier of the item
        Returns: delegated_admin_relationship_operation_item_request_builder.DelegatedAdminRelationshipOperationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .operations.item import delegated_admin_relationship_operation_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["delegatedAdminRelationshipOperation%2Did"] = id
        return delegated_admin_relationship_operation_item_request_builder.DelegatedAdminRelationshipOperationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[delegated_admin_relationship.DelegatedAdminRelationship] = None, request_configuration: Optional[DelegatedAdminRelationshipItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[delegated_admin_relationship.DelegatedAdminRelationship]:
        """
        Update the navigation property delegatedAdminRelationships in tenantRelationships
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[delegated_admin_relationship.DelegatedAdminRelationship]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models import delegated_admin_relationship

        return await self.request_adapter.send_async(request_info, delegated_admin_relationship.DelegatedAdminRelationship, error_mapping)
    
    def requests_by_id(self,id: str) -> delegated_admin_relationship_request_item_request_builder.DelegatedAdminRelationshipRequestItemRequestBuilder:
        """
        Provides operations to manage the requests property of the microsoft.graph.delegatedAdminRelationship entity.
        Args:
            id: Unique identifier of the item
        Returns: delegated_admin_relationship_request_item_request_builder.DelegatedAdminRelationshipRequestItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .requests.item import delegated_admin_relationship_request_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["delegatedAdminRelationshipRequest%2Did"] = id
        return delegated_admin_relationship_request_item_request_builder.DelegatedAdminRelationshipRequestItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[DelegatedAdminRelationshipItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property delegatedAdminRelationships for tenantRelationships
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
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
        The details of the delegated administrative privileges that a Microsoft partner has in a customer tenant.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
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
    
    def to_patch_request_information(self,body: Optional[delegated_admin_relationship.DelegatedAdminRelationship] = None, request_configuration: Optional[DelegatedAdminRelationshipItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property delegatedAdminRelationships in tenantRelationships
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
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
    def access_assignments(self) -> access_assignments_request_builder.AccessAssignmentsRequestBuilder:
        """
        Provides operations to manage the accessAssignments property of the microsoft.graph.delegatedAdminRelationship entity.
        """
        from .access_assignments import access_assignments_request_builder

        return access_assignments_request_builder.AccessAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def operations(self) -> operations_request_builder.OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.delegatedAdminRelationship entity.
        """
        from .operations import operations_request_builder

        return operations_request_builder.OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def requests(self) -> requests_request_builder.RequestsRequestBuilder:
        """
        Provides operations to manage the requests property of the microsoft.graph.delegatedAdminRelationship entity.
        """
        from .requests import requests_request_builder

        return requests_request_builder.RequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class DelegatedAdminRelationshipItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class DelegatedAdminRelationshipItemRequestBuilderGetQueryParameters():
        """
        The details of the delegated administrative privileges that a Microsoft partner has in a customer tenant.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class DelegatedAdminRelationshipItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[DelegatedAdminRelationshipItemRequestBuilder.DelegatedAdminRelationshipItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class DelegatedAdminRelationshipItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

