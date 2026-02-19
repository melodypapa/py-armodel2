"""ModeInSwcInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 38)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.sw_component_type import (
    SwComponentType,
)


class ModeInSwcInstanceRef(ARObject):
    """AUTOSAR ModeInSwcInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base: Optional[SwComponentType]
    contexts: list[Any]
    context_mode_ref: Optional[ARRef]
    context_port_ref: Optional[ARRef]
    target_mode: Optional[ModeDeclaration]
    def __init__(self) -> None:
        """Initialize ModeInSwcInstanceRef."""
        super().__init__()
        self.base: Optional[SwComponentType] = None
        self.contexts: list[Any] = []
        self.context_mode_ref: Optional[ARRef] = None
        self.context_port_ref: Optional[ARRef] = None
        self.target_mode: Optional[ModeDeclaration] = None

    def serialize(self) -> ET.Element:
        """Serialize ModeInSwcInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize base
        if self.base is not None:
            serialized = ARObject._serialize_item(self.base, "SwComponentType")
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

        # Serialize context_mode_ref
        if self.context_mode_ref is not None:
            serialized = ARObject._serialize_item(self.context_mode_ref, "ModeDeclarationGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-MODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context_port_ref
        if self.context_port_ref is not None:
            serialized = ARObject._serialize_item(self.context_port_ref, "PortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-PORT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_mode
        if self.target_mode is not None:
            serialized = ARObject._serialize_item(self.target_mode, "ModeDeclaration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-MODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeInSwcInstanceRef":
        """Deserialize XML element to ModeInSwcInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeInSwcInstanceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse base
        child = ARObject._find_child_element(element, "BASE")
        if child is not None:
            base_value = ARObject._deserialize_by_tag(child, "SwComponentType")
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

        # Parse context_mode_ref
        child = ARObject._find_child_element(element, "CONTEXT-MODE-REF")
        if child is not None:
            context_mode_ref_value = ARRef.deserialize(child)
            obj.context_mode_ref = context_mode_ref_value

        # Parse context_port_ref
        child = ARObject._find_child_element(element, "CONTEXT-PORT-REF")
        if child is not None:
            context_port_ref_value = ARRef.deserialize(child)
            obj.context_port_ref = context_port_ref_value

        # Parse target_mode
        child = ARObject._find_child_element(element, "TARGET-MODE")
        if child is not None:
            target_mode_value = ARObject._deserialize_by_tag(child, "ModeDeclaration")
            obj.target_mode = target_mode_value

        return obj



class ModeInSwcInstanceRefBuilder:
    """Builder for ModeInSwcInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeInSwcInstanceRef = ModeInSwcInstanceRef()

    def build(self) -> ModeInSwcInstanceRef:
        """Build and return ModeInSwcInstanceRef object.

        Returns:
            ModeInSwcInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
