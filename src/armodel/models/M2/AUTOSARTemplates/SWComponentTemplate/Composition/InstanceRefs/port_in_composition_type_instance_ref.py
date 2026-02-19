"""PortInCompositionTypeInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 950)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from abc import ABC, abstractmethod


class PortInCompositionTypeInstanceRef(ARObject, ABC):
    """AUTOSAR PortInCompositionTypeInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    abstract_context: Optional[Any]
    base: Optional[CompositionSwComponentType]
    target_port_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize PortInCompositionTypeInstanceRef."""
        super().__init__()
        self.abstract_context: Optional[Any] = None
        self.base: Optional[CompositionSwComponentType] = None
        self.target_port_ref: Optional[ARRef] = None
    def serialize(self) -> ET.Element:
        """Serialize PortInCompositionTypeInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize abstract_context
        if self.abstract_context is not None:
            serialized = ARObject._serialize_item(self.abstract_context, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ABSTRACT-CONTEXT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

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

        # Serialize target_port_ref
        if self.target_port_ref is not None:
            serialized = ARObject._serialize_item(self.target_port_ref, "PortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-PORT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PortInCompositionTypeInstanceRef":
        """Deserialize XML element to PortInCompositionTypeInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PortInCompositionTypeInstanceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse abstract_context
        child = ARObject._find_child_element(element, "ABSTRACT-CONTEXT")
        if child is not None:
            abstract_context_value = child.text
            obj.abstract_context = abstract_context_value

        # Parse base
        child = ARObject._find_child_element(element, "BASE")
        if child is not None:
            base_value = ARObject._deserialize_by_tag(child, "CompositionSwComponentType")
            obj.base = base_value

        # Parse target_port_ref
        child = ARObject._find_child_element(element, "TARGET-PORT")
        if child is not None:
            target_port_ref_value = ARObject._deserialize_by_tag(child, "PortPrototype")
            obj.target_port_ref = target_port_ref_value

        return obj



class PortInCompositionTypeInstanceRefBuilder:
    """Builder for PortInCompositionTypeInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PortInCompositionTypeInstanceRef = PortInCompositionTypeInstanceRef()

    def build(self) -> PortInCompositionTypeInstanceRef:
        """Build and return PortInCompositionTypeInstanceRef object.

        Returns:
            PortInCompositionTypeInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
