"""SwcServiceDependencyInSystemInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 369)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.root_sw_composition_prototype import (
    RootSwCompositionPrototype,
)


class SwcServiceDependencyInSystemInstanceRef(ARObject):
    """AUTOSAR SwcServiceDependencyInSystemInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    context_root_sw: Optional[RootSwCompositionPrototype]
    context_sw_prototypes: list[Any]
    target_swc: Optional[Any]
    def __init__(self) -> None:
        """Initialize SwcServiceDependencyInSystemInstanceRef."""
        super().__init__()
        self.context_root_sw: Optional[RootSwCompositionPrototype] = None
        self.context_sw_prototypes: list[Any] = []
        self.target_swc: Optional[Any] = None
    def serialize(self) -> ET.Element:
        """Serialize SwcServiceDependencyInSystemInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize context_root_sw
        if self.context_root_sw is not None:
            serialized = ARObject._serialize_item(self.context_root_sw, "RootSwCompositionPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-ROOT-SW")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context_sw_prototypes (list to container "CONTEXT-SW-PROTOTYPES")
        if self.context_sw_prototypes:
            wrapper = ET.Element("CONTEXT-SW-PROTOTYPES")
            for item in self.context_sw_prototypes:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize target_swc
        if self.target_swc is not None:
            serialized = ARObject._serialize_item(self.target_swc, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-SWC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcServiceDependencyInSystemInstanceRef":
        """Deserialize XML element to SwcServiceDependencyInSystemInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwcServiceDependencyInSystemInstanceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse context_root_sw
        child = ARObject._find_child_element(element, "CONTEXT-ROOT-SW")
        if child is not None:
            context_root_sw_value = ARObject._deserialize_by_tag(child, "RootSwCompositionPrototype")
            obj.context_root_sw = context_root_sw_value

        # Parse context_sw_prototypes (list from container "CONTEXT-SW-PROTOTYPES")
        obj.context_sw_prototypes = []
        container = ARObject._find_child_element(element, "CONTEXT-SW-PROTOTYPES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.context_sw_prototypes.append(child_value)

        # Parse target_swc
        child = ARObject._find_child_element(element, "TARGET-SWC")
        if child is not None:
            target_swc_value = child.text
            obj.target_swc = target_swc_value

        return obj



class SwcServiceDependencyInSystemInstanceRefBuilder:
    """Builder for SwcServiceDependencyInSystemInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcServiceDependencyInSystemInstanceRef = SwcServiceDependencyInSystemInstanceRef()

    def build(self) -> SwcServiceDependencyInSystemInstanceRef:
        """Build and return SwcServiceDependencyInSystemInstanceRef object.

        Returns:
            SwcServiceDependencyInSystemInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
