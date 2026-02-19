"""PModeInSystemInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 370)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_provided_port_prototype import (
    AbstractProvidedPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.root_sw_composition_prototype import (
    RootSwCompositionPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.system import (
    System,
)


class PModeInSystemInstanceRef(ARObject):
    """AUTOSAR PModeInSystemInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base: Optional[System]
    context: Optional[RootSwCompositionPrototype]
    context_mode_group_ref: Optional[ARRef]
    context_p_port_prototype: Optional[AbstractProvidedPortPrototype]
    target_mode: Optional[ModeDeclaration]
    def __init__(self) -> None:
        """Initialize PModeInSystemInstanceRef."""
        super().__init__()
        self.base: Optional[System] = None
        self.context: Optional[RootSwCompositionPrototype] = None
        self.context_mode_group_ref: Optional[ARRef] = None
        self.context_p_port_prototype: Optional[AbstractProvidedPortPrototype] = None
        self.target_mode: Optional[ModeDeclaration] = None
    def serialize(self) -> ET.Element:
        """Serialize PModeInSystemInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
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

        # Serialize context_mode_group_ref
        if self.context_mode_group_ref is not None:
            serialized = ARObject._serialize_item(self.context_mode_group_ref, "ModeDeclarationGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-MODE-GROUP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context_p_port_prototype
        if self.context_p_port_prototype is not None:
            serialized = ARObject._serialize_item(self.context_p_port_prototype, "AbstractProvidedPortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-P-PORT-PROTOTYPE")
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
    def deserialize(cls, element: ET.Element) -> "PModeInSystemInstanceRef":
        """Deserialize XML element to PModeInSystemInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PModeInSystemInstanceRef object
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

        # Parse context_mode_group_ref
        child = ARObject._find_child_element(element, "CONTEXT-MODE-GROUP")
        if child is not None:
            context_mode_group_ref_value = ARObject._deserialize_by_tag(child, "ModeDeclarationGroup")
            obj.context_mode_group_ref = context_mode_group_ref_value

        # Parse context_p_port_prototype
        child = ARObject._find_child_element(element, "CONTEXT-P-PORT-PROTOTYPE")
        if child is not None:
            context_p_port_prototype_value = ARObject._deserialize_by_tag(child, "AbstractProvidedPortPrototype")
            obj.context_p_port_prototype = context_p_port_prototype_value

        # Parse target_mode
        child = ARObject._find_child_element(element, "TARGET-MODE")
        if child is not None:
            target_mode_value = ARObject._deserialize_by_tag(child, "ModeDeclaration")
            obj.target_mode = target_mode_value

        return obj



class PModeInSystemInstanceRefBuilder:
    """Builder for PModeInSystemInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PModeInSystemInstanceRef = PModeInSystemInstanceRef()

    def build(self) -> PModeInSystemInstanceRef:
        """Build and return PModeInSystemInstanceRef object.

        Returns:
            PModeInSystemInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
