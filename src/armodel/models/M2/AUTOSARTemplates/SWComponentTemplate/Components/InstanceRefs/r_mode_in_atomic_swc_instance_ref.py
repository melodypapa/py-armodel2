"""RModeInAtomicSwcInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 943)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
    AbstractRequiredPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
    AtomicSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class RModeInAtomicSwcInstanceRef(ARObject):
    """AUTOSAR RModeInAtomicSwcInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base_ref: Optional[ARRef]
    context_mode_group_prototype_ref: Optional[ARRef]
    context_port_prototype_ref: Optional[ARRef]
    target_mode_declaration_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize RModeInAtomicSwcInstanceRef."""
        super().__init__()
        self.base_ref: Optional[ARRef] = None
        self.context_mode_group_prototype_ref: Optional[ARRef] = None
        self.context_port_prototype_ref: Optional[ARRef] = None
        self.target_mode_declaration_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize RModeInAtomicSwcInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize base_ref
        if self.base_ref is not None:
            serialized = ARObject._serialize_item(self.base_ref, "AtomicSwComponentType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context_mode_group_prototype_ref
        if self.context_mode_group_prototype_ref is not None:
            serialized = ARObject._serialize_item(self.context_mode_group_prototype_ref, "ModeDeclarationGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-MODE-GROUP-PROTOTYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context_port_prototype_ref
        if self.context_port_prototype_ref is not None:
            serialized = ARObject._serialize_item(self.context_port_prototype_ref, "AbstractRequiredPortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-PORT-PROTOTYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_mode_declaration_ref
        if self.target_mode_declaration_ref is not None:
            serialized = ARObject._serialize_item(self.target_mode_declaration_ref, "ModeDeclaration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-MODE-DECLARATION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RModeInAtomicSwcInstanceRef":
        """Deserialize XML element to RModeInAtomicSwcInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RModeInAtomicSwcInstanceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse base_ref
        child = ARObject._find_child_element(element, "BASE-REF")
        if child is not None:
            base_ref_value = ARRef.deserialize(child)
            obj.base_ref = base_ref_value

        # Parse context_mode_group_prototype_ref
        child = ARObject._find_child_element(element, "CONTEXT-MODE-GROUP-PROTOTYPE-REF")
        if child is not None:
            context_mode_group_prototype_ref_value = ARRef.deserialize(child)
            obj.context_mode_group_prototype_ref = context_mode_group_prototype_ref_value

        # Parse context_port_prototype_ref
        child = ARObject._find_child_element(element, "CONTEXT-PORT-PROTOTYPE-REF")
        if child is not None:
            context_port_prototype_ref_value = ARRef.deserialize(child)
            obj.context_port_prototype_ref = context_port_prototype_ref_value

        # Parse target_mode_declaration_ref
        child = ARObject._find_child_element(element, "TARGET-MODE-DECLARATION-REF")
        if child is not None:
            target_mode_declaration_ref_value = ARRef.deserialize(child)
            obj.target_mode_declaration_ref = target_mode_declaration_ref_value

        return obj



class RModeInAtomicSwcInstanceRefBuilder:
    """Builder for RModeInAtomicSwcInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RModeInAtomicSwcInstanceRef = RModeInAtomicSwcInstanceRef()

    def build(self) -> RModeInAtomicSwcInstanceRef:
        """Build and return RModeInAtomicSwcInstanceRef object.

        Returns:
            RModeInAtomicSwcInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
