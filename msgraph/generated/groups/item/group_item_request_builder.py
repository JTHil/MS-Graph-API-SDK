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
    from ...models.group import Group
    from ...models.o_data_errors.o_data_error import ODataError
    from .accepted_senders.accepted_senders_request_builder import AcceptedSendersRequestBuilder
    from .add_favorite.add_favorite_request_builder import AddFavoriteRequestBuilder
    from .app_role_assignments.app_role_assignments_request_builder import AppRoleAssignmentsRequestBuilder
    from .assign_license.assign_license_request_builder import AssignLicenseRequestBuilder
    from .calendar.calendar_request_builder import CalendarRequestBuilder
    from .calendar_view.calendar_view_request_builder import CalendarViewRequestBuilder
    from .check_granted_permissions_for_app.check_granted_permissions_for_app_request_builder import CheckGrantedPermissionsForAppRequestBuilder
    from .check_member_groups.check_member_groups_request_builder import CheckMemberGroupsRequestBuilder
    from .check_member_objects.check_member_objects_request_builder import CheckMemberObjectsRequestBuilder
    from .conversations.conversations_request_builder import ConversationsRequestBuilder
    from .created_on_behalf_of.created_on_behalf_of_request_builder import CreatedOnBehalfOfRequestBuilder
    from .drive.drive_request_builder import DriveRequestBuilder
    from .drives.drives_request_builder import DrivesRequestBuilder
    from .events.events_request_builder import EventsRequestBuilder
    from .extensions.extensions_request_builder import ExtensionsRequestBuilder
    from .get_member_groups.get_member_groups_request_builder import GetMemberGroupsRequestBuilder
    from .get_member_objects.get_member_objects_request_builder import GetMemberObjectsRequestBuilder
    from .group_lifecycle_policies.group_lifecycle_policies_request_builder import GroupLifecyclePoliciesRequestBuilder
    from .member_of.member_of_request_builder import MemberOfRequestBuilder
    from .members.members_request_builder import MembersRequestBuilder
    from .members_with_license_errors.members_with_license_errors_request_builder import MembersWithLicenseErrorsRequestBuilder
    from .onenote.onenote_request_builder import OnenoteRequestBuilder
    from .owners.owners_request_builder import OwnersRequestBuilder
    from .permission_grants.permission_grants_request_builder import PermissionGrantsRequestBuilder
    from .photo.photo_request_builder import PhotoRequestBuilder
    from .photos.photos_request_builder import PhotosRequestBuilder
    from .planner.planner_request_builder import PlannerRequestBuilder
    from .rejected_senders.rejected_senders_request_builder import RejectedSendersRequestBuilder
    from .remove_favorite.remove_favorite_request_builder import RemoveFavoriteRequestBuilder
    from .renew.renew_request_builder import RenewRequestBuilder
    from .reset_unseen_count.reset_unseen_count_request_builder import ResetUnseenCountRequestBuilder
    from .restore.restore_request_builder import RestoreRequestBuilder
    from .settings.settings_request_builder import SettingsRequestBuilder
    from .sites.sites_request_builder import SitesRequestBuilder
    from .subscribe_by_mail.subscribe_by_mail_request_builder import SubscribeByMailRequestBuilder
    from .team.team_request_builder import TeamRequestBuilder
    from .threads.threads_request_builder import ThreadsRequestBuilder
    from .transitive_member_of.transitive_member_of_request_builder import TransitiveMemberOfRequestBuilder
    from .transitive_members.transitive_members_request_builder import TransitiveMembersRequestBuilder
    from .unsubscribe_by_mail.unsubscribe_by_mail_request_builder import UnsubscribeByMailRequestBuilder
    from .validate_properties.validate_properties_request_builder import ValidatePropertiesRequestBuilder

class GroupItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the collection of group entities.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new GroupItemRequestBuilder and sets the default values.
        Args:
            path_parameters: The raw url or the Url template parameters for the request.
            request_adapter: The request adapter to use to execute the requests.
        """
        super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[GroupItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete group. When deleted, Microsoft 365 groups are moved to a temporary container and can be restored within 30 days. After that time, they're permanently deleted. This isn't applicable to Security groups and Distribution groups which are permanently deleted immediately. To learn more, see deletedItems.
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[GroupItemRequestBuilderGetRequestConfiguration] = None) -> Optional[Group]:
        """
        Get the properties and relationships of a group object. This operation returns by default only a subset of all the available properties, as noted in the Properties section. To get properties that are not returned by default, specify them in a $select OData query option. The hasMembersWithLicenseErrors and isArchived properties are an exception and are not returned in the $select query.
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Group]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.group import Group

        return await self.request_adapter.send_async(request_info, Group, error_mapping)
    
    async def patch(self,body: Optional[Group] = None, request_configuration: Optional[GroupItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[Group]:
        """
        Add a member to a security or Microsoft 365 group through the members navigation property. The following table shows the types of members that can be added to either security groups or Microsoft 365 groups.
        Args:
            body: The request body
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Group]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.group import Group

        return await self.request_adapter.send_async(request_info, Group, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[GroupItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete group. When deleted, Microsoft 365 groups are moved to a temporary container and can be restored within 30 days. After that time, they're permanently deleted. This isn't applicable to Security groups and Distribution groups which are permanently deleted immediately. To learn more, see deletedItems.
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
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
    
    def to_get_request_information(self,request_configuration: Optional[GroupItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get the properties and relationships of a group object. This operation returns by default only a subset of all the available properties, as noted in the Properties section. To get properties that are not returned by default, specify them in a $select OData query option. The hasMembersWithLicenseErrors and isArchived properties are an exception and are not returned in the $select query.
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
    
    def to_patch_request_information(self,body: Optional[Group] = None, request_configuration: Optional[GroupItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Add a member to a security or Microsoft 365 group through the members navigation property. The following table shows the types of members that can be added to either security groups or Microsoft 365 groups.
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
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def accepted_senders(self) -> AcceptedSendersRequestBuilder:
        """
        Provides operations to manage the acceptedSenders property of the microsoft.graph.group entity.
        """
        from .accepted_senders.accepted_senders_request_builder import AcceptedSendersRequestBuilder

        return AcceptedSendersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def add_favorite(self) -> AddFavoriteRequestBuilder:
        """
        Provides operations to call the addFavorite method.
        """
        from .add_favorite.add_favorite_request_builder import AddFavoriteRequestBuilder

        return AddFavoriteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def app_role_assignments(self) -> AppRoleAssignmentsRequestBuilder:
        """
        Provides operations to manage the appRoleAssignments property of the microsoft.graph.group entity.
        """
        from .app_role_assignments.app_role_assignments_request_builder import AppRoleAssignmentsRequestBuilder

        return AppRoleAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assign_license(self) -> AssignLicenseRequestBuilder:
        """
        Provides operations to call the assignLicense method.
        """
        from .assign_license.assign_license_request_builder import AssignLicenseRequestBuilder

        return AssignLicenseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def calendar(self) -> CalendarRequestBuilder:
        """
        Provides operations to manage the calendar property of the microsoft.graph.group entity.
        """
        from .calendar.calendar_request_builder import CalendarRequestBuilder

        return CalendarRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def calendar_view(self) -> CalendarViewRequestBuilder:
        """
        Provides operations to manage the calendarView property of the microsoft.graph.group entity.
        """
        from .calendar_view.calendar_view_request_builder import CalendarViewRequestBuilder

        return CalendarViewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def check_granted_permissions_for_app(self) -> CheckGrantedPermissionsForAppRequestBuilder:
        """
        Provides operations to call the checkGrantedPermissionsForApp method.
        """
        from .check_granted_permissions_for_app.check_granted_permissions_for_app_request_builder import CheckGrantedPermissionsForAppRequestBuilder

        return CheckGrantedPermissionsForAppRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def check_member_groups(self) -> CheckMemberGroupsRequestBuilder:
        """
        Provides operations to call the checkMemberGroups method.
        """
        from .check_member_groups.check_member_groups_request_builder import CheckMemberGroupsRequestBuilder

        return CheckMemberGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def check_member_objects(self) -> CheckMemberObjectsRequestBuilder:
        """
        Provides operations to call the checkMemberObjects method.
        """
        from .check_member_objects.check_member_objects_request_builder import CheckMemberObjectsRequestBuilder

        return CheckMemberObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def conversations(self) -> ConversationsRequestBuilder:
        """
        Provides operations to manage the conversations property of the microsoft.graph.group entity.
        """
        from .conversations.conversations_request_builder import ConversationsRequestBuilder

        return ConversationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def created_on_behalf_of(self) -> CreatedOnBehalfOfRequestBuilder:
        """
        Provides operations to manage the createdOnBehalfOf property of the microsoft.graph.group entity.
        """
        from .created_on_behalf_of.created_on_behalf_of_request_builder import CreatedOnBehalfOfRequestBuilder

        return CreatedOnBehalfOfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def drive(self) -> DriveRequestBuilder:
        """
        Provides operations to manage the drive property of the microsoft.graph.group entity.
        """
        from .drive.drive_request_builder import DriveRequestBuilder

        return DriveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def drives(self) -> DrivesRequestBuilder:
        """
        Provides operations to manage the drives property of the microsoft.graph.group entity.
        """
        from .drives.drives_request_builder import DrivesRequestBuilder

        return DrivesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def events(self) -> EventsRequestBuilder:
        """
        Provides operations to manage the events property of the microsoft.graph.group entity.
        """
        from .events.events_request_builder import EventsRequestBuilder

        return EventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def extensions(self) -> ExtensionsRequestBuilder:
        """
        Provides operations to manage the extensions property of the microsoft.graph.group entity.
        """
        from .extensions.extensions_request_builder import ExtensionsRequestBuilder

        return ExtensionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_member_groups(self) -> GetMemberGroupsRequestBuilder:
        """
        Provides operations to call the getMemberGroups method.
        """
        from .get_member_groups.get_member_groups_request_builder import GetMemberGroupsRequestBuilder

        return GetMemberGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_member_objects(self) -> GetMemberObjectsRequestBuilder:
        """
        Provides operations to call the getMemberObjects method.
        """
        from .get_member_objects.get_member_objects_request_builder import GetMemberObjectsRequestBuilder

        return GetMemberObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def group_lifecycle_policies(self) -> GroupLifecyclePoliciesRequestBuilder:
        """
        Provides operations to manage the groupLifecyclePolicies property of the microsoft.graph.group entity.
        """
        from .group_lifecycle_policies.group_lifecycle_policies_request_builder import GroupLifecyclePoliciesRequestBuilder

        return GroupLifecyclePoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def member_of(self) -> MemberOfRequestBuilder:
        """
        Provides operations to manage the memberOf property of the microsoft.graph.group entity.
        """
        from .member_of.member_of_request_builder import MemberOfRequestBuilder

        return MemberOfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def members(self) -> MembersRequestBuilder:
        """
        Provides operations to manage the members property of the microsoft.graph.group entity.
        """
        from .members.members_request_builder import MembersRequestBuilder

        return MembersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def members_with_license_errors(self) -> MembersWithLicenseErrorsRequestBuilder:
        """
        Provides operations to manage the membersWithLicenseErrors property of the microsoft.graph.group entity.
        """
        from .members_with_license_errors.members_with_license_errors_request_builder import MembersWithLicenseErrorsRequestBuilder

        return MembersWithLicenseErrorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def onenote(self) -> OnenoteRequestBuilder:
        """
        Provides operations to manage the onenote property of the microsoft.graph.group entity.
        """
        from .onenote.onenote_request_builder import OnenoteRequestBuilder

        return OnenoteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def owners(self) -> OwnersRequestBuilder:
        """
        Provides operations to manage the owners property of the microsoft.graph.group entity.
        """
        from .owners.owners_request_builder import OwnersRequestBuilder

        return OwnersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def permission_grants(self) -> PermissionGrantsRequestBuilder:
        """
        Provides operations to manage the permissionGrants property of the microsoft.graph.group entity.
        """
        from .permission_grants.permission_grants_request_builder import PermissionGrantsRequestBuilder

        return PermissionGrantsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def photo(self) -> PhotoRequestBuilder:
        """
        Provides operations to manage the photo property of the microsoft.graph.group entity.
        """
        from .photo.photo_request_builder import PhotoRequestBuilder

        return PhotoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def photos(self) -> PhotosRequestBuilder:
        """
        Provides operations to manage the photos property of the microsoft.graph.group entity.
        """
        from .photos.photos_request_builder import PhotosRequestBuilder

        return PhotosRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def planner(self) -> PlannerRequestBuilder:
        """
        Provides operations to manage the planner property of the microsoft.graph.group entity.
        """
        from .planner.planner_request_builder import PlannerRequestBuilder

        return PlannerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rejected_senders(self) -> RejectedSendersRequestBuilder:
        """
        Provides operations to manage the rejectedSenders property of the microsoft.graph.group entity.
        """
        from .rejected_senders.rejected_senders_request_builder import RejectedSendersRequestBuilder

        return RejectedSendersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remove_favorite(self) -> RemoveFavoriteRequestBuilder:
        """
        Provides operations to call the removeFavorite method.
        """
        from .remove_favorite.remove_favorite_request_builder import RemoveFavoriteRequestBuilder

        return RemoveFavoriteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def renew(self) -> RenewRequestBuilder:
        """
        Provides operations to call the renew method.
        """
        from .renew.renew_request_builder import RenewRequestBuilder

        return RenewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reset_unseen_count(self) -> ResetUnseenCountRequestBuilder:
        """
        Provides operations to call the resetUnseenCount method.
        """
        from .reset_unseen_count.reset_unseen_count_request_builder import ResetUnseenCountRequestBuilder

        return ResetUnseenCountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restore(self) -> RestoreRequestBuilder:
        """
        Provides operations to call the restore method.
        """
        from .restore.restore_request_builder import RestoreRequestBuilder

        return RestoreRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def settings(self) -> SettingsRequestBuilder:
        """
        Provides operations to manage the settings property of the microsoft.graph.group entity.
        """
        from .settings.settings_request_builder import SettingsRequestBuilder

        return SettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sites(self) -> SitesRequestBuilder:
        """
        Provides operations to manage the sites property of the microsoft.graph.group entity.
        """
        from .sites.sites_request_builder import SitesRequestBuilder

        return SitesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def subscribe_by_mail(self) -> SubscribeByMailRequestBuilder:
        """
        Provides operations to call the subscribeByMail method.
        """
        from .subscribe_by_mail.subscribe_by_mail_request_builder import SubscribeByMailRequestBuilder

        return SubscribeByMailRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def team(self) -> TeamRequestBuilder:
        """
        Provides operations to manage the team property of the microsoft.graph.group entity.
        """
        from .team.team_request_builder import TeamRequestBuilder

        return TeamRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def threads(self) -> ThreadsRequestBuilder:
        """
        Provides operations to manage the threads property of the microsoft.graph.group entity.
        """
        from .threads.threads_request_builder import ThreadsRequestBuilder

        return ThreadsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def transitive_member_of(self) -> TransitiveMemberOfRequestBuilder:
        """
        Provides operations to manage the transitiveMemberOf property of the microsoft.graph.group entity.
        """
        from .transitive_member_of.transitive_member_of_request_builder import TransitiveMemberOfRequestBuilder

        return TransitiveMemberOfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def transitive_members(self) -> TransitiveMembersRequestBuilder:
        """
        Provides operations to manage the transitiveMembers property of the microsoft.graph.group entity.
        """
        from .transitive_members.transitive_members_request_builder import TransitiveMembersRequestBuilder

        return TransitiveMembersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unsubscribe_by_mail(self) -> UnsubscribeByMailRequestBuilder:
        """
        Provides operations to call the unsubscribeByMail method.
        """
        from .unsubscribe_by_mail.unsubscribe_by_mail_request_builder import UnsubscribeByMailRequestBuilder

        return UnsubscribeByMailRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def validate_properties(self) -> ValidatePropertiesRequestBuilder:
        """
        Provides operations to call the validateProperties method.
        """
        from .validate_properties.validate_properties_request_builder import ValidatePropertiesRequestBuilder

        return ValidatePropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class GroupItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class GroupItemRequestBuilderGetQueryParameters():
        """
        Get the properties and relationships of a group object. This operation returns by default only a subset of all the available properties, as noted in the Properties section. To get properties that are not returned by default, specify them in a $select OData query option. The hasMembersWithLicenseErrors and isArchived properties are an exception and are not returned in the $select query.
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
    class GroupItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[GroupItemRequestBuilder.GroupItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class GroupItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

