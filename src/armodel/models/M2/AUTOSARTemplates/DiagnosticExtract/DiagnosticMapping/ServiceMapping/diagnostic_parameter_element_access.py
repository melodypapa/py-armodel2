"""DiagnosticParameterElementAccess AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 229)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_ServiceMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    context_element_refs: list[ARRef]
    target_element_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DiagnosticParameterElementAccess."""
        super().__init__()
        self.context_element_refs: list[ARRef] = []
        self.target_element_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticParameterElementAccess to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticParameterElementAccess, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize context_element_refs (list to container "CONTEXT-ELEMENT-REFS")
        if self.context_element_refs:
            wrapper = ET.Element("CONTEXT-ELEMENT-REFS")
            for item in self.context_element_refs:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticParameter")
                if serialized is not None:
                    child_elem = ET.Element("CONTEXT-ELEMENT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize target_element_ref
        if self.target_element_ref is not None:
            serialized = SerializationHelper.serialize_item(self.target_element_ref, "DiagnosticParameter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-ELEMENT-REF")
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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticParameterElementAccess, cls).deserialize(element)

        # Parse context_element_refs (list from container "CONTEXT-ELEMENT-REFS")
        obj.context_element_refs = []
        container = SerializationHelper.find_child_element(element, "CONTEXT-ELEMENT-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.context_element_refs.append(child_value)

        # Parse target_element_ref
        child = SerializationHelper.find_child_element(element, "TARGET-ELEMENT-REF")
        if child is not None:
            target_element_ref_value = ARRef.deserialize(child)
            obj.target_element_ref = target_element_ref_value

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
