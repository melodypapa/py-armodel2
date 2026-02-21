"""DiagnosticMeasurementIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 205)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTestResult.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticMeasurementIdentifier(DiagnosticCommonElement):
    """AUTOSAR DiagnosticMeasurementIdentifier."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    obd_mid: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticMeasurementIdentifier."""
        super().__init__()
        self.obd_mid: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticMeasurementIdentifier to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticMeasurementIdentifier, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize obd_mid
        if self.obd_mid is not None:
            serialized = ARObject._serialize_item(self.obd_mid, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OBD-MID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticMeasurementIdentifier":
        """Deserialize XML element to DiagnosticMeasurementIdentifier object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticMeasurementIdentifier object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticMeasurementIdentifier, cls).deserialize(element)

        # Parse obd_mid
        child = ARObject._find_child_element(element, "OBD-MID")
        if child is not None:
            obd_mid_value = child.text
            obj.obd_mid = obd_mid_value

        return obj



class DiagnosticMeasurementIdentifierBuilder:
    """Builder for DiagnosticMeasurementIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticMeasurementIdentifier = DiagnosticMeasurementIdentifier()

    def build(self) -> DiagnosticMeasurementIdentifier:
        """Build and return DiagnosticMeasurementIdentifier object.

        Returns:
            DiagnosticMeasurementIdentifier instance
        """
        # TODO: Add validation
        return self._obj
