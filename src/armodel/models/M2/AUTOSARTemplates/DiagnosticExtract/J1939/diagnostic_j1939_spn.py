"""DiagnosticJ1939Spn AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 219)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_J1939.classes.json"""

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


class DiagnosticJ1939Spn(DiagnosticCommonElement):
    """AUTOSAR DiagnosticJ1939Spn."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    spn: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticJ1939Spn."""
        super().__init__()
        self.spn: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticJ1939Spn to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticJ1939Spn, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize spn
        if self.spn is not None:
            serialized = ARObject._serialize_item(self.spn, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SPN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticJ1939Spn":
        """Deserialize XML element to DiagnosticJ1939Spn object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticJ1939Spn object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticJ1939Spn, cls).deserialize(element)

        # Parse spn
        child = ARObject._find_child_element(element, "SPN")
        if child is not None:
            spn_value = child.text
            obj.spn = spn_value

        return obj



class DiagnosticJ1939SpnBuilder:
    """Builder for DiagnosticJ1939Spn."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticJ1939Spn = DiagnosticJ1939Spn()

    def build(self) -> DiagnosticJ1939Spn:
        """Build and return DiagnosticJ1939Spn object.

        Returns:
            DiagnosticJ1939Spn instance
        """
        # TODO: Add validation
        return self._obj
