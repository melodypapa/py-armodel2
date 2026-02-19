"""DiagnosticFunctionIdentifierInhibit AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 215)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Fim.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Fim import (
    DiagnosticInhibitionMaskEnum,
)


class DiagnosticFunctionIdentifierInhibit(DiagnosticCommonElement):
    """AUTOSAR DiagnosticFunctionIdentifierInhibit."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    function: Optional[Any]
    inhibition_mask: Optional[DiagnosticInhibitionMaskEnum]
    inhibit_sources: list[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticFunctionIdentifierInhibit."""
        super().__init__()
        self.function: Optional[Any] = None
        self.inhibition_mask: Optional[DiagnosticInhibitionMaskEnum] = None
        self.inhibit_sources: list[Any] = []
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticFunctionIdentifierInhibit to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticFunctionIdentifierInhibit, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize function
        if self.function is not None:
            serialized = ARObject._serialize_item(self.function, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FUNCTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize inhibition_mask
        if self.inhibition_mask is not None:
            serialized = ARObject._serialize_item(self.inhibition_mask, "DiagnosticInhibitionMaskEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INHIBITION-MASK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize inhibit_sources (list to container "INHIBIT-SOURCES")
        if self.inhibit_sources:
            wrapper = ET.Element("INHIBIT-SOURCES")
            for item in self.inhibit_sources:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticFunctionIdentifierInhibit":
        """Deserialize XML element to DiagnosticFunctionIdentifierInhibit object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticFunctionIdentifierInhibit object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticFunctionIdentifierInhibit, cls).deserialize(element)

        # Parse function
        child = ARObject._find_child_element(element, "FUNCTION")
        if child is not None:
            function_value = child.text
            obj.function = function_value

        # Parse inhibition_mask
        child = ARObject._find_child_element(element, "INHIBITION-MASK")
        if child is not None:
            inhibition_mask_value = DiagnosticInhibitionMaskEnum.deserialize(child)
            obj.inhibition_mask = inhibition_mask_value

        # Parse inhibit_sources (list from container "INHIBIT-SOURCES")
        obj.inhibit_sources = []
        container = ARObject._find_child_element(element, "INHIBIT-SOURCES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.inhibit_sources.append(child_value)

        return obj



class DiagnosticFunctionIdentifierInhibitBuilder:
    """Builder for DiagnosticFunctionIdentifierInhibit."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticFunctionIdentifierInhibit = DiagnosticFunctionIdentifierInhibit()

    def build(self) -> DiagnosticFunctionIdentifierInhibit:
        """Build and return DiagnosticFunctionIdentifierInhibit object.

        Returns:
            DiagnosticFunctionIdentifierInhibit instance
        """
        # TODO: Add validation
        return self._obj
