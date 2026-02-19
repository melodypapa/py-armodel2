"""DltMessage AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2018)
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 12)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_LogAndTraceExtract.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    dlt_arguments: list[DltArgument]
    message_id: Optional[PositiveInteger]
    message_line: Optional[PositiveInteger]
    message_source: Optional[String]
    message_type_info: Optional[String]
    privacy_level: Optional[PrivacyLevel]
    def __init__(self) -> None:
        """Initialize DltMessage."""
        super().__init__()
        self.dlt_arguments: list[DltArgument] = []
        self.message_id: Optional[PositiveInteger] = None
        self.message_line: Optional[PositiveInteger] = None
        self.message_source: Optional[String] = None
        self.message_type_info: Optional[String] = None
        self.privacy_level: Optional[PrivacyLevel] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DltMessage":
        """Deserialize XML element to DltMessage object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DltMessage object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse dlt_arguments (list)
        obj.dlt_arguments = []
        for child in ARObject._find_all_child_elements(element, "DLT-ARGUMENTS"):
            dlt_arguments_value = ARObject._deserialize_by_tag(child, "DltArgument")
            obj.dlt_arguments.append(dlt_arguments_value)

        # Parse message_id
        child = ARObject._find_child_element(element, "MESSAGE-ID")
        if child is not None:
            message_id_value = child.text
            obj.message_id = message_id_value

        # Parse message_line
        child = ARObject._find_child_element(element, "MESSAGE-LINE")
        if child is not None:
            message_line_value = child.text
            obj.message_line = message_line_value

        # Parse message_source
        child = ARObject._find_child_element(element, "MESSAGE-SOURCE")
        if child is not None:
            message_source_value = child.text
            obj.message_source = message_source_value

        # Parse message_type_info
        child = ARObject._find_child_element(element, "MESSAGE-TYPE-INFO")
        if child is not None:
            message_type_info_value = child.text
            obj.message_type_info = message_type_info_value

        # Parse privacy_level
        child = ARObject._find_child_element(element, "PRIVACY-LEVEL")
        if child is not None:
            privacy_level_value = ARObject._deserialize_by_tag(child, "PrivacyLevel")
            obj.privacy_level = privacy_level_value

        return obj



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
