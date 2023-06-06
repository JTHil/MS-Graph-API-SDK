from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import applied_conditional_access_policy, conditional_access_status, device_detail, entity, risk_detail, risk_event_type, risk_level, risk_state, sign_in_location, sign_in_status

from . import entity

@dataclass
class SignIn(entity.Entity):
    # App name displayed in the Azure Portal. Supports $filter (eq and startsWith operators only).
    app_display_name: Optional[str] = None
    # Unique GUID representing the app ID in the Azure Active Directory. Supports $filter (eq operator only).
    app_id: Optional[str] = None
    # Provides a list of conditional access policies that are triggered by the corresponding sign-in activity.
    applied_conditional_access_policies: Optional[List[applied_conditional_access_policy.AppliedConditionalAccessPolicy]] = None
    # Identifies the client used for the sign-in activity. Modern authentication clients include Browser and modern clients. Legacy authentication clients include Exchange ActiveSync, IMAP, MAPI, SMTP, POP, and other clients. Supports $filter (eq operator only).
    client_app_used: Optional[str] = None
    # Reports status of an activated conditional access policy. Possible values are: success, failure, notApplied, and unknownFutureValue. Supports $filter (eq operator only).
    conditional_access_status: Optional[conditional_access_status.ConditionalAccessStatus] = None
    # The request ID sent from the client when the sign-in is initiated; used to troubleshoot sign-in activity. Supports $filter (eq operator only).
    correlation_id: Optional[str] = None
    # Date and time (UTC) the sign-in was initiated. Example: midnight on Jan 1, 2014 is reported as 2014-01-01T00:00:00Z. Supports $orderby and $filter (eq, le, and ge operators only).
    created_date_time: Optional[datetime] = None
    # Device information from where the sign-in occurred; includes device ID, operating system, and browser. Supports $filter (eq and startsWith operators only) on browser and operatingSytem properties.
    device_detail: Optional[device_detail.DeviceDetail] = None
    # IP address of the client used to sign in. Supports $filter (eq and startsWith operators only).
    ip_address: Optional[str] = None
    # Indicates if a sign-in is interactive or not.
    is_interactive: Optional[bool] = None
    # Provides the city, state, and country code where the sign-in originated. Supports $filter (eq and startsWith operators only) on city, state, and countryOrRegion properties.
    location: Optional[sign_in_location.SignInLocation] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Name of the resource the user signed into. Supports $filter (eq operator only).
    resource_display_name: Optional[str] = None
    # ID of the resource that the user signed into. Supports $filter (eq operator only).
    resource_id: Optional[str] = None
    # Provides the 'reason' behind a specific state of a risky user, sign-in or a risk event. The possible values are: none, adminGeneratedTemporaryPassword, userPerformedSecuredPasswordChange, userPerformedSecuredPasswordReset, adminConfirmedSigninSafe, aiConfirmedSigninSafe, userPassedMFADrivenByRiskBasedPolicy, adminDismissedAllRiskForUser, adminConfirmedSigninCompromised, unknownFutureValue. The value none means that no action has been performed on the user or sign-in so far.  Supports $filter (eq operator only).Note: Details for this property require an Azure AD Premium P2 license. Other licenses return the value hidden.
    risk_detail: Optional[risk_detail.RiskDetail] = None
    # Risk event types associated with the sign-in. The possible values are: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, and unknownFutureValue. Supports $filter (eq operator only).
    risk_event_types: Optional[List[risk_event_type.RiskEventType]] = None
    # The list of risk event types associated with the sign-in. Possible values: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, or unknownFutureValue. Supports $filter (eq and startsWith operators only).
    risk_event_types_v2: Optional[List[str]] = None
    # Aggregated risk level. The possible values are: none, low, medium, high, hidden, and unknownFutureValue. The value hidden means the user or sign-in was not enabled for Azure AD Identity Protection. Supports $filter (eq operator only).  Note: Details for this property are only available for Azure AD Premium P2 customers. All other customers will be returned hidden.
    risk_level_aggregated: Optional[risk_level.RiskLevel] = None
    # Risk level during sign-in. The possible values are: none, low, medium, high, hidden, and unknownFutureValue. The value hidden means the user or sign-in was not enabled for Azure AD Identity Protection.  Supports $filter (eq operator only). Note: Details for this property are only available for Azure AD Premium P2 customers. All other customers will be returned hidden.
    risk_level_during_sign_in: Optional[risk_level.RiskLevel] = None
    # Reports status of the risky user, sign-in, or a risk event. The possible values are: none, confirmedSafe, remediated, dismissed, atRisk, confirmedCompromised, unknownFutureValue. Supports $filter (eq operator only).
    risk_state: Optional[risk_state.RiskState] = None
    # Sign-in status. Includes the error code and description of the error (in case of a sign-in failure). Supports $filter (eq operator only) on errorCode property.
    status: Optional[sign_in_status.SignInStatus] = None
    # Display name of the user that initiated the sign-in. Supports $filter (eq and startsWith operators only).
    user_display_name: Optional[str] = None
    # ID of the user that initiated the sign-in. Supports $filter (eq operator only).
    user_id: Optional[str] = None
    # User principal name of the user that initiated the sign-in. Supports $filter (eq and startsWith operators only).
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SignIn:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SignIn
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SignIn()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import applied_conditional_access_policy, conditional_access_status, device_detail, entity, risk_detail, risk_event_type, risk_level, risk_state, sign_in_location, sign_in_status

        fields: Dict[str, Callable[[Any], None]] = {
            "appliedConditionalAccessPolicies": lambda n : setattr(self, 'applied_conditional_access_policies', n.get_collection_of_object_values(applied_conditional_access_policy.AppliedConditionalAccessPolicy)),
            "appDisplayName": lambda n : setattr(self, 'app_display_name', n.get_str_value()),
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "clientAppUsed": lambda n : setattr(self, 'client_app_used', n.get_str_value()),
            "conditionalAccessStatus": lambda n : setattr(self, 'conditional_access_status', n.get_enum_value(conditional_access_status.ConditionalAccessStatus)),
            "correlationId": lambda n : setattr(self, 'correlation_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deviceDetail": lambda n : setattr(self, 'device_detail', n.get_object_value(device_detail.DeviceDetail)),
            "ipAddress": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "isInteractive": lambda n : setattr(self, 'is_interactive', n.get_bool_value()),
            "location": lambda n : setattr(self, 'location', n.get_object_value(sign_in_location.SignInLocation)),
            "resourceDisplayName": lambda n : setattr(self, 'resource_display_name', n.get_str_value()),
            "resourceId": lambda n : setattr(self, 'resource_id', n.get_str_value()),
            "riskDetail": lambda n : setattr(self, 'risk_detail', n.get_enum_value(risk_detail.RiskDetail)),
            "riskEventTypes": lambda n : setattr(self, 'risk_event_types', n.get_collection_of_enum_values(risk_event_type.RiskEventType)),
            "riskEventTypes_v2": lambda n : setattr(self, 'risk_event_types_v2', n.get_collection_of_primitive_values(str)),
            "riskLevelAggregated": lambda n : setattr(self, 'risk_level_aggregated', n.get_enum_value(risk_level.RiskLevel)),
            "riskLevelDuringSignIn": lambda n : setattr(self, 'risk_level_during_sign_in', n.get_enum_value(risk_level.RiskLevel)),
            "riskState": lambda n : setattr(self, 'risk_state', n.get_enum_value(risk_state.RiskState)),
            "status": lambda n : setattr(self, 'status', n.get_object_value(sign_in_status.SignInStatus)),
            "userDisplayName": lambda n : setattr(self, 'user_display_name', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("appliedConditionalAccessPolicies", self.applied_conditional_access_policies)
        writer.write_str_value("appDisplayName", self.app_display_name)
        writer.write_str_value("appId", self.app_id)
        writer.write_str_value("clientAppUsed", self.client_app_used)
        writer.write_enum_value("conditionalAccessStatus", self.conditional_access_status)
        writer.write_str_value("correlationId", self.correlation_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("deviceDetail", self.device_detail)
        writer.write_str_value("ipAddress", self.ip_address)
        writer.write_bool_value("isInteractive", self.is_interactive)
        writer.write_object_value("location", self.location)
        writer.write_str_value("resourceDisplayName", self.resource_display_name)
        writer.write_str_value("resourceId", self.resource_id)
        writer.write_enum_value("riskDetail", self.risk_detail)
        writer.write_enum_value("riskEventTypes", self.risk_event_types)
        writer.write_collection_of_primitive_values("riskEventTypes_v2", self.risk_event_types_v2)
        writer.write_enum_value("riskLevelAggregated", self.risk_level_aggregated)
        writer.write_enum_value("riskLevelDuringSignIn", self.risk_level_during_sign_in)
        writer.write_enum_value("riskState", self.risk_state)
        writer.write_object_value("status", self.status)
        writer.write_str_value("userDisplayName", self.user_display_name)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    

