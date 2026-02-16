"""DltMessage AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract.dlt_argument import (
    DltArgument,
)
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract.privacy_level import (
    PrivacyLevel,
)


class DltMessage(Identifiable):
    """AUTOSAR DltMessage."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "dlt_arguments": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DltArgument,
        ),  # dltArguments
        "message_id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # messageId
        "message_line": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # messageLine
        "message_source": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # messageSource
        "message_type_info": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # messageTypeInfo
        "privacy_level": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=PrivacyLevel,
        ),  # privacyLevel
    }

    def __init__(self) -> None:
        """Initialize DltMessage."""
        super().__init__()
        self.dlt_arguments: list[DltArgument] = []
        self.message_id: Optional[PositiveInteger] = None
        self.message_line: Optional[PositiveInteger] = None
        self.message_source: Optional[String] = None
        self.message_type_info: Optional[String] = None
        self.privacy_level: Optional[PrivacyLevel] = None


class DltMessageBuilder:
    """Builder for DltMessage."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DltMessage = DltMessage()

    def build(self) -> DltMessage:
        """Build and return DltMessage object.

        Returns:
            DltMessage instance
        """
        # TODO: Add validation
        return self._obj
