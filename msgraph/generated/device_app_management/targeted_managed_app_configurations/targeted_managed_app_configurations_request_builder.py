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
    from ...models.o_data_errors.o_data_error import ODataError
    from ...models.targeted_managed_app_configuration import TargetedManagedAppConfiguration
    from ...models.targeted_managed_app_configuration_collection_response import TargetedManagedAppConfigurationCollectionResponse
    from .count.count_request_builder import CountRequestBuilder
    from .item.targeted_managed_app_configuration_item_request_builder import TargetedManagedAppConfigurationItemRequestBuilder

class TargetedManagedAppConfigurationsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the targetedManagedAppConfigurations property of the microsoft.graph.deviceAppManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new TargetedManagedAppConfigurationsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceAppManagement/targetedManagedAppConfigurations{?%24count,%24expand,%24filter,%24orderby,%24search,%24select,%24skip,%24top}", path_parameters)
    
    def by_targeted_managed_app_configuration_id(self,targeted_managed_app_configuration_id: str) -> TargetedManagedAppConfigurationItemRequestBuilder:
        """
        Provides operations to manage the targetedManagedAppConfigurations property of the microsoft.graph.deviceAppManagement entity.
        param targeted_managed_app_configuration_id: The unique identifier of targetedManagedAppConfiguration
        Returns: TargetedManagedAppConfigurationItemRequestBuilder
        """
        if not targeted_managed_app_configuration_id:
            raise TypeError("targeted_managed_app_configuration_id cannot be null.")
        from .item.targeted_managed_app_configuration_item_request_builder import TargetedManagedAppConfigurationItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["targetedManagedAppConfiguration%2Did"] = targeted_managed_app_configuration_id
        return TargetedManagedAppConfigurationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[TargetedManagedAppConfigurationCollectionResponse]:
        """
        Targeted managed app configurations.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TargetedManagedAppConfigurationCollectionResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.targeted_managed_app_configuration_collection_response import TargetedManagedAppConfigurationCollectionResponse

        return await self.request_adapter.send_async(request_info, TargetedManagedAppConfigurationCollectionResponse, error_mapping)
    
    async def post(self,body: Optional[TargetedManagedAppConfiguration] = None, request_configuration: Optional[RequestConfiguration] = None) -> Optional[TargetedManagedAppConfiguration]:
        """
        Create new navigation property to targetedManagedAppConfigurations for deviceAppManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TargetedManagedAppConfiguration]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.targeted_managed_app_configuration import TargetedManagedAppConfiguration

        return await self.request_adapter.send_async(request_info, TargetedManagedAppConfiguration, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Targeted managed app configurations.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: Optional[TargetedManagedAppConfiguration] = None, request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Create new navigation property to targetedManagedAppConfigurations for deviceAppManagement
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
    
    def with_url(self,raw_url: Optional[str] = None) -> TargetedManagedAppConfigurationsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TargetedManagedAppConfigurationsRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return TargetedManagedAppConfigurationsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class TargetedManagedAppConfigurationsRequestBuilderGetQueryParameters():
        """
        Targeted managed app configurations.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
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

    

