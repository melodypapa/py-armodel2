"""InnerPortGroupInCompositionInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 943)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_group import (
    PortGroup,
)


class InnerPortGroupInCompositionInstanceRef(ARObject):
    """AUTOSAR InnerPortGroupInCompositionInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base: Optional[CompositionSwComponentType]
    contexts: list[Any]
    target_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize InnerPortGroupInCompositionInstanceRef."""
        super().__init__()
        self.base: Optional[CompositionSwComponentType] = None
        self.contexts: list[Any] = []
        self.target_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize InnerPortGroupInCompositionInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize base
        if self.base is not None:
            serialized = ARObject._serialize_item(self.base, "CompositionSwComponentType")
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

        # Serialize contexts (list to container "CONTEXTS")
        if self.contexts:
            wrapper = ET.Element("CONTEXTS")
            for item in self.contexts:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize target_ref
        if self.target_ref is not None:
            serialized = ARObject._serialize_item(self.target_ref, "PortGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InnerPortGroupInCompositionInstanceRef":
        """Deserialize XML element to InnerPortGroupInCompositionInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized InnerPortGroupInCompositionInstanceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse base
        child = ARObject._find_child_element(element, "BASE")
        if child is not None:
            base_value = ARObject._deserialize_by_tag(child, "CompositionSwComponentType")
            obj.base = base_value

        # Parse contexts (list from container "CONTEXTS")
        obj.contexts = []
        container = ARObject._find_child_element(element, "CONTEXTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.contexts.append(child_value)

        # Parse target_ref
        child = ARObject._find_child_element(element, "TARGET-REF")
        if child is not None:
            target_ref_value = ARRef.deserialize(child)
            obj.target_ref = target_ref_value

        return obj



class InnerPortGroupInCompositionInstanceRefBuilder:
    """Builder for InnerPortGroupInCompositionInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InnerPortGroupInCompositionInstanceRef = InnerPortGroupInCompositionInstanceRef()

    def build(self) -> InnerPortGroupInCompositionInstanceRef:
        """Build and return InnerPortGroupInCompositionInstanceRef object.

        Returns:
            InnerPortGroupInCompositionInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
