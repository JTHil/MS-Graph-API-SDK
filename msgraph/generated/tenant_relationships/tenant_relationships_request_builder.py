from __future__ import annotations
from dataclasses import dataclass, field
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
    from ..models.o_data_errors.o_data_error import ODataError
    from ..models.tenant_relationship import TenantRelationship
    from .delegated_admin_customers.delegated_admin_customers_request_builder import DelegatedAdminCustomersRequestBuilder
    from .delegated_admin_relationships.delegated_admin_relationships_request_builder import DelegatedAdminRelationshipsRequestBuilder
    from .find_tenant_information_by_domain_name_with_domain_name.find_tenant_information_by_domain_name_with_domain_name_request_builder import FindTenantInformationByDomainNameWithDomainNameRequestBuilder
    from .find_tenant_information_by_tenant_id_with_tenant_id.find_tenant_information_by_tenant_id_with_tenant_id_request_builder import FindTenantInformationByTenantIdWithTenantIdRequestBuilder

class TenantRelationshipsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the tenantRelationship singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new TenantRelationshipsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/tenantRelationships{?%24expand,%24select}", path_parameters)
    
    def find_tenant_information_by_domain_name_with_domain_name(self,domain_name: Optional[str] = None) -> FindTenantInformationByDomainNameWithDomainNameRequestBuilder:
        """
        Provides operations to call the findTenantInformationByDomainName method.
        param domain_name: Usage: domainName='{domainName}'
        Returns: FindTenantInformationByDomainNameWithDomainNameRequestBuilder
        """
        if not domain_name:
            raise TypeError("domain_name cannot be null.")
        from .find_tenant_information_by_domain_name_with_domain_name.find_tenant_information_by_domain_name_with_domain_name_request_builder import FindTenantInformationByDomainNameWithDomainNameRequestBuilder

        return FindTenantInformationByDomainNameWithDomainNameRequestBuilder(self.request_adapter, self.path_parameters, domain_name)
    
    def find_tenant_information_by_tenant_id_with_tenant_id(self,tenant_id: Optional[str] = None) -> FindTenantInformationByTenantIdWithTenantIdRequestBuilder:
        """
        Provides operations to call the findTenantInformationByTenantId method.
        param tenant_id: Usage: tenantId='{tenantId}'
        Returns: FindTenantInformationByTenantIdWithTenantIdRequestBuilder
        """
        if not tenant_id:
            raise TypeError("tenant_id cannot be null.")
        from .find_tenant_information_by_tenant_id_with_tenant_id.find_tenant_information_by_tenant_id_with_tenant_id_request_builder import FindTenantInformationByTenantIdWithTenantIdRequestBuilder

        return FindTenantInformationByTenantIdWithTenantIdRequestBuilder(self.request_adapter, self.path_parameters, tenant_id)
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[TenantRelationship]:
        """
        Get tenantRelationships
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TenantRelationship]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.tenant_relationship import TenantRelationship

        return await self.request_adapter.send_async(request_info, TenantRelationship, error_mapping)
    
    async def patch(self,body: Optional[TenantRelationship] = None, request_configuration: Optional[RequestConfiguration] = None) -> Optional[TenantRelationship]:
        """
        Update tenantRelationships
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TenantRelationship]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.tenant_relationship import TenantRelationship

        return await self.request_adapter.send_async(request_info, TenantRelationship, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Get tenantRelationships
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[TenantRelationship] = None, request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Update tenantRelationships
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> TenantRelationshipsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TenantRelationshipsRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return TenantRelationshipsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def delegated_admin_customers(self) -> DelegatedAdminCustomersRequestBuilder:
        """
        Provides operations to manage the delegatedAdminCustomers property of the microsoft.graph.tenantRelationship entity.
        """
        from .delegated_admin_customers.delegated_admin_customers_request_builder import DelegatedAdminCustomersRequestBuilder

        return DelegatedAdminCustomersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def delegated_admin_relationships(self) -> DelegatedAdminRelationshipsRequestBuilder:
        """
        Provides operations to manage the delegatedAdminRelationships property of the microsoft.graph.tenantRelationship entity.
        """
        from .delegated_admin_relationships.delegated_admin_relationships_request_builder import DelegatedAdminRelationshipsRequestBuilder

        return DelegatedAdminRelationshipsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class TenantRelationshipsRequestBuilderGetQueryParameters():
        """
        Get tenantRelationships
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

    

