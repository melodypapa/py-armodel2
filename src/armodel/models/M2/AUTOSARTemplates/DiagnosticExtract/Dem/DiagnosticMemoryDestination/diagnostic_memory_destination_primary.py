"""DiagnosticMemoryDestinationPrimary AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 184)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticMemoryDestination.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticMemoryDestination.diagnostic_memory_destination import (
    DiagnosticMemoryDestination,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode import (
    DiagnosticTypeOfDtcSupportedEnum,
)


class DiagnosticMemoryDestinationPrimary(DiagnosticMemoryDestination):
    """AUTOSAR DiagnosticMemoryDestinationPrimary."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    type_of_dtc: Optional[DiagnosticTypeOfDtcSupportedEnum]
    def __init__(self) -> None:
        """Initialize DiagnosticMemoryDestinationPrimary."""
        super().__init__()
        self.type_of_dtc: Optional[DiagnosticTypeOfDtcSupportedEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticMemoryDestinationPrimary to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticMemoryDestinationPrimary, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize type_of_dtc
        if self.type_of_dtc is not None:
            serialized = ARObject._serialize_item(self.type_of_dtc, "DiagnosticTypeOfDtcSupportedEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TYPE-OF-DTC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticMemoryDestinationPrimary":
        """Deserialize XML element to DiagnosticMemoryDestinationPrimary object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticMemoryDestinationPrimary object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticMemoryDestinationPrimary, cls).deserialize(element)

        # Parse type_of_dtc
        child = ARObject._find_child_element(element, "TYPE-OF-DTC")
        if child is not None:
            type_of_dtc_value = DiagnosticTypeOfDtcSupportedEnum.deserialize(child)
            obj.type_of_dtc = type_of_dtc_value

        return obj



class DiagnosticMemoryDestinationPrimaryBuilder:
    """Builder for DiagnosticMemoryDestinationPrimary."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticMemoryDestinationPrimary = DiagnosticMemoryDestinationPrimary()

    def build(self) -> DiagnosticMemoryDestinationPrimary:
        """Build and return DiagnosticMemoryDestinationPrimary object.

        Returns:
            DiagnosticMemoryDestinationPrimary instance
        """
        # TODO: Add validation
        return self._obj
