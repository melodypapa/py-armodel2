"""DiagnosticTestRoutineIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 158)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_ObdService_Mode_0x08_RequestControlOfOnBoard.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticTestRoutineIdentifier(DiagnosticCommonElement):
    """AUTOSAR DiagnosticTestRoutineIdentifier."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    id: Optional[PositiveInteger]
    request_data: Optional[PositiveInteger]
    response_data: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticTestRoutineIdentifier."""
        super().__init__()
        self.id: Optional[PositiveInteger] = None
        self.request_data: Optional[PositiveInteger] = None
        self.response_data: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticTestRoutineIdentifier to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticTestRoutineIdentifier, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize id
        if self.id is not None:
            serialized = SerializationHelper.serialize_item(self.id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize request_data
        if self.request_data is not None:
            serialized = SerializationHelper.serialize_item(self.request_data, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUEST-DATA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize response_data
        if self.response_data is not None:
            serialized = SerializationHelper.serialize_item(self.response_data, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESPONSE-DATA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticTestRoutineIdentifier":
        """Deserialize XML element to DiagnosticTestRoutineIdentifier object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticTestRoutineIdentifier object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticTestRoutineIdentifier, cls).deserialize(element)

        # Parse id
        child = SerializationHelper.find_child_element(element, "ID")
        if child is not None:
            id_value = child.text
            obj.id = id_value

        # Parse request_data
        child = SerializationHelper.find_child_element(element, "REQUEST-DATA")
        if child is not None:
            request_data_value = child.text
            obj.request_data = request_data_value

        # Parse response_data
        child = SerializationHelper.find_child_element(element, "RESPONSE-DATA")
        if child is not None:
            response_data_value = child.text
            obj.response_data = response_data_value

        return obj



class DiagnosticTestRoutineIdentifierBuilder:
    """Builder for DiagnosticTestRoutineIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticTestRoutineIdentifier = DiagnosticTestRoutineIdentifier()

    def build(self) -> DiagnosticTestRoutineIdentifier:
        """Build and return DiagnosticTestRoutineIdentifier object.

        Returns:
            DiagnosticTestRoutineIdentifier instance
        """
        # TODO: Add validation
        return self._obj
