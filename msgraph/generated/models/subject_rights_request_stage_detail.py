from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .public_error import PublicError
    from .subject_rights_request_stage import SubjectRightsRequestStage
    from .subject_rights_request_stage_status import SubjectRightsRequestStageStatus

@dataclass
class SubjectRightsRequestStageDetail(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Describes the error, if any, for the current stage.
    error: Optional[PublicError] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The stage of the subject rights request. Possible values are: contentRetrieval, contentReview, generateReport, contentDeletion, caseResolved, unknownFutureValue.
    stage: Optional[SubjectRightsRequestStage] = None
    # Status of the current stage. Possible values are: notStarted, current, completed, failed, unknownFutureValue.
    status: Optional[SubjectRightsRequestStageStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SubjectRightsRequestStageDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SubjectRightsRequestStageDetail
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SubjectRightsRequestStageDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .public_error import PublicError
        from .subject_rights_request_stage import SubjectRightsRequestStage
        from .subject_rights_request_stage_status import SubjectRightsRequestStageStatus

        from .public_error import PublicError
        from .subject_rights_request_stage import SubjectRightsRequestStage
        from .subject_rights_request_stage_status import SubjectRightsRequestStageStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "error": lambda n : setattr(self, 'error', n.get_object_value(PublicError)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "stage": lambda n : setattr(self, 'stage', n.get_enum_value(SubjectRightsRequestStage)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(SubjectRightsRequestStageStatus)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("error", self.error)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("stage", self.stage)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

