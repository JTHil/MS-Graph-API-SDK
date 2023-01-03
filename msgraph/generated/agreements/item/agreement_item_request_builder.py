from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

acceptances_request_builder = lazy_import('msgraph.generated.agreements.item.acceptances.acceptances_request_builder')
agreement_acceptance_item_request_builder = lazy_import('msgraph.generated.agreements.item.acceptances.item.agreement_acceptance_item_request_builder')
file_request_builder = lazy_import('msgraph.generated.agreements.item.file.file_request_builder')
files_request_builder = lazy_import('msgraph.generated.agreements.item.files.files_request_builder')
agreement_file_localization_item_request_builder = lazy_import('msgraph.generated.agreements.item.files.item.agreement_file_localization_item_request_builder')
agreement = lazy_import('msgraph.generated.models.agreement')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class AgreementItemRequestBuilder():
    """
    Provides operations to manage the collection of agreement entities.
    """
    @property
    def acceptances(self) -> acceptances_request_builder.AcceptancesRequestBuilder:
        """
        Provides operations to manage the acceptances property of the microsoft.graph.agreement entity.
        """
        return acceptances_request_builder.AcceptancesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def file(self) -> file_request_builder.FileRequestBuilder:
        """
        Provides operations to manage the file property of the microsoft.graph.agreement entity.
        """
        return file_request_builder.FileRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def files(self) -> files_request_builder.FilesRequestBuilder:
        """
        Provides operations to manage the files property of the microsoft.graph.agreement entity.
        """
        return files_request_builder.FilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def acceptances_by_id(self,id: str) -> Optional[agreement_acceptance_item_request_builder.AgreementAcceptanceItemRequestBuilder]:
        """
        Provides operations to manage the acceptances property of the microsoft.graph.agreement entity.
        Args:
            id: Unique identifier of the item
        Returns: Optional[agreement_acceptance_item_request_builder.AgreementAcceptanceItemRequestBuilder]
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["agreementAcceptance%2Did"] = id
        return agreement_acceptance_item_request_builder.AgreementAcceptanceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AgreementItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/agreements/{agreement%2Did}{?%24select}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[AgreementItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete entity from agreements
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
    
    def create_get_request_information(self,request_configuration: Optional[AgreementItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get entity from agreements by key
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def create_patch_request_information(self,body: Optional[agreement.Agreement] = None, request_configuration: Optional[AgreementItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update entity in agreements
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
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    async def delete(self,request_configuration: Optional[AgreementItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete entity from agreements
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        """
        request_info = self.create_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, response_handler, error_mapping)
    
    def files_by_id(self,id: str) -> Optional[agreement_file_localization_item_request_builder.AgreementFileLocalizationItemRequestBuilder]:
        """
        Provides operations to manage the files property of the microsoft.graph.agreement entity.
        Args:
            id: Unique identifier of the item
        Returns: Optional[agreement_file_localization_item_request_builder.AgreementFileLocalizationItemRequestBuilder]
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["agreementFileLocalization%2Did"] = id
        return agreement_file_localization_item_request_builder.AgreementFileLocalizationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[AgreementItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[agreement.Agreement]:
        """
        Get entity from agreements by key
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[agreement.Agreement]
        """
        request_info = self.create_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, agreement.Agreement, response_handler, error_mapping)
    
    async def patch(self,body: Optional[agreement.Agreement] = None, request_configuration: Optional[AgreementItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[agreement.Agreement]:
        """
        Update entity in agreements
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[agreement.Agreement]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.create_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, agreement.Agreement, response_handler, error_mapping)
    
    @dataclass
    class AgreementItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class AgreementItemRequestBuilderGetQueryParameters():
        """
        Get entity from agreements by key
        """
        # Select properties to be returned
        select: Optional[List[str]] = None

        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "select":
                return "%24select"
            return original_name
        
    
    @dataclass
    class AgreementItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[AgreementItemRequestBuilder.AgreementItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class AgreementItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

