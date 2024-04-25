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
    from .........models.identity_governance.user_processing_result import UserProcessingResult
    from .........models.o_data_errors.o_data_error import ODataError
    from .subject.subject_request_builder import SubjectRequestBuilder
    from .task_processing_results.task_processing_results_request_builder import TaskProcessingResultsRequestBuilder

class UserProcessingResultItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the userProcessingResults property of the microsoft.graph.identityGovernance.run entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new UserProcessingResultItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identityGovernance/lifecycleWorkflows/workflows/{workflow%2Did}/runs/{run%2Did}/userProcessingResults/{userProcessingResult%2Did}{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[UserProcessingResultItemRequestBuilderGetRequestConfiguration] = None) -> Optional[UserProcessingResult]:
        """
        The associated individual user execution.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[UserProcessingResult]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .........models.identity_governance.user_processing_result import UserProcessingResult

        return await self.request_adapter.send_async(request_info, UserProcessingResult, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[UserProcessingResultItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The associated individual user execution.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> UserProcessingResultItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: UserProcessingResultItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return UserProcessingResultItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def subject(self) -> SubjectRequestBuilder:
        """
        Provides operations to manage the subject property of the microsoft.graph.identityGovernance.userProcessingResult entity.
        """
        from .subject.subject_request_builder import SubjectRequestBuilder

        return SubjectRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def task_processing_results(self) -> TaskProcessingResultsRequestBuilder:
        """
        Provides operations to manage the taskProcessingResults property of the microsoft.graph.identityGovernance.userProcessingResult entity.
        """
        from .task_processing_results.task_processing_results_request_builder import TaskProcessingResultsRequestBuilder

        return TaskProcessingResultsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class UserProcessingResultItemRequestBuilderGetQueryParameters():
        """
        The associated individual user execution.
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
    class UserProcessingResultItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[UserProcessingResultItemRequestBuilder.UserProcessingResultItemRequestBuilderGetQueryParameters] = None

    

