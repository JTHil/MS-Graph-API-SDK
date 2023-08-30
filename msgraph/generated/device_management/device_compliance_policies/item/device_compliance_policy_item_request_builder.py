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
    from ....models.device_compliance_policy import DeviceCompliancePolicy
    from ....models.o_data_errors.o_data_error import ODataError
    from .assign.assign_request_builder import AssignRequestBuilder
    from .assignments.assignments_request_builder import AssignmentsRequestBuilder
    from .device_setting_state_summaries.device_setting_state_summaries_request_builder import DeviceSettingStateSummariesRequestBuilder
    from .device_statuses.device_statuses_request_builder import DeviceStatusesRequestBuilder
    from .device_status_overview.device_status_overview_request_builder import DeviceStatusOverviewRequestBuilder
    from .schedule_actions_for_rules.schedule_actions_for_rules_request_builder import ScheduleActionsForRulesRequestBuilder
    from .scheduled_actions_for_rule.scheduled_actions_for_rule_request_builder import ScheduledActionsForRuleRequestBuilder
    from .user_statuses.user_statuses_request_builder import UserStatusesRequestBuilder
    from .user_status_overview.user_status_overview_request_builder import UserStatusOverviewRequestBuilder

class DeviceCompliancePolicyItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the deviceCompliancePolicies property of the microsoft.graph.deviceManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DeviceCompliancePolicyItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceManagement/deviceCompliancePolicies/{deviceCompliancePolicy%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[DeviceCompliancePolicyItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Deletes a windowsPhone81CompliancePolicy.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/intune-deviceconfig-windowsphone81compliancepolicy-delete?view=graph-rest-1.0
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
    
    async def get(self,request_configuration: Optional[DeviceCompliancePolicyItemRequestBuilderGetRequestConfiguration] = None) -> Optional[DeviceCompliancePolicy]:
        """
        Read properties and relationships of the macOSCompliancePolicy object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeviceCompliancePolicy]
        Find more info here: https://learn.microsoft.com/graph/api/intune-deviceconfig-macoscompliancepolicy-get?view=graph-rest-1.0
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
        from ....models.device_compliance_policy import DeviceCompliancePolicy

        return await self.request_adapter.send_async(request_info, DeviceCompliancePolicy, error_mapping)
    
    async def patch(self,body: Optional[DeviceCompliancePolicy] = None, request_configuration: Optional[DeviceCompliancePolicyItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[DeviceCompliancePolicy]:
        """
        Update the properties of a windows10MobileCompliancePolicy object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeviceCompliancePolicy]
        Find more info here: https://learn.microsoft.com/graph/api/intune-deviceconfig-windows10mobilecompliancepolicy-update?view=graph-rest-1.0
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
        from ....models.device_compliance_policy import DeviceCompliancePolicy

        return await self.request_adapter.send_async(request_info, DeviceCompliancePolicy, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[DeviceCompliancePolicyItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Deletes a windowsPhone81CompliancePolicy.
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
    
    def to_get_request_information(self,request_configuration: Optional[DeviceCompliancePolicyItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Read properties and relationships of the macOSCompliancePolicy object.
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
    
    def to_patch_request_information(self,body: Optional[DeviceCompliancePolicy] = None, request_configuration: Optional[DeviceCompliancePolicyItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of a windows10MobileCompliancePolicy object.
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
    
    def with_url(self,raw_url: Optional[str] = None) -> DeviceCompliancePolicyItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DeviceCompliancePolicyItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return DeviceCompliancePolicyItemRequestBuilder(raw_url, self.request_adapter)
    
    @property
    def assign(self) -> AssignRequestBuilder:
        """
        Provides operations to call the assign method.
        """
        from .assign.assign_request_builder import AssignRequestBuilder

        return AssignRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignments(self) -> AssignmentsRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.deviceCompliancePolicy entity.
        """
        from .assignments.assignments_request_builder import AssignmentsRequestBuilder

        return AssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_setting_state_summaries(self) -> DeviceSettingStateSummariesRequestBuilder:
        """
        Provides operations to manage the deviceSettingStateSummaries property of the microsoft.graph.deviceCompliancePolicy entity.
        """
        from .device_setting_state_summaries.device_setting_state_summaries_request_builder import DeviceSettingStateSummariesRequestBuilder

        return DeviceSettingStateSummariesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_statuses(self) -> DeviceStatusesRequestBuilder:
        """
        Provides operations to manage the deviceStatuses property of the microsoft.graph.deviceCompliancePolicy entity.
        """
        from .device_statuses.device_statuses_request_builder import DeviceStatusesRequestBuilder

        return DeviceStatusesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_status_overview(self) -> DeviceStatusOverviewRequestBuilder:
        """
        Provides operations to manage the deviceStatusOverview property of the microsoft.graph.deviceCompliancePolicy entity.
        """
        from .device_status_overview.device_status_overview_request_builder import DeviceStatusOverviewRequestBuilder

        return DeviceStatusOverviewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def schedule_actions_for_rules(self) -> ScheduleActionsForRulesRequestBuilder:
        """
        Provides operations to call the scheduleActionsForRules method.
        """
        from .schedule_actions_for_rules.schedule_actions_for_rules_request_builder import ScheduleActionsForRulesRequestBuilder

        return ScheduleActionsForRulesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def scheduled_actions_for_rule(self) -> ScheduledActionsForRuleRequestBuilder:
        """
        Provides operations to manage the scheduledActionsForRule property of the microsoft.graph.deviceCompliancePolicy entity.
        """
        from .scheduled_actions_for_rule.scheduled_actions_for_rule_request_builder import ScheduledActionsForRuleRequestBuilder

        return ScheduledActionsForRuleRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_statuses(self) -> UserStatusesRequestBuilder:
        """
        Provides operations to manage the userStatuses property of the microsoft.graph.deviceCompliancePolicy entity.
        """
        from .user_statuses.user_statuses_request_builder import UserStatusesRequestBuilder

        return UserStatusesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_status_overview(self) -> UserStatusOverviewRequestBuilder:
        """
        Provides operations to manage the userStatusOverview property of the microsoft.graph.deviceCompliancePolicy entity.
        """
        from .user_status_overview.user_status_overview_request_builder import UserStatusOverviewRequestBuilder

        return UserStatusOverviewRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class DeviceCompliancePolicyItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class DeviceCompliancePolicyItemRequestBuilderGetQueryParameters():
        """
        Read properties and relationships of the macOSCompliancePolicy object.
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
    class DeviceCompliancePolicyItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[DeviceCompliancePolicyItemRequestBuilder.DeviceCompliancePolicyItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class DeviceCompliancePolicyItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

