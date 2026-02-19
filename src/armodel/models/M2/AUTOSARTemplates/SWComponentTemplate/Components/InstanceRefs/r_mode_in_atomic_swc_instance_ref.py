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

    base: Optional[AtomicSwComponentType]
    context_mode_group_prototype_ref: Optional[ARRef]
    context_port_prototype: Optional[AbstractRequiredPortPrototype]
    target_mode_declaration: Optional[ModeDeclaration]
    def __init__(self) -> None:
        """Initialize RModeInAtomicSwcInstanceRef."""
        super().__init__()
        self.base: Optional[AtomicSwComponentType] = None
        self.context_mode_group_prototype_ref: Optional[ARRef] = None
        self.context_port_prototype: Optional[AbstractRequiredPortPrototype] = None
        self.target_mode_declaration: Optional[ModeDeclaration] = None
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

        # Parse base
        child = ARObject._find_child_element(element, "BASE")
        if child is not None:
            base_value = ARObject._deserialize_by_tag(child, "AtomicSwComponentType")
            obj.base = base_value

        # Parse context_mode_group_prototype_ref
        child = ARObject._find_child_element(element, "CONTEXT-MODE-GROUP-PROTOTYPE")
        if child is not None:
            context_mode_group_prototype_ref_value = ARObject._deserialize_by_tag(child, "ModeDeclarationGroup")
            obj.context_mode_group_prototype_ref = context_mode_group_prototype_ref_value

        # Parse context_port_prototype
        child = ARObject._find_child_element(element, "CONTEXT-PORT-PROTOTYPE")
        if child is not None:
            context_port_prototype_value = ARObject._deserialize_by_tag(child, "AbstractRequiredPortPrototype")
            obj.context_port_prototype = context_port_prototype_value

        # Parse target_mode_declaration
        child = ARObject._find_child_element(element, "TARGET-MODE-DECLARATION")
        if child is not None:
            target_mode_declaration_value = ARObject._deserialize_by_tag(child, "ModeDeclaration")
            obj.target_mode_declaration = target_mode_declaration_value

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
