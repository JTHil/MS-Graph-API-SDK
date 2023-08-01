from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.access_package_assignment_policy import AccessPackageAssignmentPolicy
    from ....models.access_package_assignment_policy_collection_response import AccessPackageAssignmentPolicyCollectionResponse
    from ....models.o_data_errors.o_data_error import ODataError
    from .count.count_request_builder import CountRequestBuilder
    from .item.access_package_assignment_policy_item_request_builder import AccessPackageAssignmentPolicyItemRequestBuilder

class AssignmentPoliciesRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the assignmentPolicies property of the microsoft.graph.entitlementManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AssignmentPoliciesRequestBuilder and sets the default values.
        Args:
            path_parameters: The raw url or the Url template parameters for the request.
            request_adapter: The request adapter to use to execute the requests.
        """
        super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement/assignmentPolicies{?%24top,%24skip,%24search,%24filter,%24count,%24orderby,%24select,%24expand}", path_parameters)
    
    def by_access_package_assignment_policy_id(self,access_package_assignment_policy_id: str) -> AccessPackageAssignmentPolicyItemRequestBuilder:
        """
        Provides operations to manage the assignmentPolicies property of the microsoft.graph.entitlementManagement entity.
        Args:
            access_package_assignment_policy_id: Unique identifier of the item
        Returns: AccessPackageAssignmentPolicyItemRequestBuilder
        """
        if not access_package_assignment_policy_id:
            raise TypeError("access_package_assignment_policy_id cannot be null.")
        from .item.access_package_assignment_policy_item_request_builder import AccessPackageAssignmentPolicyItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["accessPackageAssignmentPolicy%2Did"] = access_package_assignment_policy_id
        return AccessPackageAssignmentPolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[AssignmentPoliciesRequestBuilderGetRequestConfiguration] = None) -> Optional[AccessPackageAssignmentPolicyCollectionResponse]:
        """
        In Azure AD entitlement management, retrieve a list of accessPackageAssignmentPolicy objects. If the delegated user is in a directory role, the resulting list includes all the assignment policies that the caller has access to read, across all catalogs and access packages. If the delegated user is an access package manager or catalog owner, they should instead retrieve the policies for the access packages they can read with list accessPackages by including $expand=accessPackageAssignmentPolicies as a query parameter.
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AccessPackageAssignmentPolicyCollectionResponse]
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
        from ....models.access_package_assignment_policy_collection_response import AccessPackageAssignmentPolicyCollectionResponse

        return await self.request_adapter.send_async(request_info, AccessPackageAssignmentPolicyCollectionResponse, error_mapping)
    
    async def post(self,body: Optional[AccessPackageAssignmentPolicy] = None, request_configuration: Optional[AssignmentPoliciesRequestBuilderPostRequestConfiguration] = None) -> Optional[AccessPackageAssignmentPolicy]:
        """
        In Azure AD entitlement management, create a new accessPackageAssignmentPolicy object.  The request will include a reference to the accessPackage that will contain this policy, which must already exist.
        Args:
            body: The request body
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AccessPackageAssignmentPolicy]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.access_package_assignment_policy import AccessPackageAssignmentPolicy

        return await self.request_adapter.send_async(request_info, AccessPackageAssignmentPolicy, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[AssignmentPoliciesRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        In Azure AD entitlement management, retrieve a list of accessPackageAssignmentPolicy objects. If the delegated user is in a directory role, the resulting list includes all the assignment policies that the caller has access to read, across all catalogs and access packages. If the delegated user is an access package manager or catalog owner, they should instead retrieve the policies for the access packages they can read with list accessPackages by including $expand=accessPackageAssignmentPolicies as a query parameter.
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
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
    
    def to_post_request_information(self,body: Optional[AccessPackageAssignmentPolicy] = None, request_configuration: Optional[AssignmentPoliciesRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        In Azure AD entitlement management, create a new accessPackageAssignmentPolicy object.  The request will include a reference to the accessPackage that will contain this policy, which must already exist.
        Args:
            body: The request body
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
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
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class AssignmentPoliciesRequestBuilderGetQueryParameters():
        """
        In Azure AD entitlement management, retrieve a list of accessPackageAssignmentPolicy objects. If the delegated user is in a directory role, the resulting list includes all the assignment policies that the caller has access to read, across all catalogs and access packages. If the delegated user is an access package manager or catalog owner, they should instead retrieve the policies for the access packages they can read with list accessPackages by including $expand=accessPackageAssignmentPolicies as a query parameter.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "count":
                return "%24count"
            if original_name == "expand":
                return "%24expand"
            if original_name == "filter":
                return "%24filter"
            if original_name == "orderby":
                return "%24orderby"
            if original_name == "search":
                return "%24search"
            if original_name == "select":
                return "%24select"
            if original_name == "skip":
                return "%24skip"
            if original_name == "top":
                return "%24top"
            return original_name
        
        # Include count of items
        count: Optional[bool] = None

        # Expand related entities
        expand: Optional[List[str]] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Order items by property values
        orderby: Optional[List[str]] = None

        # Search items by search phrases
        search: Optional[str] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        # Skip the first n items
        skip: Optional[int] = None

        # Show only the first n items
        top: Optional[int] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class AssignmentPoliciesRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[AssignmentPoliciesRequestBuilder.AssignmentPoliciesRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class AssignmentPoliciesRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

