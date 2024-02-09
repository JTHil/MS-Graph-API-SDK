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
    from ....models.o_data_errors.o_data_error import ODataError
    from ....models.profile_photo_collection_response import ProfilePhotoCollectionResponse
    from .item.profile_photo_item_request_builder import ProfilePhotoItemRequestBuilder

class PhotosRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the photos property of the microsoft.graph.group entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new PhotosRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/photos{?%24filter,%24orderby,%24select,%24skip,%24top}", path_parameters)
    
    def by_profile_photo_id(self,profile_photo_id: str) -> ProfilePhotoItemRequestBuilder:
        """
        Provides operations to manage the photos property of the microsoft.graph.group entity.
        param profile_photo_id: The unique identifier of profilePhoto
        Returns: ProfilePhotoItemRequestBuilder
        """
        if not profile_photo_id:
            raise TypeError("profile_photo_id cannot be null.")
        from .item.profile_photo_item_request_builder import ProfilePhotoItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["profilePhoto%2Did"] = profile_photo_id
        return ProfilePhotoItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[ProfilePhotoCollectionResponse]:
        """
        Retrieve a list of profilePhoto objects.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ProfilePhotoCollectionResponse]
        Find more info here: https://learn.microsoft.com/graph/api/group-list-photos?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.profile_photo_collection_response import ProfilePhotoCollectionResponse

        return await self.request_adapter.send_async(request_info, ProfilePhotoCollectionResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve a list of profilePhoto objects.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> PhotosRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PhotosRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return PhotosRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class PhotosRequestBuilderGetQueryParameters():
        """
        Retrieve a list of profilePhoto objects.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "filter":
                return "%24filter"
            if original_name == "orderby":
                return "%24orderby"
            if original_name == "select":
                return "%24select"
            if original_name == "skip":
                return "%24skip"
            if original_name == "top":
                return "%24top"
            return original_name
        
        # Filter items by property values
        filter: Optional[str] = None

        # Order items by property values
        orderby: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        # Skip the first n items
        skip: Optional[int] = None

        # Show only the first n items
        top: Optional[int] = None

    

