"""ImplementationDataTypeSubElementRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 138)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.sub_element_ref import (
    SubElementRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.ar_parameter_in_implementation_data_instance_ref import (
    ArParameterInImplementationDataInstanceRef,
)


class ImplementationDataTypeSubElementRef(SubElementRef):
    """AUTOSAR ImplementationDataTypeSubElementRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    implementation: Optional[Any]
    parameter: Optional[ArParameterInImplementationDataInstanceRef]
    def __init__(self) -> None:
        """Initialize ImplementationDataTypeSubElementRef."""
        super().__init__()
        self.implementation: Optional[Any] = None
        self.parameter: Optional[ArParameterInImplementationDataInstanceRef] = None
    def serialize(self) -> ET.Element:
        """Serialize ImplementationDataTypeSubElementRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ImplementationDataTypeSubElementRef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize implementation
        if self.implementation is not None:
            serialized = ARObject._serialize_item(self.implementation, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IMPLEMENTATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize parameter
        if self.parameter is not None:
            serialized = ARObject._serialize_item(self.parameter, "ArParameterInImplementationDataInstanceRef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PARAMETER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ImplementationDataTypeSubElementRef":
        """Deserialize XML element to ImplementationDataTypeSubElementRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ImplementationDataTypeSubElementRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ImplementationDataTypeSubElementRef, cls).deserialize(element)

        # Parse implementation
        child = ARObject._find_child_element(element, "IMPLEMENTATION")
        if child is not None:
            implementation_value = child.text
            obj.implementation = implementation_value

        # Parse parameter
        child = ARObject._find_child_element(element, "PARAMETER")
        if child is not None:
            parameter_value = ARObject._deserialize_by_tag(child, "ArParameterInImplementationDataInstanceRef")
            obj.parameter = parameter_value

        return obj



class ImplementationDataTypeSubElementRefBuilder:
    """Builder for ImplementationDataTypeSubElementRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ImplementationDataTypeSubElementRef = ImplementationDataTypeSubElementRef()

    def build(self) -> ImplementationDataTypeSubElementRef:
        """Build and return ImplementationDataTypeSubElementRef object.

        Returns:
            ImplementationDataTypeSubElementRef instance
        """
        # TODO: Add validation
        return self._obj
