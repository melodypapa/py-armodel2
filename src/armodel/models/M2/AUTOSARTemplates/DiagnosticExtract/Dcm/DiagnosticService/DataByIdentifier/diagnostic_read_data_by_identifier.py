"""DiagnosticReadDataByIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 112)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_DataByIdentifier.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.DataByIdentifier.diagnostic_data_by_identifier import (
    DiagnosticDataByIdentifier,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef


class DiagnosticReadDataByIdentifier(DiagnosticDataByIdentifier):
    """AUTOSAR DiagnosticReadDataByIdentifier."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    read_class_ref: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticReadDataByIdentifier."""
        super().__init__()
        self.read_class_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticReadDataByIdentifier to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticReadDataByIdentifier, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize read_class_ref
        if self.read_class_ref is not None:
            serialized = ARObject._serialize_item(self.read_class_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("READ-CLASS-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticReadDataByIdentifier":
        """Deserialize XML element to DiagnosticReadDataByIdentifier object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticReadDataByIdentifier object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticReadDataByIdentifier, cls).deserialize(element)

        # Parse read_class_ref
        child = ARObject._find_child_element(element, "READ-CLASS-REF")
        if child is not None:
            read_class_ref_value = ARRef.deserialize(child)
            obj.read_class_ref = read_class_ref_value

        return obj



class DiagnosticReadDataByIdentifierBuilder:
    """Builder for DiagnosticReadDataByIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticReadDataByIdentifier = DiagnosticReadDataByIdentifier()

    def build(self) -> DiagnosticReadDataByIdentifier:
        """Build and return DiagnosticReadDataByIdentifier object.

        Returns:
            DiagnosticReadDataByIdentifier instance
        """
        # TODO: Add validation
        return self._obj
