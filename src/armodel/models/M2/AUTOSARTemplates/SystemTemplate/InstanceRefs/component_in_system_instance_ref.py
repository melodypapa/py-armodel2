"""ComponentInSystemInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 999)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.root_sw_composition_prototype import (
    RootSwCompositionPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.system import (
    System,
)


class ComponentInSystemInstanceRef(ARObject):
    """AUTOSAR ComponentInSystemInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base: Optional[System]
    context: Optional[RootSwCompositionPrototype]
    target: Any
    def __init__(self) -> None:
        """Initialize ComponentInSystemInstanceRef."""
        super().__init__()
        self.base: Optional[System] = None
        self.context: Optional[RootSwCompositionPrototype] = None
        self.target: Any = None
    def serialize(self) -> ET.Element:
        """Serialize ComponentInSystemInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize base
        if self.base is not None:
            serialized = ARObject._serialize_item(self.base, "System")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context
        if self.context is not None:
            serialized = ARObject._serialize_item(self.context, "RootSwCompositionPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target
        if self.target is not None:
            serialized = ARObject._serialize_item(self.target, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ComponentInSystemInstanceRef":
        """Deserialize XML element to ComponentInSystemInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ComponentInSystemInstanceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse base
        child = ARObject._find_child_element(element, "BASE")
        if child is not None:
            base_value = ARObject._deserialize_by_tag(child, "System")
            obj.base = base_value

        # Parse context
        child = ARObject._find_child_element(element, "CONTEXT")
        if child is not None:
            context_value = ARObject._deserialize_by_tag(child, "RootSwCompositionPrototype")
            obj.context = context_value

        # Parse target
        child = ARObject._find_child_element(element, "TARGET")
        if child is not None:
            target_value = child.text
            obj.target = target_value

        return obj



class ComponentInSystemInstanceRefBuilder:
    """Builder for ComponentInSystemInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ComponentInSystemInstanceRef = ComponentInSystemInstanceRef()

    def build(self) -> ComponentInSystemInstanceRef:
        """Build and return ComponentInSystemInstanceRef object.

        Returns:
            ComponentInSystemInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
