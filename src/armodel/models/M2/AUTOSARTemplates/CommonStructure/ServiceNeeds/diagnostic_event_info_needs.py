"""DiagnosticEventInfoNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 312)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 760)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticEventInfoNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticEventInfoNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    obd_dtc_number: Optional[PositiveInteger]
    uds_dtc_number: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticEventInfoNeeds."""
        super().__init__()
        self.obd_dtc_number: Optional[PositiveInteger] = None
        self.uds_dtc_number: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticEventInfoNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticEventInfoNeeds, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize obd_dtc_number
        if self.obd_dtc_number is not None:
            serialized = ARObject._serialize_item(self.obd_dtc_number, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OBD-DTC-NUMBER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize uds_dtc_number
        if self.uds_dtc_number is not None:
            serialized = ARObject._serialize_item(self.uds_dtc_number, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UDS-DTC-NUMBER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEventInfoNeeds":
        """Deserialize XML element to DiagnosticEventInfoNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEventInfoNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticEventInfoNeeds, cls).deserialize(element)

        # Parse obd_dtc_number
        child = ARObject._find_child_element(element, "OBD-DTC-NUMBER")
        if child is not None:
            obd_dtc_number_value = child.text
            obj.obd_dtc_number = obd_dtc_number_value

        # Parse uds_dtc_number
        child = ARObject._find_child_element(element, "UDS-DTC-NUMBER")
        if child is not None:
            uds_dtc_number_value = child.text
            obj.uds_dtc_number = uds_dtc_number_value

        return obj



class DiagnosticEventInfoNeedsBuilder:
    """Builder for DiagnosticEventInfoNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEventInfoNeeds = DiagnosticEventInfoNeeds()

    def build(self) -> DiagnosticEventInfoNeeds:
        """Build and return DiagnosticEventInfoNeeds object.

        Returns:
            DiagnosticEventInfoNeeds instance
        """
        # TODO: Add validation
        return self._obj
