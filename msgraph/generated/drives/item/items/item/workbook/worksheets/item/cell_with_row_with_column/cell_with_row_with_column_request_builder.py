from __future__ import annotations
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
    from .........models.o_data_errors.o_data_error import ODataError
    from .........models.workbook_range import WorkbookRange

class CellWithRowWithColumnRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the cell method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]], column: Optional[int] = None, row: Optional[int] = None) -> None:
        """
        Instantiates a new CellWithRowWithColumnRequestBuilder and sets the default values.
        param column: Usage: column={column}
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        param row: Usage: row={row}
        Returns: None
        """
        if isinstance(path_parameters, dict):
            path_parameters['column'] = str(column)
            path_parameters['row'] = str(row)
        super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/worksheets/{workbookWorksheet%2Did}/cell(row={row},column={column})", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[WorkbookRange]:
        """
        Gets the range object containing the single cell based on row and column numbers. The cell can be outside the bounds of its parent range, so long as it's stays within the worksheet grid.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WorkbookRange]
        Find more info here: https://learn.microsoft.com/graph/api/worksheet-cell?view=graph-rest-1.0
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
        from .........models.workbook_range import WorkbookRange

        return await self.request_adapter.send_async(request_info, WorkbookRange, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Gets the range object containing the single cell based on row and column numbers. The cell can be outside the bounds of its parent range, so long as it's stays within the worksheet grid.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> CellWithRowWithColumnRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CellWithRowWithColumnRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return CellWithRowWithColumnRequestBuilder(self.request_adapter, raw_url)
    

