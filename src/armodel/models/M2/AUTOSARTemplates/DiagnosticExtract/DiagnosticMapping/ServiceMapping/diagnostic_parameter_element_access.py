"""DiagnosticParameterElementAccess AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 229)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_ServiceMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)


class DiagnosticParameterElementAccess(ARObject):
    """AUTOSAR DiagnosticParameterElementAccess."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    context_elements: list[DiagnosticParameter]
    target_element: Optional[DiagnosticParameter]
    def __init__(self) -> None:
        """Initialize DiagnosticParameterElementAccess."""
        super().__init__()
        self.context_elements: list[DiagnosticParameter] = []
        self.target_element: Optional[DiagnosticParameter] = None
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticParameterElementAccess to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize context_elements (list to container "CONTEXT-ELEMENTS")
        if self.context_elements:
            wrapper = ET.Element("CONTEXT-ELEMENTS")
            for item in self.context_elements:
                serialized = ARObject._serialize_item(item, "DiagnosticParameter")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize target_element
        if self.target_element is not None:
            serialized = ARObject._serialize_item(self.target_element, "DiagnosticParameter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-ELEMENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticParameterElementAccess":
        """Deserialize XML element to DiagnosticParameterElementAccess object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticParameterElementAccess object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse context_elements (list from container "CONTEXT-ELEMENTS")
        obj.context_elements = []
        container = ARObject._find_child_element(element, "CONTEXT-ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.context_elements.append(child_value)

        # Parse target_element
        child = ARObject._find_child_element(element, "TARGET-ELEMENT")
        if child is not None:
            target_element_value = ARObject._deserialize_by_tag(child, "DiagnosticParameter")
            obj.target_element = target_element_value

        return obj



class DiagnosticParameterElementAccessBuilder:
    """Builder for DiagnosticParameterElementAccess."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticParameterElementAccess = DiagnosticParameterElementAccess()

    def build(self) -> DiagnosticParameterElementAccess:
        """Build and return DiagnosticParameterElementAccess object.

        Returns:
            DiagnosticParameterElementAccess instance
        """
        # TODO: Add validation
        return self._obj
