from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_package_localized_text, access_package_multiple_choice_question, access_package_text_input_question, entity

from . import entity

@dataclass
class AccessPackageQuestion(entity.Entity):
    # Specifies whether the requestor is allowed to edit answers to questions for an assignment by posting an update to accessPackageAssignmentRequest.
    is_answer_editable: Optional[bool] = None
    # Whether the requestor is required to supply an answer or not.
    is_required: Optional[bool] = None
    # The text of the question represented in a format for a specific locale.
    localizations: Optional[List[access_package_localized_text.AccessPackageLocalizedText]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Relative position of this question when displaying a list of questions to the requestor.
    sequence: Optional[int] = None
    # The text of the question to show to the requestor.
    text: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageQuestion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageQuestion
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.accessPackageMultipleChoiceQuestion":
                from . import access_package_multiple_choice_question

                return access_package_multiple_choice_question.AccessPackageMultipleChoiceQuestion()
            if mapping_value == "#microsoft.graph.accessPackageTextInputQuestion":
                from . import access_package_text_input_question

                return access_package_text_input_question.AccessPackageTextInputQuestion()
        return AccessPackageQuestion()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_package_localized_text, access_package_multiple_choice_question, access_package_text_input_question, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "isAnswerEditable": lambda n : setattr(self, 'is_answer_editable', n.get_bool_value()),
            "isRequired": lambda n : setattr(self, 'is_required', n.get_bool_value()),
            "localizations": lambda n : setattr(self, 'localizations', n.get_collection_of_object_values(access_package_localized_text.AccessPackageLocalizedText)),
            "sequence": lambda n : setattr(self, 'sequence', n.get_int_value()),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
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
        writer.write_bool_value("isAnswerEditable", self.is_answer_editable)
        writer.write_bool_value("isRequired", self.is_required)
        writer.write_collection_of_object_values("localizations", self.localizations)
        writer.write_int_value("sequence", self.sequence)
        writer.write_str_value("text", self.text)
    

